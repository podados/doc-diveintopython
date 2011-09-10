
You are here: `Home`_ `Dive Into Python 3`_
Difficulty level: ♦♦♦♦♢


Advanced Iterators
==================

❝ Great fleas have little fleas upon their backs to bite em,
And little fleas have lesser fleas, and so ad infinitum. ❞
Augustus De Morgan


Diving In
---------

Just as `regular expressions`_ put `strings`_ on steroids, the
`itertools` module puts `iterators`_ on steroids. But first, I want to
show you a classic puzzle.

::

     `HAWAII + IDAHO + IOWA + OHIO == STATES
    510199 + 98153 + 9301 + 3593 == 621246
    
    H = 5
    A = 1
    W = 0
    I = 9
    D = 8
    O = 3
    S = 6
    T = 2
    E = 4`


Puzzles like this are called cryptarithms or alphametics . The letters
spell out actual words, but if you replace each letter with a digit
from `09`, it also spells an arithmetic equation. The trick is to
figure out which letter maps to each digit. All the occurrences of
each letter must map to the same digit, no digit can be repeated, and
no word can start with the digit 0. The most well-known alphametic
puzzle is `SEND + MORE = MONEY`.
In this chapter, well dive into an incredible Python program
originally written by Raymond Hettinger. This program solves
alphametic puzzles *in just 14 lines of code*.
[`download `alphametics.py``_]

::

     `import re
    import itertools
    
    def solve(puzzle):
        words = re.findall('[A-Z]+', puzzle.upper())
        unique_characters = set(''.join(words))
        assert len(unique_characters) <= 10, 'Too many letters'
        first_letters = {word[0] for word in words}
        n = len(first_letters)
        sorted_characters = ''.join(first_letters) + \
            ''.join(unique_characters - first_letters)
        characters = tuple(ord(c) for c in sorted_characters)
        digits = tuple(ord(c) for c in '0123456789')
        zero = digits[0]
        for guess in itertools.permutations(digits, len(characters)):
            if zero not in guess[:n]:
                equation = puzzle.translate(dict(zip(characters, guess)))
                if eval(equation):
                    return equation
    
    if __name__ == '__main__':
        import sys
        for puzzle in sys.argv[1:]:
            print(puzzle)
            solution = solve(puzzle)
            if solution:
                print(solution)`


You can run the program from the command line. On Linux, it would look
like this. (These may take some time, depending on the speed of your
computer, and there is no progress bar. Just be patient!)

::

    
    you@localhost:~/diveintopython3/examples$ python3 alphametics.py "HAWAII + IDAHO + IOWA + OHIO == STATES"
    HAWAII + IDAHO + IOWA + OHIO = STATES
    510199 + 98153 + 9301 + 3593 == 621246
    you@localhost:~/diveintopython3/examples$ python3 alphametics.py "I + LOVE + YOU == DORA"
    I + LOVE + YOU == DORA
    1 + 2784 + 975 == 3760
    you@localhost:~/diveintopython3/examples$ python3 alphametics.py "SEND + MORE == MONEY"
    SEND + MORE == MONEY
    9567 + 1085 == 10652


⁂


Finding all occurrences of a pattern
------------------------------------

The first thing this alphametics solver does is find all the letters
(AZ) in the puzzle.

::

    
    >>> import re
    >>> re.findall('[0-9]+', '16 2-by-4s in rows of 8')  ①
    ['16', '2', '4', '8']
    >>> re.findall('[A-Z]+', 'SEND + MORE == MONEY')     ②
    ['SEND', 'MORE', 'MONEY']



#. The `re` module is Pythons implementation of `regular
expressions`_. It has a nifty function called `findall()` which takes
a regular expression pattern and a string, and finds all occurrences
of the pattern within the string. In this case, the pattern matches
sequences of numbers. The `findall()` function returns a list of all
the substrings that matched the pattern.
#. Here the regular expression pattern matches sequences of letters.
   Again, the return value is a list, and each item in the list is a
   string that matched the regular expression pattern.


Heres another example that will stretch your brain a little.

::

    
    >>> re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick.")
    [' sixth s', " sheikh's s", " sheep's s"]

This is the `hardest tongue twister`_ in the English language.
Surprised? The regular expression looks for a space, an `s`, and then
the shortest possible series of any character ( `.*?`), then a space,
then another `s`. Well, looking at that input string, I see five
matches:

#. `The sixth s ick sheikh's sixth sheep's sick.`
#. `The sixth sick s heikh's sixth sheep's sick.`
#. `The sixth sick sheikh's s ixth sheep's sick.`
#. `The sixth sick sheikh's sixth s heep's sick.`
#. `The sixth sick sheikh's sixth sheep's s ick.`


But the `re.findall()` function only returned three matches.
Specifically, it returned the first, the third, and the fifth. Why is
that? Because *it doesnt return overlapping matches*. The first match
overlaps with the second, so the first is returned and the second is
skipped. Then the third overlaps with the fourth, so the third is
returned and the fourth is skipped. Finally, the fifth is returned.
Three matches, not five.
This has nothing to do with the alphametics solver; I just thought it
was interesting.
⁂


Finding the unique items in a sequence
--------------------------------------

`Sets`_ make it trivial to find the unique items in a sequence.

::

    
    >>> a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
    >>> set(a_list)                      ①
    {'sixth', 'The', "sheep's", 'sick', "sheik's"}
    >>> a_string = 'EAST IS EAST'
    >>> set(a_string)                    ②
    {'A', ' ', 'E', 'I', 'S', 'T'}
    >>> words = ['SEND', 'MORE', 'MONEY']
    >>> ''.join(words)                   ③
    'SENDMOREMONEY'
    >>> set(''.join(words))              ④
    {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}



#. Given a list of several strings, the `set()` function will return a
set of unique strings from the list. This makes sense if you think of
it like a `for` loop. Take the first item from the list, put it in the
set. Second. Third. Fourth. Fifthwait, thats in the set already, so it
only gets listed once, because Python sets dont allow duplicates.
Sixth. Seventhagain, a duplicate, so it only gets listed once. The end
result? All the unique items in the original list, without any
duplicates. The original list doesnt even need to be sorted first.
#. The same technique works with strings, since a string is just a
sequence of characters.
#. Given a list of strings, `''.join( a_list )` concatenates all the
strings together into one.
#. So, given a list of strings, this line of code returns all the
   unique characters across all the strings, with no duplicates.


The alphametics solver uses this technique to build a set of all the
unique characters in the puzzle.

::

     `unique_characters = set(''.join(words))`


This list is later used to assign digits to characters as the solver
iterates through the possible solutions.
⁂


Making assertions
-----------------

Like many programming languages, Python has an `assert` statement.
Heres how it works.

::

    
    >>> assert 1 + 1 == 2                                     ①
    >>> assert 1 + 1 == 3                                     ②
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError
    >>> assert 2 + 2 == 5, "Only for very large values of 2"  ③
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError: Only for very large values of 2



#. The `assert` statement is followed by any valid Python expression.
In this case, the expression `1 + 1 == 2` evaluates to `True`, so the
`assert` statement does nothing.
#. However, if the Python expression evaluates to `False`, the
`assert` statement will raise an `AssertionError`.
#. You can also include a human-readable message that is printed if
   the `AssertionError` is raised.


Therefore, this line of code:

::

     `assert len(unique_characters) <= 10, 'Too many letters'`


is equivalent to this:

::

     `if len(unique_characters) > 10:
        raise AssertionError('Too many letters')`


The alphametics solver uses this exact `assert` statement to bail out
early if the puzzle contains more than ten unique letters. Since each
letter is assigned a unique digit, and there are only ten digits, a
puzzle with more than ten unique letters can not possibly have a
solution.
⁂


Generator expressions
---------------------

A generator expression is like a `generator function`_ without the
function.

::

    
    >>> unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
    >>> gen = (ord(c) for c in unique_characters)  ①
    >>> gen                                        ②
    <generator object <genexpr> at 0x00BADC10>
    >>> next(gen)                                  ③
    69
    >>> next(gen)
    68
    >>> tuple(ord(c) for c in unique_characters)   ④
    (69, 68, 77, 79, 78, 83, 82, 89)



#. A generator expression is like an anonymous function that yields
values. The expression itself looks like a `list comprehension`_, but
its wrapped in parentheses instead of square brackets.
#. The generator expression returns an iterator.
#. Calling `next( gen )` returns the next value from the iterator.
#. If you like, you can iterate through all the possible values and
   return a tuple, list, or set, by passing the generator expression to
   `tuple()`, `list()`, or `set()`. In these cases, you dont need an
   extra set of parenthesesjust pass the bare expression `ord(c) for c in
   unique_characters` to the `tuple()` function, and Python figures out
   that its a generator expression.


☞Using a generator expression instead of a list comprehension
can save both CPU and RAM . If youre building an list just to throw it
away ( e.g. passing it to `tuple()` or `set()`), use a generator
expression instead!
Heres another way to accomplish the same thing, using a `generator
function`_:

::

     `def ord_map(a_string):
        for c in a_string:
            yield ord(c)
    
    gen = ord_map(unique_characters)`


The generator expression is more compact but functionally equivalent.
⁂


Calculating Permutations The Lazy Way!
--------------------------------------

First of all, what the heck are permutations? Permutations are a
mathematical concept. (There are actually several definitions,
depending on what kind of math youre doing. Here Im talking about
combinatorics, but if that doesnt mean anything to you, dont worry
about it. As always, `Wikipedia is your friend`_.)
The idea is that you take a list of things (could be numbers, could be
letters, could be dancing bears) and find all the possible ways to
split them up into smaller lists. All the smaller lists have the same
size, which can be as small as 1 and as large as the total number of
items. Oh, and nothing can be repeated. Mathematicians say things like
lets find the permutations of 3 different items taken 2 at a time,
which means you have a sequence of 3 items and you want to find all
the possible ordered pairs.

::

    
    >>> import itertools                              ①
    >>> perms = itertools.permutations([1, 2, 3], 2)  ②
    >>> next(perms)                                   ③
    (1, 2)
    >>> next(perms)
    (1, 3)
    >>> next(perms)
    (2, 1)                                            ④
    >>> next(perms)
    (2, 3)
    >>> next(perms)
    (3, 1)
    >>> next(perms)
    (3, 2)
    >>> next(perms)                                   ⑤
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration



#. The `itertools` module has all kinds of fun stuff in it, including
a `permutations()` function that does all the hard work of finding
permutations.
#. The `permutations()` function takes a sequence (here a list of
three integers) and a number, which is the number of items you want in
each smaller group. The function returns an iterator, which you can
use in a `for` loop or any old place that iterates. Here Ill step
through the iterator manually to show all the values.
#. The first permutation of `[1, 2, 3]` taken 2 at a time is `(1, 2)`.
#. Note that permutations are ordered: `(2, 1)` is different than `(1,
2)`.
#. Thats it! Those are all the permutations of `[1, 2, 3]` taken 2 at
   a time. Pairs like `(1, 1)` and `(2, 2)` never show up, because they
   contain repeats so they arent valid permutations. When there are no
   more permutations, the iterator raises a `StopIteration` exception.

The `itertools` module has all kinds of fun stuff.
The `permutations()` function doesnt have to take a list. It can take
any sequenceeven a string.

::

    
    >>> import itertools
    >>> perms = itertools.permutations('ABC', 3)  ①
    >>> next(perms)
    ('A', 'B', 'C')                               ②
    >>> next(perms)
    ('A', 'C', 'B')
    >>> next(perms)
    ('B', 'A', 'C')
    >>> next(perms)
    ('B', 'C', 'A')
    >>> next(perms)
    ('C', 'A', 'B')
    >>> next(perms)
    ('C', 'B', 'A')
    >>> next(perms)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    >>> list(itertools.permutations('ABC', 3))    ③
    [('A', 'B', 'C'), ('A', 'C', 'B'),
     ('B', 'A', 'C'), ('B', 'C', 'A'),
     ('C', 'A', 'B'), ('C', 'B', 'A')]



#. A string is just a sequence of characters. For the purposes of
finding permutations, the string `'ABC'` is equivalent to the list
`['A', 'B', 'C']`.
#. The first permutation of the 3 items `['A', 'B', 'C']`, taken 3 at
a time, is `('A', 'B', 'C')`. There are five other permutationsthe
same three characters in every conceivable order.
#. Since the `permutations()` function always returns an iterator, an
   easy way to debug permutations is to pass that iterator to the built-
   in `list()` function to see all the permutations immediately.


⁂


Other Fun Stuff in the `itertools` Module
-----------------------------------------

::

    
    >>> import itertools
    >>> list(itertools.product('ABC', '123'))   ①
    [('A', '1'), ('A', '2'), ('A', '3'), 
     ('B', '1'), ('B', '2'), ('B', '3'), 
     ('C', '1'), ('C', '2'), ('C', '3')]
    >>> list(itertools.combinations('ABC', 2))  ②
    [('A', 'B'), ('A', 'C'), ('B', 'C')]



#. The `itertools.product()` function returns an iterator containing
the Cartesian product of two sequences.
#. The `itertools.combinations()` function returns an iterator
   containing all the possible combinations of the given sequence of the
   given length. This is like the `itertools.permutations()` function,
   except combinations dont include items that are duplicates of other
   items in a different order. So `itertools.permutations('ABC', 2)` will
   return both `('A', 'B')` and `('B', 'A')` (among others), but
   `itertools.combinations('ABC', 2)` will not return `('B', 'A')`
   because it is a duplicate of `('A', 'B')` in a different order.


[`download `favorite-people.txt``_]

::

    
    >>> names = list(open('examples/favorite-people.txt', encoding='utf-8'))  ①
    >>> names
    ['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n',
    'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie\n']
    >>> names = [name.rstrip() for name in names]                             ②
    >>> names
    ['Dora', 'Ethan', 'Wesley', 'John', 'Anne',
    'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']
    >>> names = sorted(names)                                                 ③
    >>> names
    ['Alex', 'Anne', 'Chris', 'Dora', 'Ethan',
    'John', 'Lizzie', 'Mike', 'Sarah', 'Wesley']
    >>> names = sorted(names, key=len)                                        ④
    >>> names
    ['Alex', 'Anne', 'Dora', 'John', 'Mike',
    'Chris', 'Ethan', 'Sarah', 'Lizzie', 'Wesley']



#. This idiom returns a list of the lines in a text file.
#. Unfortunately (for this example), the `list(open( filename ))`
idiom also includes the carriage returns at the end of each line. This
list comprehension uses the `rstrip()` string method to strip trailing
whitespace from each line. (Strings also have an `lstrip()` method to
strip leading whitespace, and a `strip()` method which strips both.)
#. The `sorted()` function takes a list and returns it sorted. By
default, it sorts alphabetically.
#. But the `sorted()` function can also take a function as the key
   parameter, and it sorts by that key. In this case, the sort function
   is `len()`, so it sorts by `len( each item )`. Shorter names come
   first, then longer, then longest.


What does this have to do with the `itertools` module? Im glad you
asked.

::

    
    continuing from the previous interactive shell
    >>> import itertools
    >>> groups = itertools.groupby(names, len)  ①
    >>> groups
    <itertools.groupby object at 0x00BB20C0>
    >>> list(groups)
    [(4, <itertools._grouper object at 0x00BA8BF0>),
     (5, <itertools._grouper object at 0x00BB4050>),
     (6, <itertools._grouper object at 0x00BB4030>)]
    >>> groups = itertools.groupby(names, len)   ②
    >>> for name_length, name_iter in groups:    ③
    ...     print('Names with {0:d} letters:'.format(name_length))
    ...     for name in name_iter:
    ...         print(name)
    ... 
    Names with 4 letters:
    Alex
    Anne
    Dora
    John
    Mike
    Names with 5 letters:
    Chris
    Ethan
    Sarah
    Names with 6 letters:
    Lizzie
    Wesley



#. The `itertools.groupby()` function takes a sequence and a key
function, and returns an iterator that generates pairs. Each pair
contains the result of `key_function( each item )` and another
iterator containing all the items that shared that key result.
#. Calling the `list()` function exhausted the iterator, i.e. youve
already generated every item in the iterator to make the list. Theres
no reset button on an iterator; you cant just start over once youve
exhausted it. If you want to loop through it again (say, in the
upcoming `for` loop), you need to call `itertools.groupby()` again to
create a new iterator.
#. In this example, given a list of names *already sorted by length*,
   `itertools.groupby(names, len)` will put all the 4-letter names in one
   iterator, all the 5-letter names in another iterator, and so on. The
   `groupby()` function is completely generic; it could group strings by
   first letter, numbers by their number of factors, or any other key
   function you can think of.


☞The `itertools.groupby()` function only works if the input
sequence is already sorted by the grouping function. In the example
above, you grouped a list of names by the `len()` function. That only
worked because the input list was already sorted by length.
Are you watching closely?

::

    
    >>> list(range(0, 3))
    [0, 1, 2]
    >>> list(range(10, 13))
    [10, 11, 12]
    >>> list(itertools.chain(range(0, 3), range(10, 13)))        ①
    [0, 1, 2, 10, 11, 12]
    >>> list(zip(range(0, 3), range(10, 13)))                    ②
    [(0, 10), (1, 11), (2, 12)]
    >>> list(zip(range(0, 3), range(10, 14)))                    ③
    [(0, 10), (1, 11), (2, 12)]
    >>> list(itertools.zip_longest(range(0, 3), range(10, 14)))  ④
    [(0, 10), (1, 11), (2, 12), (None, 13)]



#. The `itertools.chain()` function takes two iterators and returns an
iterator that contains all the items from the first iterator, followed
by all the items from the second iterator. (Actually, it can take any
number of iterators, and it chains them all in the order they were
passed to the function.)
#. The `zip()` function does something prosaic that turns out to be
extremely useful: it takes any number of sequences and returns an
iterator which returns tuples of the first items of each sequence,
then the second items of each, then the third, and so on.
#. The `zip()` function stops at the end of the shortest sequence.
`range(10, 14)` has 4 items (10, 11, 12, and 13), but `range(0, 3)`
only has 3, so the `zip()` function returns an iterator of 3 items.
#. On the other hand, the `itertools.zip_longest()` function stops at
   the end of the *longest* sequence, inserting `None` values for items
   past the end of the shorter sequences.


OK, that was all very interesting, but how does it relate to the
alphametics solver? Heres how:

::

    
    >>> characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
    >>> guess = ('1', '2', '0', '3', '4', '5', '6', '7')
    >>> tuple(zip(characters, guess))  ①
    (('S', '1'), ('M', '2'), ('E', '0'), ('D', '3'),
     ('O', '4'), ('N', '5'), ('R', '6'), ('Y', '7'))
    >>> dict(zip(characters, guess))   ②
    {'E': '0', 'D': '3', 'M': '2', 'O': '4',
     'N': '5', 'S': '1', 'R': '6', 'Y': '7'}



#. Given a list of letters and a list of digits (each represented here
as 1-character strings), the `zip` function will create a pairing of
letters and digits, in order.
#. Why is that cool? Because that data structure happens to be exactly
   the right structure to pass to the `dict()` function to create a
   dictionary that uses letters as keys and their associated digits as
   values. (This isnt the only way to do it, of course. You could use a
   `dictionary comprehension`_ to create the dictionary directly.)
   Although the printed representation of the dictionary lists the pairs
   in a different order (dictionaries have no order per se), you can see
   that each letter is associated with the digit, based on the ordering
   of the original characters and guess sequences.


The alphametics solver uses this technique to create a dictionary that
maps letters in the puzzle to digits in the solution, for each
possible solution.

::

     `characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    ...
    for guess in itertools.permutations(digits, len(characters)):
        ...
        equation = puzzle.translate(dict(zip(characters, guess)))`


But what is this `translate()` method? Ah, now youre getting to the
*really* fun part.
⁂


A New Kind Of String Manipulation
---------------------------------

Python strings have many methods. You learned about some of those
methods in `the Strings chapter`_: `lower()`, `count()`, and
`format()`. Now I want to introduce you to a powerful but little-known
string manipulation technique: the `translate()` method.

::

    
    >>> translation_table = {ord('A'): ord('O')}  ①
    >>> translation_table                         ②
    {65: 79}
    >>> 'MARK'.translate(translation_table)       ③
    'MORK'



#. String translation starts with a translation table, which is just a
dictionary that maps one character to another. Actually, character is
incorrectthe translation table really maps one *byte* to another.
#. Remember, bytes in Python 3 are integers. The `ord()` function
returns the ASCII value of a character, which, in the case of AZ, is
always a byte from 65 to 90.
#. The `translate()` method on a string takes a translation table and
   runs the string through it. That is, it replaces all occurrences of
   the keys of the translation table with the corresponding values. In
   this case, translating `MARK` to `MORK`.

Now youre getting to the *really* fun part.
What does this have to do with solving alphametic puzzles? As it turns
out, everything.

::

    
    >>> characters = tuple(ord(c) for c in 'SMEDONRY')       ①
    >>> characters
    (83, 77, 69, 68, 79, 78, 82, 89)
    >>> guess = tuple(ord(c) for c in '91570682')            ②
    >>> guess
    (57, 49, 53, 55, 48, 54, 56, 50)
    >>> translation_table = dict(zip(characters, guess))     ③
    >>> translation_table
    {68: 55, 69: 53, 77: 49, 78: 54, 79: 48, 82: 56, 83: 57, 89: 50}
    >>> 'SEND + MORE == MONEY'.translate(translation_table)  ④
    '9567 + 1085 == 10652'



#. Using a generator expression, we quickly compute the byte values
for each character in a string. characters is an example of the value
of sorted_characters in the `alphametics.solve()` function.
#. Using another generator expression, we quickly compute the byte
values for each digit in this string. The result, guess , is of the
form returned by the `itertools.permutations()` function in the
`alphametics.solve()` function.
#. This translation table is generated by zipping characters and guess
together and building a dictionary from the resulting sequence of
pairs. This is exactly what the `alphametics.solve()` function does
inside the `for` loop.
#. Finally, we pass this translation table to the `translate()` method
   of the original puzzle string. This converts each letter in the string
   to the corresponding digit (based on the letters in characters and the
   digits in guess ). The result is a valid Python expression, as a
   string.


Thats pretty impressive. But what can you do with a string that
happens to be a valid Python expression?
⁂


Evaluating Arbitrary Strings As Python Expressions
--------------------------------------------------

This is the final piece of the puzzle (or rather, the final piece of
the puzzle solver). After all that fancy string manipulation, were
left with a string like `'9567 + 1085 == 10652'`. But thats a string,
and what good is a string? Enter `eval()`, the universal Python
evaluation tool.

::

    
    >>> eval('1 + 1 == 2')
    True
    >>> eval('1 + 1 == 3')
    False
    >>> eval('9567 + 1085 == 10652')
    True


But wait, theres more! The `eval()` function isnt limited to boolean
expressions. It can handle *any* Python expression and returns *any*
datatype.

::

    
    >>> eval('"A" + "B"')
    'AB'
    >>> eval('"MARK".translate({65: 79})')
    'MORK'
    >>> eval('"AAAAA".count("A")')
    5
    >>> eval('["*"] * 5')
    ['*', '*', '*', '*', '*']


But wait, thats not all!

::

    
    >>> x = 5
    >>> eval("x * 5")         ①
    25
    >>> eval("pow(x, 2)")     ②
    25
    >>> import math
    >>> eval("math.sqrt(x)")  ③
    2.2360679774997898



#. The expression that `eval()` takes can reference global variables
defined outside the `eval()`. If called within a function, it can
reference local variables too.
#. And functions.
#. And modules.


Hey, wait a minute

::

    
    >>> import subprocess
    >>> eval("subprocess.getoutput('ls ~')")                  ①
    'Desktop         Library         Pictures \
     Documents       Movies          Public   \
     Music           Sites'
    >>> eval("subprocess.getoutput('rm /some/random/file')")  ②



#. The `subprocess` module allows you to run arbitrary shell commands
and get the result as a Python string.
#. Arbitrary shell commands can have permanent consequences.


Its even worse than that, because theres a global `__import__()`
function that takes a module name as a string, imports the module, and
returns a reference to it. Combined with the power of `eval()`, you
can construct a single expression that will wipe out all your files:

::

    
    >>> eval("__import__('subprocess').getoutput('rm /some/random/file')")  ①



#. Now imagine the output of `'rm -rf ~'`. Actually there wouldnt be
   any output, but you wouldnt have any files left either.


eval() is EVIL
Well, the evil part is evaluating arbitrary expressions from untrusted
sources. You should only use `eval()` on trusted input. Of course, the
trick is figuring out whats trusted. But heres something I know for
certain: you should **NOT** take this alphametics solver and put it on
the internet as a fun little web service. Dont make the mistake of
thinking, Gosh, the function does a lot of string manipulation before
getting a string to evaluate; *I cant imagine* how someone could
exploit that. Someone **WILL** figure out how to sneak nasty
executable code past all that string manipulation (`stranger things
have happened`_), and then you can kiss your server goodbye.
But surely theres *some* way to evaluate expressions safely? To put
`eval()` in a sandbox where it cant access or harm the outside world?
Well, yes and no.

::

    
    >>> x = 5
    >>> eval("x * 5", {}, {})               ①
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1, in <module>
    NameError: name 'x' is not defined
    >>> eval("x * 5", {"x": x}, {})         ②
    25
    >>> import math
    >>> eval("math.sqrt(x)", {"x": x}, {})  ③
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1, in <module>
    NameError: name 'math' is not defined



#. The second and third parameters passed to the `eval()` function act
as the global and local namespaces for evaluating the expression. In
this case, they are both empty, which means that when the string `"x *
5"` is evaluated, there is no reference to x in either the global or
local namespace, so `eval()` throws an exception.
#. You can selectively include specific values in the global namespace
by listing them individually. Then thoseand only thosevariables will
be available during evaluation.
#. Even though you just imported the `math` module, you didnt include
   it in the namespace passed to the `eval()` function, so the evaluation
   failed.


Gee, that was easy. Lemme make an alphametics web service now!

::

    
    >>> eval("pow(5, 2)", {}, {})                   ①
    25
    >>> eval("__import__('math').sqrt(5)", {}, {})  ②
    2.2360679774997898



#. Even though youve passed empty dictionaries for the global and
local namespaces, all of Pythons built-in functions are still
available during evaluation. So `pow(5, 2)` works, because `5` and `2`
are literals, and `pow()` is a built-in function.
#. Unfortunately (and if you dont see why its unfortunate, read on),
   the `__import__()` function is also a built-in function, so it works
   too.


Yeah, that means you can still do nasty things, even if you explicitly
set the global and local namespaces to empty dictionaries when calling
`eval()`:

::

    >>> eval("__import__('subprocess').getoutput('rm /some/random/file')", {}, {})


Oops. Im glad I didnt make that alphametics web service. Is there
*any* way to use `eval()` safely? Well, yes and no.

::

    
    >>> eval("__import__('math').sqrt(5)",
    ...     {"__builtins__":None}, {})          ①
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1, in <module>
    NameError: name '__import__' is not defined
    >>> eval("__import__('subprocess').getoutput('rm -rf /')",
    ...     {"__builtins__":None}, {})          ②
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1, in <module>
    NameError: name '__import__' is not defined



#. To evaluate untrusted expressions safely, you need to define a
global namespace dictionary that maps `"__builtins__"` to `None`, the
Python null value. Internally, the built-in functions are contained
within a pseudo-module called `"__builtins__"`. This pseudo-module (
i.e. the set of built-in functions) is made available to evaluated
expressions unless you explicitly override it.
#. Be sure youve overridden `__builtins__`. Not `__builtin__`,
   `__built-ins__`, or some other variation that will work just fine but
   expose you to catastrophic risks.


So `eval()` is safe now? Well, yes and no.

::

    
    >>> eval("2 ** 2147483647",
    ...     {"__builtins__":None}, {})          ①



#. Even without access to `__builtins__`, you can still launch a
   denial-of-service attack. For example, trying to raise `2` to the
   `2147483647` th power will spike your servers CPU utilization to 100%
   for quite some time. (If youre trying this in the interactive shell,
   press Ctrl-C a few times to break out of it.) Technically this
   expression *will* return a value eventually, but in the meantime your
   server will be doing a whole lot of nothing.


In the end, it *is* possible to safely evaluate untrusted Python
expressions, for some definition of safe that turns out not to be
terribly useful in real life. Its fine if youre just playing around,
and its fine if you only ever pass it trusted input. But anything else
is just asking for trouble.
⁂


Putting It All Together
-----------------------

To recap: this program solves alphametic puzzles by brute force, i.e.
through an exhaustive search of all possible solutions. To do this, it

#. Finds all the letters in the puzzle with the `re.findall()`
function
#. Find all the *unique* letters in the puzzle with sets and the
`set()` function
#. Checks if there are more than 10 unique letters (meaning the puzzle
is definitely unsolvable) with an `assert` statement
#. Converts the letters to their ASCII equivalents with a generator
object
#. Calculates all the possible solutions with the
`itertools.permutations()` function
#. Converts each possible solution to a Python expression with the
`translate()` string method
#. Tests each possible solution by evaluating the Python expression
with the `eval()` function
#. Returns the first solution that evaluates to `True`


in just 14 lines of code.
⁂


Further Reading
---------------


+ ` `itertools` module`_
+ ` `itertools`Iterator functions for efficient looping`_
+ `Watch Raymond Hettingers Easy AI with Python talk`_ at PyCon 2009
+ `Recipe 576615: Alphametics solver`_, Raymond Hettingers original
alphametics solver for Python 2
+ `More of Raymond Hettingers recipes`_ in the ActiveState Code
repository
+ `Alphametics on Wikipedia`_
+ `Alphametics Index`_, including `lots of puzzles`_ and `a generator
  to make your own`_


Many thanks to Raymond Hettinger for agreeing to relicense his code so
I could port it to Python 3 and use it as the basis for this chapter.
`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _x261C;: iterators.html
.. _dictionary comprehension: comprehensions.html#dictionarycomprehension
.. _alphametics.py: examples/alphametics.py
.. _Recipe 576615: Alphametics solver: http://code.activestate.com/recipes/576615/
.. _Iterator functions for efficient looping: http://www.doughellmann.com/PyMOTW/itertools/
.. _ module: http://docs.python.org/3.1/library/itertools.html
.. _ talk: http://blip.tv/file/1947373/
.. _list comprehension: comprehensions.html#listcomprehension
.. _hardest tongue twister: http://en.wikipedia.org/wiki/Tongue-twister
.. _Dive Into Python 3: table-of-contents.html#advanced-iterators
.. _Mark Pilgrim: about.html
.. _Alphametics Index: http://www.tkcs-collins.com/truman/alphamet/index.shtml
.. _Wikipedia is your friend: http://en.wikipedia.org/wiki/Permutation
.. _a generator to make your own: http://www.tkcs-collins.com/truman/alphamet/alpha_gen.shtml
.. _lots of puzzles: http://www.tkcs-collins.com/truman/alphamet/alphamet.shtml
.. _Alphametics on Wikipedia: http://en.wikipedia.org/wiki/Verbal_arithmetic
.. _regular expressions: regular-expressions.html
.. _s recipes: http://code.activestate.com/recipes/users/178123/
.. _favorite-people.txt: examples/favorite-people.txt
.. _Sets: native-datatypes.html#sets
.. _x261E;: unit-testing.html
.. _Home: index.html
.. _stranger things have happened: http://www.securityfocus.com/blogs/746
.. _the Strings chapter: strings.html
.. _generator function: generators.html


