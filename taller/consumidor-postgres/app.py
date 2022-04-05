from confluent_kafka import Consumer
import psycopg2

TABLA_ALUMNOS = "alumnos"

con = None

def conectar_a_postgres():
    print('Conectando a postgres')
    global con
    con = psycopg2.connect('host=postgres user=postgres password=mipassword dbname=escuela')

def crear_tabla_de_alumnos():
    print('Creando tabla de alumnos')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS alumnos(nombre TEXT, edad TEXT)')
    con.commit()

print('Iniciando')

conectar_a_postgres()
crear_tabla_de_alumnos()

# TODO
# - Crear topic desde aqui para que no lo tengamos que crear manualmente. Usa create_topics:
#   https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#confluent_kafka.admin.AdminClient.create_topics
#   Si necesitas mas ayuda, puedes ver `/solucion/consumidor-postgres/app.py`
# - La creacion de topics sucede de manera asincrona. Usa `list_topics` para asegurarte
#   que el topic fue creado antes de intentar consumir de el
#   https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#confluent_kafka.admin.AdminClient.list_topics
#   Si necesitas mas ayuda, puedes ver `/solucion/consumidor-postgres/app.py`
# - Crea un consumidor usando las instrucciones en:
#   https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#ak-consumer
# - Usa el consumidor para observar nuevos eventos:
#   https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#basic-poll-loop
# - Guarda cada alumno en la base de datos usando psycopg2:
#   https://www.psycopg.org/docs/usage.html
