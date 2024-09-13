from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.tls.record import TLS    #######
from scapy.layers.http import HTTPRequest
from datetime import datetime
import csv
import os

def get_tls_sni(pkt):    #NUOVA FUNZIONE TO GET THE TLS
    try:
        return pkt[TLS].msg[0].ext[0].servernames[0].servername.decode()
    except (IndexError, AttributeError):
        return ""


def process_pkt(pkt):
    if IP in pkt and TCP in pkt:
        if pkt[TCP].dport in [80, 443] or pkt[TCP].sport in [80, 443]:

            #Atributi info csv
            data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip_src = pkt[IP].src
            ip_dst = pkt[IP].dst
            tcp_src = pkt[TCP].sport
            tcp_dst = pkt[TCP].dport

            #Verifica l'host in caso di protocollo HTTP, altrimenti " "
            host = ""
            if HTTPRequest in pkt:
                if pkt[HTTPRequest].Host:
                    host = pkt[HTTPRequest].Host.decode()
            elif TLS in pkt:
                host = get_tls_sni(pkt)


            if 443 in [tcp_src, tcp_dst]:
                protocol = "HTTPS" 
            else:
                protocol = "HTTP"


                                                                    #(se il file già esiste integra i nuovi info)
            with open('connessioni.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if host != '':
                    writer.writerow([data_ora, ip_src, ip_dst, tcp_src, tcp_dst, host, protocol])

#Crea il file CSV con l'intestazione
with open('connessioni.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["data-ora", "ip_src", "ip_dst", "tcp_src", "tcp_dst", "host", "protocol"])

#Avvia lo sniffing
sniff(filter="tcp and (port 80 or port 443)", prn=process_pkt)
