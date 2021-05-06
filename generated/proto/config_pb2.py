# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/config.proto',
  package='ashwin.stocksbalancer.spec',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12proto/config.proto\x12\x1a\x61shwin.stocksbalancer.spec\"\xb7\x01\n\x06\x43onfig\x12\x31\n\x06stocks\x18\x01 \x03(\x0b\x32!.ashwin.stocksbalancer.spec.Stock\x12\x43\n\x0f\x64ownload_config\x18\x02 \x01(\x0b\x32*.ashwin.stocksbalancer.spec.DownloadConfig\x12\x35\n\x08quest_db\x18\x03 \x01(\x0b\x32#.ashwin.stocksbalancer.spec.QuestDb\"2\n\x05Stock\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x19\n\x11\x66irst_transaction\x18\x02 \x01(\t\"\x87\x01\n\x0e\x44ownloadConfig\x12\x13\n\x0boutput_size\x18\x01 \x01(\t\x12\'\n\x1fmax_tries_before_end_of_trading\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x61te_format\x18\x03 \x01(\t\x12\"\n\x1a\x62\x61tch_size_for_persistence\x18\x04 \x01(\x05\"\x89\x01\n\x07QuestDb\x12\x17\n\x0fmin_connections\x18\x01 \x01(\x05\x12\x17\n\x0fmax_connections\x18\x02 \x01(\x05\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x07 \x01(\tb\x06proto3')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='ashwin.stocksbalancer.spec.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stocks', full_name='ashwin.stocksbalancer.spec.Config.stocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='download_config', full_name='ashwin.stocksbalancer.spec.Config.download_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quest_db', full_name='ashwin.stocksbalancer.spec.Config.quest_db', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=51,
  serialized_end=234,
)


_STOCK = _descriptor.Descriptor(
  name='Stock',
  full_name='ashwin.stocksbalancer.spec.Stock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='ashwin.stocksbalancer.spec.Stock.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_transaction', full_name='ashwin.stocksbalancer.spec.Stock.first_transaction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=236,
  serialized_end=286,
)


_DOWNLOADCONFIG = _descriptor.Descriptor(
  name='DownloadConfig',
  full_name='ashwin.stocksbalancer.spec.DownloadConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_size', full_name='ashwin.stocksbalancer.spec.DownloadConfig.output_size', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_tries_before_end_of_trading', full_name='ashwin.stocksbalancer.spec.DownloadConfig.max_tries_before_end_of_trading', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_format', full_name='ashwin.stocksbalancer.spec.DownloadConfig.date_format', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size_for_persistence', full_name='ashwin.stocksbalancer.spec.DownloadConfig.batch_size_for_persistence', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=289,
  serialized_end=424,
)


_QUESTDB = _descriptor.Descriptor(
  name='QuestDb',
  full_name='ashwin.stocksbalancer.spec.QuestDb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_connections', full_name='ashwin.stocksbalancer.spec.QuestDb.min_connections', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_connections', full_name='ashwin.stocksbalancer.spec.QuestDb.max_connections', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='ashwin.stocksbalancer.spec.QuestDb.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='ashwin.stocksbalancer.spec.QuestDb.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='ashwin.stocksbalancer.spec.QuestDb.host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ashwin.stocksbalancer.spec.QuestDb.port', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database', full_name='ashwin.stocksbalancer.spec.QuestDb.database', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=427,
  serialized_end=564,
)

_CONFIG.fields_by_name['stocks'].message_type = _STOCK
_CONFIG.fields_by_name['download_config'].message_type = _DOWNLOADCONFIG
_CONFIG.fields_by_name['quest_db'].message_type = _QUESTDB
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
DESCRIPTOR.message_types_by_name['DownloadConfig'] = _DOWNLOADCONFIG
DESCRIPTOR.message_types_by_name['QuestDb'] = _QUESTDB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.Config)
  ))
_sym_db.RegisterMessage(Config)

Stock = _reflection.GeneratedProtocolMessageType('Stock', (_message.Message,), dict(
  DESCRIPTOR = _STOCK,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.Stock)
  ))
_sym_db.RegisterMessage(Stock)

DownloadConfig = _reflection.GeneratedProtocolMessageType('DownloadConfig', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADCONFIG,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.DownloadConfig)
  ))
_sym_db.RegisterMessage(DownloadConfig)

QuestDb = _reflection.GeneratedProtocolMessageType('QuestDb', (_message.Message,), dict(
  DESCRIPTOR = _QUESTDB,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.QuestDb)
  ))
_sym_db.RegisterMessage(QuestDb)


# @@protoc_insertion_point(module_scope)
