l=["c","i","a","o"]

for i in l:
    print(i)

for j in range(len(l)):
    print(l[j])


i=0

while i < len(l): #-> l=[0,1,2,3]
    print(l[i])
    i += 1

## scansione con dict

menu: dict = {"pasta": 10.50, "pizza": 9.00, "salad": 6.50,
"wine": 4.00, "water": 2.30}

for key in menu:
    print(f"chiave = {key} valore {menu[key]}")

