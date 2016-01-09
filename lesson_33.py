"""
Exercise 33: While Loops

"""

def while_loop(max):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


numbers = while_loop(6)

print "The numbers:"

for num in numbers:
    print num
