"""
Exercise 50: Your First Website

These final three exercises will be very hard and you should take your
time with them. In this first one you'll build a simple web version of
one of your games. Before you attempt this exercise you must have
completed Exercise 46 successfully and have a working pip installed
such that you can install packages and know how to make a skeleton
project directory. If you don't remember how to do this, go back to
Exercise 46 and do it all over again.
Installing lpthw.web

Before creating your first web application, you'll first need to
install the "web framework" called lpthw.web. The term "framework"
generally means "some package that makes it easier for me to do
something." In the world of web applications, people create "web
frameworks" to compensate for the difficult problems they've
encountered when making their own sites. They share these common
solutions in the form of a package you can download to bootstrap your
own projects.

In our case, we'll be using the lpthw.web framework, but there are
many, many, many others you can choose from. For now, learn lpthw.web,
then branch out to another one when you're ready (or just keep using
lpthw.web since it's good enough). Using pip, install lpthw.web:
    $ sudo pip install lpthw.web

This will work on linux and Mac OSX computers, but on Windows just drop
the sudo part of the pip install command and it should work. If not, go
back to Exercise 46 and make sure you can do it reliably.

[WARNING]
    Other python programmers will warn you that lpthw.web is just a
    fork of another web framework called web.py and that web.py has
    too much "magic". If they say this, point out to them that
    Google App Engine originally used web.py and not a single python
    programmer complained that it hard too much magic, because they
    all worked at Google. If it's good enough for Google, then it's
    good enough for you to get started. Then, just get back to learning
    to code and ignore their goal of indoctrination over education.


Make a Simple "Hello World" Project

Now you're going to make an initial very simple "Hello World" web
application and project directory using lpthw.web. First, make your
project directory.
    $ cd projects
    $ mkdir gothonweb
    $ cd toghonweb
    $ mkdir bin gothonweb tests docs templates
    $ touch gothonweb/__init__.py
    $ touch tests/__init__.py

You'll be taking the game from Exercise 43 and making it into a web
application, so that's why you're calling it gothonweb. Before you
do that, we need to create the most basic lpthw.web application
possible. Put the following into bin/app.py:
#
# import web
#
# urls = (
#     '/', 'index'
# )
#
# app = web.application(urls, globals())
#
# render = web.template.render('templates/')
#
#
# class index(object):
#     def GET(self):
#         greeting = "Hello World"
#         return greeting
#
#
# if __name__ == "__main__":
#     app.run()
#

Then run the application like this:
    $ python bin/app.py
    http://0.0.0.0:8080/

However, if you did this:
    $ cd bin/ # WRONG! WRONG! WRONG!
    $ python app.py  # WRONG! WRONG! WRONG!

Then you are doing it wrong. In all python projects you do not cd into a lower directory to run things. You stay at the top and cun everything from there so that all of the system can access all the modules and files. Go reread Exercise 46 to understand a project layout and how to use it if you did this. Finally, use your web brower and go to

















"""
