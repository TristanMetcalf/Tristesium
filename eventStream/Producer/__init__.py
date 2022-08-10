from math import prod
import configparser
import datetime
import re
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError



from util import get_logger

log = get_logger(__name__)

config = configparser.ConfigParser()
config.read("config.ini")
kafka_server = config.get("Kafka","server").split()

class producer:
    def __init__(self,tag):
        self._config.read("config.ini")

        self._rockwellTag = tag



    def addEvent(self,IP,tagValue):
        print(tagValue)
        producer = KafkaProducer(bootstrap_servers=kafka_server)
        producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
        producer.send(re.sub(r'\W+', '', self._rockwellTag), {'timestamp':str(datetime.datetime.now()),'PLCIP':str(IP),'tagValue':str(tagValue)})
    
        producer.flush()

   

        
       
