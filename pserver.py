#python3 pserver.py

import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB) # change the pattern server
socket.bind("tcp://*:5555")

scritps = ["INFY","SBILIFE","CASTROL","MINDTREE","PETRONETLNG"]

while True:
    script = random.choice(scritps)
    price= random.randrange(200,900)
    
    msg = "%s: %d" %(script,price)
    print(msg)
    socket.send_string(msg)
    time.sleep(0.5)

