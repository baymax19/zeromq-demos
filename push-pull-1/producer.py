# distribute work to multiple workers
# start this service after init the no of workers
#python3 producer.py 10
import zmq
import sys

context = zmq.Context()

sender= context.socket(zmq.PUSH)
sender.bind("tcp://*:5555")

print("Enter the when workers are ready")
_ = input()

print("Sending data to workers")
base_url = "https://xkcd.com/"
urls = [base_url+str(i) for i in range(1, int(sys.argv[1]))]

for url in urls:
    sender.send_string(url)