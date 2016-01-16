"""
Exercise 46: A Project Skeleton

This will be where you start learning how to set up a good project
"skeleton" directory. This skeleton directory will have all the basics
you need to get a new project up and running. It will have your project
layout, automated tests, modules, and install scripts. When you go to
make a new project, just copy this directory to a new name and edit the
files to get started.


Installing Python Packages

Before you can begin this exercise you need to install some software
for Python by using a tool called "pip" to install new modules. Here's
the problem though. You are at a point where it's difficult for me to
help you do that and keep this book sane and clean. There are so many
ways to install software on so many computers that I'd have to spend
10 pages walking you through every step, and let me tell you I am a
lazy guy.

Rather than tell you how to do it exactly, I'm going to tell you what
you should install, and then you tell you to watch the video that
accompanies this exercise and follow along. You will have to struggle
with this part of the exercise though as giving accurate and current
installation instructions is tricky. Computers change frequently so
you may have to do some research if you get stuck.

Install the following Python packages:
    1. pip from http://pypi.python.org/pypi/pip
    2. distribute from http://pypi.python.org/pypi/distribute
    3. nose from http://pypi.python.org/pypi/nose/
    4. virtualenv from http://pypi.python.org/pypi/virtualenv

Do not just download these packages and install them by hand. Instead
see how other people recommend you install these packages and use them
for your particular system. The process will be different for most
versions of Linux, OSX, and definitely different for Windows.

I am warning you; this will be frustrating. In the business we call
this "yak sharing". Yak sharing is any activity that is mind
numblingly, irritatingly boring and tedious that you have to do before
you can do something else that's more fun. You want to create cool
Python projects, but you can't do that until you set up a skeleton
directory, but you can't set up a skeleton director until you install
some packages, but you can't install packages until you install package
installers and you can't install package installers until you figure
out how your system installs software in general, and so on.

Struggle through this anyway. Consider it your trial by annoyance to
get into the programmer club. Every programmer has to do these
annoying tedious tasks before they can do something cool.

**[NOTE]
    Sometimes the Python installer does not add the
      "c:\Python27\Script"
    to the system PATH. If this is the case for you, go back and add
    this to the path just like you did for "c:\Python27" in Exercise 0
    with:
      [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\Scripts", "User")


Creating the Skeleton Project Directory

First, create the structure of your skeleton directory with these
commands:
    $ mkdir projects
    $ cd projects/
    $ mkdir skeleton
    $ cd skeleton
    $ mkdir bin NAME tests docs

I use a directory named projects to store all the various things I'm
working on. Inside that directory I have may skeleton directory that
I put the basis of my projects into. The directory NAME will be
renamed to whatever you are calling your project's main module when
you use the skeleton.

Next we need to set up some initial files. Here's how you do that on
Linux/OCX:
    $ touch NAME/__init__.py
    $ touch tests/__init__.py

Here's the same thing on Windows PowerShell:
    $ new-item -type file NAME/__init__.py
    $ new-item -type file tests/__init__.py

That creates an empty Python module directories we can put our code in.
Then we need to create a setup.py file we can use to install our
project later if we want:

# try:
#     from setuptools import setup
# except ImportError:
#     from distutils.core import setup
#
# config = {
#     'description': 'My project',
#     'author': 'Zhibin Quan',
#     'url': 'URL to get it at.',
#     'download_url': 'Where to download it.',
#     'author_email': 'quan.zhibin@gmail.com',
#     'version': '0.1',
#     'install_requires': ['nose'],
#     'packages': ['NAME'],
#     'scripts': [],
#     'name': 'projectname'
# }
#
# setup(**config)

Edit this file so that it has your contact information and is ready to
go for when you copy it.

Finally you will want a simple skeleton file for test named
tests/NAME_tests.py:


Final Directory Structure

When you are done setting all of this up, your directory should look
like mine here:
    skeleton/
        NAME/
            __init__.py
        bin/
        docs/
        setup.py
        tests/
            NAME_tests.py
            __init__.py

And from now on, you should run your commands from that work with this
directory from this point. If you can't do ls -R and see this same
structure, then you are in the wrong place. For example, people
commonly go into the tests/ directory to run files there, which don't
work. To run your application's tests, you would need to be above test/
and this location I have above. So, if you try this:
    $ cd tests/    # WRONG! WRONG! WRONG!
    $ nosetests

Then that is wrong! You have to be above tests, so assuming you made
this mistake, you would fix it by doing this:
    $ cd ..        # get out of tests/
    $ ls           # CORRECT! you are now in the right spot

    $ nosetests

Remember this because people make this mistake quite frequently.


Testing Your Setup

After you get all that installed you should be able to do this:
    $ nosetests

I'll explain what this nosetests thing is doing the next exercise, but
for now if you do not see that, you probably got something wrong. Make
sure you put __init__.py files in your NAME and tests directories and
make sure you got tests/NAME_tests.py right


*****
Using the Skeleton

You are now done with most of your yak shaving. Whenever you want to
start a new project, just do this:
    1. Make a copy of your skeleton directory. Name it after your new
    project.
    2. Rename (move) the NAME directory to be the name of your project
    or whatever you want to call your root module.
    3. Edit your setup.py to have all the information for your project.
    4. Rename tests/NAME_tests.py to also have your module name.
    5. Double check it's all working by using nosetests again.
    6. Start coding.


Required Quiz

This exercise doesn't have Study Drills but a quiz you should complete:
    1. Read about how to use all of the things you installed.
    2. Read about the setup.py file and all it has to offer. Warning:
        it is not a very well-written piece of software, so it will be
        very strange to use.
    3. Make a project and start putting code into the module, then get
    the module working.
    4. Put a script in the bin directory that you can run. Read about
    how you can make a Python script that's runnable for your system.
    5. Mention the bin script you created in your setup.py so that it
    gets installed.
    6. Use your setup.py to install your own module and make sure it
    works, then use pip to uninstall it.
"""