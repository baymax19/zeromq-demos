import time
import zmq
import pprint

def sink():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://localhost:5556")
    data = {}

    for x in xrange(1000):
        result = socket.recv_json()
        if data.has_key(result['consumer']):
            data[result['consumer']]= data[result['consumer']]+1
        else:
            data[result['consumer']] =1
        if x==999:
            pprint.pprint(data)

sink()