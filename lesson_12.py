"""
Exercise 12: Prompting people
    When you typed raw_input() you were typing the ( and ) characters, which
    are parenthesis characters.
"""
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)


"""
Study Drills
    1. In Terminal where you normally run python to run your scripts, type
    pydoc raw_input. Read what it says.

#     Help on built-in function raw_input in module __builtin__:
# raw_input(...)
#     raw_input([prompt]) -> string
#     Read a string from standard input.  The trailing newline is stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.

    2. Get out of pydoc by typing q to quit.
    3. Look online for what the pydoc command does.
    4. Use pydoc to also read about open, file, os, and sys. It's alright if
    you do not understand those; just read through and take notes about
    interesting things.

#     Help on built-in function open in module __builtin__:
# open(...)
#     open(name[, mode[, buffering]]) -> file object
#     Open a file using the file() type, returns a file object.  This is the
#     preferred way to open a file.  See file.__doc__ for further information.


# Help on class file in module __builtin__:
# class file(object)
#  |  file(name[, mode[, buffering]]) -> file object
#  |
#  |  Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
#  |  writing or appending.  The file will be created if it doesn't exist
#  |  when opened for writing or appending; it will be truncated when
#  |  opened for writing.  Add a 'b' to the mode for binary files.


# Help on module os:
# NAME
#     os - OS routines for Mac, NT, or Posix depending on what system we're on.
# FILE
#     /usr/lib/python2.7/os.py
# MODULE DOCS
# Help on built-in module sys:
# NAME
#     sys
# FILE
#     (built-in)
# MODULE DOCS
"""
