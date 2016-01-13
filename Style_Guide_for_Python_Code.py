"""
PEP 0008 -- Style Guide for Python
PEP:            8
Title:          Style Guide for Python
Author:         Guido van Rossum <guido@python.org>,
                Barry Warsaw <barry@python.org>,
                Nick Coghlan <ncoghlan@gmail.com>
Status:         Active
Type:           Process
Created:        05-Jul-2001
Post-History:   05-Jul-2001, 01-Aug-2013

Contents

1. Introduction
2. A Foolish Consistency is the Hobgoblin of Little Minds
3. Code lay-out
    3.1 Indentation
    3.2 Tabs or Spaces?
    3.3 Maximum Line Length
    3.4 Blank Lines
    3.5 Source File Encoding
    3.6 Imports
4. String Quotes
5. Whitespace in Expressions and Statements
    5.1 Pet Peeves
    5.2 Other Recommendations
6. Comments
    6.1 Block Comments
    6.2 Inline Comments
    6.3 Documentation Strings
7. Version Bookkeeping
8. Naming Conventions
    8.1 Overriding Principle
    8.2 Descriptive: Naming Styles
    8.3 Prescriptive: Naming Conventions
        8.3.1 Names to Avoid
        8.3.2 Package and Modules Names
        8.3.3 Class Names
        8.3.4 Exception Names
        8.3.5 Global Variable Names
        8.3.6 Function Names
        8.3.7 Function and method arguments
        8.3.8 Method Names and Instance Variables
        8.3.9 Constants
        8.3.10 Designing for inheritance
    8.4 Public and internal interfaces
9. Programming Recommendations
    9.1 Function Annotations
References
Copyright


1. Introduction

This document gives coding conventions for the Python code comprising the
standard library in the main Python distribution. Please see the companion
informational PEP describing style guidelines for the C code in the C
implementation of Python [1].

This document and PEP 257 (Docstring Conventions) were adapted from Guido's
original Python Style Guide essay, with some additions from Barry's style
guide [2].

This style guide evolves over time as additional conventions are identified
and past conventions are rendered obsolete by changes int he language itself.

Many projects have their own coding style guidelines. In the event of any
conflicts, such project-specific guides take precedence for that project.


2. A Foolish Consistency is the Hobgoblin of Little Minds

One of Guido's key insights is tha code is read much more often than it is
written. Then guidelines provided here are intended to improve the
readability of code and make it consistent across the wide spectrum of
Python code. As PEP 20 says, "Readability counts".

A style guide is about consistency. Consistency with this style guide is
important. Consistency within a project is more important. Consistency
within one module or function is most important.

But most importantly: know when to be inconsistent--Sometimes the style
guide just doesn't apply. When in doubt, use your best judgement. Look at
other examples and decide what looks best. And don't hesitate to ask!

In particular: do not break backwards compatibility just to comply with this
PEP!

Some other good reasons to ignore a particular guideline:
    1. When applying the guideline would make the code less readable, even
    for someone who is used to reading code that follows this PEP.
    2. To be consistent with surrounding code that also breaks it (maybe for
    historic reasons) -- although this is also an opportunity to learn up
    someone else's mess (in true XP style).
    3. Because the code in question predates the introduction of the
    guideline and there is no other reason to be modifying that code.
    4. When the code needs to remain compatible with older versions of
    Python that don't support the feature recommended by the style guide.


3. Code lay-out

3.1 Indentation

Use 4 spaces per indentation level.

Continuation line should align wrapped elements either vertically using
Python's implicit line joining inside parentheses, brackets and braces,
or using a hanging indent [7]. When using a hanging indent the following
considerations should be applied; there should be no arguments on the first
line and further indentation should be used to clearly distinguish itself
as a continuation line.

Yes:

# Aligned with opening delimiter.
foo = long_function_name(ver_one, var_two,
                         var_three, var_four)

# More indentation include to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

No:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var-three,
    var_four):
    print(var_one)

The 4-space rule is optional for continuation lines.

Optional:

# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

When the conditional part of an if-statement is long enough to require that
it be written across multiple lines, it's worth nothing that the combination
of a two character keyword(i.e. if), plus a single space, plus an opening
parenthesis creates a natural 4-space indent for the subsequent lines of the
multi-line conditional. This can produce a visual conflict with the indented
suite of code nested inside the if-statement, which would also naturally be
indented to 4-spaces. This PEP takes no explicit position on how (or whether)
to further visually distinguish such conditional lines from the nested suite
inside the if-statement. Acceptable options in this situation include, but
are not limited to:

"""

print "The document named \"Style Guide for Python Code\" is important!"
