# This example show connecting to multiple publisher
#python3 pserver1.py 5555
#python3 pserver1.py 5556
import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PUB) # change the pattern server
port = "5555"
if len(sys.argv)>1:
    port = sys.argv[1]
    int(port)

socket.bind("tcp://*:%s"%port)

scritps = ["INFY","SBILIFE","CASTROL","MINDTREE","PETRONETLNG"]

while True:
    script = random.choice(scritps)
    price= random.randrange(200,900)
    
    msg = "%s: %d" %(script,price)
    print(msg)
    socket.send_string(msg)
    time.sleep(0.5)

