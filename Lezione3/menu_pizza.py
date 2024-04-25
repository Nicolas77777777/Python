allAges={"alice":25,"Bob":39}

print (allAges["alice"])

print(allAges)

menu = {"pasta": 10.50, "pizza": 9.00, "salad": 6.50,
"wine": 4.00, "water": 2.30}


prices_pasta: float =menu["pasta"]
prices_wine: float=menu["wine"]

print(prices_wine,prices_pasta)

menu["pasta"]= 9.50
menu["wine"]= 3.00

print (len(menu))

print(menu)

menu.pop("pizza")

print(menu)
