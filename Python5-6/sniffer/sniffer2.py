from scapy.all import *
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse
import csv
from datetime import datetime

iPkt=0
def process_pkt(pkt):
    global iPkt
    with open('packets.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        iPkt += 1
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([data, "Ricevuto pkt",])


sniff(iface="eth0",filter="tcp", prn=process_pkt)
