from __future__ import print_function

import grpc

import microservice_pb2
import microservice_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = microservice_pb2_grpc.NoticiasStub(channel)
    # response = stub.Ping(microservice_pb2.PingRequest(message='you'))
    noticias = stub.ListaTopNoticias(microservice_pb2.NoticiaRequest(tipoNoticia='you'))
    for noticia in noticias:
    	print(noticia)

if __name__ == '__main__':
    run()
