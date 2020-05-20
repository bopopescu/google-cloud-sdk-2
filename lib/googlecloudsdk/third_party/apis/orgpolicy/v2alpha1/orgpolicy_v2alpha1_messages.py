"""Generated message classes for orgpolicy version v2alpha1.

The Org Policy API allows users to configure governance ruleson their GCP
resources across the Cloud Resource Hierarchy.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'orgpolicy'


class GoogleCloudOrgpolicyV2alpha1AlternatePolicySpec(_messages.Message):
  r"""A GoogleCloudOrgpolicyV2alpha1AlternatePolicySpec object.

  Fields:
    launch: Reference to the launch that will be used while audit logging and
      to control the launch. Should be set only in the alternate policy.
    spec: A GoogleCloudOrgpolicyV2alpha1PolicySpec attribute.
  """

  launch = _messages.StringField(1)
  spec = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1PolicySpec', 2)


class GoogleCloudOrgpolicyV2alpha1Constraint(_messages.Message):
  r"""A `Constraint` describes a way in which a resource's configuration can
  be restricted. For example, it controls which cloud services can be
  activated across an organization, or whether a Compute Engine instance can
  have serial port connections established. `Constraints` can be configured by
  the organization's policy adminstrator to fit the needs of the organzation
  by setting Policies for `Constraints` at different locations in the
  organization's resource hierarchy. Policies are inherited down the resource
  hierarchy from higher levels, but can also be overridden. For details about
  the inheritance rules please read about Policies.  `Constraints` have a
  default behavior determined by the `constraint_default` field, which is the
  enforcement behavior that is used in the absence of a `Policy` being defined
  or inherited for the resource in question.

  Enums:
    ConstraintDefaultValueValuesEnum: The evaluation behavior of this
      constraint in the absense of 'Policy'.

  Fields:
    booleanConstraint: Defines this constraint as being a BooleanConstraint.
    constraintDefault: The evaluation behavior of this constraint in the
      absense of 'Policy'.
    description: Detailed description of what this `Constraint` controls as
      well as how and where it is enforced.  Mutable.
    displayName: The human readable name.  Mutable.
    listConstraint: Defines this constraint as being a ListConstraint.
    name: The resource name of the Constraint. Must be in one of the following
      forms: * `projects/{project_number}/constraints/{constraint_name}` *
      `folders/{folder_id}/constraints/{constraint_name}` *
      `organizations/{organization_id}/constraints/{constraint_name}`  For
      example, "/projects/123/constraints/compute.disableSerialPortAccess".
      Immutable.
  """

  class ConstraintDefaultValueValuesEnum(_messages.Enum):
    r"""The evaluation behavior of this constraint in the absense of 'Policy'.

    Values:
      CONSTRAINT_DEFAULT_UNSPECIFIED: This is only used for distinguishing
        unset values and should never be used.
      ALLOW: Indicate that all values are allowed for list constraints.
        Indicate that enforcement is off for boolean constraints.
      DENY: Indicate that all values are denied for list constraints. Indicate
        that enforcement is on for boolean constraints.
    """
    CONSTRAINT_DEFAULT_UNSPECIFIED = 0
    ALLOW = 1
    DENY = 2

  booleanConstraint = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1ConstraintBooleanConstraint', 1)
  constraintDefault = _messages.EnumField('ConstraintDefaultValueValuesEnum', 2)
  description = _messages.StringField(3)
  displayName = _messages.StringField(4)
  listConstraint = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1ConstraintListConstraint', 5)
  name = _messages.StringField(6)


class GoogleCloudOrgpolicyV2alpha1ConstraintBooleanConstraint(_messages.Message):
  r"""A `Constraint` that is either enforced or not.  For example a constraint
  `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM
  instance, serial port connections will not be opened to that instance.
  """



class GoogleCloudOrgpolicyV2alpha1ConstraintListConstraint(_messages.Message):
  r"""A `Constraint` that allows or disallows a list of string values, which
  are configured by an Organization's policy administrator with a `Policy`.

  Fields:
    supportsIn: Indicates whether values grouped into categories can be used
      in `Policy.allowed_values` and `Policy.denied_values`. For example,
      `"in:Python"` would match any value in the 'Python' group.
    supportsUnder: Indicates whether subtrees of Cloud Resource Manager
      resource hierarchy can be used in `Policy.allowed_values` and
      `Policy.denied_values`. For example, `"under:folders/123"` would match
      any resource under the 'folders/123' folder.
  """

  supportsIn = _messages.BooleanField(1)
  supportsUnder = _messages.BooleanField(2)


class GoogleCloudOrgpolicyV2alpha1ListConstraintsResponse(_messages.Message):
  r"""The response returned from the ListConstraints method.

  Fields:
    constraints: The collection of constraints that are available on the
      targeted resource.
    nextPageToken: Page token used to retrieve the next page. This is
      currently not used.
  """

  constraints = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1Constraint', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudOrgpolicyV2alpha1ListPoliciesResponse(_messages.Message):
  r"""The response returned from the ListPolicies method. It will be empty if
  no `Policies` are set on the resource.

  Fields:
    nextPageToken: Page token used to retrieve the next page. This is
      currently not used, but the server may at any point start supplying a
      valid token.
    policies: All `Policies` that exist on the resource. It will be empty if
      no `Policies` are set.
  """

  nextPageToken = _messages.StringField(1)
  policies = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1Policy', 2, repeated=True)


class GoogleCloudOrgpolicyV2alpha1Policy(_messages.Message):
  r"""Defines a Cloud Organization `Policy` which is used to specify
  `Constraints` for configurations of Cloud Platform resources.

  Fields:
    alternate: An alternate policy configuration that will be used instead of
      the baseline policy configurations as determined by the launch.
      Currently the only way the launch can trigger the alternate
      configuration is via dry-run/dark.
    name: Immutable. The resource name of the Policy. Must be one of the
      following forms, where constraint_name is the name of the constraint
      which this Policy configures: *
      `projects/{project_number}/policies/{constraint_name}` *
      `folders/{folder_id}/policies/{constraint_name}` *
      `organizations/{organization_id}/policies/{constraint_name}`  For
      example, "projects/123/policies/compute.disableSerialPortAccess".  Note:
      `projects/{project_id}/policies/{constraint_name}` is also an acceptable
      name for API requests, but responses will return the name using the
      equivalent project number.
    spec: A GoogleCloudOrgpolicyV2alpha1PolicySpec attribute.
  """

  alternate = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1AlternatePolicySpec', 1)
  name = _messages.StringField(2)
  spec = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1PolicySpec', 3)


class GoogleCloudOrgpolicyV2alpha1PolicySpec(_messages.Message):
  r"""Defines a Cloud Organization `PolicySpec` which is used to specify
  `Constraints` for configurations of Cloud Platform resources.

  Fields:
    etag: An opaque tag indicating the current version of the `Policy`, used
      for concurrency control.  This field is ignored if used in a
      `CreatePolicy` request.  When the `Policy` is returned from either a
      `GetPolicy` or a `ListPolicies` request, this `etag` indicates the
      version of the current `Policy` to use when executing a read-modify-
      write loop.  When the `Policy` is returned from a `GetEffectivePolicy`
      request, the `etag` will be unset.  When the `Policy` is used in a
      `UpdatePolicy` method, use the `etag` value that was returned from a
      `GetPolicy` request as part of a read-modify-write loop for concurrency
      control. If `UpdatePolicyRequest`'s `force_unconditional_write` field is
      set to true, this field must not be set. Otherwise, the `etag` is
      required for `UpdatePolicy`.
    inheritFromParent: This field can be set only for Policies which configure
      list constraints.
    reset: Ignores policies set above this resource and restores the
      `constraint_default` enforcement behavior of the specific `Constraint`
      at this resource. This field can be set in policies for either list or
      boolean constraints. If set, `rules` must be empty and
      `inherit_from_parent` must be set to false.
    rules: Up to 10 PolicyRules are allowed.  In Policies for boolean
      constraints, the following requirements apply:   - There must be one and
      only one PolicyRule where condition is unset.   - BooleanPolicyRules
      with conditions must set `enforced` to the opposite     of the
      PolicyRule without a condition.   - During policy evaluation,
      PolicyRules with conditions that are     true for a target resource take
      precedence.
    updateTime: Output only. The time stamp this was previously updated. This
      represents the last time a call to `CreatePolicy` or `UpdatePolicy` was
      made for that `Policy`.
  """

  etag = _messages.StringField(1)
  inheritFromParent = _messages.BooleanField(2)
  reset = _messages.BooleanField(3)
  rules = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1PolicySpecPolicyRule', 4, repeated=True)
  updateTime = _messages.StringField(5)


class GoogleCloudOrgpolicyV2alpha1PolicySpecPolicyRule(_messages.Message):
  r"""A rule used to express this policy.

  Fields:
    allowAll: Setting this to true means that all values are allowed. This
      field can be set only in Policies for list constraints.
    condition: Optional. A condition which determines whether this rule is
      used in the evaluation of the policy. When set, the `expression` field
      in the `Expr' must include from 1 to 10 subexpressions, joined by the
      "||" or "&&" operators. Each subexpression must be of the form
      "resource.matchLabels(key_name, value_name)", where key_name and
      value_name are the resource names for Label Keys and Values. These names
      are available from the Label Manager Service. An example expression is:
      "resource.matchLabels('labelKeys/123, 'labelValues/456')".
    denyAll: Setting this to true means that all values are denied. This field
      can be set only in Policies for list constraints.
    enforce: If `true`, then the `Policy` is enforced. If `false`, then any
      configuration is acceptable. This field can be set only in Policies for
      boolean constraints.
    values: List of values to be used for this PolicyRule. This field can be
      set only in Policies for list constraints.
  """

  allowAll = _messages.BooleanField(1)
  condition = _messages.MessageField('GoogleTypeExpr', 2)
  denyAll = _messages.BooleanField(3)
  enforce = _messages.BooleanField(4)
  values = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1PolicySpecPolicyRuleStringValues', 5)


class GoogleCloudOrgpolicyV2alpha1PolicySpecPolicyRuleStringValues(_messages.Message):
  r"""A message that holds specific allowed and denied values. This message
  can define specific values and subtrees of Cloud Resource Manager resource
  hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or
  denied. This is achieved by using the `under:` and optional `is:` prefixes.
  The `under:` prefix is used to denote resource subtree values. The `is:`
  prefix is used to denote specific values, and is required only if the value
  contains a ":". Values prefixed with "is:" are treated the same as values
  with no prefix. Ancestry subtrees must be in one of the following formats:
  - "projects/<project-id>", e.g. "projects/tokyo-rain-123"     -
  "folders/<folder-id>", e.g. "folders/1234"     -
  "organizations/<organization-id>", e.g. "organizations/1234" The
  `supports_under` field of the associated `Constraint`  defines whether
  ancestry prefixes can be used.

  Fields:
    allowedValues: List of values allowed at this resource.
    deniedValues: List of values denied at this resource.
  """

  allowedValues = _messages.StringField(1, repeated=True)
  deniedValues = _messages.StringField(2, repeated=True)


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GoogleTypeExpr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec.  Example (Comparison):
  title: "Summary size limit"     description: "Determines if a summary is
  less than 100 chars"     expression: "document.summary.size() < 100"
  Example (Equality):      title: "Requestor is owner"     description:
  "Determines if requestor is the document owner"     expression:
  "document.owner == request.auth.claims.email"  Example (Logic):      title:
  "Public documents"     description: "Determine whether the document should
  be publicly visible"     expression: "document.type != 'private' &&
  document.type != 'internal'"  Example (Data Manipulation):      title:
  "Notification string"     description: "Create a notification string with a
  timestamp."     expression: "'New message received at ' +
  string(document.create_time)"  The exact variables and functions that may be
  referenced within an expression are determined by the service that evaluates
  it. See the service documentation for additional information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class OrgpolicyConstraintsListRequest(_messages.Message):
  r"""A OrgpolicyConstraintsListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: The Cloud resource that parents the constraint. Must be in one of
      the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyPoliciesCreateRequest(_messages.Message):
  r"""A OrgpolicyPoliciesCreateRequest object.

  Fields:
    constraint: The name of the `Constraint` the `Policy` is configuring, for
      example, `constraints/compute.disableSerialPortAccess`.
    googleCloudOrgpolicyV2alpha1Policy: A GoogleCloudOrgpolicyV2alpha1Policy
      resource to be passed as the request body.
    parent: The Cloud resource that will parent the new Policy. Must be in one
      of the following forms: * `projects/{project_number}` *
      `projects/{project_id}` * `folders/{folder_id}` *
      `organizations/{organization_id}`
  """

  constraint = _messages.StringField(1)
  googleCloudOrgpolicyV2alpha1Policy = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1Policy', 2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyPoliciesDeleteRequest(_messages.Message):
  r"""A OrgpolicyPoliciesDeleteRequest object.

  Fields:
    name: Name of the policy to delete. See `Policy` for naming rules.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyPoliciesGetEffectivePolicyRequest(_messages.Message):
  r"""A OrgpolicyPoliciesGetEffectivePolicyRequest object.

  Fields:
    name: The effective policy to compute. See `Policy` for naming rules.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyPoliciesGetRequest(_messages.Message):
  r"""A OrgpolicyPoliciesGetRequest object.

  Fields:
    name: Resource name of the policy. See `Policy` for naming requirements.
  """

  name = _messages.StringField(1, required=True)


class OrgpolicyPoliciesListRequest(_messages.Message):
  r"""A OrgpolicyPoliciesListRequest object.

  Fields:
    pageSize: Size of the pages to be returned. This is currently unsupported
      and will be ignored. The server may at any point start using this field
      to limit page size.
    pageToken: Page token used to retrieve the next page. This is currently
      unsupported and will be ignored. The server may at any point start using
      this field.
    parent: The target Cloud resource that parents the set of constraints and
      policies that will be returned from this call. Must be in one of the
      following forms: * `projects/{project_number}` * `projects/{project_id}`
      * `folders/{folder_id}` * `organizations/{organization_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrgpolicyPoliciesPatchRequest(_messages.Message):
  r"""A OrgpolicyPoliciesPatchRequest object.

  Fields:
    forceUnconditionalWrite: Indicates that this request should overwrite the
      current policy and ignore the `etag` used for optimistic currency
      control. When set to true, `etag` in `Policy` must be unset. Otherwise,
      `etag` is required.
    googleCloudOrgpolicyV2alpha1Policy: A GoogleCloudOrgpolicyV2alpha1Policy
      resource to be passed as the request body.
    name: Immutable. The resource name of the Policy. Must be one of the
      following forms, where constraint_name is the name of the constraint
      which this Policy configures: *
      `projects/{project_number}/policies/{constraint_name}` *
      `folders/{folder_id}/policies/{constraint_name}` *
      `organizations/{organization_id}/policies/{constraint_name}`  For
      example, "projects/123/policies/compute.disableSerialPortAccess".  Note:
      `projects/{project_id}/policies/{constraint_name}` is also an acceptable
      name for API requests, but responses will return the name using the
      equivalent project number.
  """

  forceUnconditionalWrite = _messages.BooleanField(1)
  googleCloudOrgpolicyV2alpha1Policy = _messages.MessageField('GoogleCloudOrgpolicyV2alpha1Policy', 2)
  name = _messages.StringField(3, required=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
