# Copyright 2015 Google Inc. All Rights Reserved.

"""A library to find a Tool Results History to publish results to."""

from googlecloudsdk.api_lib.test import util
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.third_party.apitools.base.py import exceptions as apitools_exceptions


class ToolResultsHistoryPicker(object):
  """Finds a History to publish mobile test results to.
  """

  def __init__(self, project, client, messages):
    """Construct a ToolResultsHistoryPicker.

    Args:
      project: string containing the GCE project id.
      client: ToolResults API client lib generated by apitools.
      messages: ToolResults API message classes generated by apitools.
    """
    self._project = project
    self._client = client
    self._messages = messages

  def _ListHistoriesByName(self, history_name):
    """Lists histories by name using the Tool Results API.

    Args:
       history_name: string containing the history name.

    Returns:
      A list of histories matching the name.

    Raises:
      HttpException if the Tool Results service reports a backend error.
    """
    request = self._messages.ToolresultsProjectsHistoriesListRequest(
        projectId=self._project, filterByName=history_name)
    try:
      response = self._client.projects_histories.List(request)
      log.debug('\nToolResultsHistories.List response:\n{0}\n'.format(response))
      return response
    except apitools_exceptions.HttpError as error:
      msg = ('Http error while getting list of Tool Results Histories:\n{0}'
             .format(util.GetError(error)))
      raise exceptions.HttpException(msg)

  def _CreateHistory(self, history_name):
    """Creates a History using the Tool Results API.

    Args:
       history_name: string containing the name of the history to create.

    Returns:
      The history id of the created history.

    Raises:
      HttpException if the Tool Results service reports a backend error.
    """
    history = self._messages.History(name=history_name)
    request = self._messages.ToolresultsProjectsHistoriesCreateRequest(
        projectId=self._project, history=history)
    try:
      response = self._client.projects_histories.Create(request)
      log.debug('\nToolResultsHistories.Create response:\n{0}\n'
                .format(response))
      return response
    except apitools_exceptions.HttpError as error:
      msg = ('Http error while creating a Tool Results History:\n{0}'
             .format(util.GetError(error)))
      raise exceptions.HttpException(msg)

  def _GetToolResultsHistoryId(self, history_name):
    """Gets the history id associated with a given history name.

    All the test executions for the same app should be in the same history. This
    method will try to find an existing history for the application or create
    one if necessary.

    Args:
       history_name: string containing the history's name.

    Returns:
      The id of the history to publish results to.
    """
    histories = self._ListHistoriesByName(history_name).histories

    if histories:
      # There might be several histories with the same name. We always pick the
      # first history which is the history with the most recent results.
      return histories[0].historyId
    else:
      new_history = self._CreateHistory(history_name)
      return new_history.historyId

  def FindToolResultsHistoryId(self, args):
    """Returns the Tool Results history ID to publish results to.

    The history ID corresponds to a history name. If the user provides their
    own history name, we use that to look up a history ID; If not, but the user
    provides an app-package name, we use the app-package name with ' (gcloud)'
    appended as the history name. Otherwise, we punt and let the Testing service
    determine the appropriate history ID to publish to.

    Args:
      args: an argparse namespace. All the arguments that were provided to the
        command invocation (i.e. group and command arguments combined).

    Returns:
      Either a string containing a history ID to publish to, or None if we lack
      the required information to find the ID and therefore need the Testing
      service to provide the ID for us.
    """
    if args.results_history_name:
      history_name = args.results_history_name
    elif args.app_package:
      history_name = args.app_package + ' (gcloud)'
    else:
      return None
    return self._GetToolResultsHistoryId(history_name)
