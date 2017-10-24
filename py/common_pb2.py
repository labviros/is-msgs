# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='is.common',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\tis.common\"A\n\x10SamplingSettings\x12\x13\n\tfrequency\x18\x01 \x01(\x02H\x00\x12\x10\n\x06period\x18\x02 \x01(\x02H\x00\x42\x06\n\x04rate\"\x1f\n\rFieldSelector\x12\x0e\n\x06\x66ields\x18\x01 \x03(\r\":\n\x06Status\x12#\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x15.is.common.StatusCode\x12\x0b\n\x03why\x18\x02 \x01(\t\"<\n\x0c\x44oubleMatrix\x12\x0c\n\x04rows\x18\x01 \x01(\r\x12\x0c\n\x04\x63ols\x18\x02 \x01(\r\x12\x10\n\x04\x64\x61ta\x18\x03 \x03(\x01\x42\x02\x10\x01*\xfe\x01\n\nStatusCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\r\n\tCANCELLED\x10\x02\x12\x14\n\x10INVALID_ARGUMENT\x10\x03\x12\x15\n\x11\x44\x45\x41\x44LINE_EXCEEDED\x10\x04\x12\r\n\tNOT_FOUND\x10\x05\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x06\x12\x15\n\x11PERMISSION_DENIED\x10\x07\x12\x13\n\x0fUNAUTHENTICATED\x10\x08\x12\x17\n\x13\x46\x41ILED_PRECONDITION\x10\t\x12\x10\n\x0cOUT_OF_RANGE\x10\n\x12\x11\n\rUNIMPLEMENTED\x10\x0b\x12\x12\n\x0eINTERNAL_ERROR\x10\x0c\x42\x0f\n\rcom.is.commonb\x06proto3')
)

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='is.common.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ARGUMENT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEADLINE_EXCEEDED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_EXISTS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSION_DENIED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHENTICATED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_PRECONDITION', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_RANGE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIMPLEMENTED', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=250,
  serialized_end=504,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
UNKNOWN = 0
OK = 1
CANCELLED = 2
INVALID_ARGUMENT = 3
DEADLINE_EXCEEDED = 4
NOT_FOUND = 5
ALREADY_EXISTS = 6
PERMISSION_DENIED = 7
UNAUTHENTICATED = 8
FAILED_PRECONDITION = 9
OUT_OF_RANGE = 10
UNIMPLEMENTED = 11
INTERNAL_ERROR = 12



_SAMPLINGSETTINGS = _descriptor.Descriptor(
  name='SamplingSettings',
  full_name='is.common.SamplingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='is.common.SamplingSettings.frequency', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='is.common.SamplingSettings.period', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
    _descriptor.OneofDescriptor(
      name='rate', full_name='is.common.SamplingSettings.rate',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=27,
  serialized_end=92,
)


_FIELDSELECTOR = _descriptor.Descriptor(
  name='FieldSelector',
  full_name='is.common.FieldSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='is.common.FieldSelector.fields', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=125,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='is.common.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='is.common.Status.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='why', full_name='is.common.Status.why', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=127,
  serialized_end=185,
)


_DOUBLEMATRIX = _descriptor.Descriptor(
  name='DoubleMatrix',
  full_name='is.common.DoubleMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='is.common.DoubleMatrix.rows', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cols', full_name='is.common.DoubleMatrix.cols', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='is.common.DoubleMatrix.data', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=187,
  serialized_end=247,
)

_SAMPLINGSETTINGS.oneofs_by_name['rate'].fields.append(
  _SAMPLINGSETTINGS.fields_by_name['frequency'])
_SAMPLINGSETTINGS.fields_by_name['frequency'].containing_oneof = _SAMPLINGSETTINGS.oneofs_by_name['rate']
_SAMPLINGSETTINGS.oneofs_by_name['rate'].fields.append(
  _SAMPLINGSETTINGS.fields_by_name['period'])
_SAMPLINGSETTINGS.fields_by_name['period'].containing_oneof = _SAMPLINGSETTINGS.oneofs_by_name['rate']
_STATUS.fields_by_name['code'].enum_type = _STATUSCODE
DESCRIPTOR.message_types_by_name['SamplingSettings'] = _SAMPLINGSETTINGS
DESCRIPTOR.message_types_by_name['FieldSelector'] = _FIELDSELECTOR
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['DoubleMatrix'] = _DOUBLEMATRIX
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SamplingSettings = _reflection.GeneratedProtocolMessageType('SamplingSettings', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLINGSETTINGS,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.SamplingSettings)
  ))
_sym_db.RegisterMessage(SamplingSettings)

FieldSelector = _reflection.GeneratedProtocolMessageType('FieldSelector', (_message.Message,), dict(
  DESCRIPTOR = _FIELDSELECTOR,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.FieldSelector)
  ))
_sym_db.RegisterMessage(FieldSelector)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.Status)
  ))
_sym_db.RegisterMessage(Status)

DoubleMatrix = _reflection.GeneratedProtocolMessageType('DoubleMatrix', (_message.Message,), dict(
  DESCRIPTOR = _DOUBLEMATRIX,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:is.common.DoubleMatrix)
  ))
_sym_db.RegisterMessage(DoubleMatrix)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\rcom.is.common'))
_DOUBLEMATRIX.fields_by_name['data'].has_options = True
_DOUBLEMATRIX.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
