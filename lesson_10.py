"""
Exercise 10: What Was That?

"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a lie."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

"""
Escape Sequences
    This all of the escape sequence Python supports. You may not use many of
    these, but memorize their format and what they do anyway. Try them out
    in some strings to see if you can make them work.
    ESCAPE  WHAT IT DOES.
    \\  Backslash (\)
    \'  Single-quote (')
    \"  Double-quote (")
    \a  ASCLL bell (BEL)
    \b  ASCLL backspace (BS)
    \f  ASCLL formfeed (FF)
    \n  ASCLL linefeed (LF)
    \N{name}    Character named name in the Unicode database (Unicode only)
    \r  Carriage Return (CR)
    \t  Horizontal Tab (TAB)
    \uxxxx  Character with 16-bit hex value xxxx (Unicode only)
    \Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx (Unicode only)
    \v  ASCLL vertical tab (VT)
    \ooo    Character with octal value ooo
    \ xhh    Character with hex value h
"""

"""
Study Drills
    1. Memorize all the escape sequences by putting them on flash cards.
    2. Use " ''' "(triple-single-quote) instead. Can you see why you might use
    that instead of \"\"\"(triple-double-quote)?
    3. Combine escape sequences and format strings to create a more complex
    format.
    4. Remember the %r format? Combine %r with double-quote and single-quote
    escapes and print them out. Compare %r with %s. Notice how %r prints it
    the way you'd write it in your file, but %s prints it the way you'd like
    to see it?
"""

print "%s", "\""
print "%r", "\""
print "%s", "\'"
print "%r", "\'"

