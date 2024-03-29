# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import server_data_pb2
import auto_data_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='server_message.proto',
  package='',
  serialized_pb='\n\x14server_message.proto\x1a\x11server_data.proto\x1a\x0f\x61uto_data.proto\"+\n\rInitServerReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\",\n\x10SyncServerNotice\x12\x18\n\x07servers\x18\x01 \x03(\x0b\x32\x07.Server\"\x1f\n\x0fHeartBeatNotice\x12\x0c\n\x04name\x18\x01 \x01(\t\"i\n\x0fProtocolWrapper\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\x05\x12)\n\x10\x63lient_conn_info\x18\x02 \x01(\x0b\x32\x0f.ClientConnInfo\x12\x16\n\x0einner_protocol\x18\x03 \x01(\x0c\")\n\x13PrepareAvatarNotice\x12\x12\n\naccount_id\x18\x01 \x01(\x05')




_INITSERVERREQ = descriptor.Descriptor(
  name='InitServerReq',
  full_name='InitServerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='InitServerReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='InitServerReq.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=60,
  serialized_end=103,
)


_SYNCSERVERNOTICE = descriptor.Descriptor(
  name='SyncServerNotice',
  full_name='SyncServerNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='servers', full_name='SyncServerNotice.servers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=105,
  serialized_end=149,
)


_HEARTBEATNOTICE = descriptor.Descriptor(
  name='HeartBeatNotice',
  full_name='HeartBeatNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='HeartBeatNotice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=151,
  serialized_end=182,
)


_PROTOCOLWRAPPER = descriptor.Descriptor(
  name='ProtocolWrapper',
  full_name='ProtocolWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='protocol_id', full_name='ProtocolWrapper.protocol_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_conn_info', full_name='ProtocolWrapper.client_conn_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inner_protocol', full_name='ProtocolWrapper.inner_protocol', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=184,
  serialized_end=289,
)


_PREPAREAVATARNOTICE = descriptor.Descriptor(
  name='PrepareAvatarNotice',
  full_name='PrepareAvatarNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='account_id', full_name='PrepareAvatarNotice.account_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=291,
  serialized_end=332,
)

_SYNCSERVERNOTICE.fields_by_name['servers'].message_type = server_data_pb2._SERVER
_PROTOCOLWRAPPER.fields_by_name['client_conn_info'].message_type = auto_data_pb2._CLIENTCONNINFO
DESCRIPTOR.message_types_by_name['InitServerReq'] = _INITSERVERREQ
DESCRIPTOR.message_types_by_name['SyncServerNotice'] = _SYNCSERVERNOTICE
DESCRIPTOR.message_types_by_name['HeartBeatNotice'] = _HEARTBEATNOTICE
DESCRIPTOR.message_types_by_name['ProtocolWrapper'] = _PROTOCOLWRAPPER
DESCRIPTOR.message_types_by_name['PrepareAvatarNotice'] = _PREPAREAVATARNOTICE

class InitServerReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INITSERVERREQ
  
  # @@protoc_insertion_point(class_scope:InitServerReq)

class SyncServerNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCSERVERNOTICE
  
  # @@protoc_insertion_point(class_scope:SyncServerNotice)

class HeartBeatNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEARTBEATNOTICE
  
  # @@protoc_insertion_point(class_scope:HeartBeatNotice)

class ProtocolWrapper(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROTOCOLWRAPPER
  
  # @@protoc_insertion_point(class_scope:ProtocolWrapper)

class PrepareAvatarNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PREPAREAVATARNOTICE
  
  # @@protoc_insertion_point(class_scope:PrepareAvatarNotice)

# @@protoc_insertion_point(module_scope)
