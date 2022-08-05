import pika
import sys


from util import get_logger

log = get_logger(__name__)

class producer:
    def __init__(self,tag):

        self._rockwellTag = tag



    def addEvent(self,IP,tagValue):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self._rockwellTag, durable=True)
        print(self._rockwellTag)

        message ="{" + f'"IP":"{IP}","Value":{tagValue}' + "}"
        channel.basic_publish(exchange='', routing_key=self._rockwellTag, body=message,properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        print(" [x] Sent %r" % message)
        connection.close()
       
