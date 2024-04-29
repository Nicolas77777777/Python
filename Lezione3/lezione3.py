
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
print(f"La pizza {list_pizza[0]} è davvero buona con la bufala\nanche la pizza {list_pizza[1]} non scherza\ninfine la pizza {list_pizza[2]} è la mia preferita\nAdoro la pizza.")

#4-2. Animals
#Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list,
#and then use a for loop to print out the name of each animal.
animals: list =["Wolf","Dog","Fox"]

for i in animals:
    print(i)

#Modify the program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, indicating what these animals have in common. 
#You could print a phrase, such as Any of these animals would make a great pet!
#These animals are part of the canidae family
statements_animals=["it is a totemic animal."," is man's best friend","is clever"]

for i in range(len(animals)):
    print(f"{animals[i]} {statements_animals[i]} \nThese animals are part of the canidae family")


    

    



