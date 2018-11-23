import pika
import sys
"""
Simple message producer
"""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# durable=True ensures that rabbitmq server will never loose our queue
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:] or "I wish you well")
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode=2,  # makes message persistent
                      ))

print("[x] Sent %r" % message)
connection.close()
