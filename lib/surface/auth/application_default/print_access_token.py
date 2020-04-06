# -*- coding: utf-8 -*- #
# Copyright 2016 Google LLC. All Rights Reserved.
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

"""A command that prints an access token for Application Default Credentials.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.auth import util as auth_util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions as c_exc
from googlecloudsdk.core import http
from googlecloudsdk.core import log
from googlecloudsdk.core import properties

from oauth2client import client
import six


class PrintAccessToken(base.Command):
  r"""Print an access token for your current Application Default Credentials.

  {command} generates and prints an access token for the current
  Application Default Credential (ADC). The ADC can be specified either by
  setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path
  of a service account key file (JSON) or using
  `gcloud auth application-default login`.

  The access token generated by {command} is useful for manually testing
  APIs via curl or similar tools.

  In order to print details of the access token, such as the associated account
  and the token's expiration time in seconds, run:

    $ curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=\
    $(gcloud auth application-default print-access-token)
  """

  @staticmethod
  def Args(parser):
    parser.display_info.AddFormat('value(access_token)')

  def Run(self, args):
    """Run the helper command."""
    impersonate_service_account = (
        properties.VALUES.auth.impersonate_service_account.Get())
    if impersonate_service_account:
      log.warning(
          "Impersonate service account '{}' is detected. This command cannot be"
          ' used to print the access token for an impersonate account. The '
          "token below is still the application default credentials' access "
          'token.'.format(impersonate_service_account))

    try:
      creds = client.GoogleCredentials.get_application_default()
    except client.ApplicationDefaultCredentialsError as e:
      log.debug(e, exc_info=True)
      raise c_exc.ToolException(six.text_type(e))

    if creds.create_scoped_required():
      creds_type = creds.serialization_data['type']
      token_uri_override = properties.VALUES.auth.token_host.Get()
      if creds_type == client.SERVICE_ACCOUNT and token_uri_override:
        creds = creds.create_scoped([auth_util.CLOUD_PLATFORM_SCOPE],
                                    token_uri=token_uri_override)
      else:
        creds = creds.create_scoped([auth_util.CLOUD_PLATFORM_SCOPE])

    access_token_info = creds.get_access_token(http.Http())
    if not access_token_info:
      raise c_exc.ToolException(
          'No access token could be obtained from the current credentials.')

    return access_token_info
