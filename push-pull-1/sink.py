#Collect data from the workers
#python3 sink.py
import zmq


context =zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5556")

while True:
    s = socket.recv()
    print(s)