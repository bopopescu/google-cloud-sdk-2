# Copyright 2017 Google Inc. All Rights Reserved.
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
"""Shared flags for Cloud IoT commands."""
import enum

from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base


def GetIdFlag(noun, action, metavar=None):
  return base.Argument(
      'id',
      metavar=metavar or '{}_ID'.format(noun.replace(' ', '_').upper()),
      help='ID of the {} {}.\n\n'.format(noun, action))


def _GetFlag(flag, noun=None, required=True, description=''):
  if description:
    description = ' ' + description
  return base.Argument(
      '--' + flag,
      required=required,
      help='The {}{}.'.format(noun or flag, description))


def GetRegionFlag(description='', required=True):
  return _GetFlag('region', noun='Cloud region', description=description,
                  required=required)


def _GetRegistryFlag(description='', required=True):
  return _GetFlag('registry', noun='device registry', description=description,
                  required=required)


def _GetDeviceFlag(description='', required=True):
  return _GetFlag('device', description=description, required=required)


def AddRegistryResourceFlags(parser, verb, positional=True):
  noun = 'device registry'
  if positional:
    GetIdFlag(noun, verb, 'REGISTRY_ID').AddToParser(parser)
  else:
    _GetRegistryFlag(verb).AddToParser(parser)
  GetRegionFlag('for the ' + noun, required=False).AddToParser(parser)


def AddDeviceResourceFlags(parser, verb, positional=True):
  noun = 'device'
  if positional:
    GetIdFlag(noun, verb).AddToParser(parser)
  else:
    _GetDeviceFlag(verb).AddToParser(parser)
  GetRegionFlag('for the ' + noun, required=False).AddToParser(parser)
  _GetRegistryFlag('for the ' + noun, required=False).AddToParser(parser)


def GetIndexFlag(noun, action):
  return base.Argument(
      'index',
      type=int,
      help='The index (zero-based) of the {} {}.'.format(noun, action))


def AddDeviceRegistrySettingsFlagsToParser(parser, defaults=True):
  """Get flags for device registry commands.

  Args:
    parser: argparse parser to which to add these flags.
    defaults: bool, whether to populate default values (for instance, should be
        false for Patch commands).

  Returns:
    list of base.Argument, the flags common to and specific to device commands.
  """
  base.Argument(
      '--enable-mqtt-config',
      help='Whether to allow MQTT connections to this device registry.',
      default=True if defaults else None,
      action='store_true'
  ).AddToParser(parser)
  base.Argument(
      '--enable-http-config',
      help='Whether to allow device connections to the HTTP bridge.',
      default=True if defaults else None,
      action='store_true'
  ).AddToParser(parser)

  base.Argument(
      '--state-pubsub-topic',
      required=False,
      help=('A Google Cloud Pub/Sub topic name for state notifications.')
  ).AddToParser(parser)
  pubsub_args = parser.add_mutually_exclusive_group()
  # TODO(b/64597199): Remove this flag when usage is low.
  base.Argument(
      '--pubsub-topic',
      required=False,
      action=actions.DeprecationAction('--pubsub-topic',
                                       warn=('Flag {flag_name} is deprecated. '
                                             'Use --event-pubsub-topic '
                                             'instead.')),
      hidden=True,
      help=('A Google Cloud Pub/Sub topic name for event notifications')
  ).AddToParser(pubsub_args)
  base.Argument(
      '--event-pubsub-topic',
      required=False,
      help=('A Google Cloud Pub/Sub topic name for event notifications')
  ).AddToParser(pubsub_args)


def AddDeviceRegistryCredentialFlagsToParser(parser, credentials_surface=True):
  help_text = ('Path to a file containing an X.509v3 certificate '
               '([RFC5280](https://www.ietf.org/rfc/rfc5280.txt)), encoded in '
               'base64, and wrapped by `-----BEGIN CERTIFICATE-----` and '
               '`-----END CERTIFICATE-----`.')
  if not credentials_surface:
    base.Argument(
        '--public-key-path',
        type=str,
        help=help_text
    ).AddToParser(parser)
  else:
    base.Argument(
        '--path',
        type=str,
        required=True,
        help=help_text
    ).AddToParser(parser)


def GetIamPolicyFileFlag():
  return base.Argument(
      'policy_file',
      help='JSON or YAML file with the IAM policy')


def AddDeviceFlagsToParser(parser, default_for_blocked_flags=True):
  """Add flags for device commands to parser.

  Args:
    parser: argparse parser to which to add these flags.
    default_for_blocked_flags: bool, whether to populate default values for
        device blocked state flags.
  """
  blocked_state_help_text = (
      'If {0}, connections from this device will fail.\n\n'
      'Can be used to temporarily prevent the device from '
      'connecting if, for example, the sensor is generating bad '
      'data and needs maintenance.\n\n')
  enable_device_format_args = ('disabled',)
  blocked_format_args = ('blocked',)
  if not default_for_blocked_flags:
    blocked_state_help_text += (
        '+\n\n'  # '+' here preserves markdown indentation.
        'Use `--{1}` to enable connections and `--{2}` to disable.')
    enable_device_format_args += ('enable-device', 'no-enable-device')
    blocked_format_args += ('no-blocked', 'blocked')
  else:
    blocked_state_help_text += (
        '+\n\n'
        'Connections to device is not blocked by default.')

  blocked_state_args = parser.add_mutually_exclusive_group()
  # Defaults are set to None because with nested groups, help text isn't being
  # generated correctly.
  blocked_state_args.add_argument(
      '--enable-device',
      default=None,
      action=actions.DeprecationAction('--[no-]enable-device',
                                       warn=('Flag {flag_name} is deprecated. '
                                             'Use --[no-]blocked instead.'),
                                       action='store_true'),
      help=blocked_state_help_text.format(*enable_device_format_args)
  )
  blocked_state_args.add_argument(
      '--blocked',
      default=None,
      action='store_true',
      help=blocked_state_help_text.format(*blocked_format_args)
  )

  metadata_key_validator = arg_parsers.RegexpValidator(
      r'[a-zA-Z0-9-_]{1,127}',
      'Invalid metadata key. Keys should only contain the following characters '
      '[a-zA-Z0-9-_] and be fewer than 128 bytes in length.')
  base.Argument(
      '--metadata',
      metavar='KEY=VALUE',
      type=arg_parsers.ArgDict(key_type=metadata_key_validator),
      help="""\
The metadata key/value pairs assigned to devices. This metadata is not
interpreted or indexed by Cloud IoT Core. It can be used to add contextual
information for the device.

Keys should only contain the following characters ```[a-zA-Z0-9-_]``` and be
fewer than 128 bytes in length. Values are free-form strings. Each value must
be fewer than or equal to 32 KB in size.

The total size of all keys and values must be less than 256 KB, and the
maximum number of key-value pairs is 500.
""").AddToParser(parser)

  base.Argument(
      '--metadata-from-file',
      metavar='KEY=PATH',
      type=arg_parsers.ArgDict(key_type=metadata_key_validator),
      help=('Same as --metadata, but the metadata values will be read from the '
            'file specified by path.')
  ).AddToParser(parser)


class KeyTypes(enum.Enum):
  """Valid key types for device credentials."""
  RS256 = 1
  ES256 = 2
  RSA_PEM = 3
  RSA_X509_PEM = 4
  ES256_PEM = 5
  ES256_X509_PEM = 6

  def __init__(self, value):
    self.choice_name = self.name.replace('_', '-').lower()


_VALID_KEY_TYPES = {
    KeyTypes.RSA_PEM.choice_name: """\
        An RSA public key encoded in base64, and wrapped by
        `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----`.
        This can be used to verify `RS256` signatures in JWT tokens
        ([RFC7518](https://www.ietf.org/rfc/rfc7518.txt)).""",
    KeyTypes.RSA_X509_PEM.choice_name: """\
        As RSA_PEM, but wrapped in an X.509v3 certificate
        ([RFC5280](https://www.ietf.org/rfc/rfc5280.txt)),
        encoded in base64, and wrapped by
        `-----BEGIN CERTIFICATE-----` and
        `-----END CERTIFICATE-----`.""",
    KeyTypes.ES256_PEM.choice_name: """\
        Public key for the ECDSA algorithm using P-256 and
        SHA-256, encoded in base64, and wrapped by
        `-----BEGIN PUBLIC KEY-----` and
        `-----END PUBLIC KEY-----`. This can be used to verify JWT
        tokens with the `ES256` algorithm
        ([RFC7518](https://www.ietf.org/rfc/rfc7518.txt)). This
        curve is defined in [OpenSSL](https://www.openssl.org/) as
        the `prime256v1` curve.""",
    KeyTypes.ES256_X509_PEM.choice_name: """\
        (As ES256_PEM, but wrapped in an X.509v3 certificate
        ([RFC5280]( https://www.ietf.org/rfc/rfc5280.txt)),
        encoded in base64, and wrapped by
        `-----BEGIN CERTIFICATE-----` and
        `-----END CERTIFICATE-----`.""",
    KeyTypes.RS256.choice_name: 'Deprecated name for `rsa-x509-pem`',
    KeyTypes.ES256.choice_name: 'Deprecated nmame for `es256-pem`'
}


def AddDeviceCredentialFlagsToParser(parser, combine_flags=True,
                                     only_modifiable=False):
  """Get credentials-related flags.

  Adds one of the following:

    * --public-key path=PATH,type=TYPE,expiration-time=EXPIRATION_TIME
    * --path=PATH --type=TYPE --expiration-time=EXPIRATION_TIME

  depending on the value of combine_flags.

  Args:
    parser: argparse parser to which to add these flags.
    combine_flags: bool, whether to combine these flags into one --public-key
      flag or to leave them separate.
    only_modifiable: bool, whether to include all flags or just those that can
      be modified after creation.
  """
  flags = []
  if not only_modifiable:
    flags.extend([
        base.Argument('--path', required=True, type=str,
                      help='The path on disk to the file containing the key.'),
        base.ChoiceArgument('--type', choices=_VALID_KEY_TYPES, required=True,
                            help_str='The type of the key.')
    ])
  flags.append(
      base.Argument('--expiration-time', type=arg_parsers.Datetime.Parse,
                    help=('The expiration time for the key in ISO 8601 '
                          '(ex. `2017-01-01T00:00Z`) format.')))
  if combine_flags:
    sub_argument_help = []
    spec = {}
    for flag in flags:
      name = flag.name.lstrip('-')
      required = flag.kwargs.get('required')
      choices = flag.kwargs.get('choices')
      choices_str = ''
      if choices:
        choices_str = ', '.join(map('`{}`'.format, sorted(choices)))
        choices_str = ' One of [{}].'.format(choices_str)
      help_ = flag.kwargs['help']
      spec[name] = flag.kwargs['type']
      sub_argument_help.append(
          '* *{name}*: {required}.{choices} {help}'.format(
              name=name, required=('Required' if required else 'Optional'),
              choices=choices_str, help=help_))
    key_type_help = []
    for key_type, description in reversed(sorted(_VALID_KEY_TYPES.items())):
      key_type_help.append('* `{}`: {}'.format(key_type, description))
    base.Argument(
        '--public-key',
        dest='public_keys',
        metavar='path=PATH,type=TYPE,[expiration-time=EXPIRATION-TIME]',
        type=arg_parsers.ArgDict(spec=spec),
        action='append',
        help="""\
Specify a public key.

Supports four key types:

{key_type_help}

The key specification is given via the following sub-arguments:

{sub_argument_help}

For example:

    --public-key \\
        path=/path/to/id_rsa.pem,type=RSA_PEM,expiration-time=2017-01-01T00:00-05

This flag may be provide multiple times to provide multiple keys (maximum 3).
""".format(key_type_help='\n'.join(key_type_help),
           sub_argument_help='\n'.join(sub_argument_help))).AddToParser(parser)
  else:
    for flag in flags:
      flag.AddToParser(parser)


def AddDeviceConfigFlagsToParser(parser):
  """Add flags for the `configs update` command."""
  base.Argument(
      '--version-to-update',
      type=int,
      help="""\
          The version number to update. If this value is `0` or unspecified, it
          will not check the version number of the server and will always update
          the current version; otherwise, this update will fail if the version
          number provided does not match the latest version on the server. This
          is used to detect conflicts with simultaneous updates.
          """).AddToParser(parser)
  data_group = parser.add_mutually_exclusive_group(required=True)
  base.Argument(
      '--config-file',
      help='Path to a local file containing the data for this configuration.'
  ).AddToParser(data_group)
  base.Argument(
      '--config-data',
      help=('The data for this configuration, as a string. For any values '
            'that contain special characters (in the context of your shell), '
            'use the `--config-file` flag instead.')
  ).AddToParser(data_group)
