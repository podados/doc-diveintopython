

Case Study: Porting `chardet` to Python 3
=========================================

Difficulty level: ♦♦♦♦♦

❝ Words, words. They're all we have to go on. ❞
`Rosencrantz and Guildenstern are Dead`_


Diving In
---------

Question: whats the #1 cause of gibberish text on the web, in your
inbox, and across every computer system ever written? Its character
encoding. In the `Strings`_ chapter, I talked about the history of
character encoding and the creation of Unicode, the one encoding to
rule them all. Id love it if I never had to see a gibberish character
on a web page again, because all authoring systems stored accurate
encoding information, all transfer protocols were Unicode-aware, and
every system that handled text maintained perfect fidelity when
converting between encodings.
Id also like a pony.
A Unicode pony.
A Unipony, as it were.
Ill settle for character encoding auto-detection.

⁂


What is Character Encoding Auto-Detection?
------------------------------------------

It means taking a sequence of bytes in an unknown character encoding,
and attempting to determine the encoding so you can read the text. Its
like cracking a code when you dont have the decryption key.


Isnt That Impossible?
~~~~~~~~~~~~~~~~~~~~~

In general, yes. However, some encodings are optimized for specific
languages, and languages are not random. Some character sequences pop
up all the time, while other sequences make no sense. A person fluent
in English who opens a newspaper and finds txzqJv 2!dasd0a QqdKjvz
will instantly recognize that that isnt English (even though it is
composed entirely of English letters). By studying lots of typical
text, a computer algorithm can simulate this kind of fluency and make
an educated guess about a texts language.
In other words, encoding detection is really language detection,
combined with knowledge of which languages tend to use which character
encodings.


Does Such An Algorithm Exist?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As it turns out, yes. All major browsers have character encoding auto-
detection, because the web is full of pages that have no encoding
information whatsoever. `Mozilla Firefox contains an encoding auto-
detection library`_ which is open source. `I ported the library to
Python 2`_ and dubbed it the `chardet` module. This chapter will take
you step-by-step through the process of porting the `chardet` module
from Python 2 to Python 3.

⁂


Introducing The `chardet` Module
--------------------------------

Before we set off porting the code, it would help if you understood
how the code worked! This is a brief guide to navigating the code
itself. The `chardet` library is too large to include inline here, but
you can `download it from chardet.feedparser.org`_. Encoding
detection is really language detection in drag.
The main entry point for the detection algorithm is
`universaldetector.py`, which has one class, `UniversalDetector`. (You
might think the main entry point is the `detect` function in
`chardet/__init__.py`, but thats really just a convenience function
that creates a `UniversalDetector` object, calls it, and returns its
result.)
There are 5 categories of encodings that `UniversalDetector` handles:

#. UTF-n with a Byte Order Mark ( BOM ). This includes UTF-8 , both
   Big-Endian and Little-Endian variants of UTF-16 , and all 4 byte-order
   variants of UTF-32 .
#. Escaped encodings, which are entirely 7-bit ASCII compatible, where
   non- ASCII characters start with an escape sequence. Examples:
   ISO-2022-JP (Japanese) and HZ-GB-2312 (Chinese).
#. Multi-byte encodings, where each character is represented by a
   variable number of bytes. Examples: Big5 (Chinese), SHIFT_JIS
   (Japanese), EUC-KR (Korean), and UTF-8 without a BOM .
#. Single-byte encodings, where each character is represented by one
   byte. Examples: KOI8-R (Russian), windows-1255 (Hebrew), and TIS-620
   (Thai).
#. windows-1252 , which is used primarily on Microsoft Windows by
   middle managers who wouldnt know a character encoding from a hole in
   the ground.



UTF-n With A BOM
~~~~~~~~~~~~~~~~

If the text starts with a BOM , we can reasonably assume that the text
is encoded in UTF-8 , UTF-16 , or UTF-32 . (The BOM will tell us
exactly which one; thats what its for.) This is handled inline in
`UniversalDetector`, which returns the result immediately without any
further processing.


Escaped Encodings
~~~~~~~~~~~~~~~~~

If the text contains a recognizable escape sequence that might
indicate an escaped encoding, `UniversalDetector` creates an
`EscCharSetProber` (defined in `escprober.py`) and feeds it the text.
`EscCharSetProber` creates a series of state machines, based on models
of HZ-GB-2312 , ISO-2022-CN , ISO-2022-JP , and ISO-2022-KR (defined
in `escsm.py`). `EscCharSetProber` feeds the text to each of these
state machines, one byte at a time. If any state machine ends up
uniquely identifying the encoding, `EscCharSetProber` immediately
returns the positive result to `UniversalDetector`, which returns it
to the caller. If any state machine hits an illegal sequence, it is
dropped and processing continues with the other state machines.


Multi-Byte Encodings
~~~~~~~~~~~~~~~~~~~~

Assuming no BOM , `UniversalDetector` checks whether the text contains
any high-bit characters. If so, it creates a series of probers for
detecting multi-byte encodings, single-byte encodings, and as a last
resort, `windows-1252`.
The multi-byte encoding prober, `MBCSGroupProber` (defined in
`mbcsgroupprober.py`), is really just a shell that manages a group of
other probers, one for each multi-byte encoding: Big5 , GB2312 , EUC-
TW , EUC-KR , EUC-JP , SHIFT_JIS , and UTF-8 . `MBCSGroupProber` feeds
the text to each of these encoding-specific probers and checks the
results. If a prober reports that it has found an illegal byte
sequence, it is dropped from further processing (so that, for
instance, any subsequent calls to `UniversalDetector`. `feed()` will
skip that prober). If a prober reports that it is reasonably confident
that it has detected the encoding, `MBCSGroupProber` reports this
positive result to `UniversalDetector`, which reports the result to
the caller.
Most of the multi-byte encoding probers are inherited from
`MultiByteCharSetProber` (defined in `mbcharsetprober.py`), and simply
hook up the appropriate state machine and distribution analyzer and
let `MultiByteCharSetProber` do the rest of the work.
`MultiByteCharSetProber` runs the text through the encoding-specific
state machine, one byte at a time, to look for byte sequences that
would indicate a conclusive positive or negative result. At the same
time, `MultiByteCharSetProber` feeds the text to an encoding-specific
distribution analyzer.
The distribution analyzers (each defined in `chardistribution.py`) use
language-specific models of which characters are used most frequently.
Once `MultiByteCharSetProber` has fed enough text to the distribution
analyzer, it calculates a confidence rating based on the number of
frequently-used characters, the total number of characters, and a
language-specific distribution ratio. If the confidence is high
enough, `MultiByteCharSetProber` returns the result to
`MBCSGroupProber`, which returns it to `UniversalDetector`, which
returns it to the caller.
The case of Japanese is more difficult. Single-character distribution
analysis is not always sufficient to distinguish between `EUC-JP` and
`SHIFT_JIS`, so the `SJISProber` (defined in `sjisprober.py`) also
uses 2-character distribution analysis. `SJISContextAnalysis` and
`EUCJPContextAnalysis` (both defined in `jpcntx.py` and both
inheriting from a common `JapaneseContextAnalysis` class) check the
frequency of Hiragana syllabary characters within the text. Once
enough text has been processed, they return a confidence level to
`SJISProber`, which checks both analyzers and returns the higher
confidence level to `MBCSGroupProber`.


Single-Byte Encodings
~~~~~~~~~~~~~~~~~~~~~

Seriously, wheres my Unicode pony?

The single-byte encoding prober, `SBCSGroupProber` (defined in
`sbcsgroupprober.py`), is also just a shell that manages a group of
other probers, one for each combination of single-byte encoding and
language: `windows-1251`, `KOI8-R`, `ISO-8859-5`, `MacCyrillic`,
`IBM855`, and `IBM866` (Russian); `ISO-8859-7` and `windows-1253`
(Greek); `ISO-8859-5` and `windows-1251` (Bulgarian); `ISO-8859-2` and
`windows-1250` (Hungarian); `TIS-620` (Thai); `windows-1255` and
`ISO-8859-8` (Hebrew).
`SBCSGroupProber` feeds the text to each of these encoding+language-
specific probers and checks the results. These probers are all
implemented as a single class, `SingleByteCharSetProber` (defined in
`sbcharsetprober.py`), which takes a language model as an argument.
The language model defines how frequently different 2-character
sequences appear in typical text. `SingleByteCharSetProber` processes
the text and tallies the most frequently used 2-character sequences.
Once enough text has been processed, it calculates a confidence level
based on the number of frequently-used sequences, the total number of
characters, and a language-specific distribution ratio.
Hebrew is handled as a special case. If the text appears to be Hebrew
based on 2-character distribution analysis, `HebrewProber` (defined in
`hebrewprober.py`) tries to distinguish between Visual Hebrew (where
the source text actually stored backwards line-by-line, and then
displayed verbatim so it can be read from right to left) and Logical
Hebrew (where the source text is stored in reading order and then
rendered right-to-left by the client). Because certain characters are
encoded differently based on whether they appear in the middle of or
at the end of a word, we can make a reasonable guess about direction
of the source text, and return the appropriate encoding (
`windows-1255` for Logical Hebrew, or `ISO-8859-8` for Visual Hebrew).


`windows-1252`
~~~~~~~~~~~~~~

If `UniversalDetector` detects a high-bit character in the text, but
none of the other multi-byte or single-byte encoding probers return a
confident result, it creates a `Latin1Prober` (defined in
`latin1prober.py`) to try to detect English text in a `windows-1252`
encoding. This detection is inherently unreliable, because English
letters are encoded in the same way in many different encodings. The
only way to distinguish `windows-1252` is through commonly used
symbols like smart quotes, curly apostrophes, copyright symbols, and
the like. `Latin1Prober` automatically reduces its confidence rating
to allow more accurate probers to win if at all possible.
⁂


Running `2to3`
--------------

Were going to migrate the `chardet` module from Python 2 to Python 3.
Python 3 comes with a utility script called `2to3`, which takes your
actual Python 2 source code as input and auto-converts as much as it
can to Python 3. In some cases this is easya function was renamed or
moved to a different modulebut in other cases it can get pretty
complex. To get a sense of all that it *can* do, refer to the
appendix, `Porting code to Python 3 with `2to3``_. In this chapter,
well start by running `2to3` on the `chardet` package, but as youll
see, there will still be a lot of work to do after the automated tools
have performed their magic.
The main `chardet` package is split across several different files,
all in the same directory. The `2to3` script makes it easy to convert
multiple files at once: just pass a directory as a command line
argument, and `2to3` will convert each of the files in turn.

::

    C:\home\chardet> python c:\Python30\Tools\Scripts\2to3.py -w chardet\
    RefactoringTool: Skipping implicit fixer: buffer
    RefactoringTool: Skipping implicit fixer: idioms
    RefactoringTool: Skipping implicit fixer: set_literal
    RefactoringTool: Skipping implicit fixer: ws_comma
    --- chardet\__init__.py (original)
    +++ chardet\__init__.py (refactored)
    @@ -18,7 +18,7 @@
     __version__ = "1.0.1"
    
     def detect(aBuf):
    -    import universaldetector
    +    from . import universaldetector
         u = universaldetector.UniversalDetector()
         u.reset()
         u.feed(aBuf)
    --- chardet\big5prober.py (original)
    +++ chardet\big5prober.py (refactored)
    @@ -25,10 +25,10 @@
     # 02110-1301  USA
     ######################### END LICENSE BLOCK #########################
    
    -from mbcharsetprober import MultiByteCharSetProber
    -from codingstatemachine import CodingStateMachine
    -from chardistribution import Big5DistributionAnalysis
    -from mbcssm import Big5SMModel
    +from .mbcharsetprober import MultiByteCharSetProber
    +from .codingstatemachine import CodingStateMachine
    +from .chardistribution import Big5DistributionAnalysis
    +from .mbcssm import Big5SMModel
    
     class Big5Prober(MultiByteCharSetProber):
         def __init__(self):
    --- chardet\chardistribution.py (original)
    +++ chardet\chardistribution.py (refactored)
    @@ -25,12 +25,12 @@
     # 02110-1301  USA
     ######################### END LICENSE BLOCK #########################
    
    -import constants
    -from euctwfreq import EUCTWCharToFreqOrder, EUCTW_TABLE_SIZE, EUCTW_TYPICAL_DISTRIBUTION_RATIO
    -from euckrfreq import EUCKRCharToFreqOrder, EUCKR_TABLE_SIZE, EUCKR_TYPICAL_DISTRIBUTION_RATIO
    -from gb2312freq import GB2312CharToFreqOrder, GB2312_TABLE_SIZE, GB2312_TYPICAL_DISTRIBUTION_RATIO
    -from big5freq import Big5CharToFreqOrder, BIG5_TABLE_SIZE, BIG5_TYPICAL_DISTRIBUTION_RATIO
    -from jisfreq import JISCharToFreqOrder, JIS_TABLE_SIZE, JIS_TYPICAL_DISTRIBUTION_RATIO
    +from . import constants
    +from .euctwfreq import EUCTWCharToFreqOrder, EUCTW_TABLE_SIZE, EUCTW_TYPICAL_DISTRIBUTION_RATIO
    +from .euckrfreq import EUCKRCharToFreqOrder, EUCKR_TABLE_SIZE, EUCKR_TYPICAL_DISTRIBUTION_RATIO
    +from .gb2312freq import GB2312CharToFreqOrder, GB2312_TABLE_SIZE, GB2312_TYPICAL_DISTRIBUTION_RATIO
    +from .big5freq import Big5CharToFreqOrder, BIG5_TABLE_SIZE, BIG5_TYPICAL_DISTRIBUTION_RATIO
    +from .jisfreq import JISCharToFreqOrder, JIS_TABLE_SIZE, JIS_TYPICAL_DISTRIBUTION_RATIO
    
     ENOUGH_DATA_THRESHOLD = 1024
     SURE_YES = 0.99
    .
    .
    . (it goes on like this for a while)
    .
    .
    RefactoringTool: Files that were modified:
    RefactoringTool: chardet\__init__.py
    RefactoringTool: chardet\big5prober.py
    RefactoringTool: chardet\chardistribution.py
    RefactoringTool: chardet\charsetgroupprober.py
    RefactoringTool: chardet\codingstatemachine.py
    RefactoringTool: chardet\constants.py
    RefactoringTool: chardet\escprober.py
    RefactoringTool: chardet\escsm.py
    RefactoringTool: chardet\eucjpprober.py
    RefactoringTool: chardet\euckrprober.py
    RefactoringTool: chardet\euctwprober.py
    RefactoringTool: chardet\gb2312prober.py
    RefactoringTool: chardet\hebrewprober.py
    RefactoringTool: chardet\jpcntx.py
    RefactoringTool: chardet\langbulgarianmodel.py
    RefactoringTool: chardet\langcyrillicmodel.py
    RefactoringTool: chardet\langgreekmodel.py
    RefactoringTool: chardet\langhebrewmodel.py
    RefactoringTool: chardet\langhungarianmodel.py
    RefactoringTool: chardet\langthaimodel.py
    RefactoringTool: chardet\latin1prober.py
    RefactoringTool: chardet\mbcharsetprober.py
    RefactoringTool: chardet\mbcsgroupprober.py
    RefactoringTool: chardet\mbcssm.py
    RefactoringTool: chardet\sbcharsetprober.py
    RefactoringTool: chardet\sbcsgroupprober.py
    RefactoringTool: chardet\sjisprober.py
    RefactoringTool: chardet\universaldetector.py
    RefactoringTool: chardet\utf8prober.py


Now run the `2to3` script on the testing harness, `test.py`.

::

    C:\home\chardet> python c:\Python30\Tools\Scripts\2to3.py -w test.py
    RefactoringTool: Skipping implicit fixer: buffer
    RefactoringTool: Skipping implicit fixer: idioms
    RefactoringTool: Skipping implicit fixer: set_literal
    RefactoringTool: Skipping implicit fixer: ws_comma
    --- test.py (original)
    +++ test.py (refactored)
    @@ -4,7 +4,7 @@
     count = 0
     u = UniversalDetector()
     for f in glob.glob(sys.argv[1]):
    -    print f.ljust(60),
    +    print(f.ljust(60), end=' ')
         u.reset()
         for line in file(f, 'rb'):
             u.feed(line)
    @@ -12,8 +12,8 @@
         u.close()
         result = u.result
         if result['encoding']:
    -        print result['encoding'], 'with confidence', result['confidence']
    +        print(result['encoding'], 'with confidence', result['confidence'])
         else:
    -        print '******** no result'
    +        print('******** no result')
         count += 1
    -print count, 'tests'
    +print(count, 'tests')
    RefactoringTool: Files that were modified:
    RefactoringTool: test.py


Well, that wasnt so hard. Just a few imports and print statements to
convert. Speaking of which, what *was* the problem with all those
import statements? To answer that, you need to understand how the
`chardet` module is split into multiple files.
⁂


A Short Digression Into Multi-File Modules
------------------------------------------

`chardet` is a multi-file module . I could have chosen to put all the
code in one file (named `chardet.py`), but I didnt. Instead, I made a
directory (named `chardet`), then I made an `__init__.py` file in that
directory. *If Python sees an `__init__.py` file in a directory, it
assumes that all of the files in that directory are part of the same
module.* The modules name is the name of the directory. Files within
the directory can reference other files within the same directory, or
even within subdirectories. (More on that in a minute.) But the entire
collection of files is presented to other Python code as a single
moduleas if all the functions and classes were in a single `.py` file.
What goes in the `__init__.py` file? Nothing. Everything. Something in
between. The `__init__.py` file doesnt need to define anything; it can
literally be an empty file. Or you can use it to define your main
entry point functions. Or you put all your functions in it. Or all but
one.
☞A directory with an `__init__.py` file is always treated as a
multi-file module. Without an `__init__.py` file, a directory is just
a directory of unrelated `.py` files.
Lets see how that works in practice.

::

    
    >>> import chardet
    >>> dir(chardet)             ①
    ['__builtins__', '__doc__', '__file__', '__name__',
     '__package__', '__path__', '__version__', 'detect']
    >>> chardet                  ②
    <module 'chardet' from 'C:\Python31\lib\site-packages\chardet\__init__.py'>



#. Other than the usual class attributes, the only thing in the
`chardet` module is a `detect()` function.
#. Heres your first clue that the `chardet` module is more than just a
   file: the module is listed as the `__init__.py` file within the
   `chardet/` directory.


Lets take a peek in that `__init__.py` file.

::

     `def detect(aBuf):                              ①
        from . import universaldetector            ②
        u = universaldetector.UniversalDetector()
        u.reset()
        u.feed(aBuf)
        u.close()
        return u.result`



#. The `__init__.py` file defines the `detect()` function, which is
   the main entry point into the `chardet` library.
#. But the `detect()` function hardly has any code! In fact, all it
   really does is import the `universaldetector` module and start using
   it. But where is `universaldetector` defined?


The answer lies in that odd-looking `import` statement:

::

    from . import universaldetector


Translated into English, that means import the `universaldetector`
module; thats in the same directory I am, where I is the
`chardet/__init__.py` file. This is called a relative import . Its a
way for the files within a multi-file module to reference each other,
without worrying about naming conflicts with other modules you may
have installed in `your import search path`_. This `import` statement
will *only* look for the `universaldetector` module within the
`chardet/` directory itself.
These two concepts `__init__.py` and relative importsmean that you can
break up your module into as many pieces as you like. The `chardet`
module comprises 36 `.py` files36! Yet all you need to do to start
using it is `import chardet`, then you can call the main
`chardet.detect()` function. Unbeknownst to your code, the `detect()`
function is actually defined in the `chardet/__init__.py` file. Also
unbeknownst to you, the `detect()` function uses a relative import to
reference a class defined in `chardet/universaldetector.py`, which in
turn uses relative imports on five other files, all contained in the
`chardet/` directory.
☞If you ever find yourself writing a large library in Python
(or more likely, when you realize that your small library has grown
into a large one), take the time to refactor it into a multi-file
module. Its one of the many things Python is good at, so take
advantage of it.
⁂


Fixing What `2to3` Cant
-----------------------


`False` is invalid syntax
~~~~~~~~~~~~~~~~~~~~~~~~~
You do have tests, right?
Now for the real test: running the test harness against the test
suite. Since the test suite is designed to cover all the possible code
paths, its a good way to test our ported code to make sure there arent
any bugs lurking anywhere.

::

    C:\home\chardet> python test.py tests\*\*
    Traceback (most recent call last):
      File "test.py", line 1, in <module>
        from chardet.universaldetector import UniversalDetector
      File "C:\home\chardet\chardet\universaldetector.py", line 51
        self.done = constants.False
                                  ^
    SyntaxError: invalid syntax


Hmm, a small snag. In Python 3, `False` is a reserved word, so you
cant use it as a variable name. Lets look at `constants.py` to see
where its defined. Heres the original version from `constants.py`,
before the `2to3` script changed it:

::

     `import __builtin__
    if not hasattr(__builtin__, 'False'):
        False = 0
        True = 1
    else:
        False = __builtin__.False
        True = __builtin__.True`


This piece of code is designed to allow this library to run under
older versions of Python 2. Prior to Python 2.3, Python had no built-
in `bool` type. This code detects the absence of the built-in
constants `True` and `False`, and defines them if necessary.
However, Python 3 will always have a `bool` type, so this entire code
snippet is unnecessary. The simplest solution is to replace all
instances of `constants.True` and `constants.False` with `True` and
`False`, respectively, then delete this dead code from `constants.py`.
So this line in `universaldetector.py`:

::

    self.done = constants.False


Becomes

::

    self.done = False


Ah, wasnt that satisfying? The code is shorter and more readable
already.


No module named `constants`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time to run `test.py` again and see how far it gets.

::

    C:\home\chardet> python test.py tests\*\*
    Traceback (most recent call last):
      File "test.py", line 1, in <module>
        from chardet.universaldetector import UniversalDetector
      File "C:\home\chardet\chardet\universaldetector.py", line 29, in <module>
        import constants, sys
    ImportError: No module named constants


Whats that you say? No module named `constants`? Of course theres a
module named `constants`. Its right there, in `chardet/constants.py`.
Remember when the `2to3` script fixed up all those import statements?
This library has a lot of relative importsthat is, modules that import
other modules within the same librarybut *the logic behind relative
imports has changed in Python 3*. In Python 2, you could just `import
constants` and it would look in the `chardet/` directory first. In
Python 3, `all import statements are absolute by default`_. If you
want to do a relative import in Python 3, you need to be explicit
about it:

::

    from . import constants


But wait. Wasnt the `2to3` script supposed to take care of these for
you? Well, it did, but this particular import statement combines two
different types of imports into one line: a relative import of the
`constants` module within the library, and an absolute import of the
`sys` module that is pre-installed in the Python standard library. In
Python 2, you could combine these into one import statement. In Python
3, you cant, and the `2to3` script is not smart enough to split the
import statement into two.
The solution is to split the import statement manually. So this two-
in-one import:

::

    import constants, sys


Needs to become two separate imports:

::

    from . import constants
    import sys


There are variations of this problem scattered throughout the
`chardet` library. In some places its `import constants, sys`; in
other places, its `import constants, re`. The fix is the same:
manually split the import statement into two lines, one for the
relative import, the other for the absolute import.
Onward!


Name 'file' is not defined
~~~~~~~~~~~~~~~~~~~~~~~~~~
open() is the new file(). PapayaWhip is the new black.
And here we go again, running `test.py` to try to execute our test
cases

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml
    Traceback (most recent call last):
      File "test.py", line 9, in <module>
        for line in file(f, 'rb'):
    NameError: name 'file' is not defined


This one surprised me, because Ive been using this idiom as long as I
can remember. In Python 2, the global `file()` function was an alias
for the `open()` function, which was the standard way of `opening text
files for reading`_. In Python 3, the global `file()` function no
longer exists, but the `open()` function still exists.
Thus, the simplest solution to the problem of the missing `file()` is
to call the `open()` function instead:

::

    for line in open(f, 'rb'):


And thats all I have to say about that.


Cant use a string pattern on a bytes-like object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now things are starting to get interesting. And by interesting, I mean
confusing as all hell.

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        u.feed(line)
      File "C:\home\chardet\chardet\universaldetector.py", line 98, in feed
        if self._highBitDetector.search(aBuf):
    TypeError: can't use a string pattern on a bytes-like object


To debug this, lets see what self._highBitDetector is. Its defined in
the __init__ method of the UniversalDetector class:

::

    class UniversalDetector:
        def __init__(self):
            self._highBitDetector = re.compile(r'[\x80-\xFF]')


This pre-compiles a regular expression designed to find non- ASCII
characters in the range 128255 (0x800xFF). Wait, thats not quite
right; I need to be more precise with my terminology. This pattern is
designed to find non- ASCII *bytes* in the range 128-255.
And therein lies the problem.
In Python 2, a string was an array of bytes whose character encoding
was tracked separately. If you wanted Python 2 to keep track of the
character encoding, you had to use a Unicode string ( `u''`) instead.
But in Python 3, a string is always what Python 2 called a Unicode
stringthat is, an array of Unicode characters (of possibly varying
byte lengths). Since this regular expression is defined by a string
pattern, it can only be used to search a stringagain, an array of
characters. But what were searching is not a string, its a byte array.
Looking at the traceback, this error occurred in
`universaldetector.py`:

::

     `def feed(self, aBuf):
        .
        .
        .
        if self._mInputState == ePureAscii:
            if self._highBitDetector.search(aBuf):`


And what is aBuf ? Lets backtrack further to a place that calls
`UniversalDetector.feed()`. One place that calls it is the test
harness, `test.py`.

::

     `u = UniversalDetector()
    .
    .
    .
    for line in open(f, 'rb'):
        u.feed(line)`

Not an array of characters, but an array of bytes.
And here we find our answer: in the `UniversalDetector.feed()` method,
aBuf is a line read from a file on disk. Look carefully at the
parameters used to open the file: `'rb'`. `'r'` is for read; OK, big
deal, were reading the file. Ah, but ` `'b'` is for binary.`_ Without
the `'b'` flag, this `for` loop would read the file, line by line, and
convert each line into a stringan array of Unicode charactersaccording
to the system default character encoding. But with the `'b'` flag,
this `for` loop reads the file, line by line, and stores each line
exactly as it appears in the file, as an array of bytes. That byte
array gets passed to `UniversalDetector.feed()`, and eventually gets
passed to the pre-compiled regular expression, self._highBitDetector ,
to search for high-bit characters. But we dont have characters; we
have bytes. Oops.
What we need this regular expression to search is not an array of
characters, but an array of bytes.
Once you realize that, the solution is not difficult. Regular
expressions defined with strings can search strings. Regular
expressions defined with byte arrays can search byte arrays. To define
a byte array pattern, we simply change the type of the argument we use
to define the regular expression to a byte array. (There is one other
case of this same problem, on the very next line.)

::

     `  class UniversalDetector:
          def __init__(self):
    -         self._highBitDetector = re.compile(r'[\x80-\xFF]')
    -         self._escDetector = re.compile(r'(\033|~{)')
    +         self._highBitDetector = re.compile(b'[\x80-\xFF]')
    +         self._escDetector = re.compile(b'(\033|~{)')
              self._mEscCharSetProber = None
              self._mCharSetProbers = []
              self.reset()`


Searching the entire codebase for other uses of the `re` module turns
up two more instances, in `charsetprober.py`. Again, the code is
defining regular expressions as strings but executing them on aBuf ,
which is a byte array. The solution is the same: define the regular
expression patterns as byte arrays.

::

     `  class CharSetProber:
          .
          .
          .
          def filter_high_bit_only(self, aBuf):
    -         aBuf = re.sub(r'([\x00-\x7F])+', ' ', aBuf)
    +         aBuf = re.sub(b'([\x00-\x7F])+', b' ', aBuf)
              return aBuf
        
          def filter_without_english_letters(self, aBuf):
    -         aBuf = re.sub(r'([A-Za-z])+', ' ', aBuf)
    +         aBuf = re.sub(b'([A-Za-z])+', b' ', aBuf)
              return aBuf`




Can't convert `'bytes'` object to `str` implicitly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Curiouser and curiouser

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        u.feed(line)
      File "C:\home\chardet\chardet\universaldetector.py", line 100, in feed
        elif (self._mInputState == ePureAscii) and self._escDetector.search(self._mLastChar + aBuf):
    TypeError: Can't convert 'bytes' object to str implicitly


Theres an unfortunate clash of coding style and Python interpreter
here. The `TypeError` could be anywhere on that line, but the
traceback doesnt tell you exactly where it is. It could be in the
first conditional or the second, and the traceback would look the
same. To narrow it down, you should split the line in half, like this:

::

     `elif (self._mInputState == ePureAscii) and \
        self._escDetector.search(self._mLastChar + aBuf):`


And re-run the test:

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        u.feed(line)
      File "C:\home\chardet\chardet\universaldetector.py", line 101, in feed
        self._escDetector.search(self._mLastChar + aBuf):
    TypeError: Can't convert 'bytes' object to str implicitly


Aha! The problem was not in the first conditional ( `self._mInputState
== ePureAscii`) but in the second one. So what could cause a
`TypeError` there? Perhaps youre thinking that the `search()` method
is expecting a value of a different type, but that wouldnt generate
this traceback. Python functions can take any value; if you pass the
right number of arguments, the function will execute. It may *crash*
if you pass it a value of a different type than its expecting, but if
that happened, the traceback would point to somewhere inside the
function. But this traceback says it never got as far as calling the
`search()` method. So the problem must be in that `+` operation, as
its trying to construct the value that it will eventually pass to the
`search()` method.
We know from previous debugging that aBuf is a byte array. So what is
`self._mLastChar`? Its an instance variable, defined in the `reset()`
method, which is actually called from the `__init__()` method.

::

     `class UniversalDetector:
        def __init__(self):
            self._highBitDetector = re.compile(b'[\x80-\xFF]')
            self._escDetector = re.compile(b'(\033|~{)')
            self._mEscCharSetProber = None
            self._mCharSetProbers = []
            self.reset()
    
        def reset(self):
            self.result = {'encoding': None, 'confidence': 0.0}
            self.done = False
            self._mStart = True
            self._mGotData = False
            self._mInputState = ePureAscii
            self._mLastChar = ''`


And now we have our answer. Do you see it? self._mLastChar is a
string, but aBuf is a byte array. And you cant concatenate a string to
a byte arraynot even a zero-length string.
So what is self._mLastChar anyway? In the `feed()` method, just a few
lines down from where the trackback occurred.

::

     `if self._mInputState == ePureAscii:
        if self._highBitDetector.search(aBuf):
            self._mInputState = eHighbyte
        elif (self._mInputState == ePureAscii) and \
                self._escDetector.search(self._mLastChar + aBuf):
            self._mInputState = eEscAscii
    
    self._mLastChar = aBuf[-1]`


The calling function calls this `feed()` method over and over again
with a few bytes at a time. The method processes the bytes it was
given (passed in as aBuf ), then stores the last byte in
self._mLastChar in case its needed during the next call. (In a multi-
byte encoding, the `feed()` method might get called with half of a
character, then called again with the other half.) But because aBuf is
now a byte array instead of a string, self._mLastChar needs to be a
byte array as well. Thus:

::

     `  def reset(self):
          .
          .
          .
    -     self._mLastChar = ''
    +     self._mLastChar = b''`


Searching the entire codebase for `mLastChar` turns up a similar
problem in `mbcharsetprober.py`, but instead of tracking the last
character, it tracks the last *two* characters. The
`MultiByteCharSetProber` class uses a list of 1-character strings to
track the last two characters. In Python 3, it needs to use a list of
integers, because its not really tracking characters, its tracking
bytes. (Bytes are just integers from `0-255`.)

::

     `  class MultiByteCharSetProber(CharSetProber):
          def __init__(self):
              CharSetProber.__init__(self)
              self._mDistributionAnalyzer = None
              self._mCodingSM = None
    -         self._mLastChar = ['\x00', '\x00']
    +         self._mLastChar = [0, 0]
    
          def reset(self):
              CharSetProber.reset(self)
              if self._mCodingSM:
                  self._mCodingSM.reset()
              if self._mDistributionAnalyzer:
                  self._mDistributionAnalyzer.reset()
    -         self._mLastChar = ['\x00', '\x00']
    +         self._mLastChar = [0, 0]`



Unsupported operand type(s) for +: `'int'` and `'bytes'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I have good news, and I have bad news. The good news is were making
progress

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        u.feed(line)
      File "C:\home\chardet\chardet\universaldetector.py", line 101, in feed
        self._escDetector.search(self._mLastChar + aBuf):
    TypeError: unsupported operand type(s) for +: 'int' and 'bytes'


The bad news is it doesnt always feel like progress.
But this is progress! Really! Even though the traceback calls out the
same line of code, its a different error than it used to be. Progress!
So whats the problem now? The last time I checked, this line of code
didnt try to concatenate an `int` with a byte array ( `bytes`). In
fact, you just spent a lot of time ensuring that self._mLastChar was a
byte array. How did it turn into an `int`?
The answer lies not in the previous lines of code, but in the
following lines.

::

     `if self._mInputState == ePureAscii:
        if self._highBitDetector.search(aBuf):
            self._mInputState = eHighbyte
        elif (self._mInputState == ePureAscii) and \
                self._escDetector.search(self._mLastChar + aBuf):
            self._mInputState = eEscAscii
    
    self._mLastChar = aBuf[-1]`

Each item in a string is a string. Each item in a byte array is an
integer.
This error doesnt occur the first time the `feed()` method gets
called; it occurs the *second time*, after self._mLastChar has been
set to the last byte of aBuf . Well, whats the problem with that?
Getting a single element from a byte array yields an integer, not a
byte array. To see the difference, follow me to the interactive shell:

::

    
    >>> aBuf = b'\xEF\xBB\xBF'         ①
    >>> len(aBuf)
    3
    >>> mLastChar = aBuf[-1]
    >>> mLastChar                      ②
    191
    >>> type(mLastChar)                ③
    <class 'int'>
    >>> mLastChar + aBuf               ④
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'bytes'
    >>> mLastChar = aBuf[-1:]          ⑤
    >>> mLastChar
    b'\xbf'
    >>> mLastChar + aBuf               ⑥
    b'\xbf\xef\xbb\xbf'



#. Define a byte array of length 3.
#. The last element of the byte array is 191.
#. Thats an integer.
#. Concatenating an integer with a byte array doesnt work. Youve now
replicated the error you just found in `universaldetector.py`.
#. Ah, heres the fix. Instead of taking the last element of the byte
array, use `list slicing`_ to create a new byte array containing just
the last element. That is, start with the last element and continue
the slice until the end of the byte array. Now mLastChar is a byte
array of length 1.
#. Concatenating a byte array of length 1 with a byte array of length
   3 returns a new byte array of length 4.


So, to ensure that the `feed()` method in `universaldetector.py`
continues to work no matter how often its called, you need to
initialize self._mLastChar as a 0-length byte array, then *make sure
it stays a byte array*.

::

     `              self._escDetector.search(self._mLastChar + aBuf):
              self._mInputState = eEscAscii
    
    - self._mLastChar = aBuf[-1]
    + self._mLastChar = aBuf[-1:]`



`ord()` expected string of length 1, but `int` found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tired yet? Youre almost there

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml                       ascii with confidence 1.0
    tests\Big5\0804.blogspot.com.xml
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        u.feed(line)
      File "C:\home\chardet\chardet\universaldetector.py", line 116, in feed
        if prober.feed(aBuf) == constants.eFoundIt:
      File "C:\home\chardet\chardet\charsetgroupprober.py", line 60, in feed
        st = prober.feed(aBuf)
      File "C:\home\chardet\chardet\utf8prober.py", line 53, in feed
        codingState = self._mCodingSM.next_state(c)
      File "C:\home\chardet\chardet\codingstatemachine.py", line 43, in next_state
        byteCls = self._mModel['classTable'][ord(c)]
    TypeError: ord() expected string of length 1, but int found


OK, so c is an `int`, but the `ord()` function was expecting a
1-character string. Fair enough. Where is c defined?

::

     `# codingstatemachine.py
    def next_state(self, c):
        # for each byte we get its class
        # if it is first byte, we also get byte length
        byteCls = self._mModel['classTable'][ord(c)]`


Thats no help; its just passed into the function. Lets pop the stack.

::

     `# utf8prober.py
    def feed(self, aBuf):
        for c in aBuf:
            codingState = self._mCodingSM.next_state(c)`


Do you see it? In Python 2, aBuf was a string, so c was a 1-character
string. (Thats what you get when you iterate over a stringall the
characters, one by one.) But now, aBuf is a byte array, so c is an
`int`, not a 1-character string. In other words, theres no need to
call the `ord()` function because c is already an `int`!
Thus:

::

      def next_state(self, c):
          # for each byte we get its class
          # if it is first byte, we also get byte length
    -     byteCls = self._mModel['classTable'][ord(c)]
    +     byteCls = self._mModel['classTable'][c]


Searching the entire codebase for instances of `ord(c)` uncovers
similar problems in `sbcharsetprober.py`

::

    # sbcharsetprober.py
    def feed(self, aBuf):
        if not self._mModel['keepEnglishLetter']:
            aBuf = self.filter_without_english_letters(aBuf)
        aLen = len(aBuf)
        if not aLen:
            return self.get_state()
        for c in aBuf:
            order = self._mModel['charToOrderMap'][ord(c)]


and `latin1prober.py`

::

    # latin1prober.py
    def feed(self, aBuf):
        aBuf = self.filter_with_english_letters(aBuf)
        for c in aBuf:
            charClass = Latin1_CharToClass[ord(c)]


c is iterating over aBuf , which means it is an integer, not a
1-character string. The solution is the same: change `ord(c)` to just
plain `c`.

::

      # sbcharsetprober.py
      def feed(self, aBuf):
          if not self._mModel['keepEnglishLetter']:
              aBuf = self.filter_without_english_letters(aBuf)
          aLen = len(aBuf)
          if not aLen:
              return self.get_state()
          for c in aBuf:
    -         order = self._mModel['charToOrderMap'][ord(c)]
    +         order = self._mModel['charToOrderMap'][c]
    
      # latin1prober.py
      def feed(self, aBuf):
          aBuf = self.filter_with_english_letters(aBuf)
          for c in aBuf:
    -         charClass = Latin1_CharToClass[ord(c)]
    +         charClass = Latin1_CharToClass[c]


Unorderable types: `int()` >= `str()`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lets go again.

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml                       ascii with confidence 1.0
    tests\Big5\0804.blogspot.com.xml
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        u.feed(line)
      File "C:\home\chardet\chardet\universaldetector.py", line 116, in feed
        if prober.feed(aBuf) == constants.eFoundIt:
      File "C:\home\chardet\chardet\charsetgroupprober.py", line 60, in feed
        st = prober.feed(aBuf)
      File "C:\home\chardet\chardet\sjisprober.py", line 68, in feed
        self._mContextAnalyzer.feed(self._mLastChar[2 - charLen :], charLen)
      File "C:\home\chardet\chardet\jpcntx.py", line 145, in feed
        order, charLen = self.get_order(aBuf[i:i+2])
      File "C:\home\chardet\chardet\jpcntx.py", line 176, in get_order
        if ((aStr[0] >= '\x81') and (aStr[0] <= '\x9F')) or \
    TypeError: unorderable types: int() >= str()


So whats this all about? Unorderable types? Once again, the difference
between byte arrays and strings is rearing its ugly head. Take a look
at the code:

::

    class SJISContextAnalysis(JapaneseContextAnalysis):
        def get_order(self, aStr):
            if not aStr: return -1, 1
            # find out current char's byte length
            if ((aStr[0] >= '\x81') and (aStr[0] <= '\x9F')) or \
               ((aStr[0] >= '\xE0') and (aStr[0] <= '\xFC')):
                charLen = 2
            else:
                charLen = 1


And where does aStr come from? Lets pop the stack:

::

    def feed(self, aBuf, aLen):
        .
        .
        .
        i = self._mNeedToSkipCharNum
        while i < aLen:
            order, charLen = self.get_order(aBuf[i:i+2])


Oh look, its our old friend, aBuf . As you might have guessed from
every other issue weve encountered in this chapter, aBuf is a byte
array. Here, the `feed()` method isnt just passing it on wholesale;
its slicing it. But as you saw earlier in this chapter, slicing a byte
array returns a byte array, so the aStr parameter that gets passed to
the `get_order()` method is still a byte array.
And what is this code trying to do with aStr ? Its taking the first
element of the byte array and comparing it to a string of length 1. In
Python 2, that worked, because aStr and aBuf were strings, and aStr[0]
would be a string, and you can compare strings for inequality. But in
Python 3, aStr and aBuf are byte arrays, aStr[0] is an integer, and
you cant compare integers and strings for inequality without
explicitly coercing one of them.
In this case, theres no need to make the code more complicated by
adding an explicit coercion. aStr[0] yields an integer; the things
youre comparing to are all constants. Lets change them from
1-character strings to integers. And while were at it, lets change
aStr to aBuf , since its not actually a string.

::

      class SJISContextAnalysis(JapaneseContextAnalysis):
    -     def get_order(self, aStr):
    -      if not aStr: return -1, 1
    +     def get_order(self, aBuf):
    +      if not aBuf: return -1, 1
              # find out current char's byte length
    -         if ((aStr[0] >= '\x81') and (aStr[0] <= '\x9F')) or \
    -            ((aBuf[0] >= '\xE0') and (aBuf[0] <= '\xFC')):
    +         if ((aBuf[0] >= 0x81) and (aBuf[0] <= 0x9F)) or \
    +            ((aBuf[0] >= 0xE0) and (aBuf[0] <= 0xFC)):
                  charLen = 2
              else:
                  charLen = 1
    
              # return its order if it is hiragana
    -      if len(aStr) > 1:
    -             if (aStr[0] == '\202') and \
    -                (aStr[1] >= '\x9F') and \
    -                (aStr[1] <= '\xF1'):
    -                return ord(aStr[1]) - 0x9F, charLen
    +      if len(aBuf) > 1:
    +             if (aBuf[0] == 202) and \
    +                (aBuf[1] >= 0x9F) and \
    +                (aBuf[1] <= 0xF1):
    +                return aBuf[1] - 0x9F, charLen
    
              return -1, charLen
    
      class EUCJPContextAnalysis(JapaneseContextAnalysis):
    -     def get_order(self, aStr):
    -      if not aStr: return -1, 1
    +     def get_order(self, aBuf):
    +      if not aBuf: return -1, 1
              # find out current char's byte length
    -         if (aStr[0] == '\x8E') or \
    -           ((aStr[0] >= '\xA1') and (aStr[0] <= '\xFE')):
    +         if (aBuf[0] == 0x8E) or \
    +           ((aBuf[0] >= 0xA1) and (aBuf[0] <= 0xFE)):
                  charLen = 2
    -         elif aStr[0] == '\x8F':
    +         elif aBuf[0] == 0x8F:
                  charLen = 3
              else:
                  charLen = 1
    
            # return its order if it is hiragana
    -    if len(aStr) > 1:
    -           if (aStr[0] == '\xA4') and \
    -              (aStr[1] >= '\xA1') and \
    -              (aStr[1] <= '\xF3'):
    -                 return ord(aStr[1]) - 0xA1, charLen
    +    if len(aBuf) > 1:
    +           if (aBuf[0] == 0xA4) and \
    +              (aBuf[1] >= 0xA1) and \
    +              (aBuf[1] <= 0xF3):
    +               return aBuf[1] - 0xA1, charLen
    
            return -1, charLen


Searching the entire codebase for occurrences of the `ord()` function
uncovers the same problem in `chardistribution.py` (specifically, in
the `EUCTWDistributionAnalysis`, `EUCKRDistributionAnalysis`,
`GB2312DistributionAnalysis`, `Big5DistributionAnalysis`,
`SJISDistributionAnalysis`, and `EUCJPDistributionAnalysis` classes.
In each case, the fix is similar to the change we made to the
`EUCJPContextAnalysis` and `SJISContextAnalysis` classes in
`jpcntx.py`.


Global name `'reduce'` is not defined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once more into the breach

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml                       ascii with confidence 1.0
    tests\Big5\0804.blogspot.com.xml
    Traceback (most recent call last):
      File "test.py", line 12, in <module>
        u.close()
      File "C:\home\chardet\chardet\universaldetector.py", line 141, in close
        proberConfidence = prober.get_confidence()
      File "C:\home\chardet\chardet\latin1prober.py", line 126, in get_confidence
        total = reduce(operator.add, self._mFreqCounter)
    NameError: global name 'reduce' is not defined


According to the official `Whats New In Python 3.0`_ guide, the
`reduce()` function has been moved out of the global namespace and
into the `functools` module. Quoting the guide: Use
`functools.reduce()` if you really need it; however, 99 percent of the
time an explicit `for` loop is more readable. You can read more about
the decision from Guido van Rossums weblog: `The fate of reduce() in
Python 3000`_.

::

    def get_confidence(self):
        if self.get_state() == constants.eNotMe:
            return 0.01
      
        total = reduce(operator.add, self._mFreqCounter)


The `reduce()` function takes two argumentsa function and a list
(strictly speaking, any iterable object will do)and applies the
function cumulatively to each item of the list. In other words, this
is a fancy and roundabout way of adding up all the items in a list and
returning the result.
This monstrosity was so common that Python added a global `sum()`
function.

::

      def get_confidence(self):
          if self.get_state() == constants.eNotMe:
              return 0.01
      
    -     total = reduce(operator.add, self._mFreqCounter)
    +     total = sum(self._mFreqCounter)


Since youre no longer using the `operator` module, you can remove that
`import` from the top of the file as well.

::

      from .charsetprober import CharSetProber
      from . import constants
    - import operator


I CAN HAZ TESTZ?

::

    C:\home\chardet> python test.py tests\*\*
    tests\ascii\howto.diveintomark.org.xml                       ascii with confidence 1.0
    tests\Big5\0804.blogspot.com.xml                             Big5 with confidence 0.99
    tests\Big5\blog.worren.net.xml                               Big5 with confidence 0.99
    tests\Big5\carbonxiv.blogspot.com.xml                        Big5 with confidence 0.99
    tests\Big5\catshadow.blogspot.com.xml                        Big5 with confidence 0.99
    tests\Big5\coolloud.org.tw.xml                               Big5 with confidence 0.99
    tests\Big5\digitalwall.com.xml                               Big5 with confidence 0.99
    tests\Big5\ebao.us.xml                                       Big5 with confidence 0.99
    tests\Big5\fudesign.blogspot.com.xml                         Big5 with confidence 0.99
    tests\Big5\kafkatseng.blogspot.com.xml                       Big5 with confidence 0.99
    tests\Big5\ke207.blogspot.com.xml                            Big5 with confidence 0.99
    tests\Big5\leavesth.blogspot.com.xml                         Big5 with confidence 0.99
    tests\Big5\letterlego.blogspot.com.xml                       Big5 with confidence 0.99
    tests\Big5\linyijen.blogspot.com.xml                         Big5 with confidence 0.99
    tests\Big5\marilynwu.blogspot.com.xml                        Big5 with confidence 0.99
    tests\Big5\myblog.pchome.com.tw.xml                          Big5 with confidence 0.99
    tests\Big5\oui-design.com.xml                                Big5 with confidence 0.99
    tests\Big5\sanwenji.blogspot.com.xml                         Big5 with confidence 0.99
    tests\Big5\sinica.edu.tw.xml                                 Big5 with confidence 0.99
    tests\Big5\sylvia1976.blogspot.com.xml                       Big5 with confidence 0.99
    tests\Big5\tlkkuo.blogspot.com.xml                           Big5 with confidence 0.99
    tests\Big5\tw.blog.xubg.com.xml                              Big5 with confidence 0.99
    tests\Big5\unoriginalblog.com.xml                            Big5 with confidence 0.99
    tests\Big5\upsaid.com.xml                                    Big5 with confidence 0.99
    tests\Big5\willythecop.blogspot.com.xml                      Big5 with confidence 0.99
    tests\Big5\ytc.blogspot.com.xml                              Big5 with confidence 0.99
    tests\EUC-JP\aivy.co.jp.xml                                  EUC-JP with confidence 0.99
    tests\EUC-JP\akaname.main.jp.xml                             EUC-JP with confidence 0.99
    tests\EUC-JP\arclamp.jp.xml                                  EUC-JP with confidence 0.99
    .
    .
    .
    316 tests


Holy crap, it actually works! *`/me does a little dance`_*
⁂


Summary
-------

What have we learned?

#. Porting any non-trivial amount of code from Python 2 to Python 3 is
   going to be a pain. Theres no way around it. Its hard.
#. The `automated `2to3` tool`_ is helpful as far as it goes, but it
   will only do the easy partsfunction renames, module renames, syntax
   changes. Its an impressive piece of engineering, but in the end its
   just an intelligent search-and-replace bot.
#. The #1 porting problem in this library was the difference between
   strings and bytes. In this case that seems obvious, since the whole
   point of the `chardet` library is to convert a stream of bytes into a
   string. But a stream of bytes comes up more often than you might
   think. Reading a file in binary mode? Youll get a stream of bytes.
   Fetching a web page? Calling a web API ? They return a stream of
   bytes, too.
#. *You* need to understand your program. Thoroughly. Preferably
   because you wrote it, but at the very least, you need to be
   comfortable with all its quirks and musty corners. The bugs are
   everywhere.
#. Test cases are essential. Dont port anything without them. The
   *only* reason I have any confidence that `chardet` works in Python 3
   is that I started with a test suite that exercised all major code
   paths. If you dont have any tests, write some tests before you start
   porting to Python 3. If you have a few tests, write more. If you have
   a lot of tests, then the real fun can begin.


`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _The fate of reduce() in Python 3000: 'http://www.artima.com/weblogs/viewpost.jsp?thread=98196'
.. _Mozilla Firefox contains an encoding auto-detection library: http://lxr.mozilla.org/seamonkey/source/extensions/universalchardet/src/base/
.. _Rosencrantz and Guildenstern are Dead: http://www.imdb.com/title/tt0100519/quotes
.. _list slicing: native-datatypes.html#slicinglists
.. _I ported the library to Python 2: http://chardet.feedparser.org/
.. _Dive Into Python 3: table-of-contents.html#case-study-porting-chardet-to-python-3
.. _ tool: porting-code-to-python-3-with-2to3.html
.. _/me does a little dance: http://www.hampsterdance.com/
.. _s New In Python 3.0: http://docs.python.org/3.0/whatsnew/3.0.html#builtins
.. _opening text files for reading: files.html#reading
.. _binary.: files.html#binary
.. _all import statements are absolute by default: http://www.python.org/dev/peps/pep-0328/
.. _Mark Pilgrim: about.html
.. _chardet.feedparser.org: http://chardet.feedparser.org/download/
.. _Strings: strings.html
.. _your import search path: your-first-python-program.html#importsearchpath


