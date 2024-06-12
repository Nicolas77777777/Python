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