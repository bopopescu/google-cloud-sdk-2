# -*- coding: utf-8 -*- # Lint as: python3
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to create an Apigee API product."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib import apigee
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.apigee import defaults
from googlecloudsdk.command_lib.apigee import resource_args


class _HashDelimitedArgList(arg_parsers.ArgList):
  DEFAULT_DELIM_CHAR = "#"


class Deploy(base.DescribeCommand):
  """Create an Apigee API product."""

  detailed_help = {
      "DESCRIPTION":
          """
          Create an Apigee API product.

          An API product is a collection of API resources combined with quota
          settings and metadata, used to deliver customized and productized API
          bundles to the developer community. Call this after the API resources
          to be collected have already been deployed to a public-facing
          environment.

          API products enable the repackaging of APIs on-the-fly, without having
          to do any additional coding or configuration. Apigee recommends
          starting with a simple API product including only required elements,
          and then provisioning credentials to apps to enable them to start
          testing your APIs.
          """,
      "EXAMPLES":
          """
          To create an API product that publicly exposes all API proxies
          deployed to the ``prod'' environment, run:

              $ {command} kitchen-sink --environments=prod --all-proxies --public-access

          To expose all API proxies that are deployed to a URI fragment
          beginning with `/v1` or `/v0`, run:

              $ {command} legacy --all-environments --resources="/v0/**#/v1/**" --public-access

          To expose a few specific API proxies on all URI paths where they're
          deployed, run:

              $ {command} consumer --environments=prod --apis=menu,cart,delivery-tracker --public-access

          To expose only those API calls that match both a set of API proxies
          and a set of API resources, run:

              $ {command} legacy-consumer --environments=prod --apis=menu,cart,delivery-tracker --resources="/v0/**#/v1/**" --public-access

          To impose a quota of 50 calls per half-hour on a new all-inclusive API
          product, run:

              $ {command} kitchen-sink --environments=prod --all-proxies --public-access --quota=50 --quota-interval=30 --quota-unit=minute

          To require manual approval of developers before they can access the
          new API product, run:

              $ {command} kitchen-sink --environments=prod --all-proxies --public-access --manual-approval

          To hide the new API product while still making it accessible to
          developers, run:

              $ {command} kitchen-sink --environments=prod --all-proxies --private-access

          To restrict the new API product to internal users only, run:

              $ {command} kitchen-sink --environments=prod --all-proxies --internal-access

          To specify a human-friendly display name and description for the
          product, run:

              $ {command} consumer --environments=prod --apis=menu,cart,delivery-tracker --public-access --display-name="Consumer APIs" --description="APIs for the consumer side of the delivery network: ordering food and tracking deliveries."
          """
  }

  @staticmethod
  def Args(parser):
    resource_args.AddSingleResourceArgument(
        parser,
        "organization.product",
        "The API product to be created. Characters in a product's internal "
        "name are restricted to: ```A-Za-z0-9._-$ %```.",
        validate=True,
        argument_name="INTERNAL_NAME",
        fallthroughs=[defaults.GCPProductOrganizationFallthrough()])

    environment_group = parser.add_mutually_exclusive_group()

    environment_group.add_argument(
        "--environments",
        metavar="ENVIRONMENT",
        type=arg_parsers.ArgList(min_length=1),
        help=("Environments to which the API product is bound. Requests to "
              "environments that are not listed are rejected, preventing "
              "developers from accessing those resources through API Proxies "
              "deployed in another environment. For example, this can prevent "
              "resources associated with API proxies in ``prod'' from being "
              "accessed by API proxies deployed in ``test''."))

    environment_group.add_argument(
        "--all-environments",
        dest="environments",
        action="store_const",
        const=[],
        help="Make all environments accessible through this API product.")

    parser.add_argument(
        "--display-name",
        help=("The name to be displayed in the UI or developer portal to "
              "developers registering for API access."))

    access_group = parser.add_mutually_exclusive_group()
    access_group.add_argument(
        "--public-access",
        dest="access",
        action="store_const",
        const="public",
        help=("Make this API product visible to developers in the Apigee "
              "developer portal."))
    access_group.add_argument(
        "--private-access",
        dest="access",
        action="store_const",
        const="private",
        help=("Hide this API product in the developer portal but make it "
              "accessible by external developers."))
    access_group.add_argument(
        "--internal-access",
        dest="access",
        action="store_const",
        const="internal",
        help="Prevent external access to this API product.")

    proxies_mutex_group = parser.add_mutually_exclusive_group(
        "Arguments specifying which API proxies and resources to expose.")

    proxies_mutex_group.add_argument(
        "--all-proxies",
        action="store_true",
        help=("Expose all available API proxies and their resources. Must be "
              "explicitly specified if neither `--apis` nor `--resources` is "
              "provided."))

    proxies_group = proxies_mutex_group.add_argument_group(
        "Arguments that restrict exposed API proxies. One or both of these may "
        "be specified if `--all-proxies` is not:")

    proxies_group.add_argument(
        "--apis",
        metavar="API",
        type=arg_parsers.ArgList(),
        help="""\
Comma-separated names of API proxies to which this API product is bound. Only
those API proxies will be accessible through the new API product.

If not specified, all deployed API proxies will be included in the product, so
long as they match the other parameters.

The API proxy names must already be deployed to the bound environments, or
creation of the API product will fail.""")

    # Resource paths conform to RFC 2396's segment format, so a "," may appear
    # in one, but a "#" will not. " " or "|" would also have worked, but would
    # have been harder to read in help text (spaces ).
    proxies_group.add_argument(
        "--resources",
        metavar="RESOURCE",
        type=_HashDelimitedArgList(min_length=1),
        help="""\
API resources to be bundled in the API product, separated by `#` signs.

By default, the resource paths are mapped from the `proxy.pathsuffix` variable.

The proxy path suffix is defined as the URI fragment following the
ProxyEndpoint base path. For example, if `/forecastrss` is given as an element
of this list, and the base path defined for the API proxy is `/weather`, then
only requests to `/weather/forecastrss` are permitted by the API product.

Proxy paths can use asterisks as wildcards; `/**` indicates that all sub-URIs
are included, whereas a single asterisk indicates that only URIs one level
down are included.

By default, `/` supports the same resources as `/**` as well as the base path
defined by the API proxy.

For example, if the base path of the API proxy is `/v1/weatherapikey`, then
the API product supports requests to `/v1/weatherapikey` and to any sub-URIs,
such as `/v1/weatherapikey/forecastrss`, `/v1/weatherapikey/region/CA`, and so
on.

If not specified, all deployed API resources will be included in the product, so
long as they match the other parameters.""")

    quota_group = parser.add_argument_group(
        ("To impose a quota limit on calls to the API product, specify all of "
         "the following:"))

    quota_group.add_argument(
        "--quota",
        type=int,
        help="""The number of request messages permitted per app by this API
product for the specified `--quota-interval` and `--quota-unit`.

For example, `--quota=50 --quota-interval=12 --quota-unit=hour` means 50
requests are allowed every 12 hours.""")
    quota_group.add_argument(
        "--quota-interval",
        type=int,
        help=("The time interval over which the number of "
              "request messages is calculated."))
    quota_group.add_argument(
        "--quota-unit",
        choices=["minute", "hour", "day", "month"],
        help=("The time unit for `--quota-interval`."))

    parser.add_argument(
        "--description",
        help=("An overview of the API product. Include key information about "
              "the API product that is not captured by other fields."))

    parser.add_argument(
        "--manual-approval",
        action="store_true",
        help=("Require manual approval of developer requests to access this "
              "API product before their consumer keys can be used. If unset, "
              "the consumer key is generated in an \"approved\" state and can "
              "be used immediately."))

    parser.add_argument(
        "--oauth-scopes",
        metavar="SCOPE",
        type=arg_parsers.ArgList(),
        help=("Comma-separated list of OAuth scopes that are validated at "
              "runtime. Apigee validates that the scopes in any access token "
              "presented match the scopes defined in the OAuth policy "
              "assoicated with the API product."))

    parser.add_argument(
        "--attributes",
        metavar="NAME=VALUE",
        type=arg_parsers.ArgDict(max_length=17),
        help=("Key-value attribute pairs that may be used to extend the "
              "default API product profile with customer-specific metadata. Up "
              "to 17 attributes can be specified."))

  def Run(self, args):
    """Run the deploy command."""
    # TODO(b/150221336): add interactive mode for required arguments.
    if args.environments is None:
      raise exceptions.OneOfArgumentsRequiredException(
          ["--environments", "--all-environments"],
          "All API products must include at least one environment.")

    if args.access is None:
      raise exceptions.OneOfArgumentsRequiredException([
          "--public-access", "--private-access", "--internal-access"
      ], "All API products must specify whether they can be publicly accessed.")

    if not args.apis and not args.resources and not args.all_proxies:
      raise exceptions.OneOfArgumentsRequiredException(
          ["--apis", "--resources", "--all-proxies"],
          "All API products must include at least one API proxy or resource.")
    if args.all_proxies and args.apis:
      raise exceptions.ConflictingArgumentsException("--apis", "--all-proxies")
    if args.all_proxies and args.resources:
      raise exceptions.ConflictingArgumentsException("--resources",
                                                     "--all-proxies")

    quota_args_missing = [
        arg for arg in vars(args) if "quota" in arg and vars(args)[arg] is None
    ]
    if quota_args_missing:
      if len(quota_args_missing) < 3:
        raise exceptions.RequiredArgumentException(
            "--" + quota_args_missing[0].replace("_", "-"),
            "Must specify all quota arguments to use quotas.")
    else:
      args.quota = "%d"%args.quota
      args.quota_interval = "%d"%args.quota_interval

    attributes = [{"name": "access", "value": args.access}]
    if args.attributes:
      for key in args.attributes:
        attributes.append({"name": key, "value": args.attributes[key]})

    identifiers = args.CONCEPTS.internal_name.Parse().AsDict()

    if args.display_name is None:
      args.display_name = identifiers["apiproductsId"]

    product = apigee.ProductsInfo(
        name=identifiers["apiproductsId"],
        displayName=args.display_name,
        approvalType="manual" if args.manual_approval else "auto",
        attributes=attributes,
        description=args.description,
        apiResources=args.resources if args.resources else None,
        environments=args.environments if args.environments else None,
        proxies=args.apis if args.apis else None,
        quota=args.quota,
        quotaInterval=args.quota_interval,
        quotaTimeUnit=args.quota_unit,
        scopes=args.oauth_scopes)
    return apigee.ProductsClient.Create(identifiers, product)
