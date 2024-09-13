from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.tls.record import TLS
from scapy.layers.http import HTTPRequest
from datetime import datetime
import csv
import os


iPkt = 0

def process_pkt(pkt):
    global iPkt
    with open('packets.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        iPkt += 1
        writer.writerow(['Data', 'IP Sorgente', 'IP Destinazione', 'Porta Sorgente', 'Porta Destinazione','Host'])
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
        #tcp = pkt[TCP].show()
        if pkt.haslayer(HTTPRequest):
            host = pkt[HTTPRequest].Host
            #host = pkt[HTTPRequest].Host.decode() 
        else:
            host = "Unkonwn"
        print(f"Ho ricevuto un pacchetto {iPkt} IP: {pkt[IP]} da {ip_src} a {ip_dst} (sport: {sport}, dport: {dport},Host {host}")
        writer.writerow([data, ip_src, ip_dst, sport, dport, host])
