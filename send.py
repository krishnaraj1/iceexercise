#!/usr/bin/env python
import pika
import os
import logging
import sys
logging.basicConfig(filename='logs.log', level=logging.INFO, format="%(asctime)s:%(levelname)s: %(message)s")
logging.getLogger().addHandler(logging.StreamHandler())


rabbit_pass =os.environ['RABBITMQ_PASSWORD']
credentials = pika.PlainCredentials('user', rabbit_pass)
connection = pika.BlockingConnection(pika.ConnectionParameters('icerabbitmq',5672,'/',credentials))


channel = connection.channel()

channel.queue_declare(queue='iceone')

channel.basic_publish(exchange='',
                      routing_key='iceone',
                      body='Hello World!')


logging.info(" [x] Sent 'Hello World!'")

def callback(ch, method, properties, body):
  logging.info(" [x] Received %r" % body)

channel.basic_consume(queue='iceone', on_message_callback=callback, auto_ack=True)
logging.info(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()