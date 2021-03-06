"""Generated client library for cloudresourcesearch version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudresourcesearch.v1 import cloudresourcesearch_v1_messages as messages


class CloudresourcesearchV1(base_api.BaseApiClient):
  """Generated client library for service cloudresourcesearch version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudresourcesearch.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudresourcesearch.mtls.googleapis.com/'

  _PACKAGE = 'cloudresourcesearch'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudresourcesearchV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudresourcesearch handle."""
    url = url or self.BASE_URL
    super(CloudresourcesearchV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.resources = self.ResourcesService(self)

  class ResourcesService(base_api.BaseApiService):
    """Service class for the resources resource."""

    _NAME = 'resources'

    def __init__(self, client):
      super(CloudresourcesearchV1.ResourcesService, self).__init__(client)
      self._upload_configs = {
          }

    def Search(self, request, global_params=None):
      r"""Lists accessible Google Cloud Platform resources that match a query. A.
resource is accessible to the caller if the caller has permission
to perform a GET operation on the resource.

      Args:
        request: (CloudresourcesearchResourcesSearchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchResponse) The response message.
      """
      config = self.GetMethodConfig('Search')
      return self._RunMethod(
          config, request, global_params=global_params)

    Search.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudresourcesearch.resources.search',
        ordered_params=[],
        path_params=[],
        query_params=['orderBy', 'pageSize', 'pageToken', 'query'],
        relative_path='v1/resources:search',
        request_field='',
        request_type_name='CloudresourcesearchResourcesSearchRequest',
        response_type_name='SearchResponse',
        supports_download=False,
    )
