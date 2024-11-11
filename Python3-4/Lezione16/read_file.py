with open('/Users/nicolas/Desktop/la religione.txt', 'r') as file:
    content = file.read()  # Legge il contenuto del file
    print(content)  # Stampa il contenuto

class MyResource:
    def __enter__(self):
        print("Resource acquired")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")
        if exc_type is not None:  # Se c'è stata un'eccezione, stampiamo i dettagli
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        return False  # Propaga l'eccezione se c'è, altrimenti la silenzierebbe se fosse True

# Uso del context manager
with MyResource() as resource:
    print("Inside the with block")

with MyResource() as resource:
    print("Inside the with block")
    raise ValueError("Something went wrong!")  # Simuliamo un'eccezione


#Creazione del context manager per la gestione di un file
class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Apre il file
        self.file = open(self.file_name, self.mode)
        print(f"File '{self.file_name}' opened.")
        return self.file  # Restituiamo l'oggetto file per poterlo usare nel blocco with

    def __exit__(self, exc_type, exc_value, traceback):
        # Chiude il file
        if self.file:
            self.file.close()
            print(f"File '{self.file_name}' closed.")
        
        if exc_type is not None:  # Se c'è stata un'eccezione, stampiamo i dettagli
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        
        return False  # Propaga l'eccezione, se presente

#  Utilizzo del context manager

file_path = '/Users/nicolas/Desktop/la religione.txt'

with FileManager(file_path, 'r') as file:
    content = file.read()  # Legge il contenuto del file
    print("File content:")
    print(content)

