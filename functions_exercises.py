#Project under Python Crash Course Chapter 8

'''Write a function called display_message() that prints one sentence telling
everyone what you are learning about in this chapter. Call the function, and 
make sure the message displays correctly'''

def display_message():
    """Display a simple message_First Exercise"""
    print('I am learning functions in this Chapter')
display_message()

''' Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making sure to 
include a book title as an argument in the function call.'''

def favorite_book(title):
    """Displaying Favorite Book_Second Exercise"""
    print(f"My favorite book is, {title.title()}")
favorite_book('Alice')

'''Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print 
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments'''

def make_shirt(size, message):
  print(f"A {size} size shirt with the message '{message}' will be made.")
# Call the function using positional arguments
make_shirt("Large", "Python is Life")
# Call the function using keyword arguments
make_shirt(message="I love Python", size="Medium")

'''Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message'''

def make_shirt(size='large', message='I love Python'):
  print(f"The shirt is size {size} and the message on it reads '{message}'.")
# Call the function using the default values for size and message
make_shirt()
# Call the function using the default value for message and a different size
make_shirt(size='medium')
# Call the function using a different message and size
make_shirt(size='small', message='I love programming!')

''' Write a function called describe_city() that accepts the name of 
a city and its country. The function should print a simple sentence, such as 
Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the 
default country.'''

def describe_city(city, country="the United States"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik")
describe_city("Paris", "France")
describe_city("Sydney", "Australia")

'''Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the 
values that are returned'''

def city_country(city, country):
    return f"{city}, {country}"
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))


'''Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Use None to add an optional parameter to make_album() that allows you to 
store the number of songs on an album. If the calling line includes a value for 
the number of songs, add that value to the album’s dictionary. Make at least 
one new function call that includes the number of songs on an album.'''

def make_album(artist, album, songs=None):
    album_info = {'artist': artist, 'album': album}
    if songs:
        album_info['songs'] = songs
    return album_info
album1 = make_album('Eminem', 'Revival')
album2 = make_album('Drake', 'Scorpion')
album3 = make_album('Kendrick Lamar', 'Good Kid, M.A.A.D City', 15)
print(album1)
print(album2)
print(album3)


'''Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created. Be sure to include a quit value in the while loop'''

#def make_album(artist, album, songs=None):
 #   album_dict = {'artist': artist, 'album': album}
  #  if songs:
   #     album_dict['songs'] = songs
    #return album_dict

'''while True:
        print("Enter album information: (Enter 'q' to quit)")
        artist = input("Artist: ")
        if artist == 'q':
            break
        album = input("Album: ")
        if album == 'q':
            break
        songs = input("songs (optional, enter 'q' to skip): ")
        if songs == 'q':
            album_info = make_album(artist, album)
else:
            album_info = make_album(artist, album, songs)
            print(album_info)'''

''' Make a list containing a series of short text messages. Pass the 
list to a function called show_messages(), which prints each text message'''

def show_messages(messages):
    for message in messages:
        print(message)
        
text_messages = ['Hello, how are you?', 'I hope you are doing well.', 'Have a great day!']
show_messages(text_messages[:])

'''Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and 
moves each message to a new list called sent_messages as it’s printed. After 
calling the function, print both of your lists to make sure the messages were 
moved correctly'''

def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages
sent_messages = send_messages(text_messages[:])

'''Start with your work from Exercise 8-10. Call the function send_messages() 
with a copy of the list of messages. After calling the function, print both of 
your lists to show that the original list has retained its messages'''

archive_messages = send_messages(text_messages[:])
print("\nOriginal list of messages:")
print(text_messages)
print("\nSent messages:")
print(sent_messages)


''' Write a function that accepts a list of items a person wants 
on a sandwich. The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the 
sandwich that’s being ordered. Call the function three times, using a 
different number of arguments each time'''

def sandwich_order(*items):
  print("Sandwich order:")
  for item in items:
    print("- " + item)

sandwich_order("lettuce", "tomato", "mayo")
print("\n")
sandwich_order("lettuce", "tomato")
print("\n")
sandwich_order("lettuce", "tomato", "mayo", "cheese")


''': Start with a copy of user_profile.py from page 149. Build a 
profile of yourself by calling build_profile(), using your first and last names 
and three other key-value pairs that describe you.'''

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

fatima_profile = build_profile('Fatima', 'Usman',
                                location='Hadejia',
                                field='statistics',
                                hobbies=['reading', 'traveling', 'research'])

print(fatima_profile)


'''Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It 
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a color
or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was 
stored correctly.'''

def make_car(manufacturer, model, **kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    for key, value in kwargs.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


''' Put the functions for the example printing_models.py in a 
separate file called printing_functions.py. Write an import statement at the top 
of printing_models.py, and modify the file to use the imported functions'''

import printing_models


'''Using a program you wrote that has one function in it, store that function
 in a separate file. Import the function into your main program file, 
 and call the function using each of these approaches: 
import module_name 
from module_name import function_name 
from module_name import function_name as fn 
import module_name as mn 
from module_name import'''

import models
from models import show_models
from models import show_models as mdl
import models as mdl
from models import *


'''
 Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section'''

