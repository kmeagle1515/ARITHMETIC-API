# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MY_example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MY_example.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10MY_example.proto\" \n\x08\x66\x65\x61tures\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x03\"\x10\n\x03\x61ns\x12\t\n\x01p\x18\x01 \x01(\x03\x32(\n\x0emultiplication\x12\x16\n\x03met\x12\t.features\x1a\x04.ansb\x06proto3')
)




_FEATURES = _descriptor.Descriptor(
  name='features',
  full_name='features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='features.a', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='features.b', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=52,
)


_ANS = _descriptor.Descriptor(
  name='ans',
  full_name='ans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p', full_name='ans.p', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['features'] = _FEATURES
DESCRIPTOR.message_types_by_name['ans'] = _ANS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

features = _reflection.GeneratedProtocolMessageType('features', (_message.Message,), dict(
  DESCRIPTOR = _FEATURES,
  __module__ = 'MY_example_pb2'
  # @@protoc_insertion_point(class_scope:features)
  ))
_sym_db.RegisterMessage(features)

ans = _reflection.GeneratedProtocolMessageType('ans', (_message.Message,), dict(
  DESCRIPTOR = _ANS,
  __module__ = 'MY_example_pb2'
  # @@protoc_insertion_point(class_scope:ans)
  ))
_sym_db.RegisterMessage(ans)



_MULTIPLICATION = _descriptor.ServiceDescriptor(
  name='multiplication',
  full_name='multiplication',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=72,
  serialized_end=112,
  methods=[
  _descriptor.MethodDescriptor(
    name='met',
    full_name='multiplication.met',
    index=0,
    containing_service=None,
    input_type=_FEATURES,
    output_type=_ANS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MULTIPLICATION)

DESCRIPTOR.services_by_name['multiplication'] = _MULTIPLICATION

# @@protoc_insertion_point(module_scope)