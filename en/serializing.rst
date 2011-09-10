
You are here: `Home`_ `Dive Into Python 3`_
Difficulty level: ♦♦♦♦♢


Serializing Python Objects
==========================

❝ Every Saturday since weve lived in this apartment, I have
awakened at 6:15, poured myself a bowl of cereal, added
a quarter-cup of 2% milk, sat on this end of this couch, turned on BBC
America, and watched Doctor Who. ❞
Sheldon, `The Big Bang Theory`_


Diving In
---------

On the surface, the concept of serialization is simple. You have a
data structure in memory that you want to save, reuse, or send to
someone else. How would you do that? Well, that depends on how you
want to save it, how you want to reuse it, and to whom you want to
send it. Many games allow you to save your progress when you quit the
game and pick up where you left off when you relaunch the game.
(Actually, many non-gaming applications do this as well.) In this
case, a data structure that captures your progress so far needs to be
stored on disk when you quit, then loaded from disk when you relaunch.
The data is only meant to be used by the same program that created it,
never sent over a network, and never read by anything other than the
program that created it. Therefore, the interoperability issues are
limited to ensuring that later versions of the program can read data
written by earlier versions.
For cases like this, the `pickle` module is ideal. Its part of the
Python standard library, so its always available. Its fast; the bulk
of it is written in C, like the Python interpreter itself. It can
store arbitrarily complex Python data structures.
What can the `pickle` module store?

+ All the `native datatypes`_ that Python supports: booleans,
integers, floating point numbers, complex numbers, strings, `bytes`
objects, byte arrays, and `None`.
+ Lists, tuples, dictionaries, and sets containing any combination of
native datatypes.
+ Lists, tuples, dictionaries, and sets containing any combination of
lists, tuples, dictionaries, and sets containing any combination of
native datatypes (and so on, to `the maximum nesting level that Python
supports`_).
+ Functions, classes, and instances of classes (with caveats).


If this isnt enough for you, the `pickle` module is also extensible.
If youre interested in extensibility, check out the links in the
Further Reading section at the end of the chapter.


A Quick Note About The Examples in This Chapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This chapter tells a tale with two Python Shells. All of the examples
in this chapter are part of a single story arc. You will be asked to
switch back and forth between the two Python Shells as I demonstrate
the `pickle` and `json` modules.
To help keep things straight, open the Python Shell and define the
following variable:

::

    
    >>> shell = 1


Keep that window open. Now open another Python Shell and define the
following variable:

::

    
    >>> shell = 2


Throughout this chapter, I will use the `shell` variable to indicate
which Python Shell is being used in each example.
⁂


Saving Data to a Pickle File
----------------------------

The `pickle` module works with data structures. Lets build one.

::

    
    >>> shell                                                                                              ①
    1
    >>> entry = {}                                                                                         ②
    >>> entry['title'] = 'Dive into history, 2009 edition'
    >>> entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
    >>> entry['comments_link'] = None
    >>> entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
    >>> entry['tags'] = ('diveintopython', 'docbook', 'html')
    >>> entry['published'] = True
    >>> import time
    >>> entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')                                ③
    >>> entry['published_date']
    time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1)



#. Follow along in Python Shell #1.
#. The idea here is to build a Python dictionary that could represent
something useful, like an `entry in an Atom feed`_. But I also want to
ensure that it contains several different types of data, to show off
the `pickle` module. Dont read too much into these values.
#. The `time` module contains a data structure ( `struct_time`) to
   represent a point in time (accurate to one millisecond) and functions
   to manipulate time structs. The `strptime()` function takes a
   formatted string an converts it to a `struct_time`. This string is in
   the default format, but you can control that with format codes. See
   the ` `time` module`_ for more details.


Thats a handsome-looking Python dictionary. Lets save it to a file.

::

    
    >>> shell                                    ①
    1
    >>> import pickle
    >>> with open('entry.pickle', 'wb') as f:    ②
    ...     pickle.dump(entry, f)                ③
    ... 



#. This is still in Python Shell #1.
#. Use the `open()` function to open a file. Set the file mode to
`'wb'` to open the file for writing `in binary mode`_. Wrap it in a `
`with` statement`_ to ensure the file is closed automatically when
youre done with it.
#. The `dump()` function in the `pickle` module takes a serializable
   Python data structure, serializes it into a binary, Python-specific
   format using the latest version of the pickle protocol, and saves it
   to an open file.


That last sentence was pretty important.

+ The `pickle` module takes a Python data structure and saves it to a
file.
+ To do this, it serializes the data structure using a data format
called the pickle protocol.
+ The pickle protocol is Python-specific; there is no guarantee of
cross-language compatibility. You probably couldnt take the
`entry.pickle` file you just created and do anything useful with it in
Perl, PHP , Java, or any other language.
+ Not every Python data structure can be serialized by the `pickle`
module. The pickle protocol has changed several times as new data
types have been added to the Python language, but there are still
limitations.
+ As a result of these changes, there is no guarantee of compatibility
between different versions of Python itself. Newer versions of Python
support the older serialization formats, but older versions of Python
do not support newer formats (since they dont support the newer data
types).
+ Unless you specify otherwise, the functions in the `pickle` module
will use the latest version of the pickle protocol. This ensures that
you have maximum flexibility in the types of data you can serialize,
but it also means that the resulting file will not be readable by
older versions of Python that do not support the latest version of the
pickle protocol.
+ The latest version of the pickle protocol is a binary format. Be
  sure to open your pickle files `in binary mode`_, or the data will get
  corrupted during writing.


⁂


Loading Data from a Pickle File
-------------------------------

Now switch to your second Python Shell i.e. not the one where you
created the `entry` dictionary.

::

    
    >>> shell                                    ①
    2
    >>> entry                                    ②
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'entry' is not defined
    >>> import pickle
    >>> with open('entry.pickle', 'rb') as f:    ③
    ...     entry = pickle.load(f)               ④
    ... 
    >>> entry                                    ⑤
    {'comments_link': None,
     'internal_id': b'\xDE\xD5\xB4\xF8',
     'title': 'Dive into history, 2009 edition',
     'tags': ('diveintopython', 'docbook', 'html'),
     'article_link':
     'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
     'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
     'published': True}



#. This is Python Shell #2.
#. There is no entry variable defined here. You defined an entry
variable in Python Shell #1, but thats a completely different
environment with its own state.
#. Open the `entry.pickle` file you created in Python Shell #1. The
`pickle` module uses a binary data format, so you should always open
pickle files in binary mode.
#. The `pickle.load()` function takes a `stream object`_, reads the
serialized data from the stream, creates a new Python object,
recreates the serialized data in the new Python object, and returns
the new Python object.
#. Now the entry variable is a dictionary with familiar-looking keys
   and values.


The `pickle.dump() / pickle.load()` cycle results in a new data
structure that is equal to the original data structure.

::

    
    >>> shell                                    ①
    1
    >>> with open('entry.pickle', 'rb') as f:    ②
    ...     entry2 = pickle.load(f)              ③
    ... 
    >>> entry2 == entry                          ④
    True
    >>> entry2 is entry                          ⑤
    False
    >>> entry2['tags']                           ⑥
    ('diveintopython', 'docbook', 'html')
    >>> entry2['internal_id']
    b'\xDE\xD5\xB4\xF8'



#. Switch back to Python Shell #1.
#. Open the `entry.pickle` file.
#. Load the serialized data into a new variable, entry2 .
#. Python confirms that the two dictionaries, entry and entry2 , are
equal. In this shell, you built entry from the ground up, starting
with an empty dictionary and manually assigning values to specific
keys. You serialized this dictionary and stored it in the
`entry.pickle` file. Now youve read the serialized data from that file
and created a perfect replica of the original data structure.
#. Equality is not the same as identity. I said youve created a
*perfect replica* of the original data structure, which is true. But
its still a copy.
#. For reasons that will become clear later in this chapter, I want to
   point out that the value of the `'tags'` key is a tuple, and the value
   of the `'internal_id'` key is a `bytes` object.


⁂


Pickling Without a File
-----------------------

The examples in the previous section showed how to serialize a Python
object directly to a file on disk. But what if you dont want or need a
file? You can also serialize to a `bytes` object in memory.

::

    
    >>> shell
    1
    >>> b = pickle.dumps(entry)     ①
    >>> type(b)                     ②
    <class 'bytes'>
    >>> entry3 = pickle.loads(b)    ③
    >>> entry3 == entry             ④
    True



#. The `pickle.dumps()` function (note the `'s'` at the end of the
function name) performs the same serialization as the `pickle.dump()`
function. Instead of taking a stream object and writing the serialized
data to a file on disk, it simply returns the serialized data.
#. Since the pickle protocol uses a binary data format, the
`pickle.dumps()` function returns a `bytes` object.
#. The `pickle.loads()` function (again, note the `'s'` at the end of
the function name) performs the same deserialization as the
`pickle.load()` function. Instead of taking a stream object and
reading the serialized data from a file, it takes a `bytes` object
containing serialized data, such as the one returned by the
`pickle.dumps()` function.
#. The end result is the same: a perfect replica of the original
   dictionary.


⁂


Bytes and Strings Rear Their Ugly Heads Again
---------------------------------------------

The pickle protocol has been around for many years, and it has matured
as Python itself has matured. There are now `four different versions`_
of the pickle protocol.

+ Python 1.x had two pickle protocols, a text-based format (version 0)
and a binary format (version 1).
+ Python 2.3 introduced a new pickle protocol (version 2) to handle
new functionality in Python class objects. It is a binary format.
+ Python 3.0 introduced another pickle protocol (version 3) with
  explicit support for `bytes` objects and byte arrays. It is a binary
  format.


Oh look, `the difference between bytes and strings`_ rears its ugly
head again. (If youre surprised, you havent been paying attention.)
What this means in practice is that, while Python 3 can read data
pickled with protocol version 2, Python 2 can not read data pickled
with protocol version 3.
⁂


Debugging Pickle Files
----------------------

What does the pickle protocol look like? Lets jump out of the Python
Shell for a moment and take a look at that `entry.pickle` file we
created. To the naked eye, its mostly gibberish.

::

    
    you@localhost:~/diveintopython3/examples$ ls -l entry.pickle
    -rw-r--r-- 1 you  you  358 Aug  3 13:34 entry.pickle
    you@localhost:~/diveintopython3/examples$ cat entry.pickle
    comments_linkqNXtagsqXdiveintopythonqXdocbookqXhtmlq?qX publishedq?
    XlinkXJhttp://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition
    q   Xpublished_dateq
    ctime
    struct_time
    ?qRqXtitleqXDive into history, 2009 editionqu.


That wasnt terribly helpful. You can see the strings, but other
datatypes end up as unprintable (or at least unreadable) characters.
Fields are not obviously delimited by tabs or spaces. This is not a
format you would want to debug by yourself.

::

    
    >>> shell
    1
    >>> import pickletools
    >>> with open('entry.pickle', 'rb') as f:
    ...     pickletools.dis(f)
        0: \x80 PROTO      3
        2: }    EMPTY_DICT
        3: q    BINPUT     0
        5: (    MARK
        6: X        BINUNICODE 'published_date'
       25: q        BINPUT     1
       27: c        GLOBAL     'time struct_time'
       45: q        BINPUT     2
       47: (        MARK
       48: M            BININT2    2009
       51: K            BININT1    3
       53: K            BININT1    27
       55: K            BININT1    22
       57: K            BININT1    20
       59: K            BININT1    42
       61: K            BININT1    4
       63: K            BININT1    86
       65: J            BININT     -1
       70: t            TUPLE      (MARK at 47)
       71: q        BINPUT     3
       73: }        EMPTY_DICT
       74: q        BINPUT     4
       76: \x86     TUPLE2
       77: q        BINPUT     5
       79: R        REDUCE
       80: q        BINPUT     6
       82: X        BINUNICODE 'comments_link'
      100: q        BINPUT     7
      102: N        NONE
      103: X        BINUNICODE 'internal_id'
      119: q        BINPUT     8
      121: C        SHORT_BINBYTES 'ÞÕ´ø'
      127: q        BINPUT     9
      129: X        BINUNICODE 'tags'
      138: q        BINPUT     10
      140: X        BINUNICODE 'diveintopython'
      159: q        BINPUT     11
      161: X        BINUNICODE 'docbook'
      173: q        BINPUT     12
      175: X        BINUNICODE 'html'
      184: q        BINPUT     13
      186: \x87     TUPLE3
      187: q        BINPUT     14
      189: X        BINUNICODE 'title'
      199: q        BINPUT     15
      201: X        BINUNICODE 'Dive into history, 2009 edition'
      237: q        BINPUT     16
      239: X        BINUNICODE 'article_link'
      256: q        BINPUT     17
      258: X        BINUNICODE 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
      337: q        BINPUT     18
      339: X        BINUNICODE 'published'
      353: q        BINPUT     19
      355: \x88     NEWTRUE
      356: u        SETITEMS   (MARK at 5)
      357: .    STOP
    highest protocol among opcodes = 3


The most interesting piece of information in that disassembly is on
the last line, because it includes the version of the pickle protocol
with which this file was saved. There is no explicit version marker in
the pickle protocol. To determine which protocol version was used to
store a pickle file, you need to look at the markers (opcodes) within
the pickled data and use hard-coded knowledge of which opcodes were
introduced with each version of the pickle protocol. The
`pickletools.dis()` function does exactly that, and it prints the
result in the last line of the disassembly output. Here is a function
that returns just the version number, without printing anything:
[`download `pickleversion.py``_]

::

     `import pickletools
    
    def protocol_version(file_object):
        maxproto = -1
        for opcode, arg, pos in pickletools.genops(file_object):
            maxproto = max(maxproto, opcode.proto)
        return maxproto`


And here it is in action:


::

    
    >>> import pickleversion
    >>> with open('entry.pickle', 'rb') as f:
    ...     v = pickleversion.protocol_version(f)
    >>> v
    3


⁂


Serializing Python Objects to be Read by Other Languages
--------------------------------------------------------

The data format used by the `pickle` module is Python-specific. It
makes no attempt to be compatible with other programming languages. If
cross-language compatibility is one of your requirements, you need to
look at other serialization formats. One such format is ` JSON `_.
JSON stands for JavaScript Object Notation, but dont let the name fool
you JSON is explicitly designed to be usable across multiple
programming languages.
Python 3 includes a `json` module in the standard library. Like the
`pickle` module, the `json` module has functions for serializing data
structures, storing the serialized data on disk, loading serialized
data from disk, and unserializing the data back into a new Python
object. But there are some important differences, too. First of all,
the JSON data format is text-based, not binary. `RFC 4627`_ defines
the JSON format and how different types of data must be encoded as
text. For example, a boolean value is stored as either the five-
character string `'false'` or the four-character string `'true'`. All
JSON values are case-sensitive.
Second, as with any text-based format, there is the issue of
whitespace. JSON allows arbitrary amounts of whitespace (spaces, tabs,
carriage returns, and line feeds) between values. This whitespace is
insignificant, which means that JSON encoders can add as much or as
little whitespace as they like, and JSON decoders are required to
ignore the whitespace between values. This allows you to pretty-print
your JSON data, nicely nesting values within values at different
indentation levels so you can read it in a standard browser or text
editor. Pythons `json` module has options for pretty-printing during
encoding.
Third, theres the perennial problem of character encoding. JSON
encodes values as plain text, but as you know, `there aint no such
thing as plain text.`_ JSON must be stored in a Unicode encoding
(UTF-32, UTF-16, or the default, UTF-8 ), and `section 3 of RFC 4627`_
defines how to tell which encoding is being used.
⁂


Saving Data to a JSON File
--------------------------

JSON looks remarkably like a data structure you might define manually
in JavaScript. This is no accident; you can actually use the
JavaScript `eval()` function to decode JSON -serialized data. (The
usual `caveats about untrusted input`_ apply, but the point is that
JSON *is* valid JavaScript.) As such, JSON may already look familiar
to you.

::

    
    >>> shell
    1
    >>> basic_entry = {}                                           ①
    >>> basic_entry['id'] = 256
    >>> basic_entry['title'] = 'Dive into history, 2009 edition'
    >>> basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
    >>> basic_entry['published'] = True
    >>> basic_entry['comments_link'] = None
    >>> import json
    >>> with open('basic.json', mode='w', encoding='utf-8') as f:  ②
    ...     json.dump(basic_entry, f)                              ③



#. Were going to create a new data structure instead of re-using the
existing entry data structure. Later in this chapter, well see what
happens when we try to encode the more complex data structure in JSON
.
#. JSON is a text-based format, which means you need to open this file
in text mode and specify a character encoding. You can never go wrong
with UTF-8 .
#. Like the `pickle` module, the `json` module defines a `dump()`
   function which takes a Python data structure and a writeable stream
   object. The `dump()` function serializes the Python data structure and
   writes it to the stream object. Doing this inside a `with` statement
   will ensure that the file is closed properly when were done.


So what does the resulting JSON serialization look like?

::

    
    you@localhost:~/diveintopython3/examples$ cat basic.json
    {"published": true, "tags": ["diveintopython", "docbook", "html"], "comments_link": null,
    "id": 256, "title": "Dive into history, 2009 edition"}


Thats certainly more readable than a pickle file. But JSON can contain
arbitrary whitespace between values, and the `json` module provides an
easy way to take advantage of this to create even more readable JSON
files.

::

    
    >>> shell
    1
    >>> with open('basic-pretty.json', mode='w', encoding='utf-8') as f:
    ...     json.dump(basic_entry, f, indent=2)                            ①



#. If you pass an indent parameter to the `json.dump()` function, it
   will make the resulting JSON file more readable, at the expense of
   larger file size. The indent parameter is an integer. 0 means put each
   value on its own line. A number greater than 0 means put each value on
   its own line, and use this number of spaces to indent nested data
   structures.


And this is the result:

::

    
    you@localhost:~/diveintopython3/examples$ cat basic-pretty.json
    {
      "published": true, 
      "tags": [
        "diveintopython", 
        "docbook", 
        "html"
      ], 
      "comments_link": null, 
      "id": 256, 
      "title": "Dive into history, 2009 edition"
    }


⁂


Mapping of Python Datatypes to JSON
-----------------------------------

Since JSON is not Python-specific, there are some mismatches in its
coverage of Python datatypes. Some of them are simply naming
differences, but there is two important Python datatypes that are
completely missing. See if you can spot them: Notes JSON Python 3
object `dictionary`_ array `list`_ string `string`_ integer `integer`_
real number `float`_ * `true` ` `True``_ * `false` ` `False``_ *
`null` ``None`_` * All JSON values are case-sensitive.
Did you notice what was missing? Tuples & bytes! JSON has an array
type, which the `json` module maps to a Python list, but it does not
have a separate type for frozen arrays (tuples). And while JSON
supports strings quite nicely, it has no support for `bytes` objects
or byte arrays.
⁂


Serializing Datatypes Unsupported by JSON
-----------------------------------------

Even if JSON has no built-in support for bytes, that doesnt mean you
cant serialize `bytes` objects. The `json` module provides
extensibility hooks for encoding and decoding unknown datatypes. (By
unknown, I mean not defined in JSON . Obviously the `json` module
knows about byte arrays, but its constrained by the limitations of the
JSON specification.) If you want to encode bytes or other datatypes
that JSON doesnt support natively, you need to provide custom encoders
and decoders for those types.

::

    
    >>> shell
    1
    >>> entry                                                 ①
    {'comments_link': None,
     'internal_id': b'\xDE\xD5\xB4\xF8',
     'title': 'Dive into history, 2009 edition',
     'tags': ('diveintopython', 'docbook', 'html'),
     'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
     'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
     'published': True}
    >>> import json
    >>> with open('entry.json', 'w', encoding='utf-8') as f:  ②
    ...     json.dump(entry, f)                               ③
    ... 
    Traceback (most recent call last):
      File "<stdin>", line 5, in <module>
      File "C:\Python31\lib\json\__init__.py", line 178, in dump
        for chunk in iterable:
      File "C:\Python31\lib\json\encoder.py", line 408, in _iterencode
        for chunk in _iterencode_dict(o, _current_indent_level):
      File "C:\Python31\lib\json\encoder.py", line 382, in _iterencode_dict
        for chunk in chunks:
      File "C:\Python31\lib\json\encoder.py", line 416, in _iterencode
        o = _default(o)
      File "C:\Python31\lib\json\encoder.py", line 170, in default
        raise TypeError(repr(o) + " is not JSON serializable")
    TypeError: b'\xDE\xD5\xB4\xF8' is not JSON serializable



#. OK, its time to revisit the entry data structure. This has it all:
a boolean value, a `None` value, a string, a tuple of strings, a
`bytes` object, and a `time` structure.
#. I know Ive said it before, but its worth repeating: JSON is a text-
based format. Always open JSON files in text mode with a UTF-8
character encoding.
#. Well *thats* not good. What happened?


Heres what happened: the `json.dump()` function tried to serialize the
`bytes` object `b'\xDE\xD5\xB4\xF8'`, but it failed, because JSON has
no support for `bytes` objects. However, if storing bytes is important
to you, you can define your own mini-serialization format.
[`download `customserializer.py``_]

::

     `
    def to_json(python_object):                                             ①
        if isinstance(python_object, bytes):                                ②
            return {'__class__': 'bytes',
                    '__value__': list(python_object)}                       ③
        raise TypeError(repr(python_object) + ' is not JSON serializable')  ④`



#. To define your own mini-serialization format for a datatype that
JSON doesnt support natively, just define a function that takes a
Python object as a parameter. This Python object will be the actual
object that the `json.dump()` function is unable to serialize by
itselfin this case, the `bytes` object `b'\xDE\xD5\xB4\xF8'`.
#. Your custom serialization function should check the type of the
Python object that the `json.dump()` function passed to it. This is
not strictly necessary if your function only serializes one datatype,
but it makes it crystal clear what case your function is covering, and
it makes it easier to extend if you need to add serializations for
more datatypes later.
#. In this case, Ive chosen to convert a `bytes` object into a
dictionary. The `__class__` key will hold the original datatype (as a
string, `'bytes'`), and the `__value__` key will hold the actual
value. Of course this cant be a `bytes` object; the entire point is to
convert it into something that can be serialized in JSON ! A `bytes`
object is just a sequence of integers; each integer is somewhere in
the range 0255. We can use the `list()` function to convert the
`bytes` object into a list of integers. So `b'\xDE\xD5\xB4\xF8'`
becomes `[222, 213, 180, 248]`. (Do the math! It works! The byte
`\xDE` in hexadecimal is 222 in decimal, `\xD5` is 213, and so on.)
#. This line is important. The data structure youre serializing may
   contain types that neither the built-in JSON serializer nor your
   custom serializer can handle. In this case, your custom serializer
   must raise a `TypeError` so that the `json.dump()` function knows that
   your custom serializer did not recognize the type.


Thats it; you dont need to do anything else. In particular, this
custom serialization function *returns a Python dictionary*, not a
string. Youre not doing the entire serializing-to- JSON yourself;
youre only doing the converting-to-a-supported-datatype part. The
`json.dump()` function will do the rest.

::

    
    >>> shell
    1
    >>> import customserializer                                                             ①
    >>> with open('entry.json', 'w', encoding='utf-8') as f:                                ②
    ...     json.dump(entry, f, default=customserializer.to_json)                           ③
    ... 
    Traceback (most recent call last):
      File "<stdin>", line 9, in <module>
        json.dump(entry, f, default=customserializer.to_json)
      File "C:\Python31\lib\json\__init__.py", line 178, in dump
        for chunk in iterable:
      File "C:\Python31\lib\json\encoder.py", line 408, in _iterencode
        for chunk in _iterencode_dict(o, _current_indent_level):
      File "C:\Python31\lib\json\encoder.py", line 382, in _iterencode_dict
        for chunk in chunks:
      File "C:\Python31\lib\json\encoder.py", line 416, in _iterencode
        o = _default(o)
      File "/Users/pilgrim/diveintopython3/examples/customserializer.py", line 12, in to_json
        raise TypeError(repr(python_object) + ' is not JSON serializable')                     ④
    TypeError: time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1) is not JSON serializable



#. The `customserializer` module is where you just defined the
`to_json()` function in the previous example.
#. Text mode, UTF-8 encoding, yadda yadda. (Youll forget! I forget
sometimes! And everything will work right up until the moment that it
fails, and then it will fail most spectacularly.)
#. This is the important bit: to hook your custom conversion function
into the `json.dump()` function, pass your function into the
`json.dump()` function in the default parameter. (Hooray, `everything
in Python is an object`_!)
#. OK, so it didnt actually work. But take a look at the exception.
   The `json.dump()` function is no longer complaining about being unable
   to serialize the `bytes` object. Now its complaining about a
   completely different object: the `time.struct_time` object.


While getting a different exception might not seem like progress, it
really is! Itll just take one more tweak to get past this.

::

     `
    import time
    
    def to_json(python_object):
        if isinstance(python_object, time.struct_time):          ①
            return {'__class__': 'time.asctime',
                    '__value__': time.asctime(python_object)}    ②
        if isinstance(python_object, bytes):
            return {'__class__': 'bytes',
                    '__value__': list(python_object)}
        raise TypeError(repr(python_object) + ' is not JSON serializable')`



#. Adding to our existing `customserializer.to_json()` function, we
need to check whether the Python object (that the `json.dump()`
function is having trouble with) is a `time.struct_time`.
#. If so, well do something similar to the conversion we did with the
   `bytes` object: convert the `time.struct_time` object to a dictionary
   that only contains JSON -serializable values. In this case, the
   easiest way to convert a datetime into a JSON -serializable value is
   to convert it to a string with the `time.asctime()` function. The
   `time.asctime()` function will convert that nasty-looking
   `time.struct_time` into the string `'Fri Mar 27 22:20:42 2009'`.


With these two custom conversions, the entire entry data structure
should serialize to JSON without any further problems.

::

    
    >>> shell
    1
    >>> with open('entry.json', 'w', encoding='utf-8') as f:
    ...     json.dump(entry, f, default=customserializer.to_json)
    ... 



::

    
    you@localhost:~/diveintopython3/examples$ ls -l example.json
    -rw-r--r-- 1 you  you  391 Aug  3 13:34 entry.json
    you@localhost:~/diveintopython3/examples$ cat example.json
    {"published_date": {"__class__": "time.asctime", "__value__": "Fri Mar 27 22:20:42 2009"},
    "comments_link": null, "internal_id": {"__class__": "bytes", "__value__": [222, 213, 180, 248]},
    "tags": ["diveintopython", "docbook", "html"], "title": "Dive into history, 2009 edition",
    "article_link": "http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition",
    "published": true}


⁂


Loading Data from a JSON File
-----------------------------

Like the `pickle` module, the `json` module has a `load()` function
which takes a stream object, reads JSON -encoded data from it, and
creates a new Python object that mirrors the JSON data structure.

::

    
    >>> shell
    2
    >>> del entry                                             ①
    >>> entry
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'entry' is not defined
    >>> import json
    >>> with open('entry.json', 'r', encoding='utf-8') as f:
    ...     entry = json.load(f)                              ②
    ... 
    >>> entry                                                 ③
    {'comments_link': None,
     'internal_id': {'__class__': 'bytes', '__value__': [222, 213, 180, 248]},
     'title': 'Dive into history, 2009 edition',
     'tags': ['diveintopython', 'docbook', 'html'],
     'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
     'published_date': {'__class__': 'time.asctime', '__value__': 'Fri Mar 27 22:20:42 2009'},
     'published': True}



#. For demonstration purposes, switch to Python Shell #2 and delete
the entry data structure that you created earlier in this chapter with
the `pickle` module.
#. In the simplest case, the `json.load()` function works the same as
the `pickle.load()` function. You pass in a stream object and it
returns a new Python object.
#. I have good news and bad news. Good news first: the `json.load()`
   function successfully read the `entry.json` file you created in Python
   Shell #1 and created a new Python object that contained the data. Now
   the bad news: it didnt recreate the original entry data structure. The
   two values `'internal_id'` and `'published_date'` were recreated as
   dictionariesspecifically, the dictionaries with JSON -compatible
   values that you created in the `to_json()` conversion function.


`json.load()` doesnt know anything about any conversion function you
may have passed to `json.dump()`. What you need is the opposite of the
`to_json()` functiona function that will take a custom-converted JSON
object and convert it back to the original Python datatype.

::

     `# add this to customserializer.py
    def from_json(json_object):                                   ①
        if '__class__' in json_object:                            ②
            if json_object['__class__'] == 'time.asctime':
                return time.strptime(json_object['__value__'])    ③
            if json_object['__class__'] == 'bytes':
                return bytes(json_object['__value__'])            ④
        return json_object`



#. This conversion function also takes one parameter and returns one
value. But the parameter it takes is not a string, its a Python
objectthe result of deserializing a JSON -encoded string into Python.
#. All you need to do is check whether this object contains the
`'__class__'` key that the `to_json()` function created. If so, the
value of the `'__class__'` key will tell you how to decode the value
back into the original Python datatype.
#. To decode the time string returned by the `time.asctime()`
function, you use the `time.strptime()` function. This function takes
a formatted datetime string (in a customizable format, but it defaults
to the same format that `time.asctime()` defaults to) and returns a
`time.struct_time`.
#. To convert a list of integers back into a `bytes` object, you can
   use the `bytes()` function.


That was it; there were only two datatypes handled in the `to_json()`
function, and now those two datatypes are handled in the `from_json()`
function. This is the result:

::

    
    >>> shell
    2
    >>> import customserializer
    >>> with open('entry.json', 'r', encoding='utf-8') as f:
    ...     entry = json.load(f, object_hook=customserializer.from_json)  ①
    ... 
    >>> entry                                                             ②
    {'comments_link': None,
     'internal_id': b'\xDE\xD5\xB4\xF8',
     'title': 'Dive into history, 2009 edition',
     'tags': ['diveintopython', 'docbook', 'html'],
     'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
     'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
     'published': True}



#. To hook the `from_json()` function into the deserialization
process, pass it as the object_hook parameter to the `json.load()`
function. Functions that take functions; its so handy!
#. The entry data structure now contains an `'internal_id'` key whose
   value is a `bytes` object. It also contains a `'published_date'` key
   whose value is a `time.struct_time` object.


There is one final glitch, though.

::

    
    >>> shell
    1
    >>> import customserializer
    >>> with open('entry.json', 'r', encoding='utf-8') as f:
    ...     entry2 = json.load(f, object_hook=customserializer.from_json)
    ... 
    >>> entry2 == entry                                                    ①
    False
    >>> entry['tags']                                                      ②
    ('diveintopython', 'docbook', 'html')
    >>> entry2['tags']                                                     ③
    ['diveintopython', 'docbook', 'html']



#. Even after hooking the `to_json()` function into the serialization,
and hooking the `from_json()` function into the deserialization, we
still havent recreated a perfect replica of the original data
structure. Why not?
#. In the original entry data structure, the value of the `'tags'` key
was a tuple of three strings.
#. But in the round-tripped entry2 data structure, the value of the
   `'tags'` key is a *list* of three strings. JSON doesnt distinguish
   between tuples and lists; it only has a single list-like datatype, the
   array, and the `json` module silently converts both tuples and lists
   into JSON arrays during serialization. For most uses, you can ignore
   the difference between tuples and lists, but its something to keep in
   mind as you work with the `json` module.




Further Reading
---------------

☞Many articles about the `pickle` module make references to
`cPickle`. In Python 2, there were two implementations of the `pickle`
module, one written in pure Python and another written in C (but still
callable from Python). In Python 3, `these two modules have been
consolidated`_, so you should always just `import pickle`. You may
find these articles useful, but you should ignore the now-obsolete
information about `cPickle`.
On pickling with the `pickle` module:

+ ` `pickle` module`_
+ ` `pickle` and `cPickle`Python object serialization`_
+ `Using `pickle``_
+ `Python persistence management`_


On JSON and the `json` module:

+ ` `json`JavaScript Object Notation Serializer`_
+ `JSON encoding and ecoding with custom objects in Python`_


On pickle extensibility:

+ `Pickling class instances`_
+ `Persistence of external objects`_
+ `Handling stateful objects`_


`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _four different versions: http://docs.python.org/3.1/library/pickle.html#data-stream-format
.. _JSON encoding and ecoding with custom objects in Python: http://blog.quaternio.net/2009/07/16/json-encoding-and-decoding-with-custom-objects-in-python/
.. _caveats about untrusted input: advanced-iterators.html#eval
.. _the difference between bytes and strings: strings.html#byte-arrays
.. _x261C;: xml.html
.. _ module: http://docs.python.org/3.1/library/time.html
.. _in binary mode: files.html#binary
.. _section 3 of RFC 4627: http://www.ietf.org/rfc/rfc4627.txt
.. _float: native-datatypes.html#numbers
.. _Dive Into Python 3: table-of-contents.html#serializing
.. _JavaScript Object Notation Serializer: http://www.doughellmann.com/PyMOTW/json/
.. _customserializer.py: examples/customserializer.py
.. _ module: http://docs.python.org/3.1/library/pickle.html
.. _list: native-datatypes.html#lists
.. _Handling stateful objects: http://docs.python.org/3.1/library/pickle.html#handling-stateful-objects
.. _Persistence of external objects: http://docs.python.org/3.1/library/pickle.html#persistence-of-external-objects
.. _The Big Bang Theory: 'http://en.wikiquote.org/wiki/The_Big_Bang_Theory#The_Dumpling_Paradox_.5B1.07.5D'
.. _dictionary: native-datatypes.html#dictionaries
.. _Mark Pilgrim: about.html
.. _these two modules have been consolidated: porting-code-to-python-3-with-2to3.html#othermodules
.. _stream object: files.html#file-objects
.. _False: native-datatypes.html#booleans
.. _pickle: http://wiki.python.org/moin/UsingPickle
.. _entry in an Atom feed: xml.html#xml-structure
.. _everything in Python is an object: your-first-python-program.html#everythingisanobject
.. _the maximum nesting level that Python supports: http://docs.python.org/3.1/library/sys.html#sys.getrecursionlimit
.. _JSON: http://json.org/
.. _string: strings.html#divingin
.. _Python object serialization: http://www.doughellmann.com/PyMOTW/pickle/
.. _Home: index.html
.. _pickleversion.py: examples/pickleversion.py
.. _Python persistence management: http://www.ibm.com/developerworks/library/l-pypers.html
.. _native datatypes: native-datatypes.html
.. _x261E;: http-web-services.html
.. _None: native-datatypes.html#none
.. _ statement: files.html#with
.. _plain text.: strings.html
.. _Pickling class instances: http://docs.python.org/3.1/library/pickle.html#pickling-class-instances


