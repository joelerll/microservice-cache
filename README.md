# Proyecto Segundo Parcial Sistemas Distribuidos

# Instalación

Ubuntu 16.04

```
> sudo make install
```

```
> make
```

# Tareas

|  Tarea | Joel  | Julio  |   |
|---|---|---|---|
| script instalacion dependecias o docker (Makefile) |   |   |   |
| almacenar noticias en base de datos (dataset), con contadores de acceso (Mysql) [D1](https://archive.ics.uci.edu/ml/datasets/News+Aggregator) [D2](http://mlg.ucd.ie/datasets/bbc.html)  |   |   |   |
| html front web |   |   |   |
| almacenamiento en cache de noticias (redis, Memcached) (facil cambio de cache a sin cache) |   |   |   |
| Reverse Proxy/ Api gateway (Nginx, nodejs)  |   |   |   |
| RPC (Apache Thrift o gRPC+protobuf)  |   |   |   |
| Setup AWS  |   |   |   |
| bot generador de peticiones y guardar datos en archivo (latencia, througthput) o herramienta de benchmarking |   |   |   |
| generador de graficas boxplot  |   |   |   |


# Documento

* Documentar problema
	* Manejo de errores
	* Estructuras de datos usados
	* Librerías o middlewares utilizados
	* Mecanismos de sincronización usados
	* Cómo realizaron las pruebas de rendimiento
	* Qué nube usaron
	* Otras cosas importantes
* solucion propuesta 
* Decisiones de diseno
* experimentos de latencia
* experimentos througthput
* rendimiento con cache y sin cache
* realizar al menos 10 pruebas
* graficas box plot

# Links
https://blog.risingstack.com/building-an-api-gateway-using-nodejs/
http://2.bp.blogspot.com/-EbXflUYFwYM/T6p54bpMNXI/AAAAAAAABCk/cMlR7Cqki_k/s1600/Finagle+Diagram.png
https://github.com/grpc-ecosystem/grpc-gateway
https://www.cloudfoundry.org/scaling-real-time-apps-on-cloud-foundry-using-node-js-and-rabbitmq/