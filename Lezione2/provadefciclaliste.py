# definisco una funzione per cilcare le liste 
def CiclaListe (l1: list, l2: list): #-> due liste
     new_list=[]
     for i in range(len(l1)):
         print (f"{l1[i]} {l2[i]} ")
    

transportation= ["Ferrari","Mustang","Ducati","Lamborghini"]
statements=["comprerò una","mi piace molto il simbolo della","la mia moto preferita è",
            "potrei accontentarmi anche di una"]


out= CiclaListe(statements,transportation)

print(out)



# for i in range(len(transportation)):
#     print (f"{statements[i]} {transportation[i]} ")