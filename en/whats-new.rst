
You are here: `Home`_ `Dive Into Python 3`_


Whats New In Dive Into Python 3
===============================

❝ Isnt this where we came in? ❞
Pink Floyd, The Wall


a.k.a. the minus level
----------------------

Are you already a Python programmer? Did you read the original `Dive
Into Python`_? Did you buy it on paper? (If so, thanks!) Are you ready
to take the plunge into Python 3? If so, read on. (If none of that is
true, youd be better off `starting at the beginning`_.)
Python 3 comes with a script called `2to3`. Learn it. Love it. Use it.
`Porting Code to Python 3 with `2to3``_ is a reference of all the
things that the `2to3` tool can fix automatically. Since a lot of
those things are syntax changes, its a good starting point to learn
about a lot of the syntax changes in Python 3. ( `print` is now a
function, ``x`` doesnt work, & c.)
`Case Study: Porting `chardet` to Python 3`_ documents my (ultimately
successful) effort to port a non-trivial library from Python 2 to
Python 3. It may help you; it may not. Theres a fairly steep learning
curve, since you need to kind of understand the library first, so you
can understand why it broke and how I fixed it. A lot of the breakage
centers around strings. Speaking of which
Strings. Whew. Where to start. Python 2 had strings and Unicode
strings. Python 3 has bytes and strings. That is, all strings are now
Unicode strings, and if you want to deal with a bag of bytes, you use
the new `bytes` type. Python 3 will *never* implicitly convert between
strings and bytes, so if youre not sure which one you have at any
given moment, your code will almost certainly break. Read `the Strings
chapter`_ for more details.
Bytes vs. strings comes up again and again throughout the book.

+ In `Files`_, youll learn the difference between reading files in
binary and text mode. Reading (and writing!) files in text mode
requires an `encoding` parameter. Some text file methods count
characters, but other methods count bytes. If your code assumes that
one character == one byte, it *will* break on multi-byte characters.
+ In ` HTTP Web Services`_, the `httplib2` module fetches headers and
data over HTTP . HTTP headers are returned as strings, but the HTTP
body is returned as bytes.
+ In `Serializing Python Objects`_, youll learn why the `pickle`
module in Python 3 defines a new data format that is backwardly
incompatible with Python 2. (Hint: its because of bytes and strings.)
Also, Python 3 supports serializing objects to and from JSON , which
doesnt even have a `bytes` type. Ill show you how to hack around that.
+ In `Case study: porting `chardet` to Python 3`_, its just a bloody
  mess of bytes and strings everywhere.


Even if you dont care about Unicode (oh but you will), youll want to
read about `string formatting in Python 3`_, which is completely
different from Python 2.
Iterators are everywhere in Python 3, and I understand them a lot
better than I did five years ago when I wrote Dive Into Python. You
need to understand them too, because lots of functions that used to
return lists in Python 2 will now return iterators in Python 3. At a
minimum, you should read `the second half of the Iterators chapter`_
and `the second half of the Advanced Iterators chapter`_.
By popular request, Ive added an appendix on `Special Method Names`_,
which is kind of like `the Python docs Data Model chapter`_ but with
more snark.
When I was writing Dive Into Python, all of the available XML
libraries sucked. Then Fredrik Lundh wrote `ElementTree`_, which
doesnt suck at all. The Python gods wisely `incorporated ElementTree
into the standard library`_, and now it forms the basis for `my new
XML chapter`_. The old ways of parsing XML are still around, but you
should avoid them, because they suck!
Also new in Pythonnot in the language but in the communityis the
emergence of code repositories like `The Python Package Index`_
(PyPI). Python comes with utilities to package your code in standard
formats and distribute those packages on PyPI. Read `Packaging Python
Libraries`_ for details.
200111 `Mark Pilgrim`_

.. _Serializing Python Objects: serializing.html
.. _ElementTree: http://effbot.org/zone/element-index.htm
.. _2to3: porting-code-to-python-3-with-2to3.html
.. _my new XML chapter: xml.html
.. _incorporated ElementTree into the standard library: http://docs.python.org/3.1/library/xml.etree.elementtree.html
.. _Mark Pilgrim: about.html
.. _Dive Into Python 3: table-of-contents.html#whats-new
.. _ Web Services: http-web-services.html
.. _the second half of the Advanced Iterators chapter: advanced-iterators.html#generator-expressions
.. _Packaging Python Libraries: packaging.html
.. _ to Python 3: case-study-porting-chardet-to-python-3.html
.. _The Python Package Index: http://pypi.python.org/
.. _Files: files.html
.. _Home: index.html
.. _the second half of the Iterators chapter: iterators.html#a-fibonacci-iterator
.. _ chapter: http://www.python.org/doc/3.1/reference/datamodel.html#special-method-names
.. _string formatting in Python 3: strings.html#formatting-strings
.. _Special Method Names: special-method-names.html
.. _the Strings chapter: strings.html
.. _starting at the beginning: installing-python.html
.. _Dive Into Python: http://diveintopython.org/


