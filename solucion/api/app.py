from flask import Flask, request
from flask_cors import CORS
from confluent_kafka import Producer
import socket
import json

app = Flask(__name__)
CORS(app)

TOPIC_ALUMNOS = "alumnos"
KAFKA = "kafka:9092"

productor = None

@app.route('/alumno', methods=['POST'])
def agregar_alumno():
    producir(json.dumps(request.json))

    return ('', 204)

def producir(message):
    app.logger.info(f'Escribiendo mensaje: "{message}" al topic: {TOPIC_ALUMNOS}')
    productor.produce(TOPIC_ALUMNOS, value=message)
    productor.flush()

def crear_productor_de_kafka():
    global productor
    conf = {
        'bootstrap.servers': KAFKA,
        'client.id': socket.gethostname()
    }
    productor = Producer(conf)
    app.logger.info('Productor de kafka creado')

crear_productor_de_kafka()
