"""
Exercise 49: Making Sentences

What we should be able to get from our little game lexicon scanner is a
list that looks like this:

>>> from ex48 import lexicon
>>> lexicon.scan("go north")
[('verb', 'go'), ('direction', 'north')]
>>> lexicon.scan("kill the princess")
[('verb', 'kill'), ('stop', 'the'), ('noun', 'princess')]
>>> lexicon.scan("eat the bear")
[('verb', 'eat'), ('stop', 'the'), ('noun', 'bear')]
>>> lexicon.scan("open the door and smack the bear in the nose")
[('error', 'open'), ('stop', 'the'), ('error', 'door'), ('error', 'and'), ('error', 'smack'), ('stop', 'the'), ('noun', 'bear'), ('stop', 'in'), ('stop', 'the'), ('error', 'nose')]

Now let us turn this into something the game can work with, which would
be some kind of Sentence class.

If you remember grade school, a sentence can be a simple structure
like:
    Subject Verb Object

Obviously it gets more complex than that, and you probably did many
days of annoying sentence graphs for English class. What we want is
to turn the above lists of tuples into a nice Sentence object that
has subject, verb, and object.


Match and Peek

To do this we need four tools:
    1. A way to loop through the list of scanned words. That's easy.
    2. A way to "match" different types of tuples that we expect in
    our Subject Verb Object setup.
    3. A way to "peek" at a potential tuple so we can make some
    decisions.
    4. A way to "skip" things we do not care about, like stop words.
    5. A Sentence object to put the results in.


The Sentence Grammar

Before you can write the code you need to understand how a basic
English sentence grammar works. In our parser we want to produce a
Sentence object that has three attributes:
    Sentence.subject
        This is the subject of any sentence, but could default to
        "player" most of the time since a sentence of, "run north" is
        implying "player run north". This will be a noun.
    Sentence.verb
        This is the action of the sentence. In "run north" it would be
        "run". This will be a verb.
    Sentence.object
        This is another noun that refers to what the verb is done on.
        In our game we separate out directions which would also be
        objects. In "run north" the word "north" would be the object.
        In "hit bear" the word "bear" would be the object.
Our parser then has to use the functions we described and given a
scanned sentence, convert it into List of Sentence objects to match the
input.


A Word On Exceptions

You briefly learned about exceptions but not how to raise them. This
code demonstrates how to do that with the ParserError at the top.
Notice that it uses classes to give it the type of Exception. Also
notice the use of the raise keyword to raise the exception.

In your tests, you will want to work with these exceptions, which I'll
show you how to do.


The Parser Code

If you want an extra challenge, stop right now and try to write this
based on just my description. If you get stuck you can come back and
see how I dit it, but trying to implement the parser yourself is good
practice. I will now walk through the code so you can enter it into
your ex48/parser.py. We start the parser with the exception we need for
a parsing error:

# class ParserError(Exception):
#     pass

This is how you make your own ParserError exception class you can
throw. Next we need the Sentence object we'll create:

# class Sentence(object):
#     def __init__(self, subject, verb, obj):
#         # remember we take ('non', 'princess') tuples and convert them
#         self.subject = subject[1]
#         self.verb = verb
#         self.obj = obj

There's nothing special about this code so far. You're just making
simple classes.

In our description of the problem we need a function that can peek at
a list of words and return what type of word it is:

# def peek(word_list):
#     if word_list:
#         word = word_list[0]
#         return word[0]
#     else:
#         return None

We need this function because we'll have to make decisions about what
kind of sentence we're dealing with based on what the next word is,
and then we can call another function to consume that word and carry
on.

To







"""