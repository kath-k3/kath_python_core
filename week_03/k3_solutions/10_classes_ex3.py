'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.
Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...
'''

# Class vs object attribute -
#Class A():
   # a = "I am a class attribute"




class EntertainmentShow():
    """
    Late-night show to provide entertainment for the audience.
    Usually held at a venue with a bar.

    Attributes:
        weekday (str): When does the event take place
        occurrence (str): How often does the event take place
        type_of_show (str): What is the show about
    """
    occurrence = "weekly" # All shows happen weekly

    def __init__(self, weekday, type_of_show):
        self.weekday = weekday
        self.type_of_show = type_of_show


    organizers = ["Maria", "John", "Peter"]

    def select_organizer(self):
    # Couldn't figure out the issue here: show_1.organizer gives an error
        weekdays = ['Wednesday', 'Thursday', 'Friday']
        if self.weekday in weekdays:
            # each of the organizers is responsible for one day only
            organizer = EntertainmentShow.organizers[weekdays.index(weekday)]
            self.organizer = weekday
            return self.organizer
        else:
            return None
            #print("We don't run shows on those days, go home to sleep!")


    def __str__(self):
        return f"{self.type_of_show} happens {self.weekday}s"


class Comedy(EntertainmentShow):
    """ Stuff """
    type_of_show = "Comedy"

    def __init__(self, language='English', type_of_show = type_of_show):
        weekday = "Friday"
        self.language = language
        EntertainmentShow.__init__(self, weekday, type_of_show)

    def __add__(self, other_language):
        languages = self.language.copy()
        languages.append(other_language)
        print(type(languages))
        #return languages
        #return Comedy(languages)
        return ', '.join(Comedy(languages))

    def __str__(self):
        return f"{self.type_of_show} show is always on {self.weekday}s and it is in {self.language}"



show_1 = EntertainmentShow("Wednesday", "Cabaret")
print(show_1.organizer)
#show_2 = Comedy()
show_3 = Comedy(["Spanish"])
show_4 = Comedy(["English"])
print(''.join(show_3.language))
print (', '.join(show_3.language + show_4.language))

show_5 = Comedy()
print(show_5)
#print (show_1, show_2, show_3)



