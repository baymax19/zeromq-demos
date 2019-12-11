#python3 pclient.py SBILIFE MINDTREE

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from Stock Server...")
socket.connect("tcp://localhost:5555")

script_filter = sys.argv[1:] if len(sys.argv)>1 else ["INFY"]

for script in script_filter:
    socket.setsockopt_string(zmq.SUBSCRIBE,script)

while True:
    string = socket.recv_string()
    stock,price = string.split()
    print("%s: %s" %(stock,price))

