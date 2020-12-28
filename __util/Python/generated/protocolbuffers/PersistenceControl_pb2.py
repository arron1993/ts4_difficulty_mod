# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\dev\TS4\_deploy\Client\Releasex64\Python\Generated\protocolbuffers\PersistenceControl_pb2.py
# Compiled at: 2020-11-25 00:39:55
# Size of source mod 2**32: 6348 bytes
from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
import protocolbuffers.Consts_pb2 as Consts_pb2
import protocolbuffers.FileSerialization_pb2 as FileSerialization_pb2
DESCRIPTOR = descriptor.FileDescriptor(name='PersistenceControl.proto',
  package='EA.Sims4.Network',
  serialized_pb='\n\x18PersistenceControl.proto\x12\x10EA.Sims4.Network\x1a\x0cConsts.proto\x1a\x17FileSerialization.proto"\x91\x02\n\x1dPersistenceControlMessageData\x12B\n\x0eslot_meta_data\x18\x01 \x03(\x0b2*.EA.Sims4.Persistence.SaveGameSlotMetaData\x125\n\tsave_data\x18\x02 \x01(\x0b2".EA.Sims4.Persistence.SaveGameData\x12>\n\x10zone_object_data\x18\x03 \x03(\x0b2$.EA.Sims4.Persistence.ZoneObjectData\x125\n\x06errors\x18\x04 \x01(\x0b2%.EA.Sims4.Persistence.FeedbackContext"´\x01\n\x19PersistenceControlMessage\x12\x10\n\x08callback\x18\x01 \x01(\x04\x12\x10\n\x08userdata\x18\x02 \x01(\x04\x124\n\x06opcode\x18\x04 \x01(\x0e2$.EA.Sims4.Network.PersistenceOpTypes\x12=\n\x04data\x18\x05 \x01(\x0b2/.EA.Sims4.Network.PersistenceControlMessageData')
_PERSISTENCECONTROLMESSAGEDATA = descriptor.Descriptor(name='PersistenceControlMessageData',
  full_name='EA.Sims4.Network.PersistenceControlMessageData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
 descriptor.FieldDescriptor(name='slot_meta_data',
   full_name='EA.Sims4.Network.PersistenceControlMessageData.slot_meta_data',
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
   options=None),
 descriptor.FieldDescriptor(name='save_data',
   full_name='EA.Sims4.Network.PersistenceControlMessageData.save_data',
   index=1,
   number=2,
   type=11,
   cpp_type=10,
   label=1,
   has_default_value=False,
   default_value=None,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None),
 descriptor.FieldDescriptor(name='zone_object_data',
   full_name='EA.Sims4.Network.PersistenceControlMessageData.zone_object_data',
   index=2,
   number=3,
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
   options=None),
 descriptor.FieldDescriptor(name='errors',
   full_name='EA.Sims4.Network.PersistenceControlMessageData.errors',
   index=3,
   number=4,
   type=11,
   cpp_type=10,
   label=1,
   has_default_value=False,
   default_value=None,
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
  serialized_start=86,
  serialized_end=359)
_PERSISTENCECONTROLMESSAGE = descriptor.Descriptor(name='PersistenceControlMessage',
  full_name='EA.Sims4.Network.PersistenceControlMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
 descriptor.FieldDescriptor(name='callback',
   full_name='EA.Sims4.Network.PersistenceControlMessage.callback',
   index=0,
   number=1,
   type=4,
   cpp_type=4,
   label=1,
   has_default_value=False,
   default_value=0,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None),
 descriptor.FieldDescriptor(name='userdata',
   full_name='EA.Sims4.Network.PersistenceControlMessage.userdata',
   index=1,
   number=2,
   type=4,
   cpp_type=4,
   label=1,
   has_default_value=False,
   default_value=0,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None),
 descriptor.FieldDescriptor(name='opcode',
   full_name='EA.Sims4.Network.PersistenceControlMessage.opcode',
   index=2,
   number=4,
   type=14,
   cpp_type=8,
   label=1,
   has_default_value=False,
   default_value=0,
   message_type=None,
   enum_type=None,
   containing_type=None,
   is_extension=False,
   extension_scope=None,
   options=None),
 descriptor.FieldDescriptor(name='data',
   full_name='EA.Sims4.Network.PersistenceControlMessage.data',
   index=3,
   number=5,
   type=11,
   cpp_type=10,
   label=1,
   has_default_value=False,
   default_value=None,
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
  serialized_start=362,
  serialized_end=542)
_PERSISTENCECONTROLMESSAGEDATA.fields_by_name['slot_meta_data'].message_type = FileSerialization_pb2._SAVEGAMESLOTMETADATA
_PERSISTENCECONTROLMESSAGEDATA.fields_by_name['save_data'].message_type = FileSerialization_pb2._SAVEGAMEDATA
_PERSISTENCECONTROLMESSAGEDATA.fields_by_name['zone_object_data'].message_type = FileSerialization_pb2._ZONEOBJECTDATA
_PERSISTENCECONTROLMESSAGEDATA.fields_by_name['errors'].message_type = FileSerialization_pb2._FEEDBACKCONTEXT
_PERSISTENCECONTROLMESSAGE.fields_by_name['opcode'].enum_type = Consts_pb2._PERSISTENCEOPTYPES
_PERSISTENCECONTROLMESSAGE.fields_by_name['data'].message_type = _PERSISTENCECONTROLMESSAGEDATA
DESCRIPTOR.message_types_by_name['PersistenceControlMessageData'] = _PERSISTENCECONTROLMESSAGEDATA
DESCRIPTOR.message_types_by_name['PersistenceControlMessage'] = _PERSISTENCECONTROLMESSAGE

class PersistenceControlMessageData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTENCECONTROLMESSAGEDATA


class PersistenceControlMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTENCECONTROLMESSAGE