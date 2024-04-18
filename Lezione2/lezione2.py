# Nicola Oliveri
# 18/04/2024

print ("Hello World!")

#
# this variable contains var name
name: str= "Cesare"

print (f"Ave{name}, etc.......")

# message 
message:str=("Moritori tua te salutan")


# use method print(f"{name variabele}"")
print(f"{name}, {message}")

# upper , lower, capitalazie method

lower_case: str= name.lower()
upper_case: str= name.upper()
capitalize_case:str= name.capitalize()

print(f"{lower_case} {upper_case} {capitalize_case}")


#2.6 Famous quote 2
famous_person:str= "Romolo"
message:str=" io sono il primo Re di Roma"

print(f"{famous_person} disse {message}")

#2.8 file extension

filename: str = "python_notes.txt"
extension_to_remove: str = ".txt"
filename_wo_extension: str = filename.removesuffix(extension_to_remove)

print(filename_wo_extension)





