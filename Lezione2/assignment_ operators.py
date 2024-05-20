# Assignment Operators
import random



x = 10
x += 5

z= 1
z +=1
print(x)
x -= 3
print(x)
x *= 2
print(x)
f= x/ 4
print(f)
f= x// 4
print(f)
x /= 4
print(x)
x //= 2
print(x)
x %= 2

#Alcuni usi comuni dell'operatore %:

items = ['a', 'b', 'c', 'd']

index = 7

circular_index= index % len(items)

print (circular_index, items[circular_index])

x=10
x **= 3

print(x)

# Operator Precedence
print(10 - 4 * 2)
print((10 - 4) * 2)

# Escape Characters
print("Hello\nWorld!")
print("Name:\tAlice")
print("C:\\Users\\Alice\\Documents")
print('It\'s a sunny day.')
print("She said, \"Hello!\".")

# cicli

"""Exercise
1. Create an empty list named numbers
2. Using for loop, write a Python program that prompts the user to enter the
length of the list and then fills up the list numbers with numbers from 1
to the length entered by the user."""



# def prova_cicli (lenght: input, x : int = None):
#     length = int(input("Enter the length of the list: "))
#     numbers = []

#     for i in range(1, length +x ):
#          numbers.append(i)   

#     print(numbers)



# prova_cicli(6,2)

# print(prova_cicli)

*a, b = 1,3,3,3,3,4,5,
print(a)
print(b)


length = int(input("Enter the length of the list: "))
numbers = []

for i in range(1, length +1 ):
         numbers.append(i)   

print(numbers)


length = int(input("Enter the length of the list: "))
numbers = []

for i in range(1, length -2 ):
         numbers.append(i)   

print(numbers)

length = int(input("Enter the length of the list: "))
numbers = []

for i in range(1, length //2 ):
         numbers.append(i)   

print(numbers)

length = int(input("Enter the length of the list: "))
numbers = []

for i in range(1, length +4 ):
         numbers.append(i)   

print(numbers)

#While Loops

# x = int(input())
# while x <= 5:
#     print(x)
# x += 1

# set 

m : int= random.randint(1,120)

print(m)






