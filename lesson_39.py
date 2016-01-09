"""
Exercise: 39: Dictionaries, Oh Lovely Dictionaries

"""
# # create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }
#
# # create a basic set of state and some cities in them
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonille'
# }
#
# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
#
# # print out some cities
# print '-' * 10
# print "NY State has: ", cities['NY']
# print "OR State has: ", cities['OR']
#
# # print some states
# print '-' * 10
# print "Michigan's abbreviation is: ", states['Michigan']
# print "Florida's abbreviation is: ", states['Florida']
#
# # do it by using the state then cities dict
# print '-' * 10
# print "Michigan has: ", cities[states['Michigan']]
# print "Florida has: ", cities[states['Florida']]
#
# # print every state abbreviation
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s is abbreviated %s" % (state, abbrev)
#
# # print every city in state
# print '-' * 10
# for abbrev, city in cities.items():
#     print "%s has the city %s" % (abbrev, city)
#
# # now do both at the same time
# print '-' * 10
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has city %s" % (
#         state, abbrev, cities[abbrev]
#     )
#
# print '-' * 10
# # safely get a abbreviation by state that might not be there
# state = states.get('Texas')
#
# if not state:
#     print "Sorry, no Texas."
#
# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city


"""
What Dictionaries Can Do
    Dictionaries are another example of a data structure, and like lists
    they are one of the most commonly used data structures in programming.
    A dictionary is used to map or associate things you want to store to
    keys you need to get them. Again, programmers don't use a term like
    "dictionary" for something that doesn't work like an actual dictionary
    full of words, so let's use that as our real world example.

    Let's say you want to find out what the word "Honorificabilitudinitatibus"
    means. Today you would simply copy-paste that word into a search engine
    and then find out the answer, and we would say a search engine is like a
    really huge super complex version of the Oxford English Dictionary (OED).
    Before search engines what you would do is this:
        1. Go to your library and get "the dictionary". Let's say it's the
        OED.
        2. You know "honorificabilitudinitatibus" starts with the letter
        'H' so you look on the side of the book for the little tab that has
        'H' on it.
        3. Then you'd skim the pages until you are close to where "hon"
        started.
        4. Then you'd skim a few more pages until you found
        "honorificabilitudinitatibus" or hit the beginning of the "hp" words
         and realize this word isn't in the OED.
        5. Once you found the entry, you'd read the definition to figure out
        what it means.

    This process is nearly exactly the way a dict works, and you are
    basically "mapping" the word "nonorificabilitudinitatibus" to its
    definition. A dict in Python is just like a dictionary in the real world
    like the OED.
"""

import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."


# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


"""
When to Use Dictionaries or Lists
    As I mentioned in Exercise 38, lists have specific properties that help
    you contain and organize things that need to be in a list structure.
    Dictionaries are the same, but the properties of a dict are different
    than lists because they work with mapping keys to values. That means
    you use a dictionary when:
        1. You have to retrieve thing based on some identifier, like names,
        address, or anything that can be a key.
        2. You don't need things to be in order. Dictionaries do not
        normally have any notion of order, so you have to use a list for that.
        3. You are going to be adding and removing elements and their keys.
    This means that if you have to use a non-numeric key, use a dict. If you
    need things in order, use a list.
"""