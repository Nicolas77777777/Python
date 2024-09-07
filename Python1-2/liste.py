list1= ["franco","pippo","jhonny",1,2,2,5.4]
print (list1)

list1.append("banana")
print (list)

list1.remove("pippo")
print (list)


allowlist=["Romolo","Numa", "Tulio Ostilio","Anco Marzio",
          "Tarquinio Prisquo","Servio Tullio","TarquinioSuperbo","Romolo"]

print(allowlist)
print(len(allowlist))
# perche conta 8 elemnti, dovrebbero essere 9 la lista parte smpre da 0

lstringe=["augusto","cesare","marco aurelio"]
lint=[1,2,3,4,5,6]
lb=[True,False,True,False]
lgender=[True,"ottaviano",2,3,4.5]

print(lstringe,lint,lb,lgender)

print(type(lgender))


thislist = list(("apple", "banana", "cherry"))
print(thislist)

#Access Items
print(allowlist[3])

#negative Acces
print(allowlist[-2])
print(allowlist[-8])

#range of index
print(allowlist[2:5])

list7=["Romolo","Numa Pompilio", "Tulio Ostilio","Anco Marzio",
          "Tarquinio Prisquo","Servio Tullio","Tarquinio il Superbo",]
print(len(list7))
print(list7[:5])
print(list7[1:5])
print(list7[1:6])
print(list7[2:])

#check
if "Romolo" in list7:
    print( "si Romolo è uno dei 7 re d Roma" )

#Change Item Value

i7re=["Romolo","Numa Pompilio", "Tulio Ostilio","Anco Marzio",
          "Tarquinio Prisquo","Servio Tullio","Tarquinio il Superbo",]

#i7re[2]=("Ottaviano")
#print(i7re)

#Change a Range of Item Values
#i7re[1:2]=["cambiovalore1","cambiovalore2"]
#print(i7re)

#i7re[1:5]=["cambiovalore2","cambiovalore3"]
#print(i7re)

#i7re[1:5]=["cambiovalore4"]
#print(i7re)

i7re.insert(3,"Remo")
print(i7re)

i7re.insert(1,"Remo")
print(i7re)

# Esercizi liste 
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = ("kiwi")

print(fruits)

#appnd
fruits.append("orange")
print(fruits)

#Use the insert method to add "lemon" as the second item in the fruits list.
fruits.insert(1,"lemon")
print(fruits)

#remove
fruits.remove("banana")
print(fruits)



#tuple si definiscono con parentesi tonde 

etuple=("Dante","Ovidio","Omero")
print(type(etuple))

print(etuple)

lista= list(etuple)

print(type(etuple))

lista[1]="Boccacio"
print(lista)

etuple=tuple(lista)
print(etuple)
print(type(etuple))
