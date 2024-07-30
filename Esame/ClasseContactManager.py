#QUESTION4

"""
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di creare, 
modificare, e cercare contatti basati sui numeri di telefono. 
Il sistema dovrà essere capace di gestire una collezione
 (dizionario) di contatti e i loro numeri di telefono.

1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.
 
Attributi:

    contacts: dict[str, list[str]] - Dizionario 
    che ha per chiave il nome del contatto e per valore 
    una lista di numeri di telefono.
      I numeri di telefono sono espressi sottoforma di stringa."""

class ContactManager:
    def __init__(self) -> None:

        self.contacts: dict[str, list[str]]= {}

        

    def create_contact(self,name: str, phone_numbers: list[str]) -> dict: 
        """Crea un nuovo contatto, aggiungendolo al dizionario contacts 
        con il nome specificato e una lista di numeri di telefono. 
        Restituisce un nuovo dizionario con il solo contatto
        appena creato o il messaggio di errore "Errore: il
        contatto esiste già." se il contatto esiste già."""

        if name not in self.contacts:
            self.contacts[name]=phone_numbers
            return self.contacts
        else:
            raise ValueError (f'Errore: il contatto esiste già')

    def add_phone_number(self,contact_name: str, phone_number: str):
        """Aggiunge un numero di telefono al contatto specificato. 
        Restituisce un nuovo dizionario con il solo contatto aggiornato
        o i messaggi di errore "Errore: il contatto non esiste." 
        se il contatto non esiste oppure "Errore: il numero di telefono esiste già." 
        se il numero di telefono è già presente per il contatto specificato."""

        for key, value in self.contacts.items():
            if contact_name in self.contacts and phone_number not in self.contacts[key]:    
                self.contacts[contact_name] += phone_number
                return self.contacts
            else: 
                raise ValueError (f'Errore: il numero di telefono esiste già.')


    def remove_phone_number(contact_name: str, phone_number: str): 
        
        """Rimuove un numero di telefono dal contatto specificato.
          Restituisce un nuovo dizionario con il solo contatto aggiornato
            o i messaggi di errore "Errore: il contatto non esiste.
            " se il contatto non esiste oppure "Errore:
              il numero di telefono non è presente." 
              se il numero di telefono non esiste per il contatto specificato."""
    def update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): 
        """Sostituisce un numero di telefono con un altro nel contatto specificato.
          Restituisce un nuovo dizionario con il solo contatto aggiornato
            o i messaggi di errore "Errore: il contatto non esiste." 
            se il contatto non esiste oppure "Errore: il numero di telefono 
            non è presente." se il numero di telefono non esiste per il contatto specificato."""
    def list_contacts():
        pass     
    """ Ritorna una lista di tutte le chiavi all'interno del dizionario contacts."""

    def list_phone_numbers(contact_name: str):
        """ Mostra i numeri di telefono di un contatto specifico.
          Restituisce la lista dei numeri di telefono o 
          il messaggio di errore "Errore: il contatto non esiste." se il contatto non esiste."""
    def search_contact_by_phone_number(phone_number: str): 
        
        """Trova e restituisce tutti i contatti che contengono
          un determinato numero di telefono. 
          Restituisce una lista di tutte le chiavi 
          all'interno del dizionario contacts che hanno 
          il numero specificato tra i valori oppure 
          il messaggio di errore "Nessun contatto 
          trovato con questo numero di telefono.
          " se nessun contatto contiene il numero di telefono."""




# Creazione di un nuovo gestore di contatti
manager = ContactManager()

# Creazione di nuovi contatti
print(manager.create_contact("Alice", ["123456789"]))
print(manager.create_contact("Bob", ["987654321"]))
print(manager.create_contact("Alice", ["111222333"]))


# Aggiunta di numeri di telefono
print(manager.add_phone_number("Alice", "111222333"))
print(manager.add_phone_number("Charlie", "444555666"))
print(manager.add_phone_number("Alice", "123456789"))
