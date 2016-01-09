# coding=utf-8
"""
Exercise 11: Asking Questions
    Most of what software does is the following:
        1. Take some kind of input from a person.
        2. Change it.
        3. Print out something to show how it changed.
"""
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)


"""
Study Drills
    1. Go online and find out what Python raw_input() does.
    2. Can you find other ways to use it? Try some of the samples you find.
    3. Write another "form" like this to ask some other questions.
    4. Related to escape sequence, try to find out why the last line has
    '6\'2"' with tha \' sequence. See how the single-quote needs to be
    escaped because otherwise would end the string?
"""
# example one
raw_input_A = raw_input("raw_input: ")
print raw_input_A

input_A = input("input: ")
print input_A

# example two
raw_input_B = raw_input("raw_input:")
print raw_input_B
print type(raw_input_B)

input_B = input("input: ")
print input_B
print type(input_B)

"""
例子 1 可以看到：这两个函数均能接收 字符串 ，但
    raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
    而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输
    入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。

例子 2 可以看到：
    raw_input() 将所有输入作为字符串看待，返回字符串类型。
    而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的
    类型（ int, float ）；

    同时在例子 1 知道，input() 可接受合法的 python 表达式，
    举例：input( 1 + 3 ) 会返回 int 型的 4 。
"""