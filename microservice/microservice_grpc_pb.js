// GENERATED CODE -- DO NOT EDIT!

// Original file comments:
//  https://developers.google.com/protocol-buffers/docs/overview
//
// message Person {
//   string name = 1;
//   int32 id = 2;
//   bool has_ponycopter = 3;
// }
//
// message Noticia {
//  string id = 1;
//  string titulo  = 2;
//  string subtitulo  = 3;
//  string articulo  = 4;
//  int32 contador = 5;
// }
// python -m grpc_tools.protoc --python_out=prueba --grpc_python_out=prueba prueba.proto
// python -m grpc_tools.protoc  --python_out=prueba --proto_path=prueba prueba.proto
// python -m grpc_tools.protoc -I. --python_out=microservice --grpc_python_out=microservice microservice.proto
//
'use strict';
var grpc = require('grpc');
var microservice_microservice_pb = require('../microservice/microservice_pb.js');

function serialize_noticias_NoticiaReply(arg) {
  if (!(arg instanceof microservice_microservice_pb.NoticiaReply)) {
    throw new Error('Expected argument of type noticias.NoticiaReply');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_noticias_NoticiaReply(buffer_arg) {
  return microservice_microservice_pb.NoticiaReply.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_noticias_NoticiaRequest(arg) {
  if (!(arg instanceof microservice_microservice_pb.NoticiaRequest)) {
    throw new Error('Expected argument of type noticias.NoticiaRequest');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_noticias_NoticiaRequest(buffer_arg) {
  return microservice_microservice_pb.NoticiaRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_noticias_PingReply(arg) {
  if (!(arg instanceof microservice_microservice_pb.PingReply)) {
    throw new Error('Expected argument of type noticias.PingReply');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_noticias_PingReply(buffer_arg) {
  return microservice_microservice_pb.PingReply.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_noticias_PingRequest(arg) {
  if (!(arg instanceof microservice_microservice_pb.PingRequest)) {
    throw new Error('Expected argument of type noticias.PingRequest');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_noticias_PingRequest(buffer_arg) {
  return microservice_microservice_pb.PingRequest.deserializeBinary(new Uint8Array(buffer_arg));
}


// The greeting service definition.
var NoticiasService = exports.NoticiasService = {
  // Sends a greeting
  listaTopNoticias: {
    path: '/noticias.Noticias/ListaTopNoticias',
    requestStream: false,
    responseStream: true,
    requestType: microservice_microservice_pb.NoticiaRequest,
    responseType: microservice_microservice_pb.NoticiaReply,
    requestSerialize: serialize_noticias_NoticiaRequest,
    requestDeserialize: deserialize_noticias_NoticiaRequest,
    responseSerialize: serialize_noticias_NoticiaReply,
    responseDeserialize: deserialize_noticias_NoticiaReply,
  },
  listaTopNoticiasNoCache: {
    path: '/noticias.Noticias/ListaTopNoticiasNoCache',
    requestStream: false,
    responseStream: true,
    requestType: microservice_microservice_pb.NoticiaRequest,
    responseType: microservice_microservice_pb.NoticiaReply,
    requestSerialize: serialize_noticias_NoticiaRequest,
    requestDeserialize: deserialize_noticias_NoticiaRequest,
    responseSerialize: serialize_noticias_NoticiaReply,
    responseDeserialize: deserialize_noticias_NoticiaReply,
  },
  ping: {
    path: '/noticias.Noticias/Ping',
    requestStream: false,
    responseStream: false,
    requestType: microservice_microservice_pb.PingRequest,
    responseType: microservice_microservice_pb.PingReply,
    requestSerialize: serialize_noticias_PingRequest,
    requestDeserialize: deserialize_noticias_PingRequest,
    responseSerialize: serialize_noticias_PingReply,
    responseDeserialize: deserialize_noticias_PingReply,
  },
};

exports.NoticiasClient = grpc.makeGenericClientConstructor(NoticiasService);
