# Taller de Kafka

En este repo, aprendemos como producir y consumir mensajes de Kafka para alimentar otros sistemas.

## Requerimientos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker compose](https://docs.docker.com/compose/)

## Taller

### Iniciando servicios

Corre el taller en docker:

```
cd taller
make start
```

Este comando iniciara varios servicios:

- `web` - Un servidor web que carga un pequeño formulario en [http://localhost:8080/](http://localhost:8080/)
- `api` - Un servidor con un endpoint que sera usado para crear alumnos. Este servidor corre en [http://localhost:5000/](http://localhost:5000/)
- `zookeper` - Base de datos usada por Kafka
- `kafka` - Nuestro cluster de kafka corriendo en [http://kafka:9092](http://kafka:9092) (Solo accesible desde otros servicios)
- `postgres` - Base de datos donde guardaremos informacion de alumnos
- `consumidor-postgres` - Programa que consume eventos de `kafka` y agrega registros en postgres


### Ejercicio 1 - Producir eventos

Nuestro servidor web, envia una peticion a `http://localhost:5000/alumno`, pero nos falta implementar el codigo que producira un evento a Kafka

Abre `/taller/api/app.py` y sigue las instrucciones en los comentarios.

### Ejercicio 2 - Consumir eventos

Abre `/taller/consumidor-postgres/app.py` y sigue las instrucciones en los comentarios.

### Ejercicio 3 - Prometheus

Abre `/taller/consumidor-prometheus/app.py` y sigue las instrucciones en los comentarios.
