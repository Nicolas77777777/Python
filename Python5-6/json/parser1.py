mylist_1 = "['mario','gino','lucrezia']"
mylist_2 = ['mario', 'gino', 'lucrezia']

def Serializza(myLista):
    
    Mystring = str(myLista).replace(" ", "")
    return Mystring

def Deserializza(myString):
    if myString[0] == "[" and myString[-1] == "]":
        Mylist = myString.strip("[]").replace("'", "").split(",")
    else:
        Mylist = myString
    return Mylist

sOut = Serializza(mylist_2)

if sOut == mylist_1:
    print("PROCEDURA AVVENUTA CON SUCCESSO")
else:
    print("PROCEDURA SBAGLIATA")
