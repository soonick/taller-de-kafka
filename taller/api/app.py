from flask import Flask, request
from flask_cors import CORS
from confluent_kafka import Producer

app = Flask(__name__)
CORS(app)

@app.route('/alumno', methods=['POST'])
def agregar_alumno():
    # TODO
    # - Crea un Producer usando las instrucciones en:
    #   https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#ak-producer
    # - Una vez que tenemos el productor, podemos usarlo para generar mensajes:
    #   https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#asynchronous-writes
    #   (Pista: No necesitamos usar `key` y podemos usar cualquier string como `topic`)
    # - Crea el topic en kafka con el siguiente comando:
    #   docker exec -it kafka /bin/kafka-topics --create --topic <nombre-del-topic> --bootstrap-server localhost:9092A
    # - Crea unos alumnos desde `http://localhost:8080/`
    # - Verifica que los eventos hayan sido creados correctamente usando el comando:
    #   docker exec -it kafka /bin/kafka-console-consumer --topic <nombre-del-topic> --from-beginning --bootstrap-server localhost:9092

    return ('', 204)
