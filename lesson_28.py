"""
Exercise 28: Boolean Practice
    The logic combinations you learned from the last exercise are called
    "boolean" logic expressions. Boolean logic is used everywhere in
     programming. It is an essential fundamental parts of computation and
     knowing them very well is akin to knowing your scales in music.

     In this exercise you will take the logic exercise you memorized and
     start typing them out in Python. Take each of these logic problems and
     write you think the answer will be. In each case it will be either True
     or False. Once you have the answers written down, you will start Python
     in your Terminal and type each logic problem in to confirm your answers.
"""

print "01", (True and True), True
print "02", (False and True), False
print "03", ((1 == 1) and (2 == 1)), False
print "04", ("Test" == "test"), False
print "05", (1 == 1 or 2 != 1), True
print "06", (True and 1 == 1), True
print "07", (False and 0 != 0), False
print "08", (True or 1 == 1), True
print "09", ("test" == "testing"), False
print "10", (1 != 0 and 2 == 1), False
print "11", ("test" != "testing"), True
print "12", ("test" == 1), False
print "13", (not (True and False)), True
print "14", (not (1 == 1 and 0 != 1)), False
print "15", (not (10 == 1 or 1000 == 1000)), False
print "16", (not (1 != 10 or 3 == 4)), False
print "17", (not ("testing" == "testing" and "Zed" == "Cool Guy")), True
print "18", (1 == 1 and (not ("testing" == 1 or 1 == 0))), True
print "19", ("chunky" == "bacon" and (not (3 == 4 or 3 == 3))), False
print "20", (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))), False
