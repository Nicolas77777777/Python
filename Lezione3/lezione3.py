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

# create a new list empty for create a new var 
my_list: list = []
for i in list_pizza:
    i_like_pizza : str = "Mi piace la pizza " +(i)
    my_list.append(i_like_pizza)
    print(i_like_pizza)

print(my_list)

# Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence,
# such as I really love pizza!


piazza_margherita: str = "Con la mozzarella e pomodoro\n oppure con la bufala\n e altre cose"
pizza_4formaggi: str = " Con tutti i formaggi\n bianca \n e molto croccante"


print(piazza_margherita)


def fibonacci (numero:int) :
    if numero <= 2:
        return 1
    else:
        return fibonacci(numero-1)+ fibonacci(numero-2)
    
fibonacci(10)


def fibonacci_for(numero: int):
    memoria: list = [1,1]
    for i in range(1,numero):
        risultato: int = memoria[i-1]+memoria[i]
        memoria.append(risultato)
    return memoria[-1]

print(fibonacci_for(60))
    



