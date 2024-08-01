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
            self.contacts[name] = phone_numbers
            return {name:phone_numbers}
            
        else:
            return f'Errore: il contatto esiste già'

    def add_phone_number(self,contact_name: str, phone_number: str)-> dict:
        """Aggiunge un numero di telefono al contatto specificato. 
        Restituisce un nuovo dizionario con il solo contatto aggiornato
        o i messaggi di errore "Errore: il contatto non esiste." 
        se il contatto non esiste oppure "Errore: il numero di telefono esiste già." 
        se il numero di telefono è già presente per il contatto specificato."""

        for key, value in self.contacts.items():
            if contact_name in self.contacts and phone_number not in self.contacts[contact_name]:    
                self.contacts[contact_name].append(phone_number)
                return {key:value}
            
            elif contact_name in self.contacts and phone_number in self.contacts[contact_name]:
                return f'Errore: il numero di telefono esiste già.'
            
            elif contact_name  not in self.contacts:
                return f'Errore: il contatto non esiste.'
                

    def remove_phone_number(self,contact_name: str, phone_number: str)-> dict: 
        """Rimuove un numero di telefono dal contatto specificato.
          Restituisce un nuovo dizionario con il solo contatto aggiornato
            o i messaggi di errore "Errore: il contatto non esiste.
            " se il contatto non esiste oppure "Errore:
              il numero di telefono non è presente." 
              se il numero di telefono non esiste per il contatto specificato."""
        
        for key, value in self.contacts.items():
            if contact_name in self.contacts and phone_number in self.contacts[contact_name] :    
                self.contacts[contact_name].remove(phone_number)
                return {key:value}
            
            elif contact_name in self.contacts and phone_number  not in self.contacts[contact_name]:
                return f'Errore: il numero di telefono non è presente.'
            
            elif contact_name  not in self.contacts:
                return f'Errore: il contatto non esiste.'
        
    def update_phone_number(self,contact_name: str, old_phone_number: str, new_phone_number: str) -> dict: 
        """Sostituisce un numero di telefono con un altro nel contatto specificato.
          Restituisce un nuovo dizionario con il solo contatto aggiornato
            o i messaggi di errore "Errore: il contatto non esiste." 
            se il contatto non esiste oppure "Errore: il numero di telefono 
            non è presente." se il numero di telefono non esiste per il contatto specificato."""
        
        for value in self.contacts[contact_name]:
            if value == old_phone_number:
                self.remove_phone_number(contact_name,old_phone_number)
                self.add_phone_number(contact_name, new_phone_number)
                return {contact_name: self.contacts[contact_name]}
            else:
                return f'"Errore: il numero di telefono non è presente."'

        
    def list_contacts(self):
        return list(self.contacts.keys())
    """ Ritorna una lista di tutte le chiavi all'interno del dizionario contacts."""

    def list_phone_numbers(self,contact_name: str):
        """ Mostra i numeri di telefono di un contatto specifico.
          Restituisce la lista dei numeri di telefono o 
          il messaggio di errore "Errore: il contatto non esiste." se il contatto non esiste."""
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return f'Errore: il contatto non esiste.'
        
        
    def search_contact_by_phone_number(self,phone_number: str): 

        """Trova e restituisce tutti i contatti che contengono
          un determinato numero di telefono. 
          Restituisce una lista di tutte le chiavi 
          all'interno del dizionario contacts che hanno 
          il numero specificato tra i valori oppure 
          il messaggio di errore "nNessun contatto 
          trovato con questo numero di telefoo.
          " se nessun contatto contiene il numero di telefono."""
        
        for key, value in self.contacts.items():
            #print (key)
            if phone_number in value:
               for i in value:
                   return list(self.contacts.keys())
            else: 
                return f'"Nessun contatto trovato con questo numero di telefono'

# Creazione di un nuovo gestore di contatti
manager = ContactManager()

# Creazione di nuovi contatti
print(manager.create_contact("Alice", ["123456789"])) # {'Alice': ['123456789']}
print(manager.create_contact("Bob", ["987654321"]))
print(manager.create_contact("Alice", ["111222333"]))
print(manager.create_contact("Franco", ["11122244","123456789"]))



# Aggiunta di numeri di telefono
print(manager.add_phone_number("Alice", "111222333")) 
print(manager.add_phone_number("Charlie", "444555666"))
print(manager.add_phone_number("Alice", "123456789"))
print(manager.add_phone_number("Alice", "123456"))



# Rimozione di numeri di telefono
print(manager.remove_phone_number("Alice", "111222333"))
print(manager.remove_phone_number("Charlie", "444555666"))
print(manager.remove_phone_number("Alice", "999999999"))

# Update numeri di telefono 
print(manager.update_phone_number('Alice','123456789','123'))
print(manager.update_phone_number('Alice','123456789','3333445'))
print(manager.update_phone_number('Alice','1','3333445'))

# list 
print(manager.list_contacts())

# Mostra i numeri di telefono di un contatto specifico.
print(manager.list_phone_numbers('Alice'))
print(manager.list_phone_numbers('Diego'))

# Trova e restituisce tutti i contatti che contengono
print(manager.add_phone_number("Alice", "123456"))
print(manager.add_phone_number("Franco", "123456"))
print(manager.add_phone_number("Franco", "123"))


print(manager.search_contact_by_phone_number('123'))
print(manager.search_contact_by_phone_number("123456"))





    






