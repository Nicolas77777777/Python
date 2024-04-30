# 8-1. Message:
#  Write a function called display_message() 
#  that prints one sentence telling everyone what you are 
#  learning about in this chapter. Call the function, 
#  and make sure the message displays correctly.

def display_message(): 
    return "sto imparando le funzioni"

print(display_message())

# 8-2. Favorite Book:
#  Write a function called favorite_book() 
#  that accepts one parameter, title. The function should print a message,
#  such as "One of my favorite books is Alice in Wonderland". Call the function,
#  making sure to include a book title as an argument in the function call.

def favorite_book(name_book: str =""):
    return (f'One of my favorite books is{name_book}')

print(favorite_book("The Mahābhārata"))

# 8-3. T-Shirt: 
#  Write a function called make_shirt() that accepts a size 
#  and the text of a message that should be printed on the shirt. 
#  The function should print a sentence summarizing the size of the shirt
#  and the message printed on it. Call the function once using positional 
#  arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt():
    return