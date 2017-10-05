# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import nlaapi_pb2 as nlaapi__pb2


class NLACoreApiStub(object):
  """
  Core API

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendNetlinkMessage = channel.unary_unary(
        '/nlaapi.NLACoreApi/SendNetlinkMessage',
        request_serializer=nlaapi__pb2.NetlinkMessage.SerializeToString,
        response_deserializer=nlaapi__pb2.NetlinkMessageReply.FromString,
        )
    self.MonNetlinkMessage = channel.unary_stream(
        '/nlaapi.NLACoreApi/MonNetlinkMessage',
        request_serializer=nlaapi__pb2.Node.SerializeToString,
        response_deserializer=nlaapi__pb2.NetlinkMessageUnion.FromString,
        )


class NLACoreApiServicer(object):
  """
  Core API

  """

  def SendNetlinkMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MonNetlinkMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NLACoreApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendNetlinkMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SendNetlinkMessage,
          request_deserializer=nlaapi__pb2.NetlinkMessage.FromString,
          response_serializer=nlaapi__pb2.NetlinkMessageReply.SerializeToString,
      ),
      'MonNetlinkMessage': grpc.unary_stream_rpc_method_handler(
          servicer.MonNetlinkMessage,
          request_deserializer=nlaapi__pb2.Node.FromString,
          response_serializer=nlaapi__pb2.NetlinkMessageUnion.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nlaapi.NLACoreApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NLAApiStub(object):
  """
  Application API

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ModVpn = channel.unary_unary(
        '/nlaapi.NLAApi/ModVpn',
        request_serializer=nlaapi__pb2.ModVpnRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.ModVpnReply.FromString,
        )
    self.ModNetlink = channel.unary_unary(
        '/nlaapi.NLAApi/ModNetlink',
        request_serializer=nlaapi__pb2.NetlinkMessageUnion.SerializeToString,
        response_deserializer=nlaapi__pb2.ModNetlinkReply.FromString,
        )
    self.MonNetlink = channel.unary_stream(
        '/nlaapi.NLAApi/MonNetlink',
        request_serializer=nlaapi__pb2.MonNetlinkRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.NetlinkMessageUnion.FromString,
        )
    self.GetLink = channel.unary_unary(
        '/nlaapi.NLAApi/GetLink',
        request_serializer=nlaapi__pb2.LinkKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Link.FromString,
        )
    self.GetAddr = channel.unary_unary(
        '/nlaapi.NLAApi/GetAddr',
        request_serializer=nlaapi__pb2.AddrKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Addr.FromString,
        )
    self.GetNeigh = channel.unary_unary(
        '/nlaapi.NLAApi/GetNeigh',
        request_serializer=nlaapi__pb2.NeighKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Neigh.FromString,
        )
    self.GetRoute = channel.unary_unary(
        '/nlaapi.NLAApi/GetRoute',
        request_serializer=nlaapi__pb2.RouteKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Route.FromString,
        )
    self.GetMpls = channel.unary_unary(
        '/nlaapi.NLAApi/GetMpls',
        request_serializer=nlaapi__pb2.MplsKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Route.FromString,
        )
    self.GetNode = channel.unary_unary(
        '/nlaapi.NLAApi/GetNode',
        request_serializer=nlaapi__pb2.NodeKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Node.FromString,
        )
    self.GetVpn = channel.unary_unary(
        '/nlaapi.NLAApi/GetVpn',
        request_serializer=nlaapi__pb2.VpnKey.SerializeToString,
        response_deserializer=nlaapi__pb2.Vpn.FromString,
        )
    self.GetEncapInfo = channel.unary_unary(
        '/nlaapi.NLAApi/GetEncapInfo',
        request_serializer=nlaapi__pb2.EncapInfoKey.SerializeToString,
        response_deserializer=nlaapi__pb2.EncapInfo.FromString,
        )
    self.GetLinks = channel.unary_stream(
        '/nlaapi.NLAApi/GetLinks',
        request_serializer=nlaapi__pb2.GetLinksRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Link.FromString,
        )
    self.GetAddrs = channel.unary_stream(
        '/nlaapi.NLAApi/GetAddrs',
        request_serializer=nlaapi__pb2.GetAddrsRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Addr.FromString,
        )
    self.GetNeighs = channel.unary_stream(
        '/nlaapi.NLAApi/GetNeighs',
        request_serializer=nlaapi__pb2.GetNeighsRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Neigh.FromString,
        )
    self.GetRoutes = channel.unary_stream(
        '/nlaapi.NLAApi/GetRoutes',
        request_serializer=nlaapi__pb2.GetRoutesRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Route.FromString,
        )
    self.GetMplss = channel.unary_stream(
        '/nlaapi.NLAApi/GetMplss',
        request_serializer=nlaapi__pb2.GetMplssRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Route.FromString,
        )
    self.GetNodes = channel.unary_stream(
        '/nlaapi.NLAApi/GetNodes',
        request_serializer=nlaapi__pb2.GetNodesRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Node.FromString,
        )
    self.GetVpns = channel.unary_stream(
        '/nlaapi.NLAApi/GetVpns',
        request_serializer=nlaapi__pb2.GetVpnsRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Vpn.FromString,
        )
    self.GetEncapInfos = channel.unary_stream(
        '/nlaapi.NLAApi/GetEncapInfos',
        request_serializer=nlaapi__pb2.GetEncapInfosRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.EncapInfo.FromString,
        )
    self.GetStats = channel.unary_stream(
        '/nlaapi.NLAApi/GetStats',
        request_serializer=nlaapi__pb2.GetStatsRequest.SerializeToString,
        response_deserializer=nlaapi__pb2.Stat.FromString,
        )


class NLAApiServicer(object):
  """
  Application API

  """

  def ModVpn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModNetlink(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MonNetlink(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLink(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddr(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNeigh(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMpls(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVpn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEncapInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLinks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddrs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNeighs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRoutes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMplss(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNodes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVpns(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEncapInfos(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NLAApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ModVpn': grpc.unary_unary_rpc_method_handler(
          servicer.ModVpn,
          request_deserializer=nlaapi__pb2.ModVpnRequest.FromString,
          response_serializer=nlaapi__pb2.ModVpnReply.SerializeToString,
      ),
      'ModNetlink': grpc.unary_unary_rpc_method_handler(
          servicer.ModNetlink,
          request_deserializer=nlaapi__pb2.NetlinkMessageUnion.FromString,
          response_serializer=nlaapi__pb2.ModNetlinkReply.SerializeToString,
      ),
      'MonNetlink': grpc.unary_stream_rpc_method_handler(
          servicer.MonNetlink,
          request_deserializer=nlaapi__pb2.MonNetlinkRequest.FromString,
          response_serializer=nlaapi__pb2.NetlinkMessageUnion.SerializeToString,
      ),
      'GetLink': grpc.unary_unary_rpc_method_handler(
          servicer.GetLink,
          request_deserializer=nlaapi__pb2.LinkKey.FromString,
          response_serializer=nlaapi__pb2.Link.SerializeToString,
      ),
      'GetAddr': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddr,
          request_deserializer=nlaapi__pb2.AddrKey.FromString,
          response_serializer=nlaapi__pb2.Addr.SerializeToString,
      ),
      'GetNeigh': grpc.unary_unary_rpc_method_handler(
          servicer.GetNeigh,
          request_deserializer=nlaapi__pb2.NeighKey.FromString,
          response_serializer=nlaapi__pb2.Neigh.SerializeToString,
      ),
      'GetRoute': grpc.unary_unary_rpc_method_handler(
          servicer.GetRoute,
          request_deserializer=nlaapi__pb2.RouteKey.FromString,
          response_serializer=nlaapi__pb2.Route.SerializeToString,
      ),
      'GetMpls': grpc.unary_unary_rpc_method_handler(
          servicer.GetMpls,
          request_deserializer=nlaapi__pb2.MplsKey.FromString,
          response_serializer=nlaapi__pb2.Route.SerializeToString,
      ),
      'GetNode': grpc.unary_unary_rpc_method_handler(
          servicer.GetNode,
          request_deserializer=nlaapi__pb2.NodeKey.FromString,
          response_serializer=nlaapi__pb2.Node.SerializeToString,
      ),
      'GetVpn': grpc.unary_unary_rpc_method_handler(
          servicer.GetVpn,
          request_deserializer=nlaapi__pb2.VpnKey.FromString,
          response_serializer=nlaapi__pb2.Vpn.SerializeToString,
      ),
      'GetEncapInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetEncapInfo,
          request_deserializer=nlaapi__pb2.EncapInfoKey.FromString,
          response_serializer=nlaapi__pb2.EncapInfo.SerializeToString,
      ),
      'GetLinks': grpc.unary_stream_rpc_method_handler(
          servicer.GetLinks,
          request_deserializer=nlaapi__pb2.GetLinksRequest.FromString,
          response_serializer=nlaapi__pb2.Link.SerializeToString,
      ),
      'GetAddrs': grpc.unary_stream_rpc_method_handler(
          servicer.GetAddrs,
          request_deserializer=nlaapi__pb2.GetAddrsRequest.FromString,
          response_serializer=nlaapi__pb2.Addr.SerializeToString,
      ),
      'GetNeighs': grpc.unary_stream_rpc_method_handler(
          servicer.GetNeighs,
          request_deserializer=nlaapi__pb2.GetNeighsRequest.FromString,
          response_serializer=nlaapi__pb2.Neigh.SerializeToString,
      ),
      'GetRoutes': grpc.unary_stream_rpc_method_handler(
          servicer.GetRoutes,
          request_deserializer=nlaapi__pb2.GetRoutesRequest.FromString,
          response_serializer=nlaapi__pb2.Route.SerializeToString,
      ),
      'GetMplss': grpc.unary_stream_rpc_method_handler(
          servicer.GetMplss,
          request_deserializer=nlaapi__pb2.GetMplssRequest.FromString,
          response_serializer=nlaapi__pb2.Route.SerializeToString,
      ),
      'GetNodes': grpc.unary_stream_rpc_method_handler(
          servicer.GetNodes,
          request_deserializer=nlaapi__pb2.GetNodesRequest.FromString,
          response_serializer=nlaapi__pb2.Node.SerializeToString,
      ),
      'GetVpns': grpc.unary_stream_rpc_method_handler(
          servicer.GetVpns,
          request_deserializer=nlaapi__pb2.GetVpnsRequest.FromString,
          response_serializer=nlaapi__pb2.Vpn.SerializeToString,
      ),
      'GetEncapInfos': grpc.unary_stream_rpc_method_handler(
          servicer.GetEncapInfos,
          request_deserializer=nlaapi__pb2.GetEncapInfosRequest.FromString,
          response_serializer=nlaapi__pb2.EncapInfo.SerializeToString,
      ),
      'GetStats': grpc.unary_stream_rpc_method_handler(
          servicer.GetStats,
          request_deserializer=nlaapi__pb2.GetStatsRequest.FromString,
          response_serializer=nlaapi__pb2.Stat.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nlaapi.NLAApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
