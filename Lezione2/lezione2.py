# Nicola Oliveri
# 18/04/2024

print ("Hello World!")

# 2-3. Personal Message
eric_name: str = "Hello Eric, would you like to learn some Python today?"
print(eric_name)

# 2-4. Name Cases

# this variable contains var name_cases
name_cases: str = "caesar"

# lowercase, uppercase, and title case method
lower_case: str = name_cases.lower()
upper_case: str = name_cases.upper()
title_case: str = name_cases.capitalize()

print(f"{lower_case} {upper_case} {title_case}")

# 2-5. Famous Quote / 
print (f"{title_case} quando varco il Rubicone disse: Il dado è tratto.")

# 2-6. Famous Quote 2
famous_person: str = "Gaius Iulius Caesar"
message: str = " Alea iacta est."

# use method print(f"{name_cases variabele}"")
print(f"{famous_person} quando varco il Rubicone disse: {message}")

# example 2
famous_person2: str = "Romolo"
message2: str =" io sono il primo Re di Roma"

print(f"{famous_person2} disse {message2}")

#2.8 file extension
filename: str = "python_notes.txt"
extension_to_remove: str = ".txt"
filename_wo_extension: str = filename.removesuffix(extension_to_remove)

print(filename_wo_extension)

# 3.1 Names / 3.2 Greetings
names: list = ["Romolo","Remo","Numa Pompilio","Tulio Ostilio"]
message: str = " Ave"
for i in names:
    phrases: str = (i)+ message
    print(phrases)


# 3-3. Your Own List
transportation= ["Ferrari","Mustang","Ducati","Lamborghini"]
statements=["comprerò una","mi piace molto il simbolo della","la mia moto preferita è",
            "potrei accontentarmi anche di una"]

for i in range(len(transportation)):
    print (f"{statements[i]} {transportation[i]} ")

# 3-4. Guest List
person_invited: list =["Socrate","William Shakespeare","Rocky Marciano"]
message_invited: list =["Maestro parlami del conosci te stesso davanti un ottima cena!"
                        ,"Maestro parlami dell'Arte del teatro davanti un ottima cena!",
                       "Maestro parlami della nobile arte davanti un ottima cena!"]

for i in range(len(person_invited)):
    print (f"{person_invited[i]}, {message_invited[i]} ")

#3-5. Changing Guest List

# print Guest can’t make the dinner
print((person_invited[0]),"Conosci Te Stesso e Conoscerai gli Dei, ma purtroppo alla tua cena non potro partecipare.")

# replacing the name of the guest who can’t make it with the name of the new person
person_invited[0]="Diotima"

# replacing the message of Cleopatra guest 
message_invited[0]="Maestra vieni a cena con un attore e un pugile?"

# Print a second set of invitation messages, one for each person who is still in your list
for i in range(len(person_invited)):
    print (f"{person_invited[i]}, {message_invited[i]} ")

# definisco una funzione per cilcare le liste 
# def CiclaListe (l1: list, l2: list): #-> due liste
#     for i in range(len(l1)):
#         return (f"{l1[i]}, {l2[i]} ")
    
# print(CiclaListe(person_invited,message_invited))

# 3-6. More Guests
# definisco una funzione per cilcare le liste 
    
# informing people that you found a bigger table.
print("Cari amici si sono aggiunti altri 3 amici, per fortuna"
      " ho trovato questo tavolo piu grande")

# new guest to the beginning /to the middle/ to the end/ in the list
person_invited.insert(0,"Platone")
person_invited.insert(2,"Scipione l'Africano")
person_invited.append("Gigi Proietti")

print(person_invited)

# Print a new set of invitation messages
message_invited.insert(0, "Benvenuto")
message_invited.insert(2, "Ave Scipione")
message_invited.append("è un piacere averti tra noi")

for i in range(len(person_invited)):
    print (f"{person_invited[i]}, {message_invited[i]} ")

# 3-7. Shrinking Guest List:
#prints a message saying that you can invite only two people for dinner.
print(" Mi dispiace amici,ma il tavolo piu grande non arriverà in tempo,"
      "mi trovo costretto a disdire la cena per alcuni di voi ")

new_message_out: str =  "sei fuori!!"


# Remove guests one at a time until only two names remain
while len(person_invited) > 2:
    remove_guest = person_invited.pop()
    print(f"Scusa {remove_guest},{new_message_out}")

#Print a message to each of the two people still on your list, letting them know they’re still invited.
print(person_invited)

for message in range(len(person_invited)):
    print(f"{person_invited[message]} sei dentro")

#Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.
del person_invited

# 3-8. Seeing the World:
# Store the locations in a list. Make sure the list is not in alphabetical order.
locations: list =["Tokio","Napoli","Valcamonica","Finesterre","Himalaya"]

#Print your list in its original order
print(locations)

#Use sorted() to print your list in alphabetical order without modifying the actual list..
print(sorted(locations))

# Show that your list is still in its original order by printing it again.
print(locations)

#Use sorted() to print your list in reverse-alphabetical order without
# changing the order of the original list.
# Show that your list is still in its original order by printing it again.
print(sorted(locations,reverse=True))
print(locations)

#Use reverse()  to change the order of your list. 
#Print the list to show that its order has changed.
locations.reverse()
print(locations)

#Use reverse() to change the order of your list again. 
#Print the list to show it’s back to its original order.
locations.reverse()
print(locations)

#Use sort() to change your list so it’s stored in alphabetical order. 
#Print the list to show that its order has been changed.
locations.sort()
print(locations)

#Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
locations.sort(reverse=True)
print(locations)

#3-9. Dinner Guests
print("Ho invitato a cena",len(names),"persone")

#3-10. Every Function
# make a list of mountains, rivers, countries, cities

montains: list =["Everest","Tevere","Italia","Roma","Latino"]




















