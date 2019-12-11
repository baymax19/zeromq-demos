import zmq

context = zmq.Context()

# creating server socket
socket = context.socket(zmq.REP) #server REPLAY
socket.bind("tcp://*:5555") #binding the tcp client; we can use ipc,tipc etc..

while True:
    # getting request from client
    message = socket.recv_string()
    print ("Recived message",message)
    if message == "FromClientOne":
        socket.send_string("ResponseToClientOne")
    if message == "FromClientTwo":
        socket.send_string("ResponseToClientTwo")
    else:
        #send response to client
        socket.send_string("world")