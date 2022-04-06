from confluent_kafka import Consumer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
from prometheus_client import start_http_server, Counter
import json
import time

TOPIC_ALUMNOS = "alumnos"
TABLA_ALUMNOS = "alumnos"
GRUPO = "consumidores_prometheus"
KAFKA = "kafka:9092"
NUM_ALUMNOS_CREADOS = Counter('num_alumnos_creados', 'Numero de alumnos creados')

consumidor = None

def crear_topic():
    print(f'Creando topic {TOPIC_ALUMNOS}')
    admin_client = AdminClient({
        "bootstrap.servers": KAFKA
    })

    topic_list = []
    topic_list.append(NewTopic(TOPIC_ALUMNOS, 1, 1))
    admin_client.create_topics(topic_list)

    # Esperamos a que el topic sea creado
    while True:
        cluster_metadata = admin_client.list_topics()
        if TOPIC_ALUMNOS in cluster_metadata.topics.keys():
            print(f'Topic {TOPIC_ALUMNOS} fue creado')
            break

        print(f'Topic {TOPIC_ALUMNOS} aun no esta listo')
        time.sleep(2)

def crear_consumidor_de_kafka():
    print('Creando consumidor de kafka')

    global consumidor
    conf = {
        'bootstrap.servers': KAFKA,
        'group.id': GRUPO
    }
    consumidor = Consumer(conf)

    print('Consumidor de kafka creado')

def procesar_mensaje(mensaje):
    print(f'Guardando mensaje {mensaje.value()} en postgres')

    mensaje_json = json.loads(mensaje.value())
    print(f'1 alumno creado')
    NUM_ALUMNOS_CREADOS.inc()

def consumir():
    try:
        consumidor.subscribe([TOPIC_ALUMNOS])

        while True:
            print(f'Obteniendo nuevos mensajes')
            mensaje = consumidor.poll(timeout=10.0)
            if mensaje is None:
                print(f'0 alumnos creados')
                continue

            if mensaje.error():
                raise KafkaException(mensaje.error())
            else:
                procesar_mensaje(mensaje)
    finally:
        consumidor.close()

print('Iniciando')

# Iniciar un servidor que sera usado por prometheus para obtener las medidas
start_http_server(5777)

crear_topic()
crear_consumidor_de_kafka()
consumir()
