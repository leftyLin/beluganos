# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ribpapi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ribpapi.proto',
  package='ribpapi',
  syntax='proto3',
  serialized_pb=_b('\n\rribpapi.proto\x12\x07ribpapi\"!\n\x0f\x46\x46PacketRequest\x12\x0e\n\x06ifname\x18\x01 \x01(\t\"\x13\n\x11SendFFPacketReply2Q\n\x07RIBPApi\x12\x46\n\x0cSendFFPacket\x12\x18.ribpapi.FFPacketRequest\x1a\x1a.ribpapi.SendFFPacketReply\"\x00\x62\x06proto3')
)




_FFPACKETREQUEST = _descriptor.Descriptor(
  name='FFPacketRequest',
  full_name='ribpapi.FFPacketRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ifname', full_name='ribpapi.FFPacketRequest.ifname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=59,
)


_SENDFFPACKETREPLY = _descriptor.Descriptor(
  name='SendFFPacketReply',
  full_name='ribpapi.SendFFPacketReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['FFPacketRequest'] = _FFPACKETREQUEST
DESCRIPTOR.message_types_by_name['SendFFPacketReply'] = _SENDFFPACKETREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FFPacketRequest = _reflection.GeneratedProtocolMessageType('FFPacketRequest', (_message.Message,), dict(
  DESCRIPTOR = _FFPACKETREQUEST,
  __module__ = 'ribpapi_pb2'
  # @@protoc_insertion_point(class_scope:ribpapi.FFPacketRequest)
  ))
_sym_db.RegisterMessage(FFPacketRequest)

SendFFPacketReply = _reflection.GeneratedProtocolMessageType('SendFFPacketReply', (_message.Message,), dict(
  DESCRIPTOR = _SENDFFPACKETREPLY,
  __module__ = 'ribpapi_pb2'
  # @@protoc_insertion_point(class_scope:ribpapi.SendFFPacketReply)
  ))
_sym_db.RegisterMessage(SendFFPacketReply)



_RIBPAPI = _descriptor.ServiceDescriptor(
  name='RIBPApi',
  full_name='ribpapi.RIBPApi',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=82,
  serialized_end=163,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendFFPacket',
    full_name='ribpapi.RIBPApi.SendFFPacket',
    index=0,
    containing_service=None,
    input_type=_FFPACKETREQUEST,
    output_type=_SENDFFPACKETREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RIBPAPI)

DESCRIPTOR.services_by_name['RIBPApi'] = _RIBPAPI

# @@protoc_insertion_point(module_scope)
