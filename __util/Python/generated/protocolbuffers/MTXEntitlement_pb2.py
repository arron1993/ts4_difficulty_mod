# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\dev\TS4\_deploy\Client\Releasex64\Python\Generated\protocolbuffers\MTXEntitlement_pb2.py
# Compiled at: 2020-11-25 00:39:33
# Size of source mod 2**32: 4109 bytes
from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
DESCRIPTOR = descriptor.FileDescriptor(name='MTXEntitlement.proto',
  package='EA.Sims4.Network',
  serialized_pb='\n\x14MTXEntitlement.proto\x12\x10EA.Sims4.Network"¼\x01\n\x12ListOfEntitlements\x12F\n\x0cEntitlements\x18\x01 \x03(\x0b20.EA.Sims4.Network.ListOfEntitlements.Entitlement\x1a^\n\x0bEntitlement\x12\n\n\x02Id\x18\x01 \x02(\x04\x12\x10\n\x08UseCount\x18\x02 \x02(\r\x12\x15\n\rentitlementId\x18\x03 \x02(\x04\x12\x1a\n\x12entitlementVersion\x18\x04 \x02(\r')
_LISTOFENTITLEMENTS_ENTITLEMENT = descriptor.Descriptor(name='Entitlement',
  full_name='EA.Sims4.Network.ListOfEntitlements.Entitlement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
 descriptor.FieldDescriptor(name='Id',
   full_name='EA.Sims4.Network.ListOfEntitlements.Entitlement.Id',
   index=0,
   number=1,
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
   options=None),
 descriptor.FieldDescriptor(name='UseCount',
   full_name='EA.Sims4.Network.ListOfEntitlements.Entitlement.UseCount',
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
 descriptor.FieldDescriptor(name='entitlementId',
   full_name='EA.Sims4.Network.ListOfEntitlements.Entitlement.entitlementId',
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
   options=None),
 descriptor.FieldDescriptor(name='entitlementVersion',
   full_name='EA.Sims4.Network.ListOfEntitlements.Entitlement.entitlementVersion',
   index=3,
   number=4,
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
   options=None)],
  extensions=[],
  nested_types=[],
  enum_types=[],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=137,
  serialized_end=231)
_LISTOFENTITLEMENTS = descriptor.Descriptor(name='ListOfEntitlements',
  full_name='EA.Sims4.Network.ListOfEntitlements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
 descriptor.FieldDescriptor(name='Entitlements',
   full_name='EA.Sims4.Network.ListOfEntitlements.Entitlements',
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
  nested_types=[
 _LISTOFENTITLEMENTS_ENTITLEMENT],
  enum_types=[],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=231)
_LISTOFENTITLEMENTS_ENTITLEMENT.containing_type = _LISTOFENTITLEMENTS
_LISTOFENTITLEMENTS.fields_by_name['Entitlements'].message_type = _LISTOFENTITLEMENTS_ENTITLEMENT
DESCRIPTOR.message_types_by_name['ListOfEntitlements'] = _LISTOFENTITLEMENTS

class ListOfEntitlements(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class Entitlement(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _LISTOFENTITLEMENTS_ENTITLEMENT

    DESCRIPTOR = _LISTOFENTITLEMENTS