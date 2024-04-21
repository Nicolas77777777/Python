#Exercise: Dictionaries, Solution
#The available dishes are: pasta, pizza, salad, wine, water
#Their prices are: 10.50, 9.00, 6.50, 4.00, 2.30

menu: dict = {"pasta": 10.50, "pizza": 9.00, "salad": 6.50,
"wine": 4.00, "water": 2.30}

pasta_price= menu["pasta"]
wine_price= menu["wine"]

# diversa assegnazione varabiali
water_price,salad_price= menu["water"],menu["salad"]

#print con formatter
print(f"{pasta_price} {wine_price} {water_price} {salad_price}")

#Let’s add cake to our menu.
menu["cake"]= 3.50

print(menu)

#Dictionaries: removing elements
menu.pop("salad")

print(menu)
