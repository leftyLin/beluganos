# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import gonslapi_pb2 as gonslapi__pb2


class GoNSLApiStub(object):
  """
  Service

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFieldEntries = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetFieldEntries',
        request_serializer=gonslapi__pb2.GetFieldEntriesRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetFieldEntriesReply.FromString,
        )
    self.GetPortInfos = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetPortInfos',
        request_serializer=gonslapi__pb2.GetPortInfosRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetPortInfosReply.FromString,
        )
    self.GetVlans = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetVlans',
        request_serializer=gonslapi__pb2.GetVlansRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetVlansReply.FromString,
        )
    self.GetL2Addrs = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL2Addrs',
        request_serializer=gonslapi__pb2.GetL2AddrsRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL2AddrsReply.FromString,
        )
    self.GetL2Stations = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL2Stations',
        request_serializer=gonslapi__pb2.GetL2StationsRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL2StationsReply.FromString,
        )
    self.FindL3Iface = channel.unary_unary(
        '/gonslapi.GoNSLApi/FindL3Iface',
        request_serializer=gonslapi__pb2.FindL3IfaceRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.FindL3IfaceReply.FromString,
        )
    self.GetL3Iface = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL3Iface',
        request_serializer=gonslapi__pb2.GetL3IfaceRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL3IfaceReply.FromString,
        )
    self.GetL3Ifaces = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL3Ifaces',
        request_serializer=gonslapi__pb2.GetL3IfacesRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL3IfacesReply.FromString,
        )
    self.GetL3Egresses = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL3Egresses',
        request_serializer=gonslapi__pb2.GetL3EgressesRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL3EgressesReply.FromString,
        )
    self.GetL3Hosts = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL3Hosts',
        request_serializer=gonslapi__pb2.GetL3HostsRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL3HostsReply.FromString,
        )
    self.GetL3Routes = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetL3Routes',
        request_serializer=gonslapi__pb2.GetL3RoutesRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetL3RoutesReply.FromString,
        )
    self.GetIDMapEntries = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetIDMapEntries',
        request_serializer=gonslapi__pb2.GetIDMapEntriesRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetIDMapEntriesReply.FromString,
        )
    self.GetTunnelInitiators = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetTunnelInitiators',
        request_serializer=gonslapi__pb2.GetTunnelInitiatorsRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetTunnelInitiatorsReply.FromString,
        )
    self.GetTunnelTerminators = channel.unary_unary(
        '/gonslapi.GoNSLApi/GetTunnelTerminators',
        request_serializer=gonslapi__pb2.GetTunnelTerminatorsRequest.SerializeToString,
        response_deserializer=gonslapi__pb2.GetTunnelTerminatorsReply.FromString,
        )


class GoNSLApiServicer(object):
  """
  Service

  """

  def GetFieldEntries(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPortInfos(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVlans(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL2Addrs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL2Stations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindL3Iface(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL3Iface(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL3Ifaces(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL3Egresses(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL3Hosts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetL3Routes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetIDMapEntries(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTunnelInitiators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTunnelTerminators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GoNSLApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFieldEntries': grpc.unary_unary_rpc_method_handler(
          servicer.GetFieldEntries,
          request_deserializer=gonslapi__pb2.GetFieldEntriesRequest.FromString,
          response_serializer=gonslapi__pb2.GetFieldEntriesReply.SerializeToString,
      ),
      'GetPortInfos': grpc.unary_unary_rpc_method_handler(
          servicer.GetPortInfos,
          request_deserializer=gonslapi__pb2.GetPortInfosRequest.FromString,
          response_serializer=gonslapi__pb2.GetPortInfosReply.SerializeToString,
      ),
      'GetVlans': grpc.unary_unary_rpc_method_handler(
          servicer.GetVlans,
          request_deserializer=gonslapi__pb2.GetVlansRequest.FromString,
          response_serializer=gonslapi__pb2.GetVlansReply.SerializeToString,
      ),
      'GetL2Addrs': grpc.unary_unary_rpc_method_handler(
          servicer.GetL2Addrs,
          request_deserializer=gonslapi__pb2.GetL2AddrsRequest.FromString,
          response_serializer=gonslapi__pb2.GetL2AddrsReply.SerializeToString,
      ),
      'GetL2Stations': grpc.unary_unary_rpc_method_handler(
          servicer.GetL2Stations,
          request_deserializer=gonslapi__pb2.GetL2StationsRequest.FromString,
          response_serializer=gonslapi__pb2.GetL2StationsReply.SerializeToString,
      ),
      'FindL3Iface': grpc.unary_unary_rpc_method_handler(
          servicer.FindL3Iface,
          request_deserializer=gonslapi__pb2.FindL3IfaceRequest.FromString,
          response_serializer=gonslapi__pb2.FindL3IfaceReply.SerializeToString,
      ),
      'GetL3Iface': grpc.unary_unary_rpc_method_handler(
          servicer.GetL3Iface,
          request_deserializer=gonslapi__pb2.GetL3IfaceRequest.FromString,
          response_serializer=gonslapi__pb2.GetL3IfaceReply.SerializeToString,
      ),
      'GetL3Ifaces': grpc.unary_unary_rpc_method_handler(
          servicer.GetL3Ifaces,
          request_deserializer=gonslapi__pb2.GetL3IfacesRequest.FromString,
          response_serializer=gonslapi__pb2.GetL3IfacesReply.SerializeToString,
      ),
      'GetL3Egresses': grpc.unary_unary_rpc_method_handler(
          servicer.GetL3Egresses,
          request_deserializer=gonslapi__pb2.GetL3EgressesRequest.FromString,
          response_serializer=gonslapi__pb2.GetL3EgressesReply.SerializeToString,
      ),
      'GetL3Hosts': grpc.unary_unary_rpc_method_handler(
          servicer.GetL3Hosts,
          request_deserializer=gonslapi__pb2.GetL3HostsRequest.FromString,
          response_serializer=gonslapi__pb2.GetL3HostsReply.SerializeToString,
      ),
      'GetL3Routes': grpc.unary_unary_rpc_method_handler(
          servicer.GetL3Routes,
          request_deserializer=gonslapi__pb2.GetL3RoutesRequest.FromString,
          response_serializer=gonslapi__pb2.GetL3RoutesReply.SerializeToString,
      ),
      'GetIDMapEntries': grpc.unary_unary_rpc_method_handler(
          servicer.GetIDMapEntries,
          request_deserializer=gonslapi__pb2.GetIDMapEntriesRequest.FromString,
          response_serializer=gonslapi__pb2.GetIDMapEntriesReply.SerializeToString,
      ),
      'GetTunnelInitiators': grpc.unary_unary_rpc_method_handler(
          servicer.GetTunnelInitiators,
          request_deserializer=gonslapi__pb2.GetTunnelInitiatorsRequest.FromString,
          response_serializer=gonslapi__pb2.GetTunnelInitiatorsReply.SerializeToString,
      ),
      'GetTunnelTerminators': grpc.unary_unary_rpc_method_handler(
          servicer.GetTunnelTerminators,
          request_deserializer=gonslapi__pb2.GetTunnelTerminatorsRequest.FromString,
          response_serializer=gonslapi__pb2.GetTunnelTerminatorsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gonslapi.GoNSLApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
