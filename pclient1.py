#This Example show connect to multiple publishers
#python3 pclient1.py 5555 5556 MINDTREE 
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from Stock Server...")

port = "5555"
if len(sys.argv) > 1 :
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 1 :
    port1 = sys.argv[2]
    int(port1)

socket.connect("tcp://localhost:%s"% port)

if len(sys.argv)>2:
    socket.connect("tcp://localhost:%s"%port1)

script_filter = sys.argv[3:] if len(sys.argv)>1 else ["INFY"]

for script in script_filter:
    socket.setsockopt_string(zmq.SUBSCRIBE,script)

while True:
    # socket.setsockopt_string(zmq.SUBSCRIBE,"MINDTREE")
    string = socket.recv_string()
    stock,price = string.split()
    print("%s: %s" %(stock,price))

