"""
Exercise 24: More Practice

"""

print "Let's practice everthing."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (
    beans, jars, crates
)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

"""
Study Drills
    1. Make sure to do your checks: read it backward, read it out loud, and
    put comments above confusing parts.
    2. Break the file on purpose, then run it to see what kinds of errors
    you get. Make sure you can fix it.
"""