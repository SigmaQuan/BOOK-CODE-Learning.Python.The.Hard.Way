"""
Exercise 08: Printing, Printing
    We will now see how to do more complicated formating of a string. This
    code looks complex, bu if you do your comments above each line and break
    down to its parts, you'll understand it.
"""
# declare a output formatter, which could be used to output four variables
formatter = "%r %r %r %r"

# output some variables
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

"""
Study Drills
    1. Do your checks, write down your mistakes, and try not to make the
    same mistakes on the next exercise.
    2. Notice that the last line of output both single-quotes and double-
    quotes for individual pieces. Why do you think that is?
"""