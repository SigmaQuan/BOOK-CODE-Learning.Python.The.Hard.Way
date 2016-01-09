"""
Exercise 26: Congratulations, Take a rest.
    You are almost done with the first of the book. The second half is where
    things get interesting. You will learn logic and be able to do useful
    things like make decision.

    Before you continue, I have a quiz for you. This quiz will be very hard
    because it requires you to fix someone else's code. When you are a
    programmer you often have to deal with other programmer's code, and also
    with their arrogance. Programmers will very frequently claim that their
    code is perfect.

    These programmers are stupid people who care little for others. A good
    programmer assumes, like a good scientist, that there's always some
    probability their code is wrong. Good programmers start from the premise
    that their software is broken and then work to rule out all possible
    ways it could be wrong before finally admitting that maybe it really is
    the other guy's code.

    In this exercise, you will practice dealing with a bad programmer by
    fixing a bad programmer's code. I have poorly copied Exercise 24 and 25
    into a file and removed random characters and added flaws. Most of the
    errors are things Python will tell you, while some of them are math
    errors you should find. Others are formatting errors of spelling mistakes
    in the strings.

    All of these error are very common mistakes all programmers make. Even
    experienced ones.

    Your job in this exercise is to correct this file. Use all of your skills
    to make this file better. Analyze it first, maybe printing it out to edit
    like you would a school term paper. Fix each flaw and keep running it
    and fixing it until the script runs perfectly. Try not to get help. If
    you get stuck take a break and come back to it later.

    Even if this takes days to do, bust through it and make it right.

    The point of this exercise isn't to type it in but to fix an existing
    file. To do that, you must go to this site:
        http://learnpythonthehardway.org/book/exercise26.txt

    Copy-paste the code into a file named lesson_26.py. This is the only time
    you are allowed to copy-paste.
"""


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explnation
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)


sentence = "All god\tthings come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)

