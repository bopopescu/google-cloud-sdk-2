"""Generated client library for labelmanager version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.labelmanager.v1alpha1 import labelmanager_v1alpha1_messages as messages


class LabelmanagerV1alpha1(base_api.BaseApiClient):
  """Generated client library for service labelmanager version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://labelmanager.googleapis.com/'
  MTLS_BASE_URL = u'https://labelmanager.mtls.googleapis.com/'

  _PACKAGE = u'labelmanager'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = u'google-cloud-sdk'
  _CLIENT_CLASS_NAME = u'LabelmanagerV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new labelmanager handle."""
    url = url or self.BASE_URL
    super(LabelmanagerV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.labelBindings = self.LabelBindingsService(self)
    self.labelKeys = self.LabelKeysService(self)
    self.labelValues = self.LabelValuesService(self)
    self.operations = self.OperationsService(self)

  class LabelBindingsService(base_api.BaseApiService):
    """Service class for the labelBindings resource."""

    _NAME = u'labelBindings'

    def __init__(self, client):
      super(LabelmanagerV1alpha1.LabelBindingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a LabelBinding between a LabelValue and a cloud resource.
(currently Project, Folder, or Organization).

      Args:
        request: (LabelBinding) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'labelmanager.labelBindings.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1alpha1/labelBindings',
        request_field='<request>',
        request_type_name=u'LabelBinding',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a LabelBinding.

      Args:
        request: (LabelmanagerLabelBindingsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelBindings/{labelBindingsId}',
        http_method=u'DELETE',
        method_id=u'labelmanager.labelBindings.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'LabelmanagerLabelBindingsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the LabelBindings for the given LabelValue or cloud resource.
(currently Project, Folder, or Organization) determined by the given
filter.

List LabelBindings for LabelValue with id 123 will map to:
/v1alpha1/labelBindings?filter=labelValue:labelValues/123
List LabelBindings for Project resource with id 456 will map to:
/v1alpha1/labelBindings?filter=resource://cloudresourcemanager.googleapis.com/projects/456
because the full resource name is required.

For additional details see:
https://cloud.google.com/apis/design/resource_names#full_resource_name.

      Args:
        request: (LabelmanagerLabelBindingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLabelBindingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'labelmanager.labelBindings.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/labelBindings',
        request_field='',
        request_type_name=u'LabelmanagerLabelBindingsListRequest',
        response_type_name=u'ListLabelBindingsResponse',
        supports_download=False,
    )

  class LabelKeysService(base_api.BaseApiService):
    """Service class for the labelKeys resource."""

    _NAME = u'labelKeys'

    def __init__(self, client):
      super(LabelmanagerV1alpha1.LabelKeysService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new LabelKey. If another request with the same parameters is.
sent while the original request is in process, the second request
will receive an error. A maximum of 300 LabelKeys (with any lifecycle
state) can exist under a parent at any given time.

      Args:
        request: (LabelKey) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'labelmanager.labelKeys.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1alpha1/labelKeys',
        request_field='<request>',
        request_type_name=u'LabelKey',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Requests deletion of a LabelKey. The LabelKey is moved into the.
DELETE_REQUESTED state
immediately, and is deleted approximately 30 days later. The LabelKey
cannot be deleted if it has any child LabelValues in the
ACTIVE state.

      Args:
        request: (LabelmanagerLabelKeysDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}',
        http_method=u'DELETE',
        method_id=u'labelmanager.labelKeys.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'LabelmanagerLabelKeysDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves a LabelKey. This method will return PERMISSION_DENIED if the.
key does not exist or the user does not have permission to view it.

      Args:
        request: (LabelmanagerLabelKeysGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LabelKey) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}',
        http_method=u'GET',
        method_id=u'labelmanager.labelKeys.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'LabelmanagerLabelKeysGetRequest',
        response_type_name=u'LabelKey',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (LabelmanagerLabelKeysGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'labelmanager.labelKeys.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1alpha1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'LabelmanagerLabelKeysGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all LabelKeys for a parent resource.

      Args:
        request: (LabelmanagerLabelKeysListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLabelKeysResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'labelmanager.labelKeys.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'pageSize', u'pageToken', u'parent', u'showDeleted'],
        relative_path=u'v1alpha1/labelKeys',
        request_field='',
        request_type_name=u'LabelmanagerLabelKeysListRequest',
        response_type_name=u'ListLabelKeysResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the attributes of the LabelKey resource.

      Args:
        request: (LabelmanagerLabelKeysPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}',
        http_method=u'PATCH',
        method_id=u'labelmanager.labelKeys.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'labelKey',
        request_type_name=u'LabelmanagerLabelKeysPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (LabelmanagerLabelKeysSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'labelmanager.labelKeys.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'LabelmanagerLabelKeysSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (LabelmanagerLabelKeysTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'labelmanager.labelKeys.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'LabelmanagerLabelKeysTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Undelete(self, request, global_params=None):
      r"""Cancels the deletion request for a LabelKey. This method may only be.
called on a LabelKey in the
DELETE_REQUESTED state.
In order to succeed, the LabelKey's parent must be in the active state.

      Args:
        request: (LabelmanagerLabelKeysUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Undelete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelKeys/{labelKeysId}:undelete',
        http_method=u'POST',
        method_id=u'labelmanager.labelKeys.undelete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}:undelete',
        request_field=u'undeleteLabelKeyRequest',
        request_type_name=u'LabelmanagerLabelKeysUndeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class LabelValuesService(base_api.BaseApiService):
    """Service class for the labelValues resource."""

    _NAME = u'labelValues'

    def __init__(self, client):
      super(LabelmanagerV1alpha1.LabelValuesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a LabelValue as a child of the specified LabelKey. If a another.
request with the same parameters is sent while the original request is in
process the second request will receive an error. A maximum of 300
LabelValues (with any lifecycle state) can exist under a LabelKey at any
given time.

      Args:
        request: (LabelValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'labelmanager.labelValues.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1alpha1/labelValues',
        request_field='<request>',
        request_type_name=u'LabelValue',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Requests deletion of a LabelValue. The LabelValue is moved into the.
DELETE_REQUESTED state
immediately, and is deleted approximately 30 days later. The LabelValue
cannot have any bindings when it is deleted.

      Args:
        request: (LabelmanagerLabelValuesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelValues/{labelValuesId}',
        http_method=u'DELETE',
        method_id=u'labelmanager.labelValues.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'LabelmanagerLabelValuesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves LabelValue. This method will return PERMISSION_DENIED if the.
LabelValue does not exist or the user does not have permission to view it.

      Args:
        request: (LabelmanagerLabelValuesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LabelValue) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelValues/{labelValuesId}',
        http_method=u'GET',
        method_id=u'labelmanager.labelValues.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'LabelmanagerLabelValuesGetRequest',
        response_type_name=u'LabelValue',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all LabelValues for a specific LabelKey.

      Args:
        request: (LabelmanagerLabelValuesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLabelValuesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'labelmanager.labelValues.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'pageSize', u'pageToken', u'parent', u'showDeleted'],
        relative_path=u'v1alpha1/labelValues',
        request_field='',
        request_type_name=u'LabelmanagerLabelValuesListRequest',
        response_type_name=u'ListLabelValuesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the attributes of the LabelValue resource.

      Args:
        request: (LabelmanagerLabelValuesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelValues/{labelValuesId}',
        http_method=u'PATCH',
        method_id=u'labelmanager.labelValues.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'labelValue',
        request_type_name=u'LabelmanagerLabelValuesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Undelete(self, request, global_params=None):
      r"""Cancels the deletion request for a LabelValue. This method may only be.
called on a LabelValue in the
DELETE_REQUESTED state.
In order to succeed, the LabelValue's parent must be in the
ACTIVE state.

      Args:
        request: (LabelmanagerLabelValuesUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Undelete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/labelValues/{labelValuesId}:undelete',
        http_method=u'POST',
        method_id=u'labelmanager.labelValues.undelete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}:undelete',
        request_field=u'undeleteLabelValueRequest',
        request_type_name=u'LabelmanagerLabelValuesUndeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(LabelmanagerV1alpha1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (LabelmanagerOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'labelmanager.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'LabelmanagerOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )
