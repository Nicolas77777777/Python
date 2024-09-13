import csv

# Inizializza il contatore di pacchetti
iPkt = 0

def process_packet(packet):
    global iPkt
    iPkt += 1
    
    # Estrai informazioni dal pacchetto (ad esempio, l'indirizzo sorgente e destinazione)
    src_ip = packet[0].src
    dst_ip = packet[0].dst
    protocol = packet[0].proto
    
    # Crea o apri il file CSV in modalità append
    with open('pacchetti_sniffati.csv', mode='a', newline='') as file_csv:
        writer = csv.writer(file_csv)
        
        # Se è il primo pacchetto, scrivi l'intestazione
        if iPkt == 1:
            writer.writerow(['Numero Pacchetto', 'Indirizzo Sorgente', 'Indirizzo Destinazione', 'Protocollo'])
        
        # Scrivi i dettagli del pacchetto nel file CSV
        writer.writerow([iPkt, src_ip, dst_ip, protocol])
    
    # Stampa il contenuto su output
    print(f"Letto PKT {iPkt}: Sorgente={src_ip}, Destinazione={dst_ip}, Protocollo={protocol}")
