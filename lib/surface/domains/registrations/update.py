# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""`gcloud domains registrations update` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.domains import registrations
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.domains import flags
from googlecloudsdk.command_lib.domains import resource_args
from googlecloudsdk.command_lib.domains import util
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Update(base.UpdateCommand):
  """Update a Cloud Domains registration.

  Update an existing registration. Currently used for updating labels only.
  Run:

    $ gcloud help alpha domains registrations configure

  to see how to change management, DNS or contact settings.

  ## EXAMPLES

  To add a label with key ``environment'' and value ``test'' for
  ``example.com'', run:

    $ {command} example.com --update-labels="project=example,environment=test"
  """

  @staticmethod
  def Args(parser):
    resource_args.AddRegistrationResourceArg(parser, 'to update')
    labels_util.AddUpdateLabelsFlags(parser)
    flags.AddAsyncFlagToParser(parser)

  def Run(self, args):
    client = registrations.RegistrationsClient()
    args.registration = util.NormalizeResourceName(args.registration)
    registration_ref = args.CONCEPTS.registration.Parse()

    new_labels = None
    labels_diff = labels_util.Diff.FromUpdateArgs(args)
    if labels_diff.MayHaveUpdates():
      orig_resource = client.Get(registration_ref)
      new_labels = labels_diff.Apply(
          client.messages.Registration.LabelsValue,
          orig_resource.labels).GetOrNone()
    else:
      raise exceptions.Error(
          'Specify labels to update.\n'
          'Run `gcloud help alpha domains registrations configure` to see '
          'how to change management, DNS or contact settings.')

    response = client.Patch(registration_ref, labels=new_labels)

    response = util.WaitForOperation(response, args.async_)
    log.UpdatedResource(registration_ref.Name(), 'registration', args.async_)
    return response
