"""
Exercise 40: Modules, Class, and Objects
    Python is called an "object-oriented programming language". This means
    there is a construct in Python call a class that lets you structure
    your software in a particular way. Using calsses, you can add consistency
    to your programs so that they can be used in a clear way. At least
    that's the theory.

    I am now going to teach you the beginnings of object-oriented programming,
    classes, and objects using what you already know about dictionaries and
    modules. My problems is that Object-Oriented Programming (OOP) is just
    plain weird. You have to struggle with this, try to understand what I say
    here, type in the code, and in the next exercise I'll hammer it in.
"""

"""
Modules Are Like Dictionaries
    You know how a dictionary is created and used and that it is a way to
    mapy one thing to another. That means if you have a dictionary with a
    key "apple" and you want to get it then you do this:
        mystuff = {'apple': "I AM APPLES!"}
        print mystuff['apple']

    Keep this idea of "get X from Y" in your head, and how think about
    modules. You've made a few so far, and you should know they are:
        1. A Python file with some functions or variables in it ..
        2. You import that file.
        3. And you can access the functions or variables in that modules
        with the . (dot) operator.

    Imagine I have a module that I decide to name mystuff.py and I put a
    function in it called apple. Here's the modules mystuff.py:
        # this goes in mystuff.py
        def apple():
            print "I AM APPLES!"

    Once I have this code, I can use the module mystuff with import and
    then access the apple function:
"""
import mystuff
mystuff.apple()

"""
    I could also put a variable in it named tangerine:
        # this is just a variable
        tangerine = "Living reflection of a dream"

    I can access that the same way:
"""
print mystuff.tangerine

"""
    Refer back to the dictionary, and you should start to see how this is
    similar to using a dictionary, but the syntax is different. Let's
    compare:

"""
# mystuff['apple']  # get apple from dict
mystuff.apple()  # get apple from the module
mystuff.tangerine  # same thing, it's just a variable

"""
    This means we have a very common pattern in Python:
        1. Take a key=value style container.
        2. Get something out of it by the key's name.

    In the case of the dictionary, the key is s string and the syntax is
    [key]. In the case of the module, they key is an identifier, and the
    syntax is .key. Other than that are nearly the same thing.
"""


"""
Classes Are Like Modules
    You can think about a module as a specialized dictionary that can store
    Python code so you can access it with . operator. Python also has another
    construct that serves a similar purpose called class. A class is a way to
    take a grouping of functions and data and place them inside a container
    so you can access them with . operator.

    If I were to create a class just like the mystuff modules, I'd do
    something like this:
"""
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

"""
    That looks complicated compared to modules, and there is definitely a
    lot going on by comparison, but you should be able to make out how this
    is like a "mini-module" with MyStuff having an apple() function in it.
    What is probably confusing is the __init__() function and use of self.
    tangerine for setting the tangerine instance variable.

    Here's why classes are used instead of modules: You can take the MyStuff
    class and use it to craft many of them millions at a time if you want
    and each one won't interfere with each other. When you import a modules
    there is only one for the entire program unless you do some monster
    hacks.

    Before you can understand this though, you need to know what an "object"
    is and how to work with MyStuff just like you do with the mystuff.py
    module.
"""

"""
Object are Like Import
    If a class is like a "mini-module", then there has to be a similar
    concept to import but for classes. That concept is called "instantiate",
    which is just a fancy, obnoxious, overly smart way to say "create". When
    you instantiate a class what you get is called an object.

    You instantiate (create) a class by calling the class like it's a
    function, like this:
"""

thing = MyStuff()
thing.apple()
print thing.tangerine

"""
    The first line is the "instantiate" operation, and it's a lot like calling
    a function. However, Python coordinates a sequence of events for you
    behind the scenes. I'll go through these steps using the above code for
    MyStuff:
        1. Python looks for MyStuff() and sees that it is a class you've
        defined.
        2. Python crafts an empty object with all the functions you've
        specified in the class using def.
        3. Python then looks to see if you made a "magic" __init__ function,
        and if you have it calls the function to initialize your newly
        created empty objcet.
        4. In the MyStuff function __init__ I then get this extra variable
        self, which is that empty object Python made for me, and I can set
        variables on it just like you would with a modules, dictionary, or
        other object.
        5. In this case, I set self.tangerine to a song Iyric and then I've
        initialized this object.
        6 Now Python can take this newly minted object and assign it to the
        thing variable for me to work with.

    That's the basics of how Python does this "mini-import" when you call a
    class like a function. Remember that this is not giving you the class,
    but instead is using the class as a blueprint for building a copy of
    that type of thing.

    Keep in mind that I'm giving you a slightly inaccurate idea for how
    these work so that you can start to build up and understanding of
    classes based on what you know about modules. The truth is, classes
    and objects suddenly diverge from modules at this point. If I were
    being totally honest, I'd say something more like this:
        Class are like blueprints or definitions for creating new mini-
        modules.
        Instantiation is how you make one of these mini-modules and import
        it at the same time. "Instantiate" just means to create an object
        from the class.
        The resulting created mini-module is called an object and you then
        assign it to a variable to work with it.

    At this point objects behave differently from modules and this should
    only serve as a way for you to bridge over to understanding classes
    and objects.

"""

"""
Getting Things from Things
    I now have three ways to get things from things:

"""
# dict style
# mystuff['apple']

# module style
mystuff.apple()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apple()
print thing.tangerine


"""
A First Class Example

"""

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()