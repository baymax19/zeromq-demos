import sys
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    socket.send_string(sys.argv[2])
    
    message = socket.recv_string()
    print("Recived replay",message)
    time.sleep(float(sys.argv[1]))