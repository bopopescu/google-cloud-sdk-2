"""Generated client library for recommender version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.recommender.v1beta1 import recommender_v1beta1_messages as messages


class RecommenderV1beta1(base_api.BaseApiClient):
  """Generated client library for service recommender version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://recommender.googleapis.com/'

  _PACKAGE = u'recommender'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'RecommenderV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new recommender handle."""
    url = url or self.BASE_URL
    super(RecommenderV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_recommenders_recommendations = self.ProjectsLocationsRecommendersRecommendationsService(self)
    self.projects_locations_recommenders = self.ProjectsLocationsRecommendersService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsRecommendersRecommendationsService(base_api.BaseApiService):
    """Service class for the projects_locations_recommenders_recommendations resource."""

    _NAME = u'projects_locations_recommenders_recommendations'

    def __init__(self, client):
      super(RecommenderV1beta1.ProjectsLocationsRecommendersRecommendationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the requested recommendation and requires the recommender.*.get.
IAM permission.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1beta1Recommendation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}',
        http_method=u'GET',
        method_id=u'recommender.projects.locations.recommenders.recommendations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'RecommenderProjectsLocationsRecommendersRecommendationsGetRequest',
        response_type_name=u'GoogleCloudRecommenderV1beta1Recommendation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists recommendations for a Cloud project and requires the.
recommender.*.list IAM permission.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1beta1ListRecommendationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations',
        http_method=u'GET',
        method_id=u'recommender.projects.locations.recommenders.recommendations.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/recommendations',
        request_field='',
        request_type_name=u'RecommenderProjectsLocationsRecommendersRecommendationsListRequest',
        response_type_name=u'GoogleCloudRecommenderV1beta1ListRecommendationsResponse',
        supports_download=False,
    )

    def MarkClaimed(self, request, global_params=None):
      r"""Mark the Recommendation State as Claimed. Users can use this method to.
indicate to the Recommender API that they are starting to apply the
recommendation themselves. This stops the recommendation content from being
updated.

MarkClaimed can be applied to recommendations in CLAIMED, or ACTIVE state.

recommender.*.update IAM permission is required to make this change.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsMarkClaimedRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1beta1Recommendation) The response message.
      """
      config = self.GetMethodConfig('MarkClaimed')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkClaimed.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}:markClaimed',
        http_method=u'POST',
        method_id=u'recommender.projects.locations.recommenders.recommendations.markClaimed',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:markClaimed',
        request_field=u'googleCloudRecommenderV1beta1MarkRecommendationClaimedRequest',
        request_type_name=u'RecommenderProjectsLocationsRecommendersRecommendationsMarkClaimedRequest',
        response_type_name=u'GoogleCloudRecommenderV1beta1Recommendation',
        supports_download=False,
    )

    def MarkFailed(self, request, global_params=None):
      r"""Mark the Recommendation State as Failed. Users can use this method to.
indicate to the Recommender API that they have applied the recommendation
themselves, and the operation failed. This stops the recommendation content
from being updated.

MarkFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED,
or FAILED state.

recommender.*.update IAM permission is required to make this change.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsMarkFailedRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1beta1Recommendation) The response message.
      """
      config = self.GetMethodConfig('MarkFailed')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkFailed.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}:markFailed',
        http_method=u'POST',
        method_id=u'recommender.projects.locations.recommenders.recommendations.markFailed',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:markFailed',
        request_field=u'googleCloudRecommenderV1beta1MarkRecommendationFailedRequest',
        request_type_name=u'RecommenderProjectsLocationsRecommendersRecommendationsMarkFailedRequest',
        response_type_name=u'GoogleCloudRecommenderV1beta1Recommendation',
        supports_download=False,
    )

    def MarkSucceeded(self, request, global_params=None):
      r"""Mark the Recommendation State as Succeeded. Users can use this method to.
indicate to the Recommender API that they have applied the recommendation
themselves, and the operation was successful. This stops the recommendation
content from being updated.

MarkSucceeded can be applied to recommendations in ACTIVE, CLAIMED,
SUCCEEDED, or FAILED state.

recommender.*.update IAM permission is required to make this change.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsMarkSucceededRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1beta1Recommendation) The response message.
      """
      config = self.GetMethodConfig('MarkSucceeded')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkSucceeded.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}:markSucceeded',
        http_method=u'POST',
        method_id=u'recommender.projects.locations.recommenders.recommendations.markSucceeded',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:markSucceeded',
        request_field=u'googleCloudRecommenderV1beta1MarkRecommendationSucceededRequest',
        request_type_name=u'RecommenderProjectsLocationsRecommendersRecommendationsMarkSucceededRequest',
        response_type_name=u'GoogleCloudRecommenderV1beta1Recommendation',
        supports_download=False,
    )

  class ProjectsLocationsRecommendersService(base_api.BaseApiService):
    """Service class for the projects_locations_recommenders resource."""

    _NAME = u'projects_locations_recommenders'

    def __init__(self, client):
      super(RecommenderV1beta1.ProjectsLocationsRecommendersService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(RecommenderV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(RecommenderV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
