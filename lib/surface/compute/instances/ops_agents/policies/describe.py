# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""Implements command to delete a specified guest policy."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.api_lib.compute.instances.ops_agents.converters import guest_policy_to_ops_agents_policy_converter as to_ops_agents
from googlecloudsdk.api_lib.compute.instances.ops_agents.policies import exceptions as policy_exceptions
from googlecloudsdk.api_lib.compute.instances.ops_agents.validators import guest_policy_validator
from googlecloudsdk.api_lib.compute.os_config import utils as osconfig_api_utils
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions as calliope_exceptions
from googlecloudsdk.command_lib.compute.instances.ops_agents.policies import parser_utils
from googlecloudsdk.command_lib.compute.os_config import utils as osconfig_command_utils
from googlecloudsdk.core import properties


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Describe(base.DescribeCommand):
  """Describe a policy that manages Google Cloud Operations Suite agents across Google Cloud Compute instances."""

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
          To describe an Ops agents policy named ``policy1'' in the current project, run:

            $ {command} policy1
          """,
  }

  @staticmethod
  def Args(parser):
    """See base class."""
    parser_utils.AddSharedArgs(parser)

  def Run(self, args):
    """See base class."""
    release_track = self.ReleaseTrack()

    project = properties.VALUES.core.project.GetOrFail()
    guest_policy_uri_path = osconfig_command_utils.GetGuestPolicyUriPath(
        'projects', project, args.POLICY_ID)
    client = osconfig_api_utils.GetClientInstance(
        release_track, api_version_override='v1beta')
    service = client.projects_guestPolicies
    messages = osconfig_api_utils.GetClientMessages(
        release_track, api_version_override='v1beta')

    get_request = messages.OsconfigProjectsGuestPoliciesGetRequest(
        name=guest_policy_uri_path)
    try:
      get_response = service.Get(get_request)
    except apitools_exceptions.HttpNotFoundError:
      raise policy_exceptions.NotFoundError(policy_id=args.POLICY_ID)
    if not guest_policy_validator.IsOpsAgentPolicy(get_response):
      raise policy_exceptions.NotFoundError(policy_id=args.POLICY_ID)
    try:
      ops_agents_policy = to_ops_agents.ConvertGuestPolicyToOpsAgentPolicy(
          get_response)
    except calliope_exceptions.BadArgumentException:
      raise policy_exceptions.MalformedError(policy_id=args.POLICY_ID)
    return ops_agents_policy
