from confluent_kafka import Consumer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
import time
import psycopg2
import json

TOPIC_ALUMNOS = "alumnos"
TABLA_ALUMNOS = "alumnos"
GRUPO = "consumidores_postgres"
KAFKA = "kafka:9092"

consumidor = None
con = None

def crear_consumidor_de_kafka():
    print('Creando consumidor de kafka')

    global consumidor
    conf = {
        'bootstrap.servers': KAFKA,
        'group.id': GRUPO
    }
    consumidor = Consumer(conf)

    print('Consumidor de kafka creado')

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

def conectar_a_postgres():
    print('Conectando a postgres')
    global con
    con = psycopg2.connect('host=postgres user=postgres password=mipassword dbname=escuela')

def crear_tabla_de_alumnos():
    print('Creando tabla de alumnos')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS alumnos(nombre TEXT, edad TEXT)')
    con.commit()

def procesar_mensaje(mensaje):
    print(f'Guardando mensaje {mensaje.value()} en postgres')

    mensaje_json = json.loads(mensaje.value())

    cursor = con.cursor()
    cursor.execute(
        'INSERT INTO alumnos(nombre, edad) values(%s, %s)',
        (mensaje_json['nombre'], mensaje_json['edad'])
    )
    con.commit()

def consumir():
    try:
        consumidor.subscribe([TOPIC_ALUMNOS])

        while True:
            print(f'Obteniendo nuevos mensajes')
            mensaje = consumidor.poll(timeout=10.0)
            if mensaje is None:
                continue

            if mensaje.error():
                raise KafkaException(mensaje.error())
            else:
                procesar_mensaje(mensaje)
    finally:
        consumidor.close()

print('Iniciando')
crear_topic()
crear_consumidor_de_kafka()
conectar_a_postgres()
crear_tabla_de_alumnos()
consumir()
