"""
Exercise 52: The Start of Your Web Game

We're coming to the end of the book, and in this exercise I'm going to
really challenge you. When you're done, you'll be a reasonably
competent Python beginner. You'll still need to go through a few more
books and write a couple more project, but you'll have the skills to
complete them. The only thing in your way will be time, motivation,
and resources.

In this exercise, we won't make a complete game, but instead we'll make
an "engine" that can run the game from exercise 47 in the browser. This
will involve refactoring exercise 43, mixing in the structure from
exercise 47, adding automated tests, and finally creating a web engine
that can run the games.

This exercise will be huge, and I predict you could spend anywhere from
a week to months on it before moving on. It's best to attack it in
little chunks and do a bit a night, taking your time to make everything
work before moving on.


Refactoring the Exercise 43 Game

You've been altering the gothonweb project for two exercise and you'll
do it one more time in this exercise. The skill you're learning is
called "refactoring", or as I like to call it, "fixing stuff".
Refactoring is a term programmers use to describe the progress of
taking old code, and changing it to have new features or just to clean
it up. You've been doing this without even knowing it, as it's second
nature to building software.

What you'll do in this part is take the ideas from exercise 47 of a
testable "map" of Rooms, and the game from exercise 43, and combine
them together to create a new game structure. It will have the same
content, just "refactored" to have a better structure.

The first step is to grab the code from ex47/game.py and copy it to
gothonweb/map.py and copy the tests/ex47_tests.py file to
tests/map_tests.py and run nosetests again to make sure it keeps
working.

[***NOTE]
    From now on I won't show you the output of a test run just assume
    that you should be doing it and it'll look like the above unless
    you have an error.

Once you have code from exercise 47 copied over, it's time to refactor
it to have the exercise 43 map in it. I'm going to start off by laying
down the basic structure, and then you'll have an assignment to make
the map.py file and the map_test file complete.

Lay out the basic structure of the map using the Room class as it is
now:


"""