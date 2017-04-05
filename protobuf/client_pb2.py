# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/client.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf import shared_pb2 as protobuf_dot_shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/client.proto',
  package='starbelly',
  syntax='proto2',
  serialized_pb=_b('\n\x15protobuf/client.proto\x12\tstarbelly\x1a\x15protobuf/shared.proto\"\xb0\x03\n\x07Request\x12\x12\n\nrequest_id\x18\x01 \x02(\x05\x12/\n\tlist_jobs\x18\x02 \x01(\x0b\x32\x1a.starbelly.RequestListJobsH\x00\x12&\n\x04ping\x18\x03 \x01(\x0b\x32\x16.starbelly.RequestPingH\x00\x12=\n\x11set_job_run_state\x18\x04 \x01(\x0b\x32 .starbelly.RequestSetJobRunStateH\x00\x12/\n\tstart_job\x18\x05 \x01(\x0b\x32\x1a.starbelly.RequestStartJobH\x00\x12\x45\n\x15subscribe_jobs_status\x18\x06 \x01(\x0b\x32$.starbelly.RequestSubscribeJobStatusH\x00\x12@\n\x12subscribe_job_sync\x18\x07 \x01(\x0b\x32\".starbelly.RequestSubscribeJobSyncH\x00\x12\x34\n\x0bunsubscribe\x18\x08 \x01(\x0b\x32\x1d.starbelly.RequestUnsubscribeH\x00\x42\t\n\x07\x43ommand\"0\n\x0fRequestListJobs\x12\x1d\n\x04page\x18\x01 \x01(\x0b\x32\x0f.starbelly.Page\"\x1b\n\x0bRequestPing\x12\x0c\n\x04pong\x18\x01 \x01(\t\"R\n\x15RequestSetJobRunState\x12\x0e\n\x06job_id\x18\x01 \x02(\x0c\x12)\n\trun_state\x18\x02 \x02(\x0e\x32\x16.starbelly.JobRunState\".\n\x0fRequestStartJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05seeds\x18\x02 \x03(\t\"4\n\x19RequestSubscribeJobStatus\x12\x17\n\x0cmin_interval\x18\x01 \x01(\x01:\x01\x31\"[\n\x17RequestSubscribeJobSync\x12\x0e\n\x06job_id\x18\x01 \x02(\x0c\x12\x12\n\nsync_token\x18\x02 \x01(\x0c\x12\x1c\n\x0e\x63ompression_ok\x18\x03 \x01(\x08:\x04true\"-\n\x12RequestUnsubscribe\x12\x17\n\x0fsubscription_id\x18\x01 \x02(\x05')
  ,
  dependencies=[protobuf_dot_shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='starbelly.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='starbelly.Request.request_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_jobs', full_name='starbelly.Request.list_jobs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='starbelly.Request.ping', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_job_run_state', full_name='starbelly.Request.set_job_run_state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_job', full_name='starbelly.Request.start_job', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscribe_jobs_status', full_name='starbelly.Request.subscribe_jobs_status', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscribe_job_sync', full_name='starbelly.Request.subscribe_job_sync', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unsubscribe', full_name='starbelly.Request.unsubscribe', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Command', full_name='starbelly.Request.Command',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=60,
  serialized_end=492,
)


_REQUESTLISTJOBS = _descriptor.Descriptor(
  name='RequestListJobs',
  full_name='starbelly.RequestListJobs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='starbelly.RequestListJobs.page', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=542,
)


_REQUESTPING = _descriptor.Descriptor(
  name='RequestPing',
  full_name='starbelly.RequestPing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pong', full_name='starbelly.RequestPing.pong', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=571,
)


_REQUESTSETJOBRUNSTATE = _descriptor.Descriptor(
  name='RequestSetJobRunState',
  full_name='starbelly.RequestSetJobRunState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='starbelly.RequestSetJobRunState.job_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run_state', full_name='starbelly.RequestSetJobRunState.run_state', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=655,
)


_REQUESTSTARTJOB = _descriptor.Descriptor(
  name='RequestStartJob',
  full_name='starbelly.RequestStartJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='starbelly.RequestStartJob.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seeds', full_name='starbelly.RequestStartJob.seeds', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=657,
  serialized_end=703,
)


_REQUESTSUBSCRIBEJOBSTATUS = _descriptor.Descriptor(
  name='RequestSubscribeJobStatus',
  full_name='starbelly.RequestSubscribeJobStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_interval', full_name='starbelly.RequestSubscribeJobStatus.min_interval', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=757,
)


_REQUESTSUBSCRIBEJOBSYNC = _descriptor.Descriptor(
  name='RequestSubscribeJobSync',
  full_name='starbelly.RequestSubscribeJobSync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='starbelly.RequestSubscribeJobSync.job_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_token', full_name='starbelly.RequestSubscribeJobSync.sync_token', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compression_ok', full_name='starbelly.RequestSubscribeJobSync.compression_ok', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=850,
)


_REQUESTUNSUBSCRIBE = _descriptor.Descriptor(
  name='RequestUnsubscribe',
  full_name='starbelly.RequestUnsubscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subscription_id', full_name='starbelly.RequestUnsubscribe.subscription_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=852,
  serialized_end=897,
)

_REQUEST.fields_by_name['list_jobs'].message_type = _REQUESTLISTJOBS
_REQUEST.fields_by_name['ping'].message_type = _REQUESTPING
_REQUEST.fields_by_name['set_job_run_state'].message_type = _REQUESTSETJOBRUNSTATE
_REQUEST.fields_by_name['start_job'].message_type = _REQUESTSTARTJOB
_REQUEST.fields_by_name['subscribe_jobs_status'].message_type = _REQUESTSUBSCRIBEJOBSTATUS
_REQUEST.fields_by_name['subscribe_job_sync'].message_type = _REQUESTSUBSCRIBEJOBSYNC
_REQUEST.fields_by_name['unsubscribe'].message_type = _REQUESTUNSUBSCRIBE
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['list_jobs'])
_REQUEST.fields_by_name['list_jobs'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['ping'])
_REQUEST.fields_by_name['ping'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['set_job_run_state'])
_REQUEST.fields_by_name['set_job_run_state'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['start_job'])
_REQUEST.fields_by_name['start_job'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['subscribe_jobs_status'])
_REQUEST.fields_by_name['subscribe_jobs_status'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['subscribe_job_sync'])
_REQUEST.fields_by_name['subscribe_job_sync'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUEST.oneofs_by_name['Command'].fields.append(
  _REQUEST.fields_by_name['unsubscribe'])
_REQUEST.fields_by_name['unsubscribe'].containing_oneof = _REQUEST.oneofs_by_name['Command']
_REQUESTLISTJOBS.fields_by_name['page'].message_type = protobuf_dot_shared__pb2._PAGE
_REQUESTSETJOBRUNSTATE.fields_by_name['run_state'].enum_type = protobuf_dot_shared__pb2._JOBRUNSTATE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['RequestListJobs'] = _REQUESTLISTJOBS
DESCRIPTOR.message_types_by_name['RequestPing'] = _REQUESTPING
DESCRIPTOR.message_types_by_name['RequestSetJobRunState'] = _REQUESTSETJOBRUNSTATE
DESCRIPTOR.message_types_by_name['RequestStartJob'] = _REQUESTSTARTJOB
DESCRIPTOR.message_types_by_name['RequestSubscribeJobStatus'] = _REQUESTSUBSCRIBEJOBSTATUS
DESCRIPTOR.message_types_by_name['RequestSubscribeJobSync'] = _REQUESTSUBSCRIBEJOBSYNC
DESCRIPTOR.message_types_by_name['RequestUnsubscribe'] = _REQUESTUNSUBSCRIBE

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.Request)
  ))
_sym_db.RegisterMessage(Request)

RequestListJobs = _reflection.GeneratedProtocolMessageType('RequestListJobs', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTLISTJOBS,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestListJobs)
  ))
_sym_db.RegisterMessage(RequestListJobs)

RequestPing = _reflection.GeneratedProtocolMessageType('RequestPing', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTPING,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestPing)
  ))
_sym_db.RegisterMessage(RequestPing)

RequestSetJobRunState = _reflection.GeneratedProtocolMessageType('RequestSetJobRunState', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSETJOBRUNSTATE,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestSetJobRunState)
  ))
_sym_db.RegisterMessage(RequestSetJobRunState)

RequestStartJob = _reflection.GeneratedProtocolMessageType('RequestStartJob', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSTARTJOB,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestStartJob)
  ))
_sym_db.RegisterMessage(RequestStartJob)

RequestSubscribeJobStatus = _reflection.GeneratedProtocolMessageType('RequestSubscribeJobStatus', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSUBSCRIBEJOBSTATUS,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestSubscribeJobStatus)
  ))
_sym_db.RegisterMessage(RequestSubscribeJobStatus)

RequestSubscribeJobSync = _reflection.GeneratedProtocolMessageType('RequestSubscribeJobSync', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSUBSCRIBEJOBSYNC,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestSubscribeJobSync)
  ))
_sym_db.RegisterMessage(RequestSubscribeJobSync)

RequestUnsubscribe = _reflection.GeneratedProtocolMessageType('RequestUnsubscribe', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUNSUBSCRIBE,
  __module__ = 'protobuf.client_pb2'
  # @@protoc_insertion_point(class_scope:starbelly.RequestUnsubscribe)
  ))
_sym_db.RegisterMessage(RequestUnsubscribe)


# @@protoc_insertion_point(module_scope)
