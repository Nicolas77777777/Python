import time

a: float= time.time()


#4-1. Pizzas
#Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
#and then use a for loop to print the name of each pizza.
#fun cicli ()
list_pizza : list =["Margherita","4 Formaggi","Zucca e Guanciale"]


for i in list_pizza:
    print(i)
    
for i in list_pizza:
    i_like_pizza : str = "Mi piace la pizza " +(i)
    print(i_like_pizza)

#list comprenshion
my_list: list = [index for index in range(100)]

my_list2: list = [index for index in range(100) if index %2==0]

my_list4: list = [index for index  % 2==0 in else (100) if index %2==0]


my_list3: list = ["ciao", "MI","CHIAMO","FLAVIO"]

mydict: dict {"key":1,"key2":1}

mydict3={}


print(my_list,my_list2)

