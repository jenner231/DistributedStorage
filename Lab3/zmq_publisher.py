# Weather update server
# Binds PUB socket to tcp://*:5556
# Publishes random weather updates
import weatherupdate_message_pb2
import zmq
from random import randrange
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://localhost:5556")
while True:
    pb_file = weatherupdate_message_pb2.file()
    pb_file.zipcode = randrange(1, 100000)
    pb_file.temperature = randrange(-80, 135)
    pb_file.relhumidity = randrange(10, 60)
    # Serialize the file message to a string,
    # which can be transported over any protocol
    encoded_pb_file = pb_file.SerializeToString()
    socket.send(encoded_pb_file)