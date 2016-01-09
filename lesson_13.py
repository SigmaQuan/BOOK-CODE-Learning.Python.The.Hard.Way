"""
Exercise 13: Parameters, Unpacking, Variables
    In this exercise we will cover one more input method you can use to pass
    variables to a script (script being another name for you .py files). You
    know how you type python lesson_03.py to run the lesson_03.py file? Well
    the lesson_13.py part of the command is called an "argument". What we'll
    do now is write a script that also accepts arguments.
"""

from sys import argv  # line 1

script, first, second = argv  # line 3, third

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
# print "Your third variable is: ", third

"""
On line 1 we have what's called an "import". This is how you add features to
your script from the Python feature set. Rather than give you all the
feature at once, Python asks you to say what you plan to use. This keeps your
programs small, but it also acts documentation for other programmers who read
you code later.

The argv is the "argument variable", a very standard name in programming, that
you will find used in many other language. This variable holds the arguments
you pass to your Python script when you run it. In the exercise you will get
to play with this more and see what happens.

Line 3 "unpacks" argv so that, rather than holding all the arguments, it gets
assigned to four variables you can work with: script, first, second, and
third. This may look strange, but "unpack" is probably the best word to
describe what it does. It just says, "Take whatever is in argv, unpack it,
and assign it to all of these variables on the left in order".
"""

"""
Hold Up! Features Have Another Name
    I call them "features" here (these little things you import to make your
    Python program do more) but nobody else call them features. I just used
    that name because I needed to trick you into learning what they are
    without jargon. Before you can continue, you need to learn their real
    name: modules.

    From now on we will be calling these "features" that we import modules.
    I'll say things like, "You want to import the sys module". They are also
    call "libraries" by other programmers, but let's just stick with modules.
"""

"""
Study Drills
    1. Try giving fewer than three arguments to your script. See that error
    you get?
    2. Write a script that has fewer arguments and one that has more. Make
    sure you give the unpacked variable good names.
    3. Combine raw_input with argv to make a script that gets more input
    from a user.
    4. Remember that modules give you features. Modules. Modules. Remember
    this because we'll need it later.
"""