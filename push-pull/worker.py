import zmq
import time
import random
import json


def consumer():
    cosumer_id = random.randrange(1,100005)
    print("Consumer %d" %cosumer_id)
    context = zmq.Context()
    reciver = context.socket(zmq.PULL)
    reciver.connect("tcp://localhost:5555")

    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5556")

    while True:
        work = reciver.recv_json()
        data = work['num']
        result = {'consumer':consumer,'num':data}
        print('consumer',result)
        if data%2 ==0:
            sender.send_json(result)

consumer()