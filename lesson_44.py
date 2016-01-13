"""
Exercise 44: Inheritance Versus Composition
    In the fairy about heroes defeating evil villains there's always a dark
    forest of some kind. It could be a cave, a forest, another planet, just
    some place that everyone knows the hero shouldn't go. Of course, shortly
    after the villain is introduce you find out, yes, the hero has to go to
    that stupid forest to kill the bad guy. It seems the hero just keeps
    getting into situations that require him to risk his life in this evil
    forest.

    You rarely read fairly about the heroes who are smart enough to just
    avoid the whole situation entirely. You never hear a hero say, "Wait a
    minute, if I leave to make may fortunes on the high seas leaving
    Buttercup behind I could die and then she'd have to marry some ugle
    prince named Humperdink. Humperdink! I think I'll stay here and start
    a Farm Boy for Rent business." I he did that there'd be no fire swamp,
    dying, reanimation, sword fights, giants, or any kind of story really.
    Because of this, the forest in these stories seems to exist like a black
    hole that drags the hero in no matter what they do.

    In object-oriented programming, Inheritance is the evil forest.
    Experienced programmers know to avoid this evil because they know that
    deep inside the Dark Forest Inheritance is the Evil Queen Multiple
    Inheritance. She likes to eat software and programmers with her massive
    complexity teeth, chewing on the flesh of the fallen. But the forest is
    so powerful and so tempting that nearly every programmer has to go into
    it, and try to make it out alive with the Evil Queen's head before they
    can call themselves real programmers. You just can't resist the
    Inheritance Forest's pull, so you go in. After the adventure you learn
    to just stay out of that stupid forest and bring an army if you are ever
    forced to go in again.

    This is basically a funny way to say that I'm going to teach you
    something you should use carefully call Inheritance. Programmers who are
    currently in the forest battling the Queen will probably tell you have to
    go in. They say this because they need your help since what they've
    created is probably too much for them to handle. But you should always
    remember this:
        *****
        Most of the uses of inheritance can be simplified or replaced with
        composition, and multiple inheritance should be avoided at all costs.

What is Inheritance
    Inheritance is used to indicate that one class will get most or small of
    its features from a parent class. This happens implicity whenever you
    write class Foo(Bar), which says "Make a class Foo that inherits from
    Bar". When you do this, the language makes any action that you do on
    instances of Foo also work as if they were done to an instance of Bar.
    Doing this lets you put common functionality in the Bar class, then
    specialize that functionality in the Foo class as needed.

    When you are doing this kind of specialization, there are three ways that
    the parent and child classes car interact:
        1. Actions on the child imply an action on the parent.
        2. Actions on the child override the action on the parent.
        3. Actions on the child alter the action on the parent.

    I will now demonstrate each of these in order and show you code for them.
"""

"""
Implicit Inheritance
    First I will show you the implicit actions that happen when you define a
    function in the parent, but not in the child.
"""
# class Parent(object):
#     def implicit(self):
#         print "PARENT implicit()"
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()

"""
Override Explicity
    The problem with having functions called implicitly is sometimes you want
    the child to behave differently. In this case you want to override the
    function in the child, effectively replacing the functionality. To do
    this just define a function with the same name in Child. Here's an
    example:
"""
class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()