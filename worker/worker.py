import pika
import time
"""
Simple message receiver
"""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# durable=True ensures that rabbitmq server will never loose our queue
channel.queue_declare(queue='task_queue', durable=True)


def cb(ch, method, properties, body):
    print("[x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print("[x] Done")
    # if a worker dies all unacknowledged messages will be redelivered
    ch.basic_ack(delivery_tag=method.delivery_tag)


# don't give more than 1 message to a worker at a time until it returns ack_tag
channel.basic_qos(prefetch_count=1)

channel.basic_consume(cb, queue='task_queue')

print("{*} Waiting for message, to exit press ^C")
channel.start_consuming()

