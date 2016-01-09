"""
Exercise 05: More Variables and Printing

"""

my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are actually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)


"""
Study Drills
    1. Change all the variables so there is no my_ in front of each one.
    Make sure you change the name everywhere, not just where you used =
    to set them.
    2. Try to write some variables that convert the inches and pounds to
    centimeters and kilograms. Do not just type in the measurements. Work
    out the math in Python.
    3. Search online for all of the Python format characters.
    4. Try more format characters. %r is a very useful one. It's like saying
    "print this no mater what."
"""


"""
1. Change all the variables so there is no my_ in front of each one.
    Make sure you change the name everywhere, not just where you used =
    to set them.
"""
print """1. Change all the variables so there is no my_ in front of each one.
    Make sure you change the name everywhere, not just where you used =
    to set them."""
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are actually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)


"""
2. Try to write some variables that convert the inches and pounds to
    centimeters and kilograms. Do not just type in the measurements. Work
    out the math in Python.
"""
print """2. Try to write some variables that convert the inches and pounds to
    centimeters and kilograms. Do not just type in the measurements. Work
    out the math in Python."""
name = 'Zed A. Shaw'
age = 35  # not a lie
height_inch = 74  # inches
inch_to_centimeter = 2.54
height_centimeter = height_inch * inch_to_centimeter
weight_pound = 180  # lbs
pound_to_kilogram = .4535923
weight_kilogram = weight_pound * pound_to_kilogram
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inch
print "He's %f centimeters tall." % height_centimeter
print "He's %d pounds heavy." % weight_pound
print "He's %f kilograms heavy." % weight_kilogram
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are actually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_inch, weight_pound, age + height_inch + weight_pound)


"""
3. Search online for all of the Python format characters.
# https://docs.python.org/2/library/stdtypes.html#string-formatting
# Conversion 	Meaning 	Notes
# 'd' 	Signed integer decimal.
# 'i' 	Signed integer decimal.
# 'o' 	Signed octal value. 	(1)
# 'u'   Obsolete type - it is identical to 'd'.    (7)
# 'x' 	Signed hexadecimal (lowercase). 	(2)
# 'X' 	Signed hexadecimal (uppercase). 	(2)
# 'e' 	Floating point exponential format (lowercase). 	(3)
# 'E' 	Floating point exponential format (uppercase). 	(3)
# 'f' 	Floating point decimal format. 	(3)
# 'F' 	Floating point decimal format. 	(3)
# 'g' 	Floating point format. Uses lowercase exponential format if exponent
#       is less than -4 or not less than precision, decimal format otherwise.
#       (4)
# 'G' 	Floating point format. Uses uppercase exponential format if exponent
#       is less than -4 or not less than precision, decimal format otherwise.
#       (4)
# 'c' 	Single character (accepts integer or single character string).
# 'r' 	String (converts any Python object using repr()). 	(5)
# 's' 	String (converts any Python object using str()). 	(6)
# '%' 	No argument is converted, results in a '%' character in the result.
#
# Notes:
# (1)   The alternate form causes a leading zero ('0') to be inserted between
#       left-hand padding and the formatting of the number if the leading
#       character of the result is not already a zero.
# (2)   The alternate form causes a leading '0x' or '0X' (depending on whether
#       the 'x' or 'X' format was used) to be inserted between left-hand
#       padding and the formatting of the number if the leading character of
#       the result is not already a zero.
# (3)   The alternate form causes the result to always contain a decimal point,
#       even if no digits follow it. The precision determines the number of
#       digits after the decimal point and defaults to 6.
# (4)   The alternate form causes the result to always contain a decimal point,
#       and trailing zeroes are not removed as they would otherwise be. The
#       precision determines the number of significant digits before and after
#       the decimal point and defaults to 6.
# (5)   The %r conversion was added in Python 2.0.  The precision determines
#       the maximal number of characters used.
# (6)   If the object or format provided is a unicode string, the resulting
#       string will also be unicode. The precision determines the maximal
#       number of characters used.
# (7)   See PEP 237.
#
# Since Python strings have an explicit length, %s conversions do not assume
# that '\0' is the end of the string.
# Changed in version 2.7: %f conversions for numbers whose absolute value is
# over 1e50 are no longer replaced by %g conversions.
# Additional string operations are defined in standard modules string and re.
"""


print """4. Try more format characters. %r is a very useful one. It's like saying
    "print this no mater what." """
name = 'Zed A. Shaw'
age = 35  # not a lie
height_inch = 74  # inches
inch_to_centimeter = 2.54
height_centimeter = height_inch * inch_to_centimeter
weight_pound = 180  # lbs
pound_to_kilogram = .4535923
weight_kilogram = weight_pound * pound_to_kilogram
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % height_inch
print "He's %r centimeters tall." % height_centimeter
print "He's %r pounds heavy." % weight_pound
print "He's %r kilograms heavy." % weight_kilogram
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are actually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height_inch, weight_pound, age + height_inch + weight_pound)
