"""
Exercise 25: Even More Practice
    We're going to do some more practice involving functions and variables
    to make sure you know them well. This exercise should be straightforward
    for you type in, break down, and understand.

    However, this exercise is a little different. You won't be running it.
    Instead you will import it into Python and run the functions yourself.
"""


def break_words(stuff):
    """This function will break up words for us. """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words. """
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

"""

In[4]: import lesson_25
In[5]: sentence = "All good things come to those who wait."
In[6]: words = lesson_25.break_words(sentence)
In[7]: words
Out[7]: ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
In[8]: sorted_words = lesson_25.sort_words(words)
In[9]: sorted_words
Out[9]: ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
In[10]: lesson_25.print_first_word(words)
All
In[11]: lesson_25.print_last_word(words)
wait.
In[12]: lesson_25.print_first_word(sorted_words)
All
In[13]: lesson_25.print_last_word(sorted_words)
who
In[14]: sorted_words
Out[14]: ['come', 'good', 'things', 'those', 'to', 'wait.']
In[15]: sorted_words = lesson_25.sort_sentence(sentence)
In[16]: sorted_words
Out[16]: ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
In[17]: lesson_25.print_first_and_last(sentence)
All
wait.
In[18]: lesson_25.print_first_and_last_sorted(sentence)
All
who
In[19]: help(lesson_25)
Out[19]...
"""