"""
Exercise 38: Doing Things to Lists

"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # whoa! fancy
print stuff.pop()
print ' '.join(stuff)  # what? cool!
print '#'.join(stuff[3:5])  # super stellar!


"""
When to Use Lists
    You use a list whenever you have something that matches the list data
    structure's useful features:
        1. If you need to maintain order. Remember, this is listed order,
        not sorted order. Lists do not sort for you.
        2. If you need to access the contents randomly by a number. Remember,
        this is using cardinal numbers starting at 0.
        3. If you need to go through the contents linearly (first to last).
        Remember, that's what for-loops are for.
"""