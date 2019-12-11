import zmq

context = zmq.Context()

#creating client socket 
socket = context.socket(zmq.REQ) #client REQUEST
socket.connect("tcp://localhost:5555") #connecting to server

for req_no in range(10):
    socket.send(b"hello")
    
    message= socket.recv()
    print("Recived message",message)