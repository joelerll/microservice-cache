# contactar el query de la peticion de la base de datos
# uno que pida con la data cacheada, si no esta pedirla de nuev
# debe retornar las 10 noticias mas vistas
# uno que pida sin la data cacheada
# uno que limpie la base de datos de redis desde una url

# como guardar los datos de redis?
# la clave debe ser un string que represente el dia en que se hizo la consulta y se cachearian las noticias top 10 del dia

import pymysql.cursors
import redis
import csv
import datetime
from concurrent import futures
import time
import json
import grpc

import microservice_pb2
import microservice_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

user = ''
password = ''
db = ''
host = ''
with open('.env', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		user = row['user']
		password = row['password']
		db = row['db']
		host = row['host']

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def ObtenerTopNoticiasMysql():
	try:
		with connection.cursor() as cursor:
			sql = "SELECT `id`, `titulo`, `subtitulo`, `articulo`, `contador` FROM `noticias` ORDER BY `contador`  DESC LIMIT %s"
			cursor.execute(sql, (10,))
			result = cursor.fetchall()
			return result
	finally:
		print('finalizado de leer la base de datos')

def ObtenerFechaHoy():
	fecha = datetime.datetime.now()
	return fecha.strftime('%x')

def BuscarTopNoticiaDiaRedis():
	noticias = r.get(ObtenerFechaHoy())
	return noticias

def GuardarTopNoticiasRedis(topNoticias):
	r.set(ObtenerFechaHoy(), topNoticias)

def LimpiarRedis():
	r.flushall()

def serializarNoticias(topNoticias):
	topNoticiasSerializado = []
	for noticia in topNoticias:
		noticia_tmp = microservice_pb2.NoticiaReply(id=noticia["id"],titulo=noticia["titulo"],subtitulo=noticia["subtitulo"],articulo=noticia["articulo"],contador=noticia["contador"])
		topNoticiasSerializado.append(noticia_tmp)
	return topNoticiasSerializado

class Microservice(microservice_pb2_grpc.NoticiasServicer):
    def ListaTopNoticias(self, request, context):
    	noticias = BuscarTopNoticiaDiaRedis()
    	noticiasSerializado = []
    	if noticias:
    		print('Noticias cargadas REDIS')
    		noticiasSerializado = serializarNoticias(json.loads(noticias.decode()))
    	else:
    		print('Noticias cargadas MYSQL')
    		topNoticias = ObtenerTopNoticiasMysql()
    		noticiasSerializado = serializarNoticias(topNoticias)
    		GuardarTopNoticiasRedis(json.dumps(topNoticias))

    	for noticia in noticiasSerializado:
    		yield noticia

    def ListaTopNoticiasNoCache(self, request, context):
        print('Noticias cargadas MYSQL: Nunca se cachearan')
        topNoticias = ObtenerTopNoticiasMysql()
        noticiasSerializado = serializarNoticias(topNoticias)
        for noticia in noticiasSerializado:
            yield noticia


    def Ping(self, request, context):
        return microservice_pb2.PingReply(message="Mi mensaje de prueba")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    microservice_pb2_grpc.add_NoticiasServicer_to_server(Microservice(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


# TODO: Setear un l  EXPIRE resource:lock 120 (TTL resource:lock) a redis para las noticias

if __name__ == '__main__':
	serve()