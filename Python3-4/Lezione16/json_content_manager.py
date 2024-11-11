# Esempio di context manager per un file JSON

#Prima, creiamo una classe JSONFileManager 
#che gestisce l'apertura, lettura e scrittura di file JSON:


import json

class JSONFileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Apre il file
        self.file = open(self.file_name, self.mode)
        print(f"File '{self.file_name}' opened.")
        return self.file  # Restituisce l'oggetto file

    def __exit__(self, exc_type, exc_value, traceback):
        # Chiude il file
        if self.file:
            self.file.close()
            print(f"File '{self.file_name}' closed.")
        
        # Gestione delle eccezioni
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        
        return False  # Propaga l'eccezione
    
# Lettura di un file JSON con il context manager    
file_path = 'data.json'

with JSONFileManager(file_path, 'r') as file:
    data = json.load(file)  # Legge il contenuto del file JSON
    print("File content:")
    print(data)  # Stampa il contenuto del file

# Scrittura su un file JSON con il context manager

new_data = {
    "name": "Bob",
    "age": 25,
    "city": "Milan"
}

file_path = 'data.json'

with JSONFileManager(file_path, 'w') as file:
    json.dump(new_data, file, indent=4)  # Scrive il contenuto nel file JSON
    print("File content written.")

