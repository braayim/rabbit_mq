import pika
import time
"""
Simple message receiver
"""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# We are declaring first_kit just to make sure it's there
channel.queue_declare(queue='first_kit')


def cb(ch, method, properties, body):
    print("[x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print("[x] Done")


channel.basic_consume(cb,
                      queue='first_kit',
                      no_ack=True)

print("{*} Waiting for message, to exit press ^C")
channel.start_consuming()

