# work will get form the ventilator
#python3 worker.py
#python3 worker.py
import json
import zmq

import requests
from lxml import etree

def get_title(url):
    r = requests.get(url)
    tree = etree.HTML(r.content)
    tittle = tree.xpath('//div[@id="comic"]/img/@title')
    if tittle:
        return tittle[0]
    else:
        return None

context = zmq.Context()
reciver = context.socket(zmq.PULL)
reciver.connect("tcp://localhost:5555")

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5556")

while True:
    s = reciver.recv_string()
    tittle = get_title(s)

    print(s, tittle)
    sender.send_string(json.dumps({'url':s,'tittle':tittle}))