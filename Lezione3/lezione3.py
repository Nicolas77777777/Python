
# 4-1. Pizzas
#  Think of at least three kinds of your favorite pizza. Store these pizza
#  names in a list,and then use a for loop to print the name of each pizza.
list_pizza : list =["Margherita","4 Formaggi","Zucca e Guanciale"]

for i in list_pizza:
    print(i)

# Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should have
# one line of output containing a simple statement like I like pepperoni pizza.

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

# 4-2. Animals
#  Think of at least three different animals that have a common characteristic. 
#  Store the names of these animals in a list,
#  and then use a for loop to print out the name of each animal.
animals: list =["Wolf","Dog","Fox"]

for i in animals:
    print(i)

# Modify the program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, indicating what these animals have in common. 
# You could print a phrase, such as Any of these animals would make a great pet!
# These animals are part of the canidae family
statements_animals: list =["it is a totemic animal."," is man's best friend","is clever"]

for i in range(len(animals)):
    print(f"{animals[i]} {statements_animals[i]} \nThese animals are part of the canidae family")

# 4-3. 
#  Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(1,21):
    print(i)

# 4-4.One Million:
#  Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
million: list =[]
for i in range(1,100001):
    million.append(i)

print(million)

# 4-5.  Summing a Million:
#  Make a list of the numbers from one to one million, 
#  and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#  Also, use the sum() function to see how quickly Python can add a million numbers.

print(f"use min()= {min(million)} and max()= {max(million)} use the sum() = {sum(million)}")

# 4-6. Odd Numbers: 
#  Use the third argument of the range() function to make a list of 
#  the odd numbers from 1 to 20. Use a for loop to print each number.
for i in range(1,21,2):
    print(i)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
#  Use a for loop to print the numbers in your list.
for i in range(3,31,3):
    print(i)

# 4-8. Cubes: 
#  A number raised to the third power is called a cube. For example, 
#  the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
#  (that is, the cube of each integer from 1 through 10), 
#  and use a for loop to print out the value of each cube.

# Create a list with numeber from 1 trough 10 
list_cube: list =[]
for i in range(1,11):
    list_cube.append(i)

list_cube_com=[x for x in range(1,11)]
print(list_cube_com)

for z in  list_cube:
    x=z**3
    print(f"The cube of numner{z} is: {x}")

# 4-9. Cube Comprehension:
# Use a list comprehension to generate a list of the first 10 cubes.
list_comprehension_cube=[x **3 for x in list_cube ]
print(list_comprehension_cube)

# 4-10. Slices: 
# Using one of the programs you wrote in this chapter, add several lines to the end 
# of the program that do the following:
# Print the message The first three items in the list are:.
# Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:
# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

print(f"The first three items in the list are:{list_comprehension_cube[:3]}")
print(f"Three items from the middle of the list are:{list_comprehension_cube[4:7]}")
print(f"The last three items in the list are:{list_comprehension_cube[7:10]}")

# 4-11. My Pizzas, Your Pizzas:
# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, 
# and call it friend_pizzas.
friends_pizza: list = list_pizza.copy()

# Add a new pizza to the original list.
list_pizza.append("Napoletana")

# Add a different pizza to the list friend_pizzas.
friends_pizza.insert(4,"4 Stagioni")

# Prove that you have two separate lists.
print(f"{list_pizza} {friends_pizza}")

# Print the message My favorite pizzas are:, and then use a for 
# loop to print the first list.
print ("My favorite pizzas are :")

for i in list_pizza:
    print(i)
# Print the message My friend’s favorite pizzas are:,
# and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

print ("My friend’s favorite pizzas are:")
for i in friends_pizza:
    print(i)

# 4-12. More Loops: 
# All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.
for i in list_pizza,friends_pizza:
    print(i)

# 4-14. PEP 8 /4-15. Code Review: 
# Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

list_pizza_pep : list = [
    "Margherita", 
    "4 Formaggi",
    "Zucca e Guanciale"
    ]

for i in list_pizza:
    print(i)

my_list: list =[]
for i in list_pizza:
    i_like_pizza : str = "Mi piace la pizza " +(i)
    my_list.append(i_like_pizza)
    print(i_like_pizza)

print(my_list)
    
print(f'La pizza {list_pizza[0]} è davvero buona con la bufala\nanche la pizza {list_pizza[1]}\
       non scherza\ninfine la pizza {list_pizza[2]} è la mia preferita\nAdoro la pizza".')

animals: list = [
    "Wolf",
    "Dog",
    "Fox"
    ]

for i in animals:
    print(i)
    
# 5-1. Conditional Tests: 
#  Write a series of conditional tests. Print a statement describing 
#  each test and your prediction for the results of each test.

# Create at least 10 tests. 
# Have at least 5 tests evaluate to True 
x: int = 10
print(f'the number {x} is == 10 ? I predict True.')
print(x==10)

print(f'the number {x} is > 9 ? I predict True.')
print(x>9)

print(f'the number {x} is != 9 ? I predict True.')
print(x!=9)

print(f'the number {x} is < 100 ? I predict True.')
print(x<100)

print(f'the number {x} is >= 10 ? I predict True.')
print(x>=10)

# 5 tests evaluate to False.
print(f'the number {x} is >= 100 ? I predict False.')
print(x>=100)

print(f'the number {x} is != 10 ? I predict False.')
print(x!=10)

print(f'the number {x} is < 9 ? I predict False.')
print(x<9)

print(f'the number {x} is > 11 ? I predict False.')
print(x>11)


# 5-2. More Conditional Tests:
# Have at least one True and one False result for each of the following:

# Tests for equality and inequality with strings

string_one: str = "Ama l'amicizia"
string_two: str = "Preferisci ciò che è sacro"

if string_one == "Ama l'amicizia" and string_one != string_two :
    print(f"Ama l'amicizia == {string_one}, I predict True ")
    print(string_one == "Ama l'amicizia")
    print(f"if {string_one} is == a {string_two},I predict False")
    print(string_one == string_two)



















