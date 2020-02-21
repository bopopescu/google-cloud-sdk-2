"""Generated client library for servicenetworking version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.servicenetworking.v1 import servicenetworking_v1_messages as messages


class ServicenetworkingV1(base_api.BaseApiClient):
  """Generated client library for service servicenetworking version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://servicenetworking.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'servicenetworking'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/service.management']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ServicenetworkingV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new servicenetworking handle."""
    url = url or self.BASE_URL
    super(ServicenetworkingV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.services_connections = self.ServicesConnectionsService(self)
    self.services = self.ServicesService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(ServicenetworkingV1.OperationsService, self).__init__(client)
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
        request: (ServicenetworkingOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'servicenetworking.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'ServicenetworkingOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (ServicenetworkingOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'servicenetworking.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'ServicenetworkingOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (ServicenetworkingOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'servicenetworking.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'ServicenetworkingOperationsGetRequest',
        response_type_name=u'Operation',
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
        request: (ServicenetworkingOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations',
        http_method=u'GET',
        method_id=u'servicenetworking.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'ServicenetworkingOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ServicesConnectionsService(base_api.BaseApiService):
    """Service class for the services_connections resource."""

    _NAME = u'services_connections'

    def __init__(self, client):
      super(ServicenetworkingV1.ServicesConnectionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a private connection that establishes a VPC Network Peering.
connection to a VPC network in the service producer's organization.
The administrator of the service consumer's VPC network invokes this
method. The administrator must assign one or more allocated IP ranges for
provisioning subnetworks in the service producer's VPC network. This
connection is used for all supported services in the service producer's
organization, so it only needs to be invoked once. The response from the
`get` operation will be of type `Connection` if the operation successfully
completes.

      Args:
        request: (ServicenetworkingServicesConnectionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}/connections',
        http_method=u'POST',
        method_id=u'servicenetworking.services.connections.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/connections',
        request_field=u'connection',
        request_type_name=u'ServicenetworkingServicesConnectionsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List the private connections that are configured in a service consumer's.
VPC network.

      Args:
        request: (ServicenetworkingServicesConnectionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}/connections',
        http_method=u'GET',
        method_id=u'servicenetworking.services.connections.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'network'],
        relative_path=u'v1/{+parent}/connections',
        request_field='',
        request_type_name=u'ServicenetworkingServicesConnectionsListRequest',
        response_type_name=u'ListConnectionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the allocated ranges that are assigned to a connection.
The response from the `get` operation will be of type `Connection` if the
operation successfully completes.

      Args:
        request: (ServicenetworkingServicesConnectionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}/connections/{connectionsId}',
        http_method=u'PATCH',
        method_id=u'servicenetworking.services.connections.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'force', u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'connection',
        request_type_name=u'ServicenetworkingServicesConnectionsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ServicesService(base_api.BaseApiService):
    """Service class for the services resource."""

    _NAME = u'services'

    def __init__(self, client):
      super(ServicenetworkingV1.ServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def AddSubnetwork(self, request, global_params=None):
      r"""For service producers, provisions a new subnet in a.
peered service's shared VPC network in the requested region and with the
requested size that's expressed as a CIDR range (number of leading bits of
ipV4 network mask). The method checks against the assigned allocated ranges
to find a non-conflicting IP address range. The method will reuse a subnet
if subsequent calls contain the same subnet name, region, and prefix
length. This method will make producer's tenant project to be a shared VPC
service project as needed. The response from the `get` operation will be of
type `Subnetwork` if the operation successfully completes.

      Args:
        request: (ServicenetworkingServicesAddSubnetworkRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddSubnetwork')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddSubnetwork.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}/{servicesId1}/{servicesId2}:addSubnetwork',
        http_method=u'POST',
        method_id=u'servicenetworking.services.addSubnetwork',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:addSubnetwork',
        request_field=u'addSubnetworkRequest',
        request_type_name=u'ServicenetworkingServicesAddSubnetworkRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def DisableVpcServiceControls(self, request, global_params=None):
      r"""Disables VPC service controls for a connection.

      Args:
        request: (ServicenetworkingServicesDisableVpcServiceControlsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('DisableVpcServiceControls')
      return self._RunMethod(
          config, request, global_params=global_params)

    DisableVpcServiceControls.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}:disableVpcServiceControls',
        http_method=u'PATCH',
        method_id=u'servicenetworking.services.disableVpcServiceControls',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:disableVpcServiceControls',
        request_field=u'disableVpcServiceControlsRequest',
        request_type_name=u'ServicenetworkingServicesDisableVpcServiceControlsRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def EnableVpcServiceControls(self, request, global_params=None):
      r"""Enables VPC service controls for a connection.

      Args:
        request: (ServicenetworkingServicesEnableVpcServiceControlsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('EnableVpcServiceControls')
      return self._RunMethod(
          config, request, global_params=global_params)

    EnableVpcServiceControls.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}:enableVpcServiceControls',
        http_method=u'PATCH',
        method_id=u'servicenetworking.services.enableVpcServiceControls',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:enableVpcServiceControls',
        request_field=u'enableVpcServiceControlsRequest',
        request_type_name=u'ServicenetworkingServicesEnableVpcServiceControlsRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SearchRange(self, request, global_params=None):
      r"""Service producers can use this method to find a currently unused range.
within consumer allocated ranges.   This returned range is not reserved,
and not guaranteed to remain unused.
It will validate previously provided allocated ranges, find
non-conflicting sub-range of requested size (expressed in
number of leading bits of ipv4 network mask, as in CIDR range
notation).
Operation<response: Range>

      Args:
        request: (ServicenetworkingServicesSearchRangeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SearchRange')
      return self._RunMethod(
          config, request, global_params=global_params)

    SearchRange.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}:searchRange',
        http_method=u'POST',
        method_id=u'servicenetworking.services.searchRange',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:searchRange',
        request_field=u'searchRangeRequest',
        request_type_name=u'ServicenetworkingServicesSearchRangeRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Validate(self, request, global_params=None):
      r"""Service producers use this method to validate if the consumer provided.
network, project and the requested range is valid. This allows them to use
a fail-fast mechanism for consumer requests, and not have to wait for
AddSubnetwork operation completion to determine if user request is invalid.

      Args:
        request: (ServicenetworkingServicesValidateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ValidateConsumerConfigResponse) The response message.
      """
      config = self.GetMethodConfig('Validate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Validate.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/services/{servicesId}:validate',
        http_method=u'POST',
        method_id=u'servicenetworking.services.validate',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:validate',
        request_field=u'validateConsumerConfigRequest',
        request_type_name=u'ServicenetworkingServicesValidateRequest',
        response_type_name=u'ValidateConsumerConfigResponse',
        supports_download=False,
    )
