"""
Exercise 15: Reading Files
    You know how to get input from a user with raw_input and argv. Now will
    learn about reading from a file. You may have to play with this exercise
    the most to understand what's going on, so do the exercise carefully and
    remember you checks. Working with files is an easy way to erase your
    work if you are not careful.

    This exercise involves two files. One is the usual lesson_15.py file
    that you will run, but the other is name lesson_15_sample.txt. This
    second file isn't a script but a plain text file we'll be reading in our
    script. Here are the contents of that file:

    This is stuff I typed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.
"""
# for use argv variable
from sys import argv
# unpack the argv to get the script name and file name
script, filename = argv

# open the file
txt = open(filename)

# output the file name and file content
print "Here's your file %r:" % filename
print txt.read()

# close txt
txt.close()

# try again
# get file name from terminal
print "Type the filename again:"  # line 10
file_again = raw_input("> ")

# open file
txt_again = open(file_again)

# output the content of the file
print txt_again.read()  # line 15

# close the file
txt_again.close()


"""
Study Drills
    This is a big jump so be sure you do this Study Drill as best you can
    before moving on.
        1. Above each line, write out in English what that line does.
        2. If you are not sure ask someone for help or search online. Many
        times searching for "python THING" will find answers to what that
        THING does in Python. Try search for "python open".
        3. I used the word "commands" here, but commands are also called
        "functions" and "methods". You will learn about functions and methods
        later in the book.
        4. Get rid of the lines 10-15 where you use raw_input and run the
        script again.
        5. Use only raw_input and try the script that way. Why is one way of
        getting the filename better than another?
        6. Start python to start the python shell, and use open from the
        prompt just like in this program. Notice how you can open files and
        run read on them from within python?
        7. Have your script also call close() on the txt and txt_again
        variables. It's important to close files when you are done with them.
"""
