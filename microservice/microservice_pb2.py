# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: microservice.proto

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
  name='microservice.proto',
  package='noticias',
  syntax='proto3',
  serialized_pb=_b('\n\x12microservice.proto\x12\x08noticias\"%\n\x0eNoticiaRequest\x12\x13\n\x0btipoNoticia\x18\x01 \x01(\t\"a\n\x0cNoticiaReply\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06titulo\x18\x02 \x01(\t\x12\x11\n\tsubtitulo\x18\x03 \x01(\t\x12\x10\n\x08\x61rticulo\x18\x04 \x01(\t\x12\x10\n\x08\x63ontador\x18\x05 \x01(\x05\"\x1e\n\x0bPingRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\tPingReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xdb\x01\n\x08Noticias\x12H\n\x10ListaTopNoticias\x12\x18.noticias.NoticiaRequest\x1a\x16.noticias.NoticiaReply\"\x00\x30\x01\x12O\n\x17ListaTopNoticiasNoCache\x12\x18.noticias.NoticiaRequest\x1a\x16.noticias.NoticiaReply\"\x00\x30\x01\x12\x34\n\x04Ping\x12\x15.noticias.PingRequest\x1a\x13.noticias.PingReply\"\x00\x62\x06proto3')
)




_NOTICIAREQUEST = _descriptor.Descriptor(
  name='NoticiaRequest',
  full_name='noticias.NoticiaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipoNoticia', full_name='noticias.NoticiaRequest.tipoNoticia', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=69,
)


_NOTICIAREPLY = _descriptor.Descriptor(
  name='NoticiaReply',
  full_name='noticias.NoticiaReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='noticias.NoticiaReply.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='titulo', full_name='noticias.NoticiaReply.titulo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtitulo', full_name='noticias.NoticiaReply.subtitulo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='articulo', full_name='noticias.NoticiaReply.articulo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contador', full_name='noticias.NoticiaReply.contador', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=71,
  serialized_end=168,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='noticias.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='noticias.PingRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=170,
  serialized_end=200,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='noticias.PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='noticias.PingReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=202,
  serialized_end=230,
)

DESCRIPTOR.message_types_by_name['NoticiaRequest'] = _NOTICIAREQUEST
DESCRIPTOR.message_types_by_name['NoticiaReply'] = _NOTICIAREPLY
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoticiaRequest = _reflection.GeneratedProtocolMessageType('NoticiaRequest', (_message.Message,), dict(
  DESCRIPTOR = _NOTICIAREQUEST,
  __module__ = 'microservice_pb2'
  # @@protoc_insertion_point(class_scope:noticias.NoticiaRequest)
  ))
_sym_db.RegisterMessage(NoticiaRequest)

NoticiaReply = _reflection.GeneratedProtocolMessageType('NoticiaReply', (_message.Message,), dict(
  DESCRIPTOR = _NOTICIAREPLY,
  __module__ = 'microservice_pb2'
  # @@protoc_insertion_point(class_scope:noticias.NoticiaReply)
  ))
_sym_db.RegisterMessage(NoticiaReply)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'microservice_pb2'
  # @@protoc_insertion_point(class_scope:noticias.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), dict(
  DESCRIPTOR = _PINGREPLY,
  __module__ = 'microservice_pb2'
  # @@protoc_insertion_point(class_scope:noticias.PingReply)
  ))
_sym_db.RegisterMessage(PingReply)



_NOTICIAS = _descriptor.ServiceDescriptor(
  name='Noticias',
  full_name='noticias.Noticias',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=233,
  serialized_end=452,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListaTopNoticias',
    full_name='noticias.Noticias.ListaTopNoticias',
    index=0,
    containing_service=None,
    input_type=_NOTICIAREQUEST,
    output_type=_NOTICIAREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListaTopNoticiasNoCache',
    full_name='noticias.Noticias.ListaTopNoticiasNoCache',
    index=1,
    containing_service=None,
    input_type=_NOTICIAREQUEST,
    output_type=_NOTICIAREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='noticias.Noticias.Ping',
    index=2,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTICIAS)

DESCRIPTOR.services_by_name['Noticias'] = _NOTICIAS

# @@protoc_insertion_point(module_scope)
