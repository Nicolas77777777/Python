# Nicola Oliveri
# 29/04/2024

import random


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

# Tests for equality and inequality with strings/ Test using the e keyword and the o keyword

string_one: str = "Ama l'amicizia"
string_two: str = "Preferisci ciò che è sacro"

if string_one == "Ama l'amicizia" or string_one != string_two :
    print(f"Ama l'amicizia == {string_one}, I predict True ")
    print(string_one == "Ama l'amicizia")
    print(f"if {string_one} is == a {string_two},I predict False")
    print(string_one == string_two)

# Tests using the lower() method Test using the e keyword and the o keyword
if string_one.lower() == "ama l'amicizia" and string_one.lower != "Ama l'amicizia":
     print(f" if{string_one.lower()}, is == 'ama l'amicizia' I predict True")
     print(string_one.lower() == "ama l'amicizia")
     print(f"{string_one.lower()} is == 'Ama l'amicizia',I predict False")
     print(string_one.lower == "Ama l'amicizia")

# Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to

# look at exercise number: 5-1

# Test whether an item is in a list or is not in a list
print(f'27 is in list_comprehension_cube, I predict True  {27 in list_comprehension_cube}')
print(f'28 is in list_comprehension_cube, I predict True  {28 is not list_comprehension_cube}')

# 5-3. Alien Colors 
#  Imagine an alien has just been shot down during a game. Create a variable called alien_color
#  and assign it the value "green", "yellow", or "red".

alien_color_list: list = ["green",
                          "yellow",
                          "red"
                          ]

alien_color= alien_color_list[0]

# Write an if statement to test whether the alien's color is green. If it is, 
# it prints a message that the player has just earned 5 points.
# Write a version of this program that passes the if test and another that fails.
# (The version that fails will have no output.)

if alien_color == "green":
    print("you earned 5 points")

# 5-4. Alien Colors #2:
#  If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
#  If the alien's color isn't green, print a statement that the player just earned 10 points.
#  Write one version of this program that runs the if block and another that runs the else block.

alien_color= alien_color_list[1]

if alien_color == "green":
    print("you earned 5 points")
else : 
    alien_color != "green"
    print("you earned 10 points")

# 5-5. Alien Colors #3:
#  If the alien is green, print a message that the player earned 5 points.
#  If the alien is yellow, print a message that the player earned 10 points.
#  If the alien is red, print a message that the player earned 15 points.
#  Write three versions of this program, making sure each message is printed for the appropriate alien color.

alien_color= alien_color_list[2]

if alien_color == "green":
    print("you earned 5 points")
elif alien_color == "yellow":
    print("you earned 10 points")
else:
 alien_color == "red"
print("you earned 15 points")

# 5-6. Stages of Life: 
#  Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#  If the person is less than 2 years old, print a message that the person is a baby.
#  If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#  If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#  If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#  If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#  If the person is age 65 or older, print a message that the person is an elder.

# create a function
def function_age (x):
    if x < 2:
        return ("You are a baby")
    elif x < 4 and x >= 2:
        return ("You are a toddler")
    elif x >= 4 and x < 13:
        return ("You are a kid")
    elif x >= 13 and x < 20:
        return ("You are a teenager")
    elif x >= 20 and x < 65:
        return ("You are adult")
    else: 
        x >= 65 and x < 120
        return ("You are elder")

# I define a variable that generates a random number. 
#this variable will be the argument in the function
age: int= random.randint(1,120)

print(f'the person {age} years old, {function_age(age)}')
print(f'the person {age} years old, {function_age(age)}')
print(f'the person {age} years old, {function_age(age)}')
print(f'the person {age} years old, {function_age(age)}')

# 5-7. Favorite Fruit:
#  Make a list of your favorite fruits, and then write a series of independent if statements 
#  that check for certain fruits in your list.
#  Make a list of your three favorite fruits and call it favorite_fruits.
#  Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#  If the fruit is in your list, the if block should print a statement, such as You really like Apples!

favorite_fruits = ["strawberry",
                    "banana", 
                    "peach"
]

if "strawberry" in favorite_fruits:
    print ("such as You really like strawberry !")
if "banana" in favorite_fruits:
    print ("such as You really like banana !")
if "peach" in favorite_fruits:
    print ("such as You really like peach !")
if "anguria" is not  favorite_fruits:
    print ("anguria its not present !")
if "apple" is not  favorite_fruits:
    print ("apple its not present !")


# 5-8. Hello Admin:
#  Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will 
#  print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#  If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#  Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
user_name: list = ["mario", 
                   "giulia", 
                   "francesco", 
                   "laura", 
                   "admin"
                   ]

for i in user_name:
    if i == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f' Hello {i}, thank you for logging in again.')

# 5-9. No Users:
#  Add an if test to hello_admin.py to make sure the list of users is not empty.
#  If the list is empty, print the message We need to find some users!
#  Remove all of the usernames from your list, and make sure the correct message is printed.

current_users: list = user_name.copy()
user_name.clear()

if user_name:
    for i in user_name:
        print("thank you for logging in again.'")
else :
    print("We need to find some users!")

# 5-10. Checking Usernames:
#  do the following to create a program that simulates how websites ensure that everyone has a unique username.
#  Make a list of five or more usernames called current_users.
#  Make another list of five usernames called new_users. Make sure one or two of 
#  the new usernames are also in the current_users list.
#  Loop through the new_users list to see if each new username has already been used. 
#  If it has, print a message that the person will need to enter a new username. If a username has not been used, 
#  print a message saying that the username is available.
#  Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
    

current_users[4]="franco"

new_users: list = ["mario", 
                   "giulia", 
                   "dino",
                   "mimmo",
                   "demetrio"]

for i in new_users:
    if i in current_users:
        print(f'{i} will need to enter a new username')
    else: 
        i is not current_users
        print(f"{i} that the username is available.")

# 5-11.
#  Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#  Store the numbers 1 through 9 in a list. Loop through the list.
#  Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#  Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line

numbers: list = list(range(1, 10))
for numbers in numbers:
    if numbers == 1:
        print(f"{numbers}st")
    elif numbers == 2:
        print(f"{numbers}nd")
    elif numbers == 3:
        print(f"{numbers}rd")
    else:
        print(f"{numbers}th")


































