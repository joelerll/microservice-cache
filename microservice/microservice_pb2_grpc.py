# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import microservice_pb2 as microservice__pb2


class NoticiasStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListaTopNoticias = channel.unary_stream(
        '/noticias.Noticias/ListaTopNoticias',
        request_serializer=microservice__pb2.NoticiaRequest.SerializeToString,
        response_deserializer=microservice__pb2.NoticiaReply.FromString,
        )
    self.ListaTopNoticiasNoCache = channel.unary_stream(
        '/noticias.Noticias/ListaTopNoticiasNoCache',
        request_serializer=microservice__pb2.NoticiaRequest.SerializeToString,
        response_deserializer=microservice__pb2.NoticiaReply.FromString,
        )
    self.Ping = channel.unary_unary(
        '/noticias.Noticias/Ping',
        request_serializer=microservice__pb2.PingRequest.SerializeToString,
        response_deserializer=microservice__pb2.PingReply.FromString,
        )


class NoticiasServicer(object):
  """The greeting service definition.
  """

  def ListaTopNoticias(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListaTopNoticiasNoCache(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NoticiasServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListaTopNoticias': grpc.unary_stream_rpc_method_handler(
          servicer.ListaTopNoticias,
          request_deserializer=microservice__pb2.NoticiaRequest.FromString,
          response_serializer=microservice__pb2.NoticiaReply.SerializeToString,
      ),
      'ListaTopNoticiasNoCache': grpc.unary_stream_rpc_method_handler(
          servicer.ListaTopNoticiasNoCache,
          request_deserializer=microservice__pb2.NoticiaRequest.FromString,
          response_serializer=microservice__pb2.NoticiaReply.SerializeToString,
      ),
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=microservice__pb2.PingRequest.FromString,
          response_serializer=microservice__pb2.PingReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'noticias.Noticias', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
