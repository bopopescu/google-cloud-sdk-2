"""Generated client library for networkmanagement version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.networkmanagement.v1 import networkmanagement_v1_messages as messages


class NetworkmanagementV1(base_api.BaseApiClient):
  """Generated client library for service networkmanagement version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://networkmanagement.googleapis.com/'
  MTLS_BASE_URL = 'https://networkmanagement.mtls.googleapis.com/'

  _PACKAGE = 'networkmanagement'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'NetworkmanagementV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new networkmanagement handle."""
    url = url or self.BASE_URL
    super(NetworkmanagementV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_global_connectivityTests = self.ProjectsLocationsGlobalConnectivityTestsService(self)
    self.projects_locations_global_operations = self.ProjectsLocationsGlobalOperationsService(self)
    self.projects_locations_global = self.ProjectsLocationsGlobalService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsGlobalConnectivityTestsService(base_api.BaseApiService):
    """Service class for the projects_locations_global_connectivityTests resource."""

    _NAME = 'projects_locations_global_connectivityTests'

    def __init__(self, client):
      super(NetworkmanagementV1.ProjectsLocationsGlobalConnectivityTestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Connectivity Test.
After you create a test, the reachability analysis is performed as part
of the long running operation, which completes when the analysis completes.

If the endpoint specifications in `ConnectivityTest` are invalid
(for example, containing non-existent resources in the network, or you
don't have read permissions to the network configurations of listed
projects), then the reachability result returns a value of `UNKNOWN`.

If the endpoint specifications in `ConnectivityTest` are
incomplete, the reachability result returns a value of
<code>AMBIGUOUS</code>. For more information,
see the Connectivity Test documentation.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests',
        http_method='POST',
        method_id='networkmanagement.projects.locations.global.connectivityTests.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['testId'],
        relative_path='v1/{+parent}/connectivityTests',
        request_field='connectivityTest',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a specific `ConnectivityTest`.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}',
        http_method='DELETE',
        method_id='networkmanagement.projects.locations.global.connectivityTests.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the details of a specific Connectivity Test.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ConnectivityTest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}',
        http_method='GET',
        method_id='networkmanagement.projects.locations.global.connectivityTests.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsGetRequest',
        response_type_name='ConnectivityTest',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}:getIamPolicy',
        http_method='GET',
        method_id='networkmanagement.projects.locations.global.connectivityTests.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all Connectivity Tests owned by a project.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectivityTestsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests',
        http_method='GET',
        method_id='networkmanagement.projects.locations.global.connectivityTests.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/connectivityTests',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsListRequest',
        response_type_name='ListConnectivityTestsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the configuration of an existing `ConnectivityTest`.
After you update a test, the reachability analysis is performed as part
of the long running operation, which completes when the analysis completes.
The Reachability state in the test resource is updated with the new result.

If the endpoint specifications in `ConnectivityTest` are invalid
(for example, they contain non-existent resources in the network, or the
user does not have read permissions to the network configurations of
listed projects), then the reachability result returns a value of
<code>UNKNOWN</code>.

If the endpoint specifications in `ConnectivityTest` are incomplete, the
reachability result returns a value of `AMBIGUOUS`. See the documentation
in `ConnectivityTest` for for more details.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}',
        http_method='PATCH',
        method_id='networkmanagement.projects.locations.global.connectivityTests.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='connectivityTest',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Rerun(self, request, global_params=None):
      r"""Rerun an existing `ConnectivityTest`.
After the user triggers the rerun, the reachability analysis is performed
as part of the long running operation, which completes when the analysis
completes.

Even though the test configuration remains the same, the reachability
result may change due to underlying network configuration changes.

If the endpoint specifications in `ConnectivityTest` become invalid (for
example, specified resources are deleted in the network, or you lost
read permissions to the network configurations of listed projects), then
the reachability result returns a value of `UNKNOWN`.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsRerunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Rerun')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rerun.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}:rerun',
        http_method='POST',
        method_id='networkmanagement.projects.locations.global.connectivityTests.rerun',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:rerun',
        request_field='rerunConnectivityTestRequest',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsRerunRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}:setIamPolicy',
        http_method='POST',
        method_id='networkmanagement.projects.locations.global.connectivityTests.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalConnectivityTestsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/connectivityTests/{connectivityTestsId}:testIamPermissions',
        http_method='POST',
        method_id='networkmanagement.projects.locations.global.connectivityTests.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='NetworkmanagementProjectsLocationsGlobalConnectivityTestsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsGlobalOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_global_operations resource."""

    _NAME = 'projects_locations_global_operations'

    def __init__(self, client):
      super(NetworkmanagementV1.ProjectsLocationsGlobalOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='networkmanagement.projects.locations.global.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='NetworkmanagementProjectsLocationsGlobalOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/operations/{operationsId}',
        http_method='DELETE',
        method_id='networkmanagement.projects.locations.global.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/operations/{operationsId}',
        http_method='GET',
        method_id='networkmanagement.projects.locations.global.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (NetworkmanagementProjectsLocationsGlobalOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/global/operations',
        http_method='GET',
        method_id='networkmanagement.projects.locations.global.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGlobalOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsGlobalService(base_api.BaseApiService):
    """Service class for the projects_locations_global resource."""

    _NAME = 'projects_locations_global'

    def __init__(self, client):
      super(NetworkmanagementV1.ProjectsLocationsGlobalService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(NetworkmanagementV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (NetworkmanagementProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='networkmanagement.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (NetworkmanagementProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='networkmanagement.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='NetworkmanagementProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(NetworkmanagementV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
