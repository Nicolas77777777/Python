import random

# Scrivi una funzione che prenda un dizionario e un valore, 
# e ritorni la prima chiave che corrisponde a quel valore, 
# o None se il valore non è presente.

def cerca_valore_diz (diz: dict, valore):

        for key, value in diz.items():
            if value == valore:
                print (key)
                return key 
        else:
                print(None)
        

dit: dict = {"a":1,"b":2}

cerca_valore_diz(dit,2)
    
# 2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario.
# Se ci sono valori duplicati, scarta i duplicati.

def inverte_valori_dizionario( diz: dict ):
    diz_inverso: dict = {}

    for key, value in diz.items():
            diz_inverso[value]= key

            return diz_inverso
    
print (f'{inverte_valori_dizionario(dit)}\n')
      
     
# Scrivi una funzione che riceve una lista di numeri,
#  filtra i numeri pari, e restituisce una nuova 
#  lista con i numeri pari moltiplicati per un fattore dato

def lista_numeri_pari_per_fattore (l1: list[int], fattore: int):
    l2=[]
    l3= []
    for elemento in l1 : 
        if elemento % 2 == 0:
            l2.append(elemento)

            for i in l2:
                f= i* fattore
                l3.append(f)
    
    return l2,l3
          
l1 = []
for i in range(10):
    l1.append(random.randint(1, 100))

l5= [7,3,4,5,6,8,10]


print(lista_numeri_pari_per_fattore(l5,2))

 
"""4. Scrivi una funzione che determina se un numero è 'magico'. Un numero è considerato magico se è divisibile per 4 ma non per 6.
 
5. Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
 
6. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
 
7. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
 
8. Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
 
9. Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
 
10. Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
 
11. Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro. Utilizza il concetto di parametri opzionali.
 
12. Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
 
13. Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
 
14. Scrivi una funzione che ritorna un dizionario che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario.
 
15. Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
 
16. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
 
17. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
 
18. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
 
19. Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
 
20. Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
 
21. Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
 
22. Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
 
23. Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
 
24.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
 
25. Scrivi una funzione che conta quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato da elementi uguali.
 
26. Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}
Last modified: Tuesday, 14 May 2024, 4:31 PM"""