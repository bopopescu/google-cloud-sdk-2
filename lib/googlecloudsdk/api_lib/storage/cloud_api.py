# -*- coding: utf-8 -*- #
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API interface for interacting with cloud storage providers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import threading

GCS_PREFIX = 'gs'
AWS_S3_PREFIX = 's3'

# Module variable for holding one API instance per thread per provider.
_cloud_api_thread_local_storage = threading.local()


def GetApi(provider):
  """Returns thread local API instance for cloud provider.

  Uses thread local storage to make sure only one instance of an API exists
  per thread per provider.

  Args:
    provider (string): Cloud provider prefix (i.e. "gs").

  Raises:
     ValueError for invalid API providers.

  Returns:
    API for cloud provider or None if unrecognized provider.
  """
  if getattr(_cloud_api_thread_local_storage, provider, None) is None:
    if provider == GCS_PREFIX:
      # TODO(b/159164504): Update with implemented GCS API.
      _cloud_api_thread_local_storage.gs = CloudApi()
    elif provider == AWS_S3_PREFIX:
      # TODO(b/159164385): Update with implemented S3 API.
      _cloud_api_thread_local_storage.s3 = CloudApi()
    else:
      raise ValueError('Provider API value must be "gs" or "s3".')
  return getattr(_cloud_api_thread_local_storage, provider)


class CloudApi(object):
  """Abstract base class for interacting with cloud storage providers.

  Implementations of the Cloud API are not guaranteed to be thread-safe.
  Behavior when calling a Cloud API instance simultaneously across
  threads is undefined and doing so will likely cause errors. Therefore,
  a separate instance of the Cloud API should be instantiated per-thread.
  """

  def ListBuckets(self, project_id=None, provider=None, fields_scope=None):
    """Lists bucket metadata for the given project.

    Args:
      project_id: Project owning the buckets, default from config if None.
      provider: Cloud storage provider to connect to.  If not present,
        class-wide default is used.
      fields_scope: Determines the fields and projection parameters of API call.

    Raises:
      InvalidArgumentException for errors during input validation.
      CloudProviderException for errors interacting with cloud storage
      providers.

    Returns:
      Iterator over Bucket objects.
    """
    raise NotImplementedError('ListBuckets must be overloaded')

  def ListObjects(self,
                  bucket_name,
                  prefix=None,
                  delimiter=None,
                  all_versions=None,
                  provider=None,
                  fields_scope=None):
    """Lists objects (with metadata) and prefixes in a bucket.

    Args:
      bucket_name: Bucket containing the objects.
      prefix: Prefix for directory-like behavior.
      delimiter: Delimiter for directory-like behavior.
      all_versions: If true, list all object versions.
      provider: Cloud storage provider to connect to.  If not present,
        class-wide default is used.
      fields_scope: Determines the fields and projection parameters of API call.

    Raises:
      InvalidArgumentException for errors during input validation.
      CloudProviderException for errors interacting with cloud storage
      providers.

    Returns:
      Iterator over CsObjectOrPrefix wrapper class.
    """
    raise NotImplementedError('ListObjects must be overloaded')

  def GetObjectMetadata(self,
                        bucket_name,
                        object_name,
                        generation=None,
                        provider=None,
                        fields_scope=None):
    """Gets object metadata.

    If decryption is supported by the implementing class, this function will
    read decryption keys from configuration and appropriately retry requests to
    encrypted objects with the correct key.

    Args:
      bucket_name: Bucket containing the object.
      object_name: Object name.
      generation: Generation of the object to retrieve.
      provider: Cloud storage provider to connect to.  If not present,
        class-wide default is used.
      fields_scope: Determines the fields and projection parameters of API call.

    Raises:
      InvalidArgumentException for errors during input validation.
      CloudProviderException for errors interacting with cloud storage
      providers.

    Returns:
      Object object.
    """
    raise NotImplementedError('GetObjectMetadata must be overloaded')

  def PatchObjectMetadata(self,
                          bucket_name,
                          object_name,
                          metadata,
                          canned_acl=None,
                          generation=None,
                          preconditions=None,
                          provider=None,
                          fields_scope=None):
    """Updates object metadata with patch semantics.

    Args:
      bucket_name: Bucket containing the object.
      object_name: Object name for object.
      metadata: Object object defining metadata to be updated.
      canned_acl: Canned ACL to be set on the object.
      generation: Generation (or version) of the object to update.
      preconditions: Preconditions for the request.
      provider: Cloud storage provider to connect to.  If not present,
        class-wide default is used.
      fields_scope: Determines the fields and projection parameters of API call.

    Raises:
      InvalidArgumentException for errors during input validation.
      CloudProviderException for errors interacting with cloud storage
      providers.

    Returns:
      Updated object metadata.
    """
    raise NotImplementedError('PatchObjectMetadata must be overloaded')

  def UploadObject(self,
                   upload_stream,
                   object_metadata,
                   canned_acl=None,
                   size=None,
                   preconditions=None,
                   progress_callback=None,
                   encryption_tuple=None,
                   provider=None,
                   fields_scope=None,
                   gzip_encoded=False):
    """Uploads object data and metadata.

    Args:
      upload_stream: Seekable stream of object data.
      object_metadata: Object metadata for new object.  Must include bucket and
        object name.
      canned_acl: Optional canned ACL to apply to object. Overrides ACL set in
        object_metadata.
      size: Optional object size.
      preconditions: Preconditions for the request.
      progress_callback: Optional callback function for progress notifications.
        Receives calls with arguments (bytes_transferred, total_size).
      encryption_tuple: Optional utils.encryption_helper.CryptoKeyWrapper for
        encrypting the uploaded object.
      provider: Cloud storage provider to connect to.  If not present,
        class-wide default is used.
      fields_scope: Determines the fields and projection parameters of API call.
      gzip_encoded: Whether to use gzip transport encoding for the upload.

    Raises:
      InvalidArgumentException for errors during input validation.
      CloudProviderException for errors interacting with cloud storage
      providers.

    Returns:
      Object object for newly created destination object.
    """
    raise NotImplementedError('UploadObject must be overloaded')
