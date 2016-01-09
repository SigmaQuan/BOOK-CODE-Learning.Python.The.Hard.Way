"""
Exercise 20: Functions and Files

"""

from sys import argv
# get the input file name from terminal
[script, input_file] = argv


def print_all(f):
    # output a whole file
    print f.read()


def rewind(f):
    # jump to the beginning of a file
    f.seek(0)


def print_a_line(line_count, f):
    # output a line of the file
    print line_count, f.readline()

# open a file
current_file = open(input_file)

print "First let's print the whole file:\n"
# print the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# jump the reader to the beginning of the file
rewind(current_file)

print "Let's print three lines:"
# output the first line of the file
current_line = 1
print_a_line(current_line, current_file)
# output the second line of the file
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# output the third line of the file
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)


"""
Study Drills
    1. Write English comments for each line to understand what that line does.
    2. Each time print_a_line is run, you are passing in a variable
    current_line. Write out what current_line is equal to on each function
    call, and trace how it becomes line_count in print_a_line.
    3. Find each place a function is used, and check its def to make sure that
    you are giving it the right arguments.
    4. Research online what the seek function for file does. Try pydoc file
    and see if you can figure it out from there. Then try pydoc file.seek to
    see what see does.
    5. Research the shorthand notation += and rewrite the script to use +=
    instead.
"""