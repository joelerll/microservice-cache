var grpc = require('grpc')
var async = require('async');
var messages = require('./microservice_pb')
var services = require('./microservice_grpc_pb')
var client = new services.NoticiasClient('localhost:50051', grpc.credentials.createInsecure())

function runListaTopNoticias(callback) {
  // var next = _.after(2, callback);
  var noticia = new messages.NoticiaRequest();
  noticia.setTiponoticia("mi noticia");
  var call = client.listaTopNoticias(noticia);
  noticias = []
  call.on('data', function(noticia) {
    noticias.push(noticia.getTitulo())
    console.log(noticias)
  })
  call.on('end', callback);
}

function main() {
  runListaTopNoticias(function(noti) {
    console.log('fina')
  })
}

if (require.main === module) {
  main();
}
