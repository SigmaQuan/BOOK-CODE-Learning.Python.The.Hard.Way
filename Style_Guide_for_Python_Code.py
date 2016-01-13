# coding=utf-8
"""
https://www.python.org/dev/peps/pep-0008/#introduction
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

This document gives coding conventions for the Python code comprising
the standard library in the main Python distribution. Please see the
companion informational PEP describing style guidelines for the C code
in the C implementation of Python [1].

This document and PEP 257 (Docstring Conventions) were adapted from
Guido's original Python Style Guide essay, with some additions from
Barry's style guide [2].

This style guide evolves over time as additional conventions are
identified and past conventions are rendered obsolete by changes in
the language itself.

Many projects have their own coding style guidelines. In the event of
any conflicts, such project-specific guides take precedence for that
project.


2. A Foolish Consistency is the Hobgoblin of Little Minds

One of Guido's key insights is tha code is read much more often than
it is written. Then guidelines provided here are intended to improve
the readability of code and make it consistent across the wide
spectrum of Python code. As PEP 20 says, "Readability counts".

A style guide is about consistency. Consistency with this style guide
is important. Consistency within a project is more important.
Consistency within one module or function is most important.

But most importantly: know when to be inconsistent--Sometimes the style
guide just doesn't apply. When in doubt, use your best judgement. Look
at other examples and decide what looks best. And don't hesitate to
ask!

In particular: do not break backwards compatibility just to comply with
this PEP!

Some other good reasons to ignore a particular guideline:
    1. When applying the guideline would make the code less readable,
    even for someone who is used to reading code that follows this PEP.
    2. To be consistent with surrounding code that also breaks it (
    maybe for historic reasons) -- although this is also an opportunity
    to learn up someone else's mess (in true XP style).
    3. Because the code in question predates the introduction of the
    guideline and there is no other reason to be modifying that code.
    4. When the code needs to remain compatible with older versions of
    Python that don't support the feature recommended by the style
    guide.


3. Code lay-out

3.1 Indentation

Use 4 spaces per indentation level.

Continuation line should align wrapped elements either vertically using
Python's implicit line joining inside parentheses, brackets and braces,
or using a hanging indent [7]. When using a hanging indent the
following considerations should be applied; there should be no
arguments on the first line and further indentation should be used to
clearly distinguish itself as a continuation line.

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

When the conditional part of an if-statement is long enough to require
that it be written across multiple lines, it's worth nothing that the
combination of a two character keyword(i.e. if), plus a single space,
plus an opening parenthesis creates a natural 4-space indent for the
subsequent lines of the multi-line conditional. This can produce a
visual conflict with the indented suite of code nested inside the
if-statement, which would also naturally be indented to 4-spaces. This
PEP takes no explicit position on how (or whether) to further visually
distinguish such conditional lines from the nested suite inside the
if-statement. Acceptable options in this situation include, but are
not limited to:

# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

The closing brace/bracket/parenthesis on multi-line constructs may
either line up under the first non-whitespace character of the last
line of list, as in:

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

or it may be lined up under the first character of the line that starts
the multi-line construct, as in:

my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

3.2 Tabs or Spaces?

Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is
already indented with tabs.

Python 3 disallows mixing the use of tabs and spaces for indentation.

Python 2 code indented with a mixture of tabs ans spaces should be
converted to using spaces exclusively.

When invoking the Python 2 command line interpreter wit -t option, it
issues warnings about code that illegally mixes tabs and spaces. When
using -tt these warmings become errors. These options are highly
recommend!

3.3 Maximum Line Length

Limit all lines to a maximum 79 characters.

For flowing long blocks of text with fewer structural restrictions
(docstring or comments), the line length should be limited to 72
characters.

Limiting the required editor window width makes it possible to have
several files open side-by-side, and works well when using code review
tools that present the two versions in adjacent columns.

The default wrapping in most tools disrupts the visual structure of the
code, making it more difficult to understand. The limits are chosen to
avoid wrapping in editors with the window width set to 80, even if the
tool places a marker glyph in the final column when wrapping lines.
Some web based tools may not offer dynamic line wrapping at all.

Some teams strongly prefer a longer line length. For code maintained
exclusively or primarily by a team that can reach agreement on this
issue, it is okay to increase the nominal line length from 80 to 100
characters ( effectively increasing the maximum length to 99
characters), provided that comments and docstrings are still wrapped
at 72 characters.

The Python standard library is conservative and requires limiting
lines to 79 characters (and docstrings/comments to 72). *****

The preferred way of wrapping long lines is by using Python's implied
line continuation inside parentheses, brackets and braces. Long lines
can be broken over multiple lines by wrapping expressions in
parentheses. These should be used in preference to using a backslash
for line continuation.

Backslashes may still be appropriate at times. For example, long,
multiple with - statement cannot use implicit continuation, so
backslashes are acceptable:

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/you/being/written', 'w') as file_2:
    file_w.write(file_1.read())

(See the previous discussion on multi-line if-statements for further
thoughts on the indentation of such multi-line with-statements.)

Another such case is with assert statements.

Make sure to indent the continued line appropriately. The preferred
place to break around a binary operator is after the operator, not
before it. Some examples:

class Rectangle(Blob):
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if(width == 0 and height == 0 and
                color == 'red' and emphasis == 'strong' or
                highlight > 100):
            raise ValueError("sorry, you lose")
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blog.__init__(self, width, height,
                      color, emphasis, highlight)

3.4 Blank Lines

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank
line.

Extra blank lines may be used (sparingly) to separate groups of
related functions. Bland lines may be omitted between a bunch of
related one-liners (e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.

Python accepts the control-L (i.e. ^L) form feed character as
whitespace; Many tools treat these characters as page separators, so
you may use them to separate pages of related sections of your file.
Note, some editors and web-based code viewers may not recognize
control-L as a form feed and will show another glyph in its place.


3.5 Source File Encoding

Code in the core Python distribution should always use UTF-8 (or ASCLL
in Python 2).

Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have
an encoding declaration.

In the standard library, non-default encoding should be used only for
test purposes or when a comment or docstring needs to mention an author
name that contains non-ASCII characters; otherwise, using \ x, \u, \U,
or \N escapes is the preferred way to include non-ASCII data in string
literals.

For Python 3.0 and beyond, the following policy is prescribed for the
standard library (see PEP 3131)： All identifiers in the Python standard
library MUST use ASCII-only identifiers, and SHOULD use English words
wherever feasible (in many cases, abbreviations and technical terms are
used which aren't English). In addition, string literals and comments.
must also be in ASCII. The only exceptions are (a) test cases testing
the non-ASCII features, and (b) names of authors. Authors whose names
are not based on the latin alphabet MUST provide a latin
transliteration of their names.

Open source projects with a global audience are encouraged to adopt a
similar policy.


3.6 Imports

*Imports should usually be on separate lines, e.g:

 Yes: import os
      import sys

 No:  import sys, os

It's okay to say this though:

 from subprocess import Popen, PIPE

*Imports are always put at the top of the file, just after any modules
comments and docstrings, and before modules globals and constants.

Imports should be grouped in the following order:
    1. standard library imports
    2. related third party imports
    3. local application/library specific imports

Put any relevant __all__ specification after the imports.

*Absolute imports are recommended, as they are usually more readable
and tend to be better behaved (or at least give better error messages)
if the import system is incorrectly configured (such as when a
directory inside a package ends up on sys.path):

 import mypkg.sibling
 from mypkg import sibling
 from mypkg.sibling import example

However, explicit relative imports are an acceptable alternative to
absolute imports, especially when dealing with complex package
layouts where using absolute imports would be unnecessarily verbose:

    from . import sibling
    from .sibling import example

Standard library code should avoid complex package layouts and always
use absolute imports.

Implicit relative imports should never be used and have been removed
in Python 3.

*When importing a class from a class-containing module, it's usually
okay to spell this:

 from myClass import MyClass
 from foo.bar.yourclass import YourClass

If this spelling causes local name clashes, then spell them

 import myclass
 import foo.bar.yourclass

and use "myclass.MyClass" and "foo.bar.yourclass.YourClass".

*Wildcard imports (from <modules import *) should be avoided, as they
make it unclear which names are present in the namespace, confusing
both readers and many automated tools. These is one defensible use
case for a wildcard import, which is to republish an internal
interface as part of a public API (for example, overwriting a pure
Python implementation of an interface with the definitions from an
optional accelerator module and exactly which definitions will be
overwritten isn't known in advance).

When republishing names this way, the guidelines below regarding public
and internal interfaces still apply.


4. String Quotes

In Python, single-quote strings and double-quoted strings are the same.
This PEP does not make a recommendation for this. Pick a rule and stick
to it. When a string contains single or double quote characters,
however, use the other one to avoid backslashes in the string. It
improves readability.

For triple-quoted strings, always use double quote characters to be
consistent with docstring convention in PEP 257.


5. Whitespace in Expressions and Statements

5.1 Pet Peeves

Avoid extraneous whitespace in the following situations:

*Immediately inside parentheses, brackets or braces.

 Yes: spam(ham[1], {eggs: 2})
 No:  spam( ham[ 1 ], { eggs: 2 } )

*Immediately before a comma, semicolon, or colon:

 Yes: if x == 4: print x, y; x, y = y, x
 No:  if x == 4 : print x , y ; x , y = y , x

*However, in a slice the colon acts like a binary operator, and should
have equal amounts on either side (treating it as the operator with the
lowest priority). In an extended slice, both colons must have the same
amount of spacing applied. Exception: when a slice parameter is
omitted, the space is omitted.

Yes:
 ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
 ham[lower:upper], ham[lower:upper:], ham[lower::step]
 ham[lower+offset : upper+offset]
 ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
 ham[lower + offset : upper + offset]

No:
 ham[lower + offset:upper + offset]
 ham[1: 9], ham[1 :9], ham[1:9 :3]
 ham[lower : : upper]
 ham[ : upper]

*Immediately before the open parenthesis that starts the argument list
of a function call:

 Yes: spam(1)
 No:  spam (1)

*Immediately before the open parenthesis that starts an indexing or
slicing:

 Yes: dct['key'] = lst[index]
 No: dct ['key'] = lst [index]

*More than one space around an assignment (or other) operator to align
it with another.

 Yes:
 x = 1
 y = 2
 long_variable = 3

 No:
 x             = 1
 y             = 2
 long_variable = 3

5.2 Other Recommendations

*Avoid trailing whitespace anywhere. Because it's usually invisible,
it can be confusing: e.g. a backslash followed by a space and a newline
does not count as a line continuation marker. Some editors don't
preserve it and many projects (like CPython ifself) have pre-commit
hooks that reject it.

*Always surround these binary operators with a single space on either
side:
    assignment ( = ),
    augmented assignment ( += , -= etc.),
    comparisons
     ( == , < , > , != , <> , <= , >= , in , not in , is , is not),
    Booleans (and , or , not ).

*If operators with different priorities are used, consider adding
whitespace around the operators with the lowest priority (ies). Use
your own judgment; however, never use more than one space, and always
have the same amount of whitespace on both sides of a binary operator.

Yes:
 i = i + 1
 submitted += 1
 x = x*2 - 1
 hypot2 = x*x + y*y
 c = (a+b) * (a-b)

No:
 i=i+1
 submitted +=1
 x = x * 2 -1
 hypot2 = x * x + y * y
 c = (a + b) * (a - b)

*Don't use spaces around the = sign when used to indicate a keyword
argument or a default parameter value.

Yes:
 def complex(real, imag=0.0):
    return magic(r=real, i=imag)

No:
 def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

*Function annotations should use the normal rules for colons and always
have spaces around the -> arrow if present. (See Function Annotations
below for more about function annotations.)

Yes:
 def munge(input: AnyStr): ...
 def munge() -> AnyStr: ...

No:
 def munge(input:AnyStr): ...
 def munge()->AnyStr: ...

*When combining an argument annotation with a default value, use spaces
around the = sign (but only for those arguments that have both an
annotation and a default).

Yes:
 def munge(seq: AnyStr = None): ...
 def munge(input: AnyStr, seq: AnyStr = None, limit=1000): ...

No:
 def munge(seq: AnyStr=None): ...
 def munge(input: AnyStr, limit = 1000): ...

*Compound statements (multiple statements on the same line) are
generally discouraged.

Yes:
 if foo == 'blash':
    do_blah_thing()
 do_one()
 do_two()
 do_three()

Rather not:
 if foo == 'blah': do_blah_thing()
 do_one(); do_two(); do_three()

*While sometimes it's okay to put an if/for/while with a small body on
the same line, never do this for multi-clause statements. Also avoid
folding such long lines!

Rather not:
 if foo == 'blah': do_blah_thing()
 for x in lst: total += x
 while t < 10: t = delay()

Definitely not:
 if foo == 'blah': do_blah_thing()
 else: do_not_blah_thing()

 try: something()
 finally: cleanup()

 do_one(); do_two(); do_three(long, argument,
                              lis, like, this)
 if foo == 'blah': one(); two(); three()


6. Comments

Comments that contradict the code are worse than no comments. Always
make a priority of keeping the comments up-to-date when the code
changes!

Comments should be complete sentences. If a comment is a phrase or
sentence, its first word should be capitalized, unless it is an
identifier that begins with a lower case letter (never alter the case
of identifiers!).

If a comment is short, the period at the end can be omitted. Block
comments generally consist of one or more paragraphs built out of
complete sentence, and sentence should end in a period.

You should use two spaces after a sentence-ending period.

When writing English, follow Strunk and White.

Python coders from non-English speaking countries: please write your
comments in English, unless you are 120% sure that the code will
never be read by people who don't speak you language.

6.1 Block Comments

Block comments generally apply to some (or all) code that follows them,
and are indented to the same level as that code. Each line of a block
comment starts with a # and a single space (unless it is indented text
inside the comment).

Paragraphs inside a block comment are separated by a line containing a
single #.

6.2 Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline
comments should be separated by at least two spaces from the statement.
They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they state
the obvious. Don't do this:

 x = x + 1            # Increment x

But sometimes, this is useful:

 x = x + 1            # Compensate for border

6.3 Documentation Strings

Conventions for writing good documentation strings (a.k.a. "docstring")
are immortalized in PEP 257. https://www.python.org/dev/peps/pep-0257

*Write docstrings for all public modules, functions, classes, and
methods. Docstrings are not necessary for non-public method, but you
should have a comment that describes what the method does. This
comment should appear after the def line.

*PEP 257 describes good docstring conventions. Notes that most
importantly, the \"\"\" that ends a multi-line docstring should be on
a line by itself, e.g.:
 \"\"\"Return a foobang

 Optional plotz says to frobnicate the bizbaz first.
 \"\"\"

*For one liner docstrings, please keep the closing \"\"\" on the same
line.


7. Version Bookkeeping
If you have to have Subversion, CVS, or RCS crud in your source file,
do it as follows.
 __version__ = "$Revision$"
 # $Source$

These lines should be included after the module's docstring, before any
other code, separated by a blank line above and below.


8. Naming Conventions

The naming conventions of Python's library are a bit of a mess, so we
will never get this completely consistent -- nevertheless, here are
the currently recommended naming standards. New modules and packages
(including third party frameworks) should be written to these standards,
but where an existing library has a different style, internal
consistency is preferred.

8.1 Overriding Principle

Names that are visible to the user as public parts of the API should
follow conventions that reflect usage rather than implementation.

8.2 Descriptive: Naming Styles

These are a lot of different naming styles. It helps to be able to
recognize what naming style is being used, independently from what
they are used for.

The following naming styles are commonly distinguished:
 * b (single lowercase letter)
 * B (single uppercase letter)
 * lowercase
 * lower_case_with_underscores
 * UPPERCASE
 * UPPER_CASE_WITH_UNDERSCORES
 * CapitalizedWords (or CapWords, or CamelCase -- so named because of
 the bumpy look of its letters [3]). This is also sometimes known as
 StudlyCaps.
   Note: When using abbreviations in CapWords, capitalize all the
   letters of the abbreviation. Thus HTTPServerError is better than
   HttpServerError.
 * mixedCase (differs from CapitalizedWords by initial lowercase
 character!)
 * Capitalized_Words_With_Underscores (ugly!)

There's also the style of using a short unique prefix to group related
names together. This is not used much in Python, but it is mentioned
for completeness. For example, the os.stat() function returns a tuple
whose items traditionally have names like st_mode, st_size, st_mtime
and so on. (This is done to emphasize the correspondence with the
fields of the POSIX system call struct, which helps programmers
familiar with that.)

The X11 library uses a leading X for all its public functions. In
Python, this style is generally deemed unnecessary because attribute
and method names are prefixed with an object, and function names are
prefixed with a module name.

In addition, the following special forms using leading or trailing
underscores are recognized (these can generally be combined with any
case convention):
 * _single_leading_underscore: weak "internal use" indicator. E.g.
  from M import * does not import objects whose name starts with an
  underscore.
 * single_trailing_undrescore_: used by convention to avoid conflicts
 with Python keyword, e.g.
   Tkinter.Toplevel(master, class_='ClassName')
 * __double_leading_underscore: when naming a class attribute, invokes
 name mangling (inside class FooBar, __boo becomes _FooBar__boo; see
 below).
 * __double_leading_and_trailing_underscore_: "magic" objects or
 attributes that live in user-controlled namespaces. E.g. __init__,
 __import__or_file_. Never invent such names; only use them as
 documented.

8.3 Prescriptive: Naming Conventions
8.3.1 Names to Avoid

Never use the character 'l' (lowercase letter el), 'O' (uppercase
letter oh), or 'I' (uppercase letter eye) as single character variable
names.

In some fonts, these characters are indistinguishable from the numbers
one and zero. When tempted to use 'l', use 'L' instead.

8.3.2 Package and Modules Names

Modules should have short, all-lowercase names. Underscores can be used
in the module name if it improves readability. Python package should
also have short, all-lowercase names, although the use of underscores
is discouraged.

When an extension module written in C or C++ has an accompanying Python
module that provides a higher level (e.g. more object oriented)
interface, the C/C++ module has a leading underscore (e.g. _socket).

8.3.3 Class Names

Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where
the interface is documented and used primarily as a callable.

Note that there is a separate convention for built-in names: most
built-in names are single words (or two words run together), with the
CapWords convention used only for exception names and builtin
constants.

8.3.4 Exception Names

Because exceptions should be classes, the class naming convention
applies here. However, you should use the suffix "Error" on your
exception names (if the exception actually is an error).

8.3.5 Global Variable Names

(Let's hope that these variables are meant for use inside one module
only.) The conventions are about the same as those for functions.

Modules that are designed for use via form M import * should use the
__all__ mechanism to prevent exporting globals, or use the older
convention of prefixing such globals with an underscore (which you
might want to do to indicate these globals are "module non-public).

8.3.6 Function Names

Function names should be lowercase, with words separated by
underscores as necessary to improve readability.

mixedCase is allowed only in contexts where that's already the
prevailing style (e.g. threading.py), to retain backwards
compatibility.

8.3.7 Function and method arguments

Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.

If a function argument's name clashes with a reserved keyword, it is
generally better to append a single trailing underscore rather than
use an abbreviation or spelling corruption. Thus class_ is better
than clss. (Perhaps better is to avoid such clashes by using a
synonym.)

8.3.8 Method Names and Instance Variables

Use the function naming rules: lowercase with words separated by
underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance
variables.

To avoid name clashes with subclasses, use two leading underscores to
invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an
attribute named __a, it cannot be accessed by Foo.__a. (An insistent
user could still gain access by calling Foo.__Foo__a.) Generally,
double leading underscores should be used only to avoid name conficts
with attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names(see below).

8.3.9 Constants

Constants are ususlly defined on a modules level and written in all
capitall letters with underscores separating words. Examples include
MAX_OVERFLOW and TOTAL.

8.3.10 Designing for inheritance

Always decide whether a class's methods and instance variable (
collectively: "attributes") shold be public or non-public. If in doubt,
choose non-public; it's easier to make it public later than to make a
public attribute non-public.

Public attribute are those that you expect unrelated clients of your
class to use, with your commitment to avoid backward incompatible
changes. Non-public attributes are those that are not intended to be
used by third parties; you make no guarantees that non-public
attributes won't change or even be removed.

We don't use the term "private" here, since no attributes is really
private in Python (without a generally unnecessary amount of work).

Another category of attributes are those that are part of the "subclass
API" (often called "protected: in other languages). Some classes are
designed to be inherited from, either to extend or modify aspects of
the class's behavior. When designing such a class, take care to make
explicit decisions about which attributes are public, which are part
of the subclass API, and which are truly only to be used by your base
class.

With this in mind, here are the Pythonic guidelines:
 * Public attributes should have no leading underscores.
 * If your public attribute name collides with a reserved keyword,
 append a single trailing underscore to your attribute name. This is
 preferable to an abbreviation or corrupted spelling. (However,
 nowithstanding this rule, 'cls' is the preferred spelling for any
 variable or argument which is known to be a class, especially the
 first argument to a class method.)
   Note 1: See the argument name recommendation above for class methods.
 * For simple public data attributes. it is best to expose just the
 attribute name, without complicated accessor/mutator method. Keep in
 mind that Python provides an easy path to future enhancement, should
 you find that a simple data attribute needs to grow functional
 behavior. In that case, use properties to hide functional
 implementation behind simple data attribute access syntax.
   Note 1: Properties only work on new-style classes.
   Note 2: Try to keep the functional behavior side-effect free,
    although side-effects such as caching are generally fine.
   Note 3: Avoid using properties for computationally expensive
    operations; the attribute notation makes the caller believe that
    access is (relatively) cheap.
 * If your class is intended to be sub-classed, and you have attributes
 that do not want subclasses to use, consider naming them with double
 leading underscores and no trailing underscores. This invokes Python's
 name mangling algorithm, where the name of the class is mangled into
 the attribute name. This helps avoid attribute name collisions should
 subclasses inadvertently contain attributes with the same name.
  Note 1: Note that only the simple class name is used in the mangled
   name, so if a subclass chooses both the same class name and
   attribute name, you can still get name collisions.
  Note 2: Name mangling can make certain uses, such as debugging and
   __getattr__(), less convenient. However the name mangling algorithm
   is well documented and easy to perform manually.
  Note 3: Not everyone likes name mangling. Try to balance the need to
  avoid accidental name clashes with potential use by advanced callers.

8.4 Public and internal interfaces

Any backwards compatibility guarantees apply only to public interfaces.
Accordingly, it is important that users be able to clearly distinguish
between public and internal interfaces.

Documented interfaces are considered public, unless the documentation
explicitly declares them to be provisional or internal interfaces
exempt from the usual backwards compatibility guarantees. All
undocumented interfaces should be assumed to be internal.

To better support introspection, modules should explicitly declare the
names in their public API using the __all__ attribute. Setting __all__
to an empty list indicates that module has no public API.

Even with __all__ set appropriately, internal interfaces (packages,
modules, classes, functions, attributes or other names) should still
be prefixed with a single leading underscore.

An interface is also considered internal if any containing namespace (
package, modules or class) is considered internal.

Imported names should always be considered an implementation detail.
Other modules mush not rely on indirect access to such imported names
unless they are an explicitly documented part of the containing
module's API, such as os. path or a package's __init__ modules that
exposes functionality from submodules.


9. Programming Recommendations

9.1 Function Annotations


References


Copyright



"""

print "The document named \"Style Guide for Python Code\" is important!"
