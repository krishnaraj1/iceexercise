#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('icerabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='iceone')

channel.basic_publish(exchange='',
                      routing_key='iceone',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()

