
You are here: `Home`_ `Dive Into Python 3`_
Difficulty level: ♦♦♦♢♢


Files
=====

❝ A nine mile walk is no joke, especially in the rain. ❞
Harry Kemelman, The Nine Mile Walk


Diving In
---------

My Windows laptop had 38,493 files before I installed a single
application. Installing Python 3 added almost 3,000 files to that
total. Files are the primary storage paradigm of every major operating
system; the concept is so ingrained that most people would have
trouble `imagining an alternative`_. Your computer is, metaphorically
speaking, drowning in files.


Reading From Text Files
-----------------------

Before you can read from a file, you need to open it. Opening a file
in Python couldnt be easier:

::

     `a_file = open('examples/chinese.txt', encoding='utf-8')`


Python has a built-in `open()` function, which takes a filename as an
argument. Here the filename is `'examples/chinese.txt'`. There are
five interesting things about this filename:

#. Its not just the name of a file; its a combination of a directory
path and a filename. A hypothetical file-opening function could have
taken two argumentsa directory path and a filenamebut the `open()`
function only takes one. In Python, whenever you need a filename, you
can include some or all of a directory path as well.
#. The directory path uses a forward slash, but I didnt say what
operating system I was using. Windows uses backward slashes to denote
subdirectories, while Mac OS X and Linux use forward slashes. But in
Python, forward slashes always Just Work, even on Windows.
#. The directory path does not begin with a slash or a drive letter,
so it is called a relative path . Relative to what, you might ask?
Patience, grasshopper.
#. Its a string. All modern operating systems (even Windows!) use
Unicode to store the names of files and directories. Python 3 fully
supports non- ASCII pathnames.
#. It doesnt need to be on your local disk. You might have a network
   drive mounted. That file might be a figment of `an entirely virtual
   filesystem`_. If your computer considers it a file and can access it
   as a file, Python can open it.


But that call to the `open()` function didnt stop at the filename.
Theres another argument, called `encoding`. Oh dear, `that sounds
dreadfully familiar`_.


Character Encoding Rears Its Ugly Head
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bytes are bytes; `characters are an abstraction`_. A string is a
sequence of Unicode characters. But a file on disk is not a sequence
of Unicode characters; a file on disk is a sequence of bytes. So if
you read a text file from disk, how does Python convert that sequence
of bytes into a sequence of characters? It decodes the bytes according
to a specific character encoding algorithm and returns a sequence of
Unicode characters (otherwise known as a string).

::

    
    # This example was created on Windows. Other platforms may
    # behave differently, for reasons outlined below.
    >>> file = open('examples/chinese.txt')
    >>> a_string = file.read()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\Python31\lib\encodings\cp1252.py", line 23, in decode
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 28: character maps to <undefined>
    >>> 

The default encoding is platform-dependent.
What just happened? You didnt specify a character encoding, so Python
is forced to use the default encoding. Whats the default encoding? If
you look closely at the traceback, you can see that its dying in
`cp1252.py`, meaning that Python is using CP-1252 as the default
encoding here. (CP-1252 is a common encoding on computers running
Microsoft Windows.) The CP-1252 character set doesnt support the
characters that are in this file, so the read fails with an ugly
`UnicodeDecodeError`.
But wait, its worse than that! The default encoding is *platform-
dependent*, so this code *might* work on your computer (if your
default encoding is UTF-8 ), but then it will fail when you distribute
it to someone else (whose default encoding is different, like
CP-1252).
☞If you need to get the default character encoding, import the
`locale` module and call `locale.getpreferredencoding()`. On my
Windows laptop, it returns `'cp1252'`, but on my Linux box upstairs,
it returns `'UTF8'`. I cant even maintain consistency in my own house!
Your results may be different (even on Windows) depending on which
version of your operating system you have installed and how your
regional/language settings are configured. This is why its so
important to specify the encoding every time you open a file.


Stream Objects
~~~~~~~~~~~~~~

So far, all we know is that Python has a built-in function called
`open()`. The `open()` function returns a stream object , which has
methods and attributes for getting information about and manipulating
a stream of characters.

::

    
    >>> a_file = open('examples/chinese.txt', encoding='utf-8')
    >>> a_file.name                                              ①
    'examples/chinese.txt'
    >>> a_file.encoding                                          ②
    'utf-8'
    >>> a_file.mode                                              ③
    'r'



#. The `name` attribute reflects the name you passed in to the
`open()` function when you opened the file. It is not normalized to an
absolute pathname.
#. Likewise, `encoding` attribute reflects the encoding you passed in
to the `open()` function. If you didnt specify the encoding when you
opened the file (bad developer!) then the `encoding` attribute will
reflect `locale.getpreferredencoding()`.
#. The `mode` attribute tells you in which mode the file was opened.
   You can pass an optional mode parameter to the `open()` function. You
   didnt specify a mode when you opened this file, so Python defaults to
   `'r'`, which means open for reading only, in text mode. As youll see
   later in this chapter, the file mode serves several purposes;
   different modes let you write to a file, append to a file, or open a
   file in binary mode (in which you deal with bytes instead of strings).


☞The `documentation for the `open()` function`_ lists all the
possible file modes.


Reading Data From A Text File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you open a file for reading, youll probably want to read from it
at some point.

::

    
    >>> a_file = open('examples/chinese.txt', encoding='utf-8')
    >>> a_file.read()                                            ①
    'Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n'
    >>> a_file.read()                                            ②
    ''



#. Once you open a file (with the correct encoding), reading from it
is just a matter of calling the stream objects `read()` method. The
result is a string.
#. Perhaps somewhat surprisingly, reading the file again does not
   raise an exception. Python does not consider reading past end-of-file
   to be an error; it simply returns an empty string.

Always specify an `encoding` parameter when you open a file.
What if you want to re-read a file?

::

    
    # continued from the previous example
    >>> a_file.read()                      ①
    ''
    >>> a_file.seek(0)                     ②
    0
    >>> a_file.read(16)                    ③
    'Dive Into Python'
    >>> a_file.read(1)                     ④
    ' '
    >>> a_file.read(1)
    '是'
    >>> a_file.tell()                      ⑤
    20



#. Since youre still at the end of the file, further calls to the
stream objects `read()` method simply return an empty string.
#. The `seek()` method moves to a specific byte position in a file.
#. The `read()` method can take an optional parameter, the number of
characters to read.
#. If you like, you can even read one character at a time.
#. 16 + 1 + 1 = 20?


Lets try that again.

::

    
    # continued from the previous example
    >>> a_file.seek(17)                    ①
    17
    >>> a_file.read(1)                     ②
    '是'
    >>> a_file.tell()                      ③
    20



#. Move to the 17 th byte.
#. Read one character.
#. Now youre on the 20 th byte.


Do you see it yet? The `seek()` and `tell()` methods always count
*bytes*, but since you opened this file as text, the `read()` method
counts *characters*. Chinese characters `require multiple bytes to
encode in UTF-8 `_. The English characters in the file only require
one byte each, so you might be misled into thinking that the `seek()`
and `read()` methods are counting the same thing. But thats only true
for some characters.
But wait, it gets worse!

::

    
    >>> a_file.seek(18)                         ①
    18
    >>> a_file.read(1)                          ②
    Traceback (most recent call last):
      File "<pyshell#12>", line 1, in <module>
        a_file.read(1)
      File "C:\Python31\lib\codecs.py", line 300, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf8' codec can't decode byte 0x98 in position 0: unexpected code byte



#. Move to the 18 th byte and try to read one character.
#. Why does this fail? Because there isnt a character at the 18 th
   byte. The nearest character starts at the 17 th byte (and goes for
   three bytes). Trying to read a character from the middle will fail
   with a `UnicodeDecodeError`.




Closing Files
~~~~~~~~~~~~~

Open files consume system resources, and depending on the file mode,
other programs may not be able to access them. Its important to close
files as soon as youre finished with them.

::

    
    # continued from the previous example
    >>> a_file.close()


Well *that* was anticlimactic.
The stream object a_file still exists; calling its `close()` method
doesnt destroy the object itself. But its not terribly useful.

::

    
    # continued from the previous example
    >>> a_file.read()                           ①
    Traceback (most recent call last):
      File "<pyshell#24>", line 1, in <module>
        a_file.read()
    ValueError: I/O operation on closed file.
    >>> a_file.seek(0)                          ②
    Traceback (most recent call last):
      File "<pyshell#25>", line 1, in <module>
        a_file.seek(0)
    ValueError: I/O operation on closed file.
    >>> a_file.tell()                           ③
    Traceback (most recent call last):
      File "<pyshell#26>", line 1, in <module>
        a_file.tell()
    ValueError: I/O operation on closed file.
    >>> a_file.close()                          ④
    >>> a_file.closed                           ⑤
    True



#. You cant read from a closed file; that raises an `IOError`
exception.
#. You cant seek in a closed file either.
#. Theres no current position in a closed file, so the `tell()` method
also fails.
#. Perhaps surprisingly, calling the `close()` method on a stream
object whose file has been closed does *not* raise an exception. Its
just a no-op.
#. Closed stream objects do have one useful attribute: the `closed`
   attribute will confirm that the file is closed.




Closing Files Automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~
`try..finally` is good. `with` is better.
Stream objects have an explicit `close()` method, but what happens if
your code has a bug and crashes before you call `close()`? That file
could theoretically stay open for much longer than necessary. While
youre debugging on your local computer, thats not a big deal. On a
production server, maybe it is.
Python 2 had a solution for this: the `try..finally` block. That still
works in Python 3, and you may see it in other peoples code or in
older code that was `ported to Python 3`_. But Python 2.6 introduced a
cleaner solution, which is now the preferred solution in Python 3: the
`with` statement.

::

     `with open('examples/chinese.txt', encoding='utf-8') as a_file:
        a_file.seek(17)
        a_character = a_file.read(1)
        print(a_character)`


This code calls `open()`, but it never calls `a_file.close()`. The
`with` statement starts a code block, like an `if` statement or a
`for` loop. Inside this code block, you can use the variable a_file as
the stream object returned from the call to `open()`. All the regular
stream object methods are available `seek()`, `read()`, whatever you
need. When the `with` block ends, *Python calls `a_file.close()`
automatically*.
Heres the kicker: no matter how or when you exit the `with` block,
Python will close that file even if you exit it via an unhandled
exception. Thats right, even if your code raises an exception and your
entire program comes to a screeching halt, that file will get closed.
Guaranteed.
☞In technical terms, the `with` statement creates a runtime
context . In these examples, the stream object acts as a context
manager . Python creates the stream object a_file and tells it that it
is entering a runtime context. When the `with` code block is
completed, Python tells the stream object that it is exiting the
runtime context, and the stream object calls its own `close()` method.
See `Appendix B, Classes That Can Be Used in a `with` Block`_ for
details.
Theres nothing file-specific about the `with` statement; its just a
generic framework for creating runtime contexts and telling objects
that theyre entering and exiting a runtime context. If the object in
question is a stream object, then it does useful file-like things
(like closing the file automatically). But that behavior is defined in
the stream object, not in the `with` statement. There are lots of
other ways to use context managers that have nothing to do with files.
You can even create your own, as youll see later in this chapter.


Reading Data One Line At A Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A line of a text file is just what you think it isyou type a few words
and press ENTER , and now youre on a new line. A line of text is a
sequence of characters delimited by what exactly? Well, its
complicated, because text files can use several different characters
to mark the end of a line. Every operating system has its own
convention. Some use a carriage return character, others use a line
feed character, and some use both characters at the end of every line.
Now breathe a sigh of relief, because *Python handles line endings
automatically* by default. If you say, I want to read this text file
one line at a time, Python will figure out which kind of line ending
the text file uses and and it will all Just Work.
☞If you need fine-grained control over whats considered a line
ending, you can pass the optional `newline` parameter to the `open()`
function. See `the `open()` function documentation`_ for all the gory
details.
So, how do you actually do it? Read a file one line at a time, that
is. Its so simple, its beautiful.
[`download `oneline.py``_]

::

     `line_number = 0
    with open('examples/favorite-people.txt', encoding='utf-8') as a_file:  ①
        for a_line in a_file:                                               ②
            line_number += 1
            print('{:>4} {}'.format(line_number, a_line.rstrip()))          ③`



#. Using the `with` pattern, you safely open the file and let Python
close it for you.
#. To read a file one line at a time, use a `for` loop. Thats it.
Besides having explicit methods like `read()`, *the stream object is
also an `iterator`_* which spits out a single line every time you ask
for a value.
#. Using `the `format()` string method`_, you can print out the line
   number and the line itself. The format specifier `{:>4}` means print
   this argument right-justified within 4 spaces. The a_line variable
   contains the complete line, carriage returns and all. The `rstrip()`
   string method removes the trailing whitespace, including the carriage
   return characters.



::

    
    you@localhost:~/diveintopython3$ python3 examples/oneline.py
       1 Dora
       2 Ethan
       3 Wesley
       4 John
       5 Anne
       6 Mike
       7 Chris
       8 Sarah
       9 Alex
      10 Lizzie


Did you get this error?

::

    
    you@localhost:~/diveintopython3$ python3 examples/oneline.py
    Traceback (most recent call last):
      File "examples/oneline.py", line 4, in <module>
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
    ValueError: zero length field name in format


If so, youre probably using Python 3.0. You should really upgrade to
Python 3.1.
Python 3.0 supported string formatting, but only with `explicitly
numbered format specifiers`_. Python 3.1 allows you to omit the
argument indexes in your format specifiers. Here is the Python
3.0-compatible version for comparison:

::

     `print('{0:>4} {1}'.format(line_number, a_line.rstrip()))`


⁂


Writing to Text Files
---------------------
Just open a file and start writing.
You can write to files in much the same way that you read from them.
First you open a file and get a stream object, then you use methods on
the stream object to write data to the file, then you close the file.
To open a file for writing, use the `open()` function and specify the
write mode. There are two file modes for writing:

+ Write mode will overwrite the file. Pass `mode='w'` to the `open()`
function.
+ Append mode will add data to the end of the file. Pass `mode='a'` to
  the `open()` function.


Either mode will create the file automatically if it doesnt already
exist, so theres never a need for any sort of fiddly if the file
doesnt exist yet, create a new empty file just so you can open it for
the first time function. Just open a file and start writing.
You should always close a file as soon as youre done writing to it, to
release the file handle and ensure that the data is actually written
to disk. As with reading data from a file, you can call the stream
objects `close()` method, or you can use the `with` statement and let
Python close the file for you. I bet you can guess which technique I
recommend.

::

    
    >>> with open('test.log', mode='w', encoding='utf-8') as a_file:  ①
    ...     a_file.write('test succeeded')                            ②
    >>> with open('test.log', encoding='utf-8') as a_file:
    ...     print(a_file.read())                              
    test succeeded
    >>> with open('test.log', mode='a', encoding='utf-8') as a_file:  ③
    ...     a_file.write('and again')
    >>> with open('test.log', encoding='utf-8') as a_file:
    ...     print(a_file.read())                              
    test succeededand again                                           ④



#. You start boldly by creating the new file `test.log` (or
overwriting the existing file), and opening the file for writing. The
`mode='w'` parameter means open the file for writing. Yes, thats all
as dangerous as it sounds. I hope you didnt care about the previous
contents of that file (if any), because that data is gone now.
#. You can add data to the newly opened file with the `write()` method
of the stream object returned by the `open()` function. After the
`with` block ends, Python automatically closes the file.
#. That was so fun, lets do it again. But this time, with `mode='a'`
to append to the file instead of overwriting it. Appending will
*never* harm the existing contents of the file.
#. Both the original line you wrote and the second line you appended
   are now in the file `test.log`. Also note that neither carriage
   returns nor line feeds are included. Since you didnt write them
   explicitly to the file either time, the file doesnt include them. You
   can write a carriage return with the `'\r'` character, and/or a line
   feed with the `'\n'` character. Since you didnt do either, everything
   you wrote to the file ended up on one line.




Character Encoding Again
~~~~~~~~~~~~~~~~~~~~~~~~

Did you notice the `encoding` parameter that got passed in to the
`open()` function while you were opening a file for writing? Its
important; dont ever leave it out! As you saw in the beginning of this
chapter, files dont contain strings , they contain bytes . Reading a
string from a text file only works because you told Python what
encoding to use to read a stream of bytes and convert it to a string.
Writing text to a file presents the same problem in reverse. You cant
write characters to a file; `characters are an abstraction`_. In order
to write to the file, Python needs to know how to convert your string
into a sequence of bytes. The only way to be sure its performing the
correct conversion is to specify the `encoding` parameter when you
open the file for writing.
⁂


Binary Files
------------


Not all files contain text. Some of them contain pictures of my dog.

::

    
    >>> an_image = open('examples/beauregard.jpg', mode='rb')                ①
    >>> an_image.mode                                                        ②
    'rb'
    >>> an_image.name                                                        ③
    'examples/beauregard.jpg'
    >>> an_image.encoding                                                    ④
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: '_io.BufferedReader' object has no attribute 'encoding'



#. Opening a file in binary mode is simple but subtle. The only
difference from opening it in text mode is that the `mode` parameter
contains a `'b'` character.
#. The stream object you get from opening a file in binary mode has
many of the same attributes, including `mode`, which reflects the
`mode` parameter you passed into the `open()` function.
#. Binary stream objects also have a `name` attribute, just like text
stream objects.
#. Heres one difference, though: a binary stream object has no
   `encoding` attribute. That makes sense, right? Youre reading (or
   writing) bytes, not strings, so theres no conversion for Python to do.
   What you get out of a binary file is exactly what you put into it, no
   conversion necessary.


Did I mention youre reading bytes? Oh yes you are.

::

    
    # continued from the previous example
    >>> an_image.tell()
    0
    >>> data = an_image.read(3)  ①
    >>> data
    b'\xff\xd8\xff'
    >>> type(data)               ②
    <class 'bytes'>
    >>> an_image.tell()          ③
    3
    >>> an_image.seek(0)
    0
    >>> data = an_image.read()
    >>> len(data)
    3150



#. Like text files, you can read binary files a little bit at a time.
But theres a crucial difference
#. youre reading bytes, not strings. Since you opened the file in
binary mode, the `read()` method takes *the number of bytes to read*,
not the number of characters.
#. That means that theres never an unexpected mismatch between the
   number you passed into the `read()` method and the position index you
   get out of the `tell()` method. The `read()` method reads bytes, and
   the `seek()` and `tell()` methods track the number of bytes read. For
   binary files, theyll always agree.


⁂


Stream Objects From Non-File Sources
------------------------------------
To read from a fake file, just call `read()`.
Imagine youre writing a library, and one of your library functions is
going to read some data from a file. The function could simply take a
filename as a string, go open the file for reading, read it, and close
it before exiting. But you shouldnt do that. Instead, your API should
take *an arbitrary stream object*.
In the simplest case, a stream object is anything with a `read()`
method which takes an optional size parameter and returns a string.
When called with no size parameter, the `read()` method should read
everything there is to read from the input source and return all the
data as a single value. When called with a size parameter, it reads
that much from the input source and returns that much data. When
called again, it picks up where it left off and returns the next chunk
of data.
That sounds exactly like the stream object you get from opening a real
file. The difference is that *youre not limiting yourself to real
files*. The input source thats being read could be anything: a web
page, a string in memory, even the output of another program. As long
as your functions take a stream object and simply call the objects
`read()` method, you can handle any input source that acts like a
file, without specific code to handle each kind of input.

::

    
    >>> a_string = 'PapayaWhip is the new black.'
    >>> import io                                  ①
    >>> a_file = io.StringIO(a_string)             ②
    >>> a_file.read()                              ③
    'PapayaWhip is the new black.'
    >>> a_file.read()                              ④
    ''
    >>> a_file.seek(0)                             ⑤
    0
    >>> a_file.read(10)                            ⑥
    'PapayaWhip'
    >>> a_file.tell()                       
    10
    >>> a_file.seek(18)
    18
    >>> a_file.read()
    'new black.'



#. The `io` module defines the `StringIO` class that you can use to
treat a string in memory as a file.
#. To create a stream object out of a string, create an instance of
the `io.StringIO()` class and pass it the string you want to use as
your file data. Now you have a stream object, and you can do all sorts
of stream-like things with it.
#. Calling the `read()` method reads the entire file, which in the
case of a `StringIO` object simply returns the original string.
#. Just like a real file, calling the `read()` method again returns an
empty string.
#. You can explicitly seek to the beginning of the string, just like
seeking through a real file, by using the `seek()` method of the
`StringIO` object.
#. You can also read the string in chunks, by passing a size parameter
   to the `read()` method.


☞ `io.StringIO` lets you treat a string as a text file. Theres
also a `io.BytesIO` class, which lets you treat a byte array as a
binary file.


Handling Compressed Files
~~~~~~~~~~~~~~~~~~~~~~~~~

The Python standard library contains modules that support reading and
writing compressed files. There are a number of different compression
schemes; the two most popular on non-Windows systems are `gzip`_ and
`bzip2`_. (You may have also encountered `PKZIP archives`_ and `GNU
Tar archives`_. Python has modules for those, too.)
The `gzip` module lets you create a stream object for reading or
writing a gzip-compressed file. The stream object it gives you
supports the `read()` method (if you opened it for reading) or the
`write()` method (if you opened it for writing). That means you can
use the methods youve already learned for regular files to *directly
read or write a gzip-compressed file*, without creating a temporary
file to store the decompressed data.
As an added bonus, it supports the `with` statement too, so you can
let Python automatically close your gzip-compressed file when youre
done with it.

::

    
    you@localhost:~$ python3
    
    >>> import gzip
    >>> with gzip.open('out.log.gz', mode='wb') as z_file:                                      ①
    ...   z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
    ... 
    >>> exit()
    
    you@localhost:~$ ls -l out.log.gz                                                           ②
    -rw-r--r--  1 mark mark    79 2009-07-19 14:29 out.log.gz
    you@localhost:~$ gunzip out.log.gz                                                          ③
    you@localhost:~$ cat out.log                                                                ④
    A nine mile walk is no joke, especially in the rain.



#. You should always open gzipped files in binary mode. (Note the
`'b'` character in the `mode` argument.)
#. I constructed this example on Linux. If youre not familiar with the
command line, this command is showing the long listing of the gzip-
compressed file you just created in the Python Shell. This listing
shows that the file exists (good), and that it is 79 bytes long. Thats
actually larger than the string you started with! The gzip file format
includes a fixed-length header that contains some metadata about the
file, so its inefficient for extremely small files.
#. The `gunzip` command (pronounced gee-unzip) decompresses the file
and stores the contents in a new file named the same as the compressed
file but without the `.gz` file extension.
#. The `cat` command displays the contents of a file. This file
   contains the string you originally wrote directly to the compressed
   file `out.log.gz` from within the Python Shell.


Did you get this error?

::

    
    >>> with gzip.open('out.log.gz', mode='wb') as z_file:
    ...         z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
    ... 
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    AttributeError: 'GzipFile' object has no attribute '__exit__'


If so, youre probably using Python 3.0. You should really upgrade to
Python 3.1.
Python 3.0 had a `gzip` module, but it did not support using a
gzipped-file object as a context manager. Python 3.1 added the ability
to use gzipped-file objects in a `with` statement.
⁂


Standard Input, Output, and Error
---------------------------------
`sys.stdin`, `sys.stdout`, `sys.stderr`.
Command-line gurus are already familiar with the concept of standard
input, standard output, and standard error. This section is for the
rest of you.
Standard output and standard error (commonly abbreviated `stdout` and
`stderr`) are pipes that are built into every UNIX -like system,
including Mac OS X and Linux. When you call the `print()` function,
the thing youre printing is sent to the `stdout` pipe. When your
program crashes and prints out a traceback, it goes to the `stderr`
pipe. By default, both of these pipes are just connected to the
terminal window where you are working; when your program prints
something, you see the output in your terminal window, and when a
program crashes, you see the traceback in your terminal window too. In
the graphical Python Shell, the `stdout` and `stderr` pipes default to
your Interactive Window.

::

    
    >>> for i in range(3):
    ...     print('PapayaWhip')                ①
    PapayaWhip
    PapayaWhip
    PapayaWhip
    >>> import sys
    >>> for i in range(3):
    ...     l = sys.stdout.write('is the')     ②
    is theis theis the
    >>> for i in range(3):
    ...     l = sys.stderr.write('new black')  ③
    new blacknew blacknew black



#. The `print()` function, in a loop. Nothing surprising here.
#. `stdout` is defined in the `sys` module, and it is a stream object.
Calling its `write()` function will print out whatever string you give
it, then return the length of the output. In fact, this is what the
`print` function really does; it adds a carriage return to the end of
the string youre printing, and calls `sys.stdout.write`.
#. In the simplest case, `sys.stdout` and `sys.stderr` send their
   output to the same place: the Python IDE (if youre in one), or the
   terminal (if youre running Python from the command line). Like
   standard output, standard error does not add carriage returns for you.
   If you want carriage returns, youll need to write carriage return
   characters.


`sys.stdout` and `sys.stderr` are stream objects, but they are write-
only. Attempting to call their `read()` method will always raise an
`IOError`.

::

    
    >>> import sys
    >>> sys.stdout.read()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IOError: not readable




Redirecting Standard Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`sys.stdout` and `sys.stderr` are stream objects, albeit ones that
only support writing. But theyre not constants; theyre variables. That
means you can assign them a new valueany other stream objectto
redirect their output.
[`download `stdout.py``_]

::

     `import sys
    
    class RedirectStdoutTo:
        def __init__(self, out_new):
            self.out_new = out_new
    
        def __enter__(self):
            self.out_old = sys.stdout
            sys.stdout = self.out_new
    
        def __exit__(self, *args):
            sys.stdout = self.out_old
    
    print('A')
    with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
        print('B')
    print('C')`


Check this out:

::

    
    you@localhost:~/diveintopython3/examples$ python3 stdout.py
    A
    C
    you@localhost:~/diveintopython3/examples$ cat out.log
    B


Did you get this error?

::

    
    you@localhost:~/diveintopython3/examples$ python3 stdout.py
      File "stdout.py", line 15
        with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
                                                                  ^
    SyntaxError: invalid syntax


If so, youre probably using Python 3.0. You should really upgrade to
Python 3.1.
Python 3.0 supported the `with` statement, but each statement can only
use one context manager. Python 3.1 allows you to chain multiple
context managers in a single `with` statement.
Lets take the last part first.

::

     `print('A')
    with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
        print('B')
    print('C')`


Thats a complicated `with` statement. Let me rewrite it as something
more recognizable.

::

     `with open('out.log', mode='w', encoding='utf-8') as a_file:
        with RedirectStdoutTo(a_file):
            print('B')`


As the rewrite shows, you actually have *two* `with` statements, one
nested within the scope of the other. The outer `with` statement
should be familiar by now: it opens a UTF-8 -encoded text file named
`out.log` for writing and assigns the stream object to a variable
named a_file . But thats not the only thing odd here.

::

     `with RedirectStdoutTo(a_file):`


Wheres the `as` clause? The `with` statement doesnt actually require
one. Just like you can call a function and ignore its return value,
you can have a `with` statement that doesnt assign the `with` context
to a variable. In this case, youre only interested in the side effects
of the `RedirectStdoutTo` context.
What are those side effects? Take a look inside the `RedirectStdoutTo`
class. This class is a custom `context manager`_. Any class can be a
context manager by defining two `special methods`_: `__enter__()` and
`__exit__()`.

::

     `class RedirectStdoutTo:
        def __init__(self, out_new):    ①
            self.out_new = out_new
    
        def __enter__(self):            ②
            self.out_old = sys.stdout
            sys.stdout = self.out_new
    
        def __exit__(self, *args):      ③
            sys.stdout = self.out_old`



#. The `__init__()` method is called immediately after an instance is
created. It takes one parameter, the stream object that you want to
use as standard output for the life of the context. This method just
saves the stream object in an instance variable so other methods can
use it later.
#. The `__enter__()` method is a `special class method`_; Python calls
it when entering a context ( i.e. at the beginning of the `with`
statement). This method saves the current value of `sys.stdout` in
self.out_old , then redirects standard output by assigning
self.out_new to sys.stdout .
#. The `__exit__()` method is another special class method; Python
   calls it when exiting the context ( i.e. at the end of the `with`
   statement). This method restores standard output to its original value
   by assigning the saved self.out_old value to sys.stdout .


Putting it all together:

::

     `
    print('A')                                                                             ①
    with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):  ②
        print('B')                                                                         ③
    print('C')                                                                             ④`



#. This will print to the IDE Interactive Window (or the terminal, if
running the script from the command line).
#. This `with` statement takes *a comma-separated list of contexts*.
The comma-separated list acts like a series of nested `with` blocks.
The first context listed is the outer block; the last one listed is
the inner block. The first context opens a file; the second context
redirects `sys.stdout` to the stream object that was created in the
first context.
#. Because this `print()` function is executed with the context
created by the `with` statement, it will not print to the screen; it
will write to the file `out.log`.
#. The `with` code block is over. Python has told each context manager
   to do whatever it is they do upon exiting a context. The context
   managers form a last-in-first-out stack. Upon exiting, the second
   context changed `sys.stdout` back to its original value, then the
   first context closed the file named `out.log`. Since standard output
   has been restored to its original value, calling the `print()`
   function will once again print to the screen.


Redirecting standard error works exactly the same way, using
`sys.stderr` instead of `sys.stdout`.
⁂


Further Reading
---------------


+ `Reading and writing files`_ in the Python.org tutorial
+ ` `io` module`_
+ `Stream objects`_
+ `Context manager types`_
+ ` `sys.stdout` and `sys.stderr``_
+ ` FUSE on Wikipedia`_


`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _characters are an abstraction: strings.html#byte-arrays
.. _iterator: iterators.html
.. _oneline.py: examples/oneline.py
.. _context manager: special-method-names.html#context-managers
.. _UTF-8: strings.html#boring-stuff
.. _ module: http://docs.python.org/3.1/library/io.html
.. _x261E;: xml.html
.. _Mark Pilgrim: about.html
.. _Context manager types: http://docs.python.org/3.1/library/stdtypes.html#context-manager-types
.. _PKZIP archives: http://docs.python.org/3.1/library/zipfile.html
.. _stdout.py: examples/stdout.py
.. _x261C;: refactoring.html
.. _ function documentation: http://docs.python.org/3.1/library/io.html#module-interface
.. _Reading and writing files: http://docs.python.org/py3k/tutorial/inputoutput.html#reading-and-writing-files
.. _ on Wikipedia: http://en.wikipedia.org/wiki/Filesystem_in_Userspace
.. _gzip: http://docs.python.org/3.1/library/gzip.html
.. _Stream objects: http://docs.python.org/3.1/library/stdtypes.html#file-objects
.. _bzip2: http://docs.python.org/3.1/library/bz2.html
.. _Home: index.html
.. _Dive Into Python 3: table-of-contents.html#files
.. _sys.stderr: http://docs.python.org/3.1/library/sys.html#sys.stdout
.. _imagining an alternative: http://en.wikipedia.org/wiki/Computer_file#History
.. _special class method: iterators.html#a-fibonacci-iterator
.. _explicitly numbered format specifiers: strings.html#formatting-strings
.. _GNU Tar archives: http://docs.python.org/3.1/library/tarfile.html
.. _ported to Python 3: case-study-porting-chardet-to-python-3.html


