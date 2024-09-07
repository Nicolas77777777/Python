# Nicola Oliveri 



# 8-1. Message:
#  Write a function called display_message() 
#  that prints one sentence telling everyone what you are 
#  learning about in this chapter. Call the function, 
#  and make sure the message displays correctly.

def display_message(): 
    return "\nsto imparando le funzioni"

print(display_message())

# 8-2. Favorite Book:
#  Write a function called favorite_book() 
#  that accepts one parameter, title. The function should print a message,
#  such as "One of my favorite books is Alice in Wonderland". Call the function,
#  making sure to include a book title as an argument in the function call.

def favorite_book(name_book: str =""):
    return (f'\nOne of my favorite books is {name_book}')

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
    x = input("\nScegli la taglia tra small medium e large ")
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

def describe_city1(name_city: str = "", name_country : str = ""):
    return (f'{name_city}, {name_country}')

print(describe_city1("Roma","Italy"))
print(describe_city1("Madrid","Spain"))
print(describe_city1("Lima","Peru"))

# 8-7. Album:
#  Write a function called make_album() that builds a dictionary describing a music album.
#  The function should take in an artist name and an album title, and it should return 
#  a dictionary containing these two pieces of information. 
#  Use the function to make three dictionaries representing different albums.
#  Print each return value to show that the  dictionaries are storing the album information correctly.
#  Use None to add an optional parameter to make_album() that allows you to store the number of songs 
#  on an album. If the calling line includes a value for the number of songs, add that value to the album’s 
#  dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album( artist_name , album_title , number_song = 0 ):

    music: dict = {
                   'artist_name': artist_name,
                   'album":album':album_title,
                   }
    
    if number_song:
        music[ "number_song"] = number_song

    return music

album_one = make_album("Prince","Purple Rain")
albums_two = make_album("Pink floid"," The Wall")
albums_three = make_album("Vasco Rossi","C'è ci dice no")
albums_four= make_album("De Andre","Anime perse",number_song=10)

print(f'{album_one} {albums_two} {albums_three} {albums_four}')


# 8-8. User Albums:
#  Start with your program from Exercise 8-7. Write a while loop that allows users to 
#  enter an album’s artist and title. Once you have that information, call make_album()
#  with the user’s input and print the dictionary that’s created. 
#  Be sure to include a quit value in the while loop.

user_artist_name=""
user_album_name=""
while user_artist_name == None and user_album_name ==None:
     user_artist_name == input (" scrivi il nome artista")
     user_album_name=input (" scrivi il nome album")

print(make_album(user_artist_name,user_album_name))


# 8-9. Messages:
#  Make a list containing a series of short text messages. Pass the 
#  list to a function called show_messages(), which prints each text message.

text_messages: list =["ciao",
                      "come stai?",
                      "spero tutto bene"]

def show_messages( messages : list =[]):
    for i in messages:
        print(i) 
    
print(show_messages(text_messages))

# 8-10. Sending Messages:
#  Start with a copy of your program from Exercise 8-9. 
#  Write a function called send_messages() that prints each text message
#  and moves each message to a new list called sent_messages as it’s printed.
#  After calling the function, print both of your lists to make sure the messages were moved correctly.

def send_messages( messages : list =[]):
    sent_messages: list =[]
    for i in messages:
        print(i) 
    for x in messages:
        sent_messages.append(x)
       
    return(sent_messages)
    
print(send_messages(text_messages))


# 8-11. Archived Messages:
#  Start with your work from Exercise 8-10. Call the function send_messages() 
#  with a copy of the list of messages. After calling the function, print both of your lists to show that 
#  the original list has retained its messages.

def send_messages2( messages : list =[]):
    sent_messages: list =[]
    for i in messages:
        print(i) 
    for x in messages:
        sent_messages.append(x)
        archived_messagessent = sent_messages.copy()
    return f'\nmessaggi inviati {sent_messages}\nmessaggi archiaviati {archived_messagessent}'
    
print(send_messages2(text_messages))

# 8-12. Sandwiches:
#  Write a function that accepts a list of items a person wants on a sandwich. 
#  The function should have one parameter that collects as many items as the function call provides, 
#  and it should print a summary of the sandwich that’s being ordered. Call the function three times,
#  using a different number of arguments each time.

def make_sandwich(*items):
    print("\n What do you want in your sandwich?:")
    for item in items:
        print(f'I like {item} in my sandwich.')
    print("Il tuo panino è pronto")

make_sandwich("tomatos", "cheese", "beaf")
make_sandwich("egg", "tomatos")
make_sandwich("jam", "cheese", "salad", "egg", "mayonnaise")

# 8-13. User Profile:
#  Build a profile of yourself by calling build_profile(), 
#  using your first and last names and three other key-value pairs that describe you.
#  All the values must be passed to the function as parameters.
#  The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"


def build_profile ( name, surname, age, adress, city ):

    profile: dict = {
                   "name":name,
                   "surname":surname,
                   "age":age,
                   "adress":adress,
                    "city":city 
                   }
    
    list_profile: list =list(profile.values())
    str_list_profile=", ".join(list_profile)

    return  str_list_profile

print(build_profile("Mario", "Rossi", "45", "via castagneto", "Roma" ))

# 8-14. Cars:
#  Write a function that stores information about a car in a dictionary.
#  The function should always receive a manufacturer and a model name. 
#  It should then accept an arbitrary number of keyword arguments.
#  Call the function with the required information and two other name-value pairs,
#  such as a color or an optional feature. Your function should work for a call like this one:
#  car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s
#  returned to make sure all the information was stored correctly. 

def make_car (manufacturer, model, **kwargs ):

    car_dict: dict = {
                   "marca":manufacturer,
                   "model":model,
                   "kwargs":kwargs
                
                   }
    return  car_dict

car= make_car(manufacturer="Fiat",model="panda",color="blu", titt=True)
print(car)

#  8-15. Printing Models: / 8-16. Imports: 
#  Using a program you wrote that has one function in it, store that function in a separate file. 
#  Import the function into your main program file, and call the function using each of these approaches:
#  import module_name
#  from module_name import function_name
#  from module_name import function_name as fn
#  import module_name as mn
#  from module_name import *

# this exercise is in the file priiting_functions.py

# 8-17. Styling Functions: 
#  Choose any three programs you wrote for this chapter, and make sure 
#  they follow the styling guidelines described in this section.