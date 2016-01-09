"""
Exercise 06: String and Text

"""
# assign values for four string variables.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# output x and y directly to terminal
print x
print y

# output x as a %r, y as %s
print "I said: %r." % x
print "I also said: '%s'." % y

# assign values for two string variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# output the two string
print joke_evaluation % hilarious

# assign values for two string variables
w = "This is the left side of..."
e = "a string with a right side."

# concatenate the two strings and output it
print w + e


"""
Study Drills
    1. Go through this program and write a comment above each line explaining
    it.
    2. Find all the places where a string is put inside a string. There are
    four places.
    3. Are you sure there are only four places? How do you know? Maybe I like
    lying.
    4. Explain why adding the two strings w and e with + makes a longer string.
"""
