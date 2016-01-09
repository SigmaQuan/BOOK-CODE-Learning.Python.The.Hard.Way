"""
Exercise 37: Symbol Review
    It's time to review the symbols and Python words you know and to try to
    pick up a few more for the next few lessons. I have written out all the
    Python symbols and keywords that are important to know.

    In this lesson take each keyword and first try to write out what it does
    from memory. Next, search online for it and see what it really does. This
    may be difficult because some of these are difficult to search for, but
    try anyway.

    If you get one of these wrong from memory, make an index card with the
    correct definition and try to "correct" your memory.

    Finally, use each of these in a small Python program, or as many as you
    can get done. The goal is to find out what the symbols does, make sure
    you got it right, correct it if you do not, then use it to lock it in.

Keywords
    KEYWORD         DESCRIPTION                             XAMPLE
    and             Logical and.                            True and False==False
    as              Part of the with-as statement.          with X as Y: pass
    assert          Assert(ensure) that something is true.  assert False, "Error!"
    break           Stop this loop right now.               while True: break
    class           Define a class.                         class Person(object)
    continue        Don't process more of the loop.         while True: continue
    def             Define a function.                      def X(): pass
    del             Delete from dictionary.                 del X[Y]
    elif            Else if condition.                      if: X; elif: Y; else: J
    else            Else condition.                         if: X; elif: Y; else: J
    except          If an exception happens, do this.       except ValueError, e: print e
    exec            Run a string as Python.                 exec 'print "hello"'
    finally         Exceptions or not, finally do this.     finally: pass
    for             Loop over a collection of things.       for X in Y: pass
    from            Importing specific parts of a modules.  import X from Y
    global          Declare that you want a global variable.global X
    if              if condition.                           if: X; elif: Y; else: J
    import          Import a module into this one to use.   import os
    in              Part of for-loops.                      for X in Y: pass also 1 in [1,2] == True
    is              Like == to test equality.               1 is 1 == True
    lambda          Create a short anonymous function.      s = lambda y: y**y; s(3)
    not             Logical not.                            not True == False
    or              Logical or.                             True or False == True
    pass            This block is empty.                    def empty(): pass
    print           Print this string.                      print 'this string'
    raise           Raise an exception when things go wrong.raise ValueError("No")
    return          Exit the function with a return value.  def X(): return Y
    try             Try this block, find if exception.      try: pass
    while           while loop.                             while X: pass
    with            With an expression as a variable do.    with X as Y: pass
    yield           Pause here and return to caller.        def X(): yield; x().next()

Data Types
    TYPE        DESCRIPTION                            XAMPLE
    True        True boolean value.                     True or False == True
    False       False boolean value.                    False and True == False
    None        Represents "nothing" or "no value".     x = None
    strings     Stores textual information.             x = "hello"
    numbers     Stores integers.                        i = 100
    floats      Stores decimals.                        i = 10.389
    lists       Stores a list of things.                j = [1, 2, 3,4]
    dicts       Stores a key=value mapping of things.   e = {'x':1, 'y':2}

String Escape Sequences
    ESCAPE      DESCRIPTION
    \\          Backslash
    \'          Single-quote
    \"          Double-quote
    \a          Bell
    \b          Backspace
    \f          Formfeed
    \n          Newline
    \r          Carriage
    \t          Tab
    \v          Vertical tab

String Formats
omit..

Operators
    OPERATOR    DESCRIPTION
    +           Addition
    -           Subtraction
    *           Multiplication
    **          Power of
    /           Division
    //          Floor division
    %           String interpolate or modulus
    <           Less than
    >           Greater than
    <=          Less than equal
    >=          Greater than equal
    ==          Equal
    !=          Not equal
    <>          Not equal
    ()          Parenthesis
    []          List brackets
    {}          Dict curly braces
    @           At (decorators)
    ,           Comma
    :           Colon
    .           Dot
    =           Assign equal
    ;           semi-colon                      print "hi"; print "there"
    +=          Add and assign
    -=          Subtract and assign
    *=          Multiply and assign
    /=          Divide and assign
    //=         Floor divide and assign         x = 1; x //= 2
    %=          Modulus assign
    **=         Power assign

Reading Code
    Now find some Python code to read. You should be reading any Python
    code you can and trying to steal ideas that you find. You actually should
    have enough knowledge to be able to read, by maybe not understand what
    the code does. What this lesson teaches is how to apply things you have
    learned to understand other people's code.

    First, pint out the code yo want to understand. Yes, print it out, because
    you eyes and brain are more used to reading paper than computer screens.
    Make sure you print a few pages at a time.

    Second, go through your printout and take notes of the following:
        1. Functions and what the do.
        2. Where each variable is first given a value.
        3. Any variables with the same names in different parts of the program.
        These may be trouble later.
        4. Any if-statements without else clauses. Are they right?
        5. Any while-loops that might not end.
        6. Any parts of code that you can't understand for whatever reason.

    Third, once you have all of this marked up, try to explain it to yourself
    by writing comments as you go. Explain the functions, how they are used,
    what variables are involved and anything you can to figure this code out.

    Lastly, on all of the difficult parts, trace tha values of each variable
    line by line, function by function. In fact,do another printout and write
    in the margin the value of each variable that you need to "trace".

    Once you have a good idea of what the code does, go back to the computer
    and read it again to see if you find new things. Keep finding more code
    and doing this until you do not need the printout anymore.
"""