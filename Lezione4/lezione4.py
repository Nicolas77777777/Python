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
    return (f'One of my favorite books is {name_book}')

print(favorite_book("The Mahābhārata"))

# 8-3. T-Shirt: 
#  Write a function called make_shirt() that accepts a size 
#  and the text of a message that should be printed on the shirt. 
#  The function should print a sentence summarizing the size of the shirt
#  and the message printed on it. Call the function once using positional 
#  arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(message_printed: str = "", size : list = ["small","medium","large"]):
    return(f'size of your shirt is: {size} and your messagge is: {message_printed}')

print(make_shirt("I love 69","large"))

out=make_shirt(message_printed="I LOVE YOU",size="large")
print(out)

# 8-4. Large Shirts:
#  Modify the make_shirt() function so that shirts are large by default with
#  a message that reads I love Python. Make a large shirt and a medium shirt with
#  the default message, and a shirt of any size with a different message.

def make_shirt_large(x:str = ""):
    x = input("Scegli la taglia tra small medium e large ")
    if x == "medium":
        return(f'size of your shirt is: {x} and your messagge is: I love Python')
    elif x == "large":
        return(f'size of your shirt is: {x} and your messagge is: I love Python')
    else:
        return(f'size of your shirt is: {x} and your messagge is: I love Java')

print(make_shirt_large())

# 8-5. Cities: 
#  Write a function called describe_city() that accepts the name of a city
#  and its country. The function should print a simple sentence, such as 
#  Reykjavik is in Iceland. Give the parameter for the country a default value.
#  Call your function for three different cities, at least one of which is not 
#  in the default country.

def describe_city(name_city:str ="",name_country:str = "Italy"):

    return (f'{name_city} is in {name_country}')

print(describe_city("Roma"))
print(describe_city("Firenze"))
print(describe_city("Lima"))


# 8-6. City Names:
#  Write a function called city_country() that takes in the name of a city 
#  and its country. The function should return a string formatted like this:
#  "Santiago, Chile". Call your function with at least three city-country pairs,
#  and print the values that are returned.