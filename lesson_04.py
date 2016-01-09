"""
Exercise 04: Variables and Names
    If you get stuck with this exercise, remember the tricks you have been
    taught so far of finding difference and focusing on details:
        1. Write a comment above each line explaining to yourself what it
        does in English.
        2. Read you *.py file backward.
        3. Read you *.py file out loud, saying even the characters.
"""

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

"""
Study Drills
    Here are more study drills:
        1. I used 4.0 for space_in_a_car, but is that necessary? What happens
        if it's just 4?
        2. Remember that 4.0 if a floating point number. It's just a number
        with a decimal point, and you need 4.0 instead of just 4 so that it
        is floating point.
        3. Write comments above each of the variable assignments.
        4. Make sure you know what = is call (equals) and that it's making
        names for things.
        5. Remember that _ is an underscore character.
        6. Try running python from the Terminal as a calculator like you did
        before and use variable names to do your calculations. Popular
        variable names are also i, x, and j.
"""
