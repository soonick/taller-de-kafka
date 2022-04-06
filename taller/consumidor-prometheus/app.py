from confluent_kafka import Consumer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
from prometheus_client import start_http_server, Counter

print('Iniciando')

# Iniciar un servidor que sera usado por prometheus para obtener las medidas
start_http_server(5777)

# TODO
# - Crea el topic y el consumidor igual que en el ejercicio 2
# - Usa el consumidor para observar eventos igual que en el ejercicio 2
# - Por cada alumno emite un `Counter`:
#   https://github.com/prometheus/client_python#counter
# - Podras observar una grafica de los usuarios observados usando prometheus:
#   http://localhost:9090/
