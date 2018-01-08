# Proyecto Segundo Parcial Sistemas Distribuidos

# Dependencias

* Ubuntu 16.04
* Mysql 5.7
* Redis 4.0.6


# Instalación

Ubuntu 16.04

```
> sudo make install
```

```
> make
```

# Instalación development

Ubuntu 16.04

1. Instalar todas las dependencias

```sh
> ./scripts/install_development
```

2. Instalar virtualenv en la carpeta del proyecto

```sh
> virtualenv -p python3 .python
```

3. Usar virtualenv

```sh
> source .python/bin/activate
```

4. Instalar las dependencias de python 

```sh
>  pip install < requirements.txt 
```

5. Editar el archivo .env con los datos que se piden

```txt
host,user,password,db
localhost,usuario_base_datos,clave_base_datos,distribuidos
```

5. Crear la base de datos (pedira el password de la base de datos esta accion)

```sh
> mysql -u root -p < scripts/create_database.sql
```

6. Llenar la base de datos con las noticias

```sh
> python scripts/create_database.py
```

7. Correr redis

```sh
> ./redis-server --daemonize yes
```

# Development

__Actualizar las depencias de python__

```sh
> pip freeze > requirements.txt 
```

# Tareas

|  Tarea | Joel  | Julio  |   |
|---|---|---|---|
| script instalacion dependecias o docker (Makefile) |   |   |   |
| almacenar noticias en base de datos (dataset), con contadores de acceso (Mysql) [D1](https://archive.ics.uci.edu/ml/datasets/News+Aggregator) [D2](http://mlg.ucd.ie/datasets/bbc.html)  | x |   |   |
| html front web |   |   |   |
| almacenamiento en cache de noticias redis |  x |   |   |
| microservicio enpoint sin cache, limpiado de cache, limit time redis noticias |  |   |   |
| Reverse Proxy/ Api gateway (Nginx, nodejs)  |   |   |   |
| gRPC+protobuf  | x |   |   |
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

https://codeburst.io/build-a-nodejs-cinema-api-gateway-and-deploying-it-to-docker-part-4-703c2b0dd269

