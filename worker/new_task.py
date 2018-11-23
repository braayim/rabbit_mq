import pika
import sys
"""
Simple message producer
"""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='first_kit')

message = ' '.join(sys.argv[1:] or "I wish you well")
channel.basic_publish(exchange='',
                      routing_key='first_kit',
                      body=message)

print("[x] Sent %r" % message)
connection.close()
