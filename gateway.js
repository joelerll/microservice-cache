const express = require('express')
const bodyParser = require('body-parser')
const morgan = require('morgan')
const app = express()
const http = require('http')
const escapeStringRegexp = require('escape-string-regexp');
const port = process.env.PORT || 3000
const server = http.createServer(app)
app.set('port', port)
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

var grpc = require('grpc')
var async = require('async');
var messages = require('./microservice/microservice_pb')
var services = require('./microservice/microservice_grpc_pb')
var client = new services.NoticiasClient('localhost:50051', grpc.credentials.createInsecure())

if (process.env.NODE_ENV === 'development') {
  app.use(morgan('tiny'))
}

server.on('error', onError)
server.on('listening', onListening)
server.listen(app.get('port'))

process.on('uncaughtException', err => {
  console.error('Caught exception: ' + err)
  console.error(err.stack)
})

app.use('/api/noticias_top/cache', function(req, res) {
	res.setHeader('Content-Type', 'application/json');
    res.write('[');
	var noticia = new messages.NoticiaRequest();
	noticia.setTiponoticia("mi noticia");
	var call = client.listaTopNoticias(noticia);
	// var writable = getWritableStreamSomehow();
	noticias = []
	contador = 0

	call.on('data', function(noticia) {

		articulo = escapeStringRegexp(noticia.getArticulo().replace(/"/g, "'"))
		titulo = escapeStringRegexp(noticia.getTitulo().replace(/"/g, "'"))
		subtitulo = escapeStringRegexp(noticia.getSubtitulo())
		// .replace(/[|&;$%@"<>()+,]\n/g, "");
		// .replace(/\./g, '\\\\\\.')
		res.write(`{"titulo": ${escapeStringRegexp(JSON.stringify(noticia.getTitulo()))},"id": ${noticia.getId()},"subtitulo": ${escapeStringRegexp(JSON.stringify(noticia.getSubtitulo()))},"articulo": ${escapeStringRegexp(JSON.stringify(noticia.getArticulo()))}}`);
		contador = contador + 1
		if (contador != 10) {
			res.write(`,`);
		}
	})
	call.on('end', function(datos) {
	  res.end(']');
	});
})

function onError (error) {
  if (error.syscall !== 'listen') {
    throw error
  }
  const port = process.env.PORT
  const bind = typeof port === 'string'
    ? `Pipe ${port}`
    : `Port ${port}`
  switch (error.code) {
    case 'EACCES':
      console.error(`${bind} correr en otro puerto, este puerto requiere permisos de root`)
      process.exit(1)
    case 'EADDRINUSE':
      console.error(`${bind} el puerto ya esta en uso client`)
      process.exit(1)
    default:
      throw error
  }
}

function onListening () {
  const addr = server.address()
  const bind = typeof addr === 'string'
    ? `Pipe ${addr}`
    : `Port ${addr.port}`
  if (process.env.NODE_ENV !== 'testing') {
    console.info(`server corriendo en  ${bind}`)
  }
}