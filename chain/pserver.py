import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:26657")

while True:
    msg = socket.recv()
    print(msg)
