import zmq
import time

def producer():
    context = zmq.Context()
    socket= context.socket(zmq.PUSH)
    socket.bind("tcp://*:5555")

    for num in range(20000):
        work_message = {'num':num}
        socket.send_json(work_message)

producer()    