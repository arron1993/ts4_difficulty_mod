# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\dev\TS4\_deploy\Client\Releasex64\Python\Generated\protocolbuffers\ResourceKey_pb2.py
# Compiled at: 2020-11-25 00:39:56
# Size of source mod 2**32: 3412 bytes
from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
DESCRIPTOR = descriptor.FileDescriptor(name='ResourceKey.proto',
  package='EA.Sims4.Network',
  serialized_pb='\n\x11ResourceKey.proto\x12\x10EA.Sims4.Network"<\n\x0bResourceKey\x12\x0c\n\x04type\x18\x01 \x02(\r\x12\r\n\x05group\x18\x02 \x02(\r\x12\x10\n\x08instance\x18\x03 \x02(\x04"G\n\x0fResourceKeyList\x124\n\rresource_keys\x18\x01 \x03(\x0b2\x1d.EA.Sims4.Network.ResourceKeyB\x0eB\x0cResourceKeys')
_RESOURCEKEY = descriptor.Descriptor(name='ResourceKey',
  full_name='EA.Sims4.Network.ResourceKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
 descriptor.FieldDescriptor(name='type',
   full_name='EA.Sims4.Network.ResourceKey.type',
   index=0,
   number=1,
   type=13,
   cpp_type=3,
   label=2,
   has_default_value=False,
   default_value=0,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None),
 descriptor.FieldDescriptor(name='group',
   full_name='EA.Sims4.Network.ResourceKey.group',
   index=1,
   number=2,
   type=13,
   cpp_type=3,
   label=2,
   has_default_value=False,
   default_value=0,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None),
 descriptor.FieldDescriptor(name='instance',
   full_name='EA.Sims4.Network.ResourceKey.instance',
   index=2,
   number=3,
   type=4,
   cpp_type=4,
   label=2,
   has_default_value=False,
   default_value=0,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None)],
  extensions=[],
  nested_types=[],
  enum_types=[],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=39,
  serialized_end=99)
_RESOURCEKEYLIST = descriptor.Descriptor(name='ResourceKeyList',
  full_name='EA.Sims4.Network.ResourceKeyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
 descriptor.FieldDescriptor(name='resource_keys',
   full_name='EA.Sims4.Network.ResourceKeyList.resource_keys',
   index=0,
   number=1,
   type=11,
   cpp_type=10,
   label=3,
   has_default_value=False,
   default_value=[],
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None)],
  extensions=[],
  nested_types=[],
  enum_types=[],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=101,
  serialized_end=172)
_RESOURCEKEYLIST.fields_by_name['resource_keys'].message_type = _RESOURCEKEY
DESCRIPTOR.message_types_by_name['ResourceKey'] = _RESOURCEKEY
DESCRIPTOR.message_types_by_name['ResourceKeyList'] = _RESOURCEKEYLIST

class ResourceKey(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _RESOURCEKEY


class ResourceKeyList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _RESOURCEKEYLIST