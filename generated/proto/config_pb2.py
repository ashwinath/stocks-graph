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
  serialized_pb=_b('\n\x12proto/config.proto\x12\x1a\x61shwin.stocksbalancer.spec\"\xab\x02\n\x06\x43onfig\x12\x31\n\x06stocks\x18\x01 \x03(\x0b\x32!.ashwin.stocksbalancer.spec.Stock\x12\x43\n\x0f\x64ownload_config\x18\x02 \x01(\x0b\x32*.ashwin.stocksbalancer.spec.DownloadConfig\x12=\n\x0ctimescale_db\x18\x03 \x01(\x0b\x32\'.ashwin.stocksbalancer.spec.TimescaleDb\x12\x36\n\x08\x63urrency\x18\x04 \x01(\x0b\x32$.ashwin.stocksbalancer.spec.Currency\x12\x32\n\x06trades\x18\x05 \x01(\x0b\x32\".ashwin.stocksbalancer.spec.Trades\"\x18\n\x06Trades\x12\x0e\n\x06\x66older\x18\x01 \x01(\t\"h\n\x08\x43urrency\x12\x15\n\rbase_currency\x18\x01 \x01(\t\x12\x45\n\x10other_currencies\x18\x02 \x03(\x0b\x32+.ashwin.stocksbalancer.spec.OtherCurrencies\">\n\x0fOtherCurrencies\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x19\n\x11\x66irst_transaction\x18\x02 \x01(\t\"\xa4\x01\n\x05Stock\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x19\n\x11\x66irst_transaction\x18\x02 \x01(\t\x12\x36\n\x03\x61pi\x18\x03 \x01(\x0e\x32).ashwin.stocksbalancer.spec.Stock.ApiKind\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t\"&\n\x07\x41piKind\x12\x10\n\x0c\x41lphavantage\x10\x00\x12\t\n\x05Yahoo\x10\x01\"\xa1\x02\n\x0e\x44ownloadConfig\x12\x13\n\x0b\x64\x61te_format\x18\x01 \x01(\t\x12\x63\n\x18\x61lphavantage_output_size\x18\x02 \x01(\x0e\x32\x41.ashwin.stocksbalancer.spec.DownloadConfig.AlphavantageOutputSize\x12L\n\x0cyahoo_period\x18\x03 \x01(\x0e\x32\x36.ashwin.stocksbalancer.spec.DownloadConfig.YahooPeriod\"/\n\x16\x41lphavantageOutputSize\x12\x08\n\x04\x66ull\x10\x00\x12\x0b\n\x07\x63ompact\x10\x01\"\x16\n\x0bYahooPeriod\x12\x07\n\x03max\x10\x00\"\x8d\x01\n\x0bTimescaleDb\x12\x17\n\x0fmin_connections\x18\x01 \x01(\x05\x12\x17\n\x0fmax_connections\x18\x02 \x01(\x05\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x07 \x01(\tb\x06proto3')
)



_STOCK_APIKIND = _descriptor.EnumDescriptor(
  name='ApiKind',
  full_name='ashwin.stocksbalancer.spec.Stock.ApiKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Alphavantage', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Yahoo', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=675,
  serialized_end=713,
)
_sym_db.RegisterEnumDescriptor(_STOCK_APIKIND)

_DOWNLOADCONFIG_ALPHAVANTAGEOUTPUTSIZE = _descriptor.EnumDescriptor(
  name='AlphavantageOutputSize',
  full_name='ashwin.stocksbalancer.spec.DownloadConfig.AlphavantageOutputSize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='full', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='compact', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=934,
  serialized_end=981,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADCONFIG_ALPHAVANTAGEOUTPUTSIZE)

_DOWNLOADCONFIG_YAHOOPERIOD = _descriptor.EnumDescriptor(
  name='YahooPeriod',
  full_name='ashwin.stocksbalancer.spec.DownloadConfig.YahooPeriod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='max', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=983,
  serialized_end=1005,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADCONFIG_YAHOOPERIOD)


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
      name='timescale_db', full_name='ashwin.stocksbalancer.spec.Config.timescale_db', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='ashwin.stocksbalancer.spec.Config.currency', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trades', full_name='ashwin.stocksbalancer.spec.Config.trades', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_end=350,
)


_TRADES = _descriptor.Descriptor(
  name='Trades',
  full_name='ashwin.stocksbalancer.spec.Trades',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder', full_name='ashwin.stocksbalancer.spec.Trades.folder', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=352,
  serialized_end=376,
)


_CURRENCY = _descriptor.Descriptor(
  name='Currency',
  full_name='ashwin.stocksbalancer.spec.Currency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_currency', full_name='ashwin.stocksbalancer.spec.Currency.base_currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_currencies', full_name='ashwin.stocksbalancer.spec.Currency.other_currencies', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=378,
  serialized_end=482,
)


_OTHERCURRENCIES = _descriptor.Descriptor(
  name='OtherCurrencies',
  full_name='ashwin.stocksbalancer.spec.OtherCurrencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='ashwin.stocksbalancer.spec.OtherCurrencies.currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_transaction', full_name='ashwin.stocksbalancer.spec.OtherCurrencies.first_transaction', index=1,
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
  serialized_start=484,
  serialized_end=546,
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
    _descriptor.FieldDescriptor(
      name='api', full_name='ashwin.stocksbalancer.spec.Stock.api', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='ashwin.stocksbalancer.spec.Stock.currency', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STOCK_APIKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=549,
  serialized_end=713,
)


_DOWNLOADCONFIG = _descriptor.Descriptor(
  name='DownloadConfig',
  full_name='ashwin.stocksbalancer.spec.DownloadConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_format', full_name='ashwin.stocksbalancer.spec.DownloadConfig.date_format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alphavantage_output_size', full_name='ashwin.stocksbalancer.spec.DownloadConfig.alphavantage_output_size', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yahoo_period', full_name='ashwin.stocksbalancer.spec.DownloadConfig.yahoo_period', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOWNLOADCONFIG_ALPHAVANTAGEOUTPUTSIZE,
    _DOWNLOADCONFIG_YAHOOPERIOD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=1005,
)


_TIMESCALEDB = _descriptor.Descriptor(
  name='TimescaleDb',
  full_name='ashwin.stocksbalancer.spec.TimescaleDb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_connections', full_name='ashwin.stocksbalancer.spec.TimescaleDb.min_connections', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_connections', full_name='ashwin.stocksbalancer.spec.TimescaleDb.max_connections', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='ashwin.stocksbalancer.spec.TimescaleDb.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='ashwin.stocksbalancer.spec.TimescaleDb.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='ashwin.stocksbalancer.spec.TimescaleDb.host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ashwin.stocksbalancer.spec.TimescaleDb.port', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database', full_name='ashwin.stocksbalancer.spec.TimescaleDb.database', index=6,
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
  serialized_start=1008,
  serialized_end=1149,
)

_CONFIG.fields_by_name['stocks'].message_type = _STOCK
_CONFIG.fields_by_name['download_config'].message_type = _DOWNLOADCONFIG
_CONFIG.fields_by_name['timescale_db'].message_type = _TIMESCALEDB
_CONFIG.fields_by_name['currency'].message_type = _CURRENCY
_CONFIG.fields_by_name['trades'].message_type = _TRADES
_CURRENCY.fields_by_name['other_currencies'].message_type = _OTHERCURRENCIES
_STOCK.fields_by_name['api'].enum_type = _STOCK_APIKIND
_STOCK_APIKIND.containing_type = _STOCK
_DOWNLOADCONFIG.fields_by_name['alphavantage_output_size'].enum_type = _DOWNLOADCONFIG_ALPHAVANTAGEOUTPUTSIZE
_DOWNLOADCONFIG.fields_by_name['yahoo_period'].enum_type = _DOWNLOADCONFIG_YAHOOPERIOD
_DOWNLOADCONFIG_ALPHAVANTAGEOUTPUTSIZE.containing_type = _DOWNLOADCONFIG
_DOWNLOADCONFIG_YAHOOPERIOD.containing_type = _DOWNLOADCONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Trades'] = _TRADES
DESCRIPTOR.message_types_by_name['Currency'] = _CURRENCY
DESCRIPTOR.message_types_by_name['OtherCurrencies'] = _OTHERCURRENCIES
DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
DESCRIPTOR.message_types_by_name['DownloadConfig'] = _DOWNLOADCONFIG
DESCRIPTOR.message_types_by_name['TimescaleDb'] = _TIMESCALEDB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.Config)
  ))
_sym_db.RegisterMessage(Config)

Trades = _reflection.GeneratedProtocolMessageType('Trades', (_message.Message,), dict(
  DESCRIPTOR = _TRADES,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.Trades)
  ))
_sym_db.RegisterMessage(Trades)

Currency = _reflection.GeneratedProtocolMessageType('Currency', (_message.Message,), dict(
  DESCRIPTOR = _CURRENCY,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.Currency)
  ))
_sym_db.RegisterMessage(Currency)

OtherCurrencies = _reflection.GeneratedProtocolMessageType('OtherCurrencies', (_message.Message,), dict(
  DESCRIPTOR = _OTHERCURRENCIES,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.OtherCurrencies)
  ))
_sym_db.RegisterMessage(OtherCurrencies)

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

TimescaleDb = _reflection.GeneratedProtocolMessageType('TimescaleDb', (_message.Message,), dict(
  DESCRIPTOR = _TIMESCALEDB,
  __module__ = 'proto.config_pb2'
  # @@protoc_insertion_point(class_scope:ashwin.stocksbalancer.spec.TimescaleDb)
  ))
_sym_db.RegisterMessage(TimescaleDb)


# @@protoc_insertion_point(module_scope)
