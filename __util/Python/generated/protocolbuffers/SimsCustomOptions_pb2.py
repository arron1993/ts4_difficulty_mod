# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\dev\TS4\_deploy\Client\Releasex64\Python\Generated\protocolbuffers\SimsCustomOptions_pb2.py
# Compiled at: 2020-11-25 00:40:04
# Size of source mod 2**32: 1757 bytes
from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
import google.protobuf.descriptor_pb2
DESCRIPTOR = descriptor.FileDescriptor(name='SimsCustomOptions.proto',
  package='EA.Sims4.Persistence',
  serialized_pb='\n\x17SimsCustomOptions.proto\x12\x14EA.Sims4.Persistence\x1a google/protobuf/descriptor.proto:D\n\x14persist_for_new_game\x12\x1d.google.protobuf.FieldOptions\x18Ð\x86\x03 \x01(\x08:\x05false:F\n\x16persist_for_cloned_sim\x12\x1d.google.protobuf.FieldOptions\x18Ñ\x86\x03 \x01(\x08:\x05false')
PERSIST_FOR_NEW_GAME_FIELD_NUMBER = 50000
persist_for_new_game = descriptor.FieldDescriptor(name='persist_for_new_game',
  full_name='EA.Sims4.Persistence.persist_for_new_game',
  index=0,
  number=50000,
  type=8,
  cpp_type=7,
  label=1,
  has_default_value=True,
  default_value=False,
  message_type=None,
  enum_type=None,
  containing_type=None,
  is_extension=True,
  extension_scope=None,
  options=None)
PERSIST_FOR_CLONED_SIM_FIELD_NUMBER = 50001
persist_for_cloned_sim = descriptor.FieldDescriptor(name='persist_for_cloned_sim',
  full_name='EA.Sims4.Persistence.persist_for_cloned_sim',
  index=1,
  number=50001,
  type=8,
  cpp_type=7,
  label=1,
  has_default_value=True,
  default_value=False,
  message_type=None,
  enum_type=None,
  containing_type=None,
  is_extension=True,
  extension_scope=None,
  options=None)
google.protobuf.descriptor_pb2.FieldOptions.RegisterExtension(persist_for_new_game)
google.protobuf.descriptor_pb2.FieldOptions.RegisterExtension(persist_for_cloned_sim)