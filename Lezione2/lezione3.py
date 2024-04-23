import time

a: float= time.time()

#4-1. Pizzas
#Think of at least three kinds of your favorite pizza. Store these pizza
# names in a list,and then use a for loop to print the name of each pizza.
list_pizza : list =["Margherita","4 Formaggi","Zucca e Guanciale"]

for i in list_pizza:
    print(i)

# Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should have
#one line of output containing a simple statement like I like pepperoni pizza.
my_list: list = []

for i in list_pizza:
    i_like_pizza : str = "Mi piace la pizza " +(i)
    my_list.append(i_like_pizza + (i))
    print(i_like_pizza)
print(my_list)
# Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence,
# such as I really love pizza!


