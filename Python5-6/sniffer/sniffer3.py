from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.tls.record import TLS
from scapy.layers.http import HTTPRequest
from datetime import datetime
import csv
import os

def get_tls_sni(pkt):
    try:
        return pkt[TLS].msg[0].ext[0].servernames[0].servername.decode()
    except (IndexError, AttributeError):
        return ""


def process_pkt(pkt):
    if IP in pkt and TCP in pkt:
        if pkt[TCP].dport in [80, 443] or pkt[TCP].sport in [80, 443]: