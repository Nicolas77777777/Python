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
names: list =["Romolo","Remo","Numa Pompilio","Tulio Ostilio"]
message: str =" Ave"
for i in names:
    phrases: str = (i)+ message
    print(phrases)


# 3-3. Your Own List

transportation= ["Ferrari","Mustang","Ducati","Lamborghini"]
statements=["comprerò una","mi piace molto il simbolo della","la mia moto preferita è",
            "potrei accontentarmi anche di una"]

for i in range(len(transportation)):
    print (f"{statements[i]} {transportation[i]} ")





