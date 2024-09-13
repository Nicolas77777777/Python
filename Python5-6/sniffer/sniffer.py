from scapy.all import *
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse
import csv
from datetime import datetime


iPkt = 0
load_layer('tls')

def process_packet(packet):
	global iPkt

	iPkt += 1
	print("Letto PKT " + str(iPkt))

	
	
sniff(iface="eth0",filter="tcp", prn=process_packet)
