# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cal/calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63\x61l/calculator.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\x32.\n\nCalculator\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x62\x06proto3')



_NUMBER = DESCRIPTOR.message_types_by_name['Number']
Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'cal.calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)

_CALCULATOR = DESCRIPTOR.services_by_name['Calculator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NUMBER._serialized_start=24
  _NUMBER._serialized_end=47
  _CALCULATOR._serialized_start=49
  _CALCULATOR._serialized_end=95
# @@protoc_insertion_point(module_scope)