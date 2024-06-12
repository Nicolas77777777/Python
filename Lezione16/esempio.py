reader= open("esempio.txt")

print(reader)

reader.readline()

try: 
    reader.readline()
    
    print("sono nella trt")
    raise Exception(" ECCEZIONLAE")

except Exception:
    print ("SONO NELKLA Exepct")

finally:                #sono sempre eseguite
    print (reader)
    print (" sono in finally")
    reader.close

with open("esempio.txt") as reader:
    reader.readline()


# creare un contex manager personalizzato 

class ContexManager:
    def __enter__(self):
        print ("Ciao sono nell'enter")

        return self
    def __exit__(self, exc_type, ):
        if exc_type is not None:
            print("Eccezionale")

        return False
    
try:

    with ContexManager()  as cm: 
        print("Ciao")
        print(cm)

except Exception:
    print()

    