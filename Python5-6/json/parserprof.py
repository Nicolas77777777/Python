import sys, json 

def Serializza(myLista):
    
    Mystring = str(myLista).replace(" ", "")
    return Mystring

def Deserializza(myString):
    if myString[0] == "[" and myString[-1] == "]":
        Mylist = myString.strip("[]").replace("'", "").split(",")
    else:
        Mylist = myString
    return Mylist

mydict_1 ={}

mydic


str1 = json.dumps ( mydict_1)

dcit_1= json.loads(mydict_2)

print(my)
