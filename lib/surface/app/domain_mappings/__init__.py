# Copyright 2017 Google Inc. All Rights Reserved.
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
"""The gcloud app domain-mappings group."""

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.GA)
class DomainMappings(base.Group):
  """View and manage your App Engine domain mappings.

  This set of commands can be used to view and manage your app's
  domain mappings.

  App Engine Domain Mappings allow an application to be served via one or many
  custom domains, such as `example.com`, instead of the default `appspot.com`
  address. You can use a custom domain with or without SSL.
  """

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
          To list your App Engine domains, run:

            $ {command} list
      """,
  }


@base.ReleaseTracks(base.ReleaseTrack.ALPHA,
                    base.ReleaseTrack.BETA)
class DomainMappingsAlpha(base.Group):
  """View and manage your App Engine domain mappings.

  This set of commands can be used to view and manage your app's
  domain mappings.

  App Engine Domain Mappings allow an application to be served via one or many
  custom domains, such as `example.com`, instead of the default `appspot.com`
  address. You can use a custom domain with or without SSL. Additionally use the
  AUTOMATIC management type to automatically provision an SSL certificate for
  your domain.
  """

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
          To list your App Engine domains, run:

            $ {command} list

          To create a domain with an automatically managed certiticate, run:

            $ {command} create 'example.com' --ssl-management-type=AUTOMATIC
      """,
  }
