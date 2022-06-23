# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chiral_db.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63hiral_db.proto\x12\x08\x63hiraldb\"\x1a\n\x08Molecule\x12\x0e\n\x06smiles\x18\x01 \x01(\t\"D\n\x11RequestSimilarity\x12\x1f\n\x03mol\x18\x01 \x01(\x0b\x32\x12.chiraldb.Molecule\x12\x0e\n\x06\x63utoff\x18\x02 \x01(\x02\"z\n\x0fReplySimilarity\x12\x37\n\x07results\x18\x01 \x03(\x0b\x32&.chiraldb.ReplySimilarity.ResultsEntry\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x32W\n\x08\x43hiralDb\x12K\n\x0fQuerySimilarity\x12\x1b.chiraldb.RequestSimilarity\x1a\x19.chiraldb.ReplySimilarity\"\x00\x62\x06proto3')



_MOLECULE = DESCRIPTOR.message_types_by_name['Molecule']
_REQUESTSIMILARITY = DESCRIPTOR.message_types_by_name['RequestSimilarity']
_REPLYSIMILARITY = DESCRIPTOR.message_types_by_name['ReplySimilarity']
_REPLYSIMILARITY_RESULTSENTRY = _REPLYSIMILARITY.nested_types_by_name['ResultsEntry']
Molecule = _reflection.GeneratedProtocolMessageType('Molecule', (_message.Message,), {
  'DESCRIPTOR' : _MOLECULE,
  '__module__' : 'chiral_db_pb2'
  # @@protoc_insertion_point(class_scope:chiraldb.Molecule)
  })
_sym_db.RegisterMessage(Molecule)

RequestSimilarity = _reflection.GeneratedProtocolMessageType('RequestSimilarity', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSIMILARITY,
  '__module__' : 'chiral_db_pb2'
  # @@protoc_insertion_point(class_scope:chiraldb.RequestSimilarity)
  })
_sym_db.RegisterMessage(RequestSimilarity)

ReplySimilarity = _reflection.GeneratedProtocolMessageType('ReplySimilarity', (_message.Message,), {

  'ResultsEntry' : _reflection.GeneratedProtocolMessageType('ResultsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REPLYSIMILARITY_RESULTSENTRY,
    '__module__' : 'chiral_db_pb2'
    # @@protoc_insertion_point(class_scope:chiraldb.ReplySimilarity.ResultsEntry)
    })
  ,
  'DESCRIPTOR' : _REPLYSIMILARITY,
  '__module__' : 'chiral_db_pb2'
  # @@protoc_insertion_point(class_scope:chiraldb.ReplySimilarity)
  })
_sym_db.RegisterMessage(ReplySimilarity)
_sym_db.RegisterMessage(ReplySimilarity.ResultsEntry)

_CHIRALDB = DESCRIPTOR.services_by_name['ChiralDb']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPLYSIMILARITY_RESULTSENTRY._options = None
  _REPLYSIMILARITY_RESULTSENTRY._serialized_options = b'8\001'
  _MOLECULE._serialized_start=29
  _MOLECULE._serialized_end=55
  _REQUESTSIMILARITY._serialized_start=57
  _REQUESTSIMILARITY._serialized_end=125
  _REPLYSIMILARITY._serialized_start=127
  _REPLYSIMILARITY._serialized_end=249
  _REPLYSIMILARITY_RESULTSENTRY._serialized_start=203
  _REPLYSIMILARITY_RESULTSENTRY._serialized_end=249
  _CHIRALDB._serialized_start=251
  _CHIRALDB._serialized_end=338
# @@protoc_insertion_point(module_scope)