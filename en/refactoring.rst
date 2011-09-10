
You are here: `Home`_ `Dive Into Python 3`_
Difficulty level: ♦♦♦♦♢


Refactoring
===========

❝ After one has played a vast quantity of notes and more notes,
it is simplicity that emerges as the crowning reward of art. ❞
`Frdric Chopin`_


Diving In
---------

Like it or not, bugs happen. Despite your best efforts to write
comprehensive `unit tests`_, bugs happen. What do I mean by bug? A bug
is a test case you havent written yet.

::

    >>> import roman7
    >>> roman7.from_roman('') ①
    0



#. This is a bug. An empty string should raise an
   `InvalidRomanNumeralError` exception, just like any other sequence of
   characters that dont represent a valid Roman numeral.


After reproducing the bug, and before fixing it, you should write a
test case that fails, thus illustrating the bug.

::

     `class FromRomanBadInput(unittest.TestCase):  
        .
        .
        .
        def testBlank(self):
            '''from_roman should fail with blank string'''
            self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, '') ①`



#. Pretty simple stuff here. Call `from_roman()` with an empty string
   and make sure it raises an `InvalidRomanNumeralError` exception. The
   hard part was finding the bug; now that you know about it, testing for
   it is the easy part.


Since your code has a bug, and you now have a test case that tests
this bug, the test case will fail:

::

    
    you@localhost:~/diveintopython3/examples$ python3 romantest8.py -v
    from_roman should fail with blank string ... FAIL
    from_roman should fail with malformed antecedents ... ok
    from_roman should fail with repeated pairs of numerals ... ok
    from_roman should fail with too many repeated numerals ... ok
    from_roman should give known result with known input ... ok
    to_roman should give known result with known input ... ok
    from_roman(to_roman(n))==n for all n ... ok
    to_roman should fail with negative input ... ok
    to_roman should fail with non-integer input ... ok
    to_roman should fail with large input ... ok
    to_roman should fail with 0 input ... ok
    
    ======================================================================
    FAIL: from_roman should fail with blank string
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "romantest8.py", line 117, in test_blank
        self.assertRaises(roman8.InvalidRomanNumeralError, roman8.from_roman, '')
    AssertionError: InvalidRomanNumeralError not raised by from_roman
    
    ----------------------------------------------------------------------
    Ran 11 tests in 0.171s
    
    FAILED (failures=1)


*Now* you can fix the bug.

::

     `def from_roman(s):
        '''convert Roman numeral to integer'''
        if not s:                                                                  ①
            raise InvalidRomanNumeralError('Input can not be blank')
        if not re.search(romanNumeralPattern, s):
            raise InvalidRomanNumeralError('Invalid Roman numeral: {}'.format(s))  ②
    
        result = 0
        index = 0
        for numeral, integer in romanNumeralMap:
            while s[index:index+len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result`



#. Only two lines of code are required: an explicit check for an empty
string, and a `raise` statement.
#. I dont think Ive mentioned this yet anywhere in this book, so let
   this serve as your final lesson in `string formatting`_. Starting in
   Python 3.1, you can skip the numbers when using positional indexes in
   a format specifier. That is, instead of using the format specifier
   `{0}` to refer to the first parameter to the `format()` method, you
   can simply use `{}` and Python will fill in the proper positional
   index for you. This works for any number of arguments; the first `{}`
   is `{0}`, the second `{}` is `{1}`, and so forth.



::

    
    you@localhost:~/diveintopython3/examples$ python3 romantest8.py -v
    from_roman should fail with blank string ... ok  ①
    from_roman should fail with malformed antecedents ... ok
    from_roman should fail with repeated pairs of numerals ... ok
    from_roman should fail with too many repeated numerals ... ok
    from_roman should give known result with known input ... ok
    to_roman should give known result with known input ... ok
    from_roman(to_roman(n))==n for all n ... ok
    to_roman should fail with negative input ... ok
    to_roman should fail with non-integer input ... ok
    to_roman should fail with large input ... ok
    to_roman should fail with 0 input ... ok
    
    ----------------------------------------------------------------------
    Ran 11 tests in 0.156s
    
    OK  ②



#. The blank string test case now passes, so the bug is fixed.
#. All the other test cases still pass, which means that this bug fix
   didnt break anything else. Stop coding.


Coding this way does not make fixing bugs any easier. Simple bugs
(like this one) require simple test cases; complex bugs will require
complex test cases. In a testing-centric environment, it may *seem*
like it takes longer to fix a bug, since you need to articulate in
code exactly what the bug is (to write the test case), then fix the
bug itself. Then if the test case doesnt pass right away, you need to
figure out whether the fix was wrong, or whether the test case itself
has a bug in it. However, in the long run, this back-and-forth between
test code and code tested pays for itself, because it makes it more
likely that bugs are fixed correctly the first time. Also, since you
can easily re-run *all* the test cases along with your new one, you
are much less likely to break old code when fixing new code. Todays
unit test is tomorrows regression test.
⁂


Handling Changing Requirements
------------------------------

Despite your best efforts to pin your customers to the ground and
extract exact requirements from them on pain of horrible nasty things
involving scissors and hot wax, requirements will change. Most
customers dont know what they want until they see it, and even if they
do, they arent that good at articulating what they want precisely
enough to be useful. And even if they do, theyll want more in the next
release anyway. So be prepared to update your test cases as
requirements change.
Suppose, for instance, that you wanted to expand the range of the
Roman numeral conversion functions. Normally, no character in a Roman
numeral can be repeated more than three times in a row. But the Romans
were willing to make an exception to that rule by having 4 `M`
characters in a row to represent `4000`. If you make this change,
youll be able to expand the range of convertible numbers from
`1..3999` to `1..4999`. But first, you need to make some changes to
your test cases.
[`download `roman8.py``_]

::

     `class KnownValues(unittest.TestCase):
        known_values = ( (1, 'I'),
                          .
                          .
                          .
                         (3999, 'MMMCMXCIX'),
                         (4000, 'MMMM'),                                      ①
                         (4500, 'MMMMD'),
                         (4888, 'MMMMDCCCLXXXVIII'),
                         (4999, 'MMMMCMXCIX') )
    
    class ToRomanBadInput(unittest.TestCase):
        def test_too_large(self):
            '''to_roman should fail with large input'''
            self.assertRaises(roman8.OutOfRangeError, roman8.to_roman, 5000)  ②
    
        .
        .
        .
    
    class FromRomanBadInput(unittest.TestCase):
        def test_too_many_repeated_numerals(self):
            '''from_roman should fail with too many repeated numerals'''
            for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):     ③
                self.assertRaises(roman8.InvalidRomanNumeralError, roman8.from_roman, s)
    
        .
        .
        .
    
    class RoundtripCheck(unittest.TestCase):
        def test_roundtrip(self):
            '''from_roman(to_roman(n))==n for all n'''
            for integer in range(1, 5000):                                    ④
                numeral = roman8.to_roman(integer)
                result = roman8.from_roman(numeral)
                self.assertEqual(integer, result)`



#. The existing known values dont change (theyre all still reasonable
values to test), but you need to add a few more in the `4000` range.
Here Ive included `4000` (the shortest), `4500` (the second shortest),
`4888` (the longest), and `4999` (the largest).
#. The definition of large input has changed. This test used to call
`to_roman()` with `4000` and expect an error; now that `4000-4999` are
good values, you need to bump this up to `5000`.
#. The definition of too many repeated numerals has also changed. This
test used to call `from_roman()` with `'MMMM'` and expect an error;
now that `MMMM` is considered a valid Roman numeral, you need to bump
this up to `'MMMMM'`.
#. The sanity check loops through every number in the range, from `1`
   to `3999`. Since the range has now expanded, this `for` loop need to
   be updated as well to go up to `4999`.


Now your test cases are up to date with the new requirements, but your
code is not, so you expect several of the test cases to fail.

::

    
    you@localhost:~/diveintopython3/examples$ python3 romantest9.py -v
    from_roman should fail with blank string ... ok
    from_roman should fail with malformed antecedents ... ok
    from_roman should fail with non-string input ... ok
    from_roman should fail with repeated pairs of numerals ... ok
    from_roman should fail with too many repeated numerals ... ok
    from_roman should give known result with known input ... ERROR          ①
    to_roman should give known result with known input ... ERROR            ②
    from_roman(to_roman(n))==n for all n ... ERROR                          ③
    to_roman should fail with negative input ... ok
    to_roman should fail with non-integer input ... ok
    to_roman should fail with large input ... ok
    to_roman should fail with 0 input ... ok
    
    ======================================================================
    ERROR: from_roman should give known result with known input
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "romantest9.py", line 82, in test_from_roman_known_values
        result = roman9.from_roman(numeral)
      File "C:\home\diveintopython3\examples\roman9.py", line 60, in from_roman
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    roman9.InvalidRomanNumeralError: Invalid Roman numeral: MMMM
    
    ======================================================================
    ERROR: to_roman should give known result with known input
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "romantest9.py", line 76, in test_to_roman_known_values
        result = roman9.to_roman(integer)
      File "C:\home\diveintopython3\examples\roman9.py", line 42, in to_roman
        raise OutOfRangeError('number out of range (must be 0..3999)')
    roman9.OutOfRangeError: number out of range (must be 0..3999)
    
    ======================================================================
    ERROR: from_roman(to_roman(n))==n for all n
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "romantest9.py", line 131, in testSanity
        numeral = roman9.to_roman(integer)
      File "C:\home\diveintopython3\examples\roman9.py", line 42, in to_roman
        raise OutOfRangeError('number out of range (must be 0..3999)')
    roman9.OutOfRangeError: number out of range (must be 0..3999)
    
    ----------------------------------------------------------------------
    Ran 12 tests in 0.171s
    
    FAILED (errors=3)



#. The `from_roman()` known values test will fail as soon as it hits
`'MMMM'`, because `from_roman()` still thinks this is an invalid Roman
numeral.
#. The `to_roman()` known values test will fail as soon as it hits
`4000`, because `to_roman()` still thinks this is out of range.
#. The roundtrip check will also fail as soon as it hits `4000`,
   because `to_roman()` still thinks this is out of range.


Now that you have test cases that fail due to the new requirements,
you can think about fixing the code to bring it in line with the test
cases. (When you first start coding unit tests, it might feel strange
that the code being tested is never ahead of the test cases. While its
behind, you still have some work to do, and as soon as it catches up
to the test cases, you stop coding. After you get used to it, youll
wonder how you ever programmed without tests.)
[`download `roman9.py``_]

::

     `roman_numeral_pattern = re.compile('''
        ^                   # beginning of string
        M{0,4}              # thousands - 0 to 4 Ms  ①
        (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                            #            or 500-800 (D, followed by 0 to 3 Cs)
        (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                            #        or 50-80 (L, followed by 0 to 3 Xs)
        (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                            #        or 5-8 (V, followed by 0 to 3 Is)
        $                   # end of string
        ''', re.VERBOSE)
    
    def to_roman(n):
        '''convert integer to Roman numeral'''
        if not isinstance(n, int):
            raise NotIntegerError('non-integers can not be converted')
        if not (0 < n < 5000):                        ②
            raise OutOfRangeError('number out of range (must be 1..4999)')
    
        result = ''
        for numeral, integer in roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result
    
    def from_roman(s):
        .
        .
        .`



#. You dont need to make any changes to the `from_roman()` function at
all. The only change is to roman_numeral_pattern . If you look
closely, youll notice that I changed the maximum number of optional
`M` characters from `3` to `4` in the first section of the regular
expression. This will allow the Roman numeral equivalents of `4999`
instead of `3999`. The actual `from_roman()` function is completely
generic; it just looks for repeated Roman numeral characters and adds
them up, without caring how many times they repeat. The only reason it
didnt handle `'MMMM'` before is that you explicitly stopped it with
the regular expression pattern matching.
#. The `to_roman()` function only needs one small change, in the range
   check. Where you used to check `0 < n < 4000`, you now check `0 < n <
   5000`. And you change the error message that you `raise` to reflect
   the new acceptable range ( `1..4999` instead of `1..3999`). You dont
   need to make any changes to the rest of the function; it handles the
   new cases already. (It merrily adds `'M'` for each thousand that it
   finds; given `4000`, it will spit out `'MMMM'`. The only reason it
   didnt do this before is that you explicitly stopped it with the range
   check.)


You may be skeptical that these two small changes are all that you
need. Hey, dont take my word for it; see for yourself.

::

    
    you@localhost:~/diveintopython3/examples$ python3 romantest9.py -v
    from_roman should fail with blank string ... ok
    from_roman should fail with malformed antecedents ... ok
    from_roman should fail with non-string input ... ok
    from_roman should fail with repeated pairs of numerals ... ok
    from_roman should fail with too many repeated numerals ... ok
    from_roman should give known result with known input ... ok
    to_roman should give known result with known input ... ok
    from_roman(to_roman(n))==n for all n ... ok
    to_roman should fail with negative input ... ok
    to_roman should fail with non-integer input ... ok
    to_roman should fail with large input ... ok
    to_roman should fail with 0 input ... ok
    
    ----------------------------------------------------------------------
    Ran 12 tests in 0.203s
    
    OK  ①



#. All the test cases pass. Stop coding.


Comprehensive unit testing means never having to rely on a programmer
who says Trust me.
⁂


Refactoring
-----------

The best thing about comprehensive unit testing is not the feeling you
get when all your test cases finally pass, or even the feeling you get
when someone else blames you for breaking their code and you can
actually *prove* that you didnt. The best thing about unit testing is
that it gives you the freedom to refactor mercilessly.
Refactoring is the process of taking working code and making it work
better. Usually, better means faster, although it can also mean using
less memory, or using less disk space, or simply more elegantly.
Whatever it means to you, to your project, in your environment,
refactoring is important to the long-term health of any program.
Here, better means both faster and easier to maintain. Specifically,
the `from_roman()` function is slower and more complex than Id like,
because of that big nasty regular expression that you use to validate
Roman numerals. Now, you might think, Sure, the regular expression is
big and hairy, but how else am I supposed to validate that an
arbitrary string is a valid a Roman numeral?
Answer: theres only 5000 of them; why dont you just build a lookup
table? This idea gets even better when you realize that *you dont need
to use regular expressions at all*. As you build the lookup table for
converting integers to Roman numerals, you can build the reverse
lookup table to convert Roman numerals to integers. By the time you
need to check whether an arbitrary string is a valid Roman numeral,
you will have collected all the valid Roman numerals. Validating is
reduced to a single dictionary lookup.
And best of all, you already have a complete set of unit tests. You
can change over half the code in the module, but the unit tests will
stay the same. That means you can proveto yourself and to othersthat
the new code works just as well as the original.
[`download `roman10.py``_]

::

     `class OutOfRangeError(ValueError): pass
    class NotIntegerError(ValueError): pass
    class InvalidRomanNumeralError(ValueError): pass
    
    roman_numeral_map = (('M',  1000),
                         ('CM', 900),
                         ('D',  500),
                         ('CD', 400),
                         ('C',  100),
                         ('XC', 90),
                         ('L',  50),
                         ('XL', 40),
                         ('X',  10),
                         ('IX', 9),
                         ('V',  5),
                         ('IV', 4),
                         ('I',  1))
    
    to_roman_table = [ None ]
    from_roman_table = {}
    
    def to_roman(n):
        '''convert integer to Roman numeral'''
        if not (0 < n < 5000):
            raise OutOfRangeError('number out of range (must be 1..4999)')
        if int(n) != n:
            raise NotIntegerError('non-integers can not be converted')
        return to_roman_table[n]
    
    def from_roman(s):
        '''convert Roman numeral to integer'''
        if not isinstance(s, str):
            raise InvalidRomanNumeralError('Input must be a string')
        if not s:
            raise InvalidRomanNumeralError('Input can not be blank')
        if s not in from_roman_table:
            raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
        return from_roman_table[s]
    
    def build_lookup_tables():
        def to_roman(n):
            result = ''
            for numeral, integer in roman_numeral_map:
                if n >= integer:
                    result = numeral
                    n -= integer
                    break
            if n > 0:
                result += to_roman_table[n]
            return result
    
        for integer in range(1, 5000):
            roman_numeral = to_roman(integer)
            to_roman_table.append(roman_numeral)
            from_roman_table[roman_numeral] = integer
    
    build_lookup_tables()`


Lets break that down into digestable pieces. Arguably, the most
important line is the last one:

::

     `build_lookup_tables()`


You will note that is a function call, but theres no `if` statement
around it. This is not an `if __name__ == '__main__'` block; it gets
called *when the module is imported*. (It is important to understand
that modules are only imported once, then cached. If you import an
already-imported module, it does nothing. So this code will only get
called the first time you import this module.)
So what does the `build_lookup_tables()` function do? Im glad you
asked.

::

     `to_roman_table = [ None ]
    from_roman_table = {}
    .
    .
    .
    def build_lookup_tables():
        def to_roman(n):                                ①
            result = ''
            for numeral, integer in roman_numeral_map:
                if n >= integer:
                    result = numeral
                    n -= integer
                    break
            if n > 0:
                result += to_roman_table[n]
            return result
    
        for integer in range(1, 5000):
            roman_numeral = to_roman(integer)          ②
            to_roman_table.append(roman_numeral)       ③
            from_roman_table[roman_numeral] = integer`



#. This is a clever bit of programming perhaps too clever. The
`to_roman()` function is defined above; it looks up values in the
lookup table and returns them. But the `build_lookup_tables()`
function redefines the `to_roman()` function to actually do work (like
the previous examples did, before you added a lookup table). Within
the `build_lookup_tables()` function, calling `to_roman()` will call
this redefined version. Once the `build_lookup_tables()` function
exits, the redefined version disappearsit is only defined in the local
scope of the `build_lookup_tables()` function.
#. This line of code will call the redefined `to_roman()` function,
which actually calculates the Roman numeral.
#. Once you have the result (from the redefined `to_roman()`
   function), you add the integer and its Roman numeral equivalent to
   both lookup tables.


Once the lookup tables are built, the rest of the code is both easy
and fast.

::

     `def to_roman(n):
        '''convert integer to Roman numeral'''
        if not (0 < n < 5000):
            raise OutOfRangeError('number out of range (must be 1..4999)')
        if int(n) != n:
            raise NotIntegerError('non-integers can not be converted')
        return to_roman_table[n]                                            ①
    
    def from_roman(s):
        '''convert Roman numeral to integer'''
        if not isinstance(s, str):
            raise InvalidRomanNumeralError('Input must be a string')
        if not s:
            raise InvalidRomanNumeralError('Input can not be blank')
        if s not in from_roman_table:
            raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
        return from_roman_table[s]                                          ②`



#. After doing the same bounds checking as before, the `to_roman()`
function simply finds the appropriate value in the lookup table and
returns it.
#. Similarly, the `from_roman()` function is reduced to some bounds
   checking and one line of code. No more regular expressions. No more
   looping. O(1) conversion to and from Roman numerals.


But does it work? Why yes, yes it does. And I can prove it.

::

    
    you@localhost:~/diveintopython3/examples$ python3 romantest10.py -v
    from_roman should fail with blank string ... ok
    from_roman should fail with malformed antecedents ... ok
    from_roman should fail with non-string input ... ok
    from_roman should fail with repeated pairs of numerals ... ok
    from_roman should fail with too many repeated numerals ... ok
    from_roman should give known result with known input ... ok
    to_roman should give known result with known input ... ok
    from_roman(to_roman(n))==n for all n ... ok
    to_roman should fail with negative input ... ok
    to_roman should fail with non-integer input ... ok
    to_roman should fail with large input ... ok
    to_roman should fail with 0 input ... ok
    
    ----------------------------------------------------------------------
    Ran 12 tests in 0.031s                                                  ①
    
    OK



#. Not that you asked, but its fast, too! Like, almost 10 as fast. Of
   course, its not entirely a fair comparison, because this version takes
   longer to import (when it builds the lookup tables). But since the
   import is only done once, the startup cost is amortized over all the
   calls to the `to_roman()` and `from_roman()` functions. Since the
   tests make several thousand function calls (the roundtrip test alone
   makes 10,000), this savings adds up in a hurry!


The moral of the story?

+ Simplicity is a virtue.
+ Especially when regular expressions are involved.
+ Unit tests can give you the confidence to do large-scale
  refactoring.


⁂


Summary
-------

Unit testing is a powerful concept which, if properly implemented, can
both reduce maintenance costs and increase flexibility in any long-
term project. It is also important to understand that unit testing is
not a panacea, a Magic Problem Solver, or a silver bullet. Writing
good test cases is hard, and keeping them up to date takes discipline
(especially when customers are screaming for critical bug fixes). Unit
testing is not a replacement for other forms of testing, including
functional testing, integration testing, and user acceptance testing.
But it is feasible, and it does work, and once youve seen it work,
youll wonder how you ever got along without it.
These few chapters have covered a lot of ground, and much of it wasnt
even Python-specific. There are unit testing frameworks for many
languages, all of which require you to understand the same basic
concepts:

+ Designing test cases that are specific, automated, and independent
+ Writing test cases *before* the code they are testing
+ Writing tests that test good input and check for proper results
+ Writing tests that test bad input and check for proper failure
responses
+ Writing and updating test cases to reflect new requirements
+ Refactoring mercilessly to improve performance, scalability,
  readability, maintainability, or whatever other -ility youre lacking


`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _roman8.py: examples/roman8.py
.. _Home: index.html
.. _roman10.py: examples/roman10.py
.. _ric Chopin: http://en.wikiquote.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin
.. _x261E;: files.html
.. _string formatting: strings.html#formatting-strings
.. _Mark Pilgrim: about.html
.. _Dive Into Python 3: table-of-contents.html#refactoring
.. _roman9.py: examples/roman9.py
.. _x261C;: unit-testing.html


