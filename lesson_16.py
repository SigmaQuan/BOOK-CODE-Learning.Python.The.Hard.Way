"""
Exercise 16: Reading and Writing Files
    If you did the Study Drills from the last exercise you should have seen
    all sorts of commands (methods/functions) you can give to files. Here's
    the list of commands I want you to remember:
        close()--       Closes the file. Like File->Save.. in your editor.
        read()--        Reads the contents of the file. You can assign the
                        results to a variables.
        readline()--    Reads just one line of a text file.
        truncate()--    Empties the file. Watch out if you care about the
                        file.
        write('stuff')--Write "stuff" to the file.

    For now these are the important commands you need to know. Some of them
    take parameters, but we do not really care about that. You only need to
    remember write takes a parameter of a string you want to write to the
    file.
"""

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
