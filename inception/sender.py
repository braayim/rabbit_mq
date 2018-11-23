import pika
"""
Simple message producer
"""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='first_kit')

channel.basic_publish(exchange='',
                      routing_key='first_kit',
                      body='First message! Wishing you well')

print("[x] Sent 'First message'")
connection.close()
