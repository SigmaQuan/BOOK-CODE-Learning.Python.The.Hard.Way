"""
Exercise 03: Numbers and Math
    Every programming language has some kind of way of doing numbers and
    math. Do not worry: programmers lie frequently about being math geniuses
    when they really aren't. If they were math geniuses, they would be doing
    math, not writing buggy web frameworks so they can drive race cars.

    This exercise has lots of math symbols. Let's name them right away so you
    know what they are called. As you type this one in, say the name. When
    saying them feels boring you can stop saying them. Here are the names:
    1. + plus
    2. - minus
    3. / slash
    4. * asterisk
    5. % percent
    6. < less-than
    7. > greater-than
    8. <= less-than-equal
    9. >= greater-than-equal
"""

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, what's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2


"""
Study Drills
    1. Above each line, use the # to write a comment to yourself explaining
    what the line does.
    2. Remember in Exercise 00 when you started python? Start python this way
    again and using the math operators, use python as a calculator.
    3. Find something you need to calculate and write a new *.py file that
    does it.
    4. Notice the math seems "wrong" There are no fractions, only whole
    numbers. You need to use a "floating point" number, which is a number
    with a decimal point, as in 10.5, or 0.89, or even 3.0.
    5. Rewrite "lesson_03.py" to use floating point numbers so it's more
    accurate. 20.0 is floating point.
"""

print "Rewrite by float numbers"
print "I will now count my chickens:"

print "Hens", 25. + 30. / 6.
print "Roosters", 100. - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1. / 4. + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3. + 2
print "What is 5 - 7?", 5. - 7

print "Oh, what's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
