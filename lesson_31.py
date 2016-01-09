"""
Exercise 31: Making Decisions
    In the first half of this book you mostly just printed out things call
    functions, but everything was basically in a straight line. Your scripts
    ran starting at the top and went to the bottom where they ended. If you
    made a function you could run that function later, but it still didn't
    have the kind of branching you need to really make decisions. Now that
    you have if, else, and elif you can start to make scripts that decide
    things.

    In the last script you wrote out a simple set of tests asking some
    questions. In this script you will ask the user questions and make
    decision based on their answers. Write this script, and then play with
    it quite a lot to figure it out.
"""

print "You enter a dark room with two doors. Do you to through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats you legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs ways." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
