# coding=utf-8
"""
Exercise 14: Prompting and Passing
    Let's do one exercise that uses argv and raw_input together to ask user
    something specific.
"""
# from sys import argv
#
# script, user_name = argv
# prompt = '> '
#
# print "Hi %s, I'm the %s script. " % (user_name, script)
# print "I'd like to ask you a few questions. "
# print "Do you like me %s? " % user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s? " % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)


"""
Study Drills
    1. Find out what Zork and Adventure were. Try to find a copy and play it.
    # Zork I是电子游戏历史上最早的一款文字冒险游戏，是Colossal Cave Adventure的一个早
    # 期后继。Zork的首个版本由Tim Anderson、Marc Blank、Bruce Daniels和Dave
    # Lebling于1977至79年间在DEC PDP-10电脑上、以MDL程式语编写。他们四人全是麻省理
    # 工动力模型组的成员。
    2. Change the prompt variable to something else entirely.
    3. Add another argument and use it in your script, the same way you did
    in the previous exercise with first, second = ARGV.
    4. Make sure you understand how I combined a \"\"\" style multi-line
    string with the % format activator as the last print.
"""

from sys import argv

script, user_name, code = argv
prompt = '>> '

while (user_name != "qzb") | (code != "123"):
    print "user name and code are not matching! " + \
          "Please re-input your name and code"
    user_name = raw_input(prompt)
    if user_name == "q":
        break
    code = raw_input(prompt)

print "Hi %s, I'm the %s script. " % (user_name, script)
print "I'd like to ask you a few questions. "
print "Do you like me %s? " % user_name
likes = raw_input(prompt)

print "Where do you live %s? " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
