
Classes & Iterators
===================

Difficulty level: ♦♦♦♢♢

❝ East is East, and West is West, and never the twain shall
meet. ❞
`Rudyard Kipling`_


Diving In
---------

Iterators are the secret sauce of Python 3. Theyre everywhere,
underlying everything, always just out of sight. `Comprehensions`_ are
just a simple form of iterators . Generators are just a simple form of
iterators . A function that `yields` values is a nice, compact way of
building an iterator without building an iterator. Let me show you
what I mean by that. Remember `the Fibonacci generator`_? Here it is
as a built-from- scratch iterator:
[`download `fibonacci2.py``_]

::

    class Fib:
        '''iterator that yields numbers in the Fibonacci sequence'''
    
        def __init__(self, max):
            self.max = max
    
        def __iter__(self):
            self.a = 0
            self.b = 1
            return self
    
        def __next__(self):
            fib = self.a
            if fib > self.max:
                raise StopIteration
            self.a, self.b = self.b, self.a + self.b
            return fib


Lets take that one line at a time.

::

    class Fib:


`class`? Whats a class?

⁂


Defining Classes
----------------

Python is fully object-oriented: you can define your own classes,
inherit from your own or built-in classes, and instantiate the classes
youve defined. Defining a class in Python is simple. As with functions,
there is no separate interface definition. Just define the class and
start coding.  A Python class starts with the reserved word `class`,
followed by the class name. Technically, thats all thats required,
since a class doesnt need to inherit from any other class.

::

    class PapayaWhip:  ①
        pass           ②



#. The name of this class is `PapayaWhip`, and it doesnt inherit from
   any other class. Class names are usually capitalized,
   `EachWordLikeThis`, but this is only a convention, not a requirement.
#. You probably guessed this, but everything in a class is indented,
   just like the code within a function, `if` statement, `for` loop, or
   any other block of code. The first line not indented is outside the
   class.


This `PapayaWhip` class doesnt define any methods or attributes, but
syntactically, there needs to be something in the definition, thus the
`pass` statement. This is a Python reserved word that just means move
along, nothing to see here. Its a statement that does nothing, and its
a good placeholder when youre stubbing out functions or classes.
☞The `pass` statement in Python is like a empty set of curly
braces ( `{}`) in Java or C.

Many classes are inherited from other classes, but this one is not.
Many classes define methods, but this one does not. There is nothing
that a Python class absolutely must have, other than a name. In
particular, C++ programmers may find it odd that Python classes dont
have explicit constructors and destructors. Although its not required,
Python classes *can* have something similar to a constructor: the
`__init__()` method.


The `__init__()` Method
~~~~~~~~~~~~~~~~~~~~~~~

This example shows the initialization of the `Fib` class using the
`__init__` method.

::

    class Fib:
        '''iterator that yields numbers in the Fibonacci sequence'''  ①
    
        def __init__(self, max):                                      ②



#. Classes can (and should) have docstrings too, just like modules
   and functions.
#. The `__init__()` method is called immediately after an instance of
   the class is created. It would be temptingbut technically incorrectto
   call this the constructor of the class. Its tempting, because it looks
   like a C++ constructor (by convention, the `__init__()` method is the
   first method defined for the class), acts like one (its the first
   piece of code executed in a newly created instance of the class), and
   even sounds like one. Incorrect, because the object has already been
   constructed by the time the `__init__()` method is called, and you
   already have a valid reference to the new instance of the class.


The first argument of every class method, including the `__init__()`
method, is always a reference to the current instance of the class. By
convention, this argument is named self . This argument fills the role
of the reserved word `this` in C++ or Java, but self is not a reserved
word in Python, merely a naming convention. Nonetheless, please dont
call it anything but self ; this is a very strong convention.
In all class methods, self refers to the instance whose method was
called. But in the specific case of the `__init__()` method, the
instance whose method was called is also the newly created object.
Although you need to specify self explicitly when defining the method,
you do *not* specify it when calling the method; Python will add it
for you automatically.

⁂


Instantiating Classes
---------------------

Instantiating classes in Python is straightforward. To instantiate a
class, simply call the class as if it were a function, passing the
arguments that the `__init__()` method requires. The return value will
be the newly created object.

::

    
    >>> import fibonacci2
    >>> fib = fibonacci2.Fib(100)  ①
    >>> fib                        ②
    <fibonacci2.Fib object at 0x00DB8810>
    >>> fib.__class__              ③
    <class 'fibonacci2.Fib'>
    >>> fib.__doc__                ④
    'iterator that yields numbers in the Fibonacci sequence'



#. You are creating an instance of the `Fib` class (defined in the
   `fibonacci2` module) and assigning the newly created instance to the
   variable fib . You are passing one parameter, `100`, which will end up
   as the max argument in `Fib`s `__init__()` method.
#. fib is now an instance of the `Fib` class.
#. Every class instance has a built-in attribute, `__class__`, which
   is the objects class. Java programmers may be familiar with the
   `Class` class, which contains methods like `getName()` and
   `getSuperclass()` to get metadata information about an object. In
   Python, this kind of metadata is available through attributes, but the
   idea is the same.
#. You can access the instances `docstring` just as with a function or
   a module. All instances of a class share the same `docstring`.


☞In Python, simply call a class as if it were a function to
create a new instance of the class. There is no explicit `new`
operator like there is in C++ or Java.

⁂


Instance Variables
------------------

On to the next line:

::

    class Fib:
        def __init__(self, max):
            self.max = max        ①



#. What is self.max ? Its an instance variable. It is completely
   separate from max , which was passed into the `__init__()` method as
   an argument. self.max is global to the instance. That means that you
   can access it from other methods.



::

    class Fib:
        def __init__(self, max):
            self.max = max        ①
        .
        .
        .
        def __next__(self):
            fib = self.a
            if fib > self.max:    ②



#. self.max is defined in the `__init__()` method
#. and referenced in the `__next__()` method.


Instance variables are specific to one instance of a class. For
example, if you create two `Fib` instances with different maximum
values, they will each remember their own values.

::

    
    >>> import fibonacci2
    >>> fib1 = fibonacci2.Fib(100)
    >>> fib2 = fibonacci2.Fib(200)
    >>> fib1.max
    100
    >>> fib2.max
    200


⁂


A Fibonacci Iterator
--------------------

*Now* youre ready to learn how to build an iterator. An iterator is
just a class that defines an `__iter__()` method. All three of these
class methods, `__init__`, `__iter__`, and `__next__`, begin and end
with a pair of underscore ( `_`) characters. Why is that? Theres
nothing magical about it, but it usually indicates that these are
special methods . The only thing special about special methods is that
they arent called directly; Python calls them when you use some other
syntax on the class or an instance of the class. `More about special
methods`_.
[`download `fibonacci2.py``_]

::

    class Fib:                                        ①
        def __init__(self, max):                      ②
            self.max = max
    
        def __iter__(self):                           ③
            self.a = 0
            self.b = 1
            return self
    
        def __next__(self):                           ④
            fib = self.a
            if fib > self.max:
                raise StopIteration                   ⑤
            self.a, self.b = self.b, self.a + self.b
            return fib                                ⑥


#. To build an iterator from scratch, `Fib` needs to be a class, not a
   function.
#. Calling `Fib(max)` is really creating an instance of this class and
   calling its `__init__()` method with max . The `__init__()` method
   saves the maximum value as an instance variable so other methods can
   refer to it later.
#. The `__iter__()` method is called whenever someone calls
   `iter(fib)`. (As youll see in a minute, a `for` loop will call this
   automatically, but you can also call it yourself manually.) After
   performing beginning-of-iteration initialization (in this case,
   resetting `self.a` and `self.b`, our two counters), the `__iter__()`
   method can return any object that implements a `__next__()` method. In
   this case (and in most cases), `__iter__()` simply returns self ,
   since this class implements its own `__next__()` method.
#. The `__next__()` method is called whenever someone calls `next()`
   on an iterator of an instance of a class. That will make more sense in
   a minute.
#. When the `__next__()` method raises a `StopIteration` exception,
   this signals to the caller that the iteration is exhausted. Unlike
   most exceptions, this is not an error; its a normal condition that
   just means that the iterator has no more values to generate. If the
   caller is a `for` loop, it will notice this `StopIteration` exception
   and gracefully exit the loop. (In other words, it will swallow the
   exception.) This little bit of magic is actually the key to using
   iterators in `for` loops.
#. To spit out the next value, an iterators `__next__()` method simply
   `return`s the value. Do not use `yield` here; thats a bit of syntactic
   sugar that only applies when youre using generators. Here youre
   creating your own iterator from scratch; use `return` instead.


Thoroughly confused yet? Excellent. Lets see how to call this
iterator:

::

    
    >>> from fibonacci2 import Fib
    >>> for n in Fib(1000):
    ...     print(n, end=' ')
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


Why, its exactly the same! Byte for byte identical to how you called
`Fibonacci-as-a-generator`_ (modulo one capital letter). But how?
Theres a bit of magic involved in `for` loops. Heres what happens:

+ The `for` loop calls `Fib(1000)`, as shown. This returns an instance
  of the `Fib` class. Call this fib_inst .
+ Secretly, and quite cleverly, the `for` loop calls `iter(fib_inst)`,
  which returns an iterator object. Call this fib_iter . In this case,
  fib_iter == fib_inst , because the `__iter__()` method returns self ,
  but the `for` loop doesnt know (or care) about that.
+ To loop through the iterator, the `for` loop calls `next(fib_iter)`,
  which calls the `__next__()` method on the `fib_iter` object, which
  does the next-Fibonacci-number calculations and returns a value. The
  `for` loop takes this value and assigns it to n , then executes the
  body of the `for` loop for that value of n .
+ How does the `for` loop know when to stop? Im glad you asked! When
  `next(fib_iter)` raises a `StopIteration` exception, the `for` loop
  will swallow the exception and gracefully exit. (Any other exception
  will pass through and be raised as usual.) And where have you seen a
  `StopIteration` exception? In the `__next__()` method, of course!


⁂


A Plural Rule Iterator
----------------------
iter(f) calls f.__iter__
next(f) calls f.__next__
Now its time for the finale. Lets rewrite the `plural rules
generator`_ as an iterator.
[`download `plural6.py``_]

::

    class LazyRules:
        rules_filename = 'plural6-rules.txt'
    
        def __init__(self):
            self.pattern_file = open(self.rules_filename, encoding='utf-8')
            self.cache = []
    
        def __iter__(self):
            self.cache_index = 0
            return self
    
        def __next__(self):
            self.cache_index += 1
            if len(self.cache) >= self.cache_index:
                return self.cache[self.cache_index - 1]
    
            if self.pattern_file.closed:
                raise StopIteration
    
            line = self.pattern_file.readline()
            if not line:
                self.pattern_file.close()
                raise StopIteration
    
            pattern, search, replace = line.split(None, 3)
            funcs = build_match_and_apply_functions(
                pattern, search, replace)
            self.cache.append(funcs)
            return funcs
    
    rules = LazyRules()


So this is a class that implements `__iter__()` and `__next__()`, so
it can be used as an iterator. Then, you instantiate the class and
assign it to rules . This happens just once, on import.
Lets take the class one bite at a time.

::

    class LazyRules:
        rules_filename = 'plural6-rules.txt'
    
        def __init__(self):
            self.pattern_file = open(self.rules_filename, encoding='utf-8')  ①
            self.cache = []                                                  ②


#. When we instantiate the `LazyRules` class, open the pattern file
   but dont read anything from it. (That comes later.)
#. After opening the patterns file, initialize the cache. Youll use
   this cache later (in the `__next__()` method) as you read lines from
   the pattern file.


Before we continue, lets take a closer look at rules_filename . Its
not defined within the `__iter__()` method. In fact, its not defined
within *any* method. Its defined at the class level. Its a class
variable , and although you can access it just like an instance
variable ( self.rules_filename ), it is shared across all instances of
the `LazyRules` class.

::

    
    >>> import plural6
    >>> r1 = plural6.LazyRules()
    >>> r2 = plural6.LazyRules()
    >>> r1.rules_filename                               ①
    'plural6-rules.txt'
    >>> r2.rules_filename
    'plural6-rules.txt'
    >>> r2.rules_filename = 'r2-override.txt'           ②
    >>> r2.rules_filename
    'r2-override.txt'
    >>> r1.rules_filename
    'plural6-rules.txt'
    >>> r2.__class__.rules_filename                     ③
    'plural6-rules.txt'
    >>> r2.__class__.rules_filename = 'papayawhip.txt'  ④
    >>> r1.rules_filename
    'papayawhip.txt'
    >>> r2.rules_filename                               ⑤
    'r2-overridetxt'



#. Each instance of the class inherits the rules_filename attribute
   with the value defined by the class.
#. Changing the attributes value in one instance does not affect other
   instances
#. nor does it change the class attribute. You can access the class
   attribute (as opposed to an individual instances attribute) by using
   the special `__class__` attribute to access the class itself.
#. If you change the class attribute, all instances that are still
   inheriting that value (like r1 here) will be affected.
#. Instances that have overridden that attribute (like r2 here) will
   not be affected.


And now back to our show.

::

    def __iter__(self):       ①
        self.cache_index = 0
        return self           ②


#. The `__iter__()` method will be called every time someonesay, a
   `for` loopcalls `iter(rules)`.
#. The one thing that every `__iter__()` method must do is return an
   iterator. In this case, it returns self , which signals that this
   class defines a `__next__()` method which will take care of returning
   values throughout the iteration.



::

        def __next__(self):                                 ①
            .
            .
            .
            pattern, search, replace = line.split(None, 3)
            funcs = build_match_and_apply_functions(        ②
                pattern, search, replace)
            self.cache.append(funcs)                        ③
            return funcs

#. The `__next__()` method gets called whenever someonesay, a `for`
   loopcalls `next(rules)`. This method will only make sense if we start
   at the end and work backwards. So lets do that.
#. The last part of this function should look familiar, at least. The
   `build_match_and_apply_functions()` function hasnt changed; its the
   same as it ever was.
#. The only difference is that, before returning the match and apply
   functions (which are stored in the tuple funcs ), were going to save
   them in `self.cache`.


Moving backwards

::

        def __next__(self):
            .
            .
            .
            line = self.pattern_file.readline()  ①
            if not line:                         ②
                self.pattern_file.close()
                raise StopIteration              ③
            .
            .
            .



#. A bit of advanced file trickery here. The `readline()` method
   (note: singular, not the plural `readlines()`) reads exactly one line
   from an open file. Specifically, the next line. ( *File objects are
   iterators too! Its iterators all the way down*)
#. If there was a line for `readline()` to read, line will not be an
   empty string. Even if the file contained a blank line, line would end
   up as the one-character string `'\n'` (a carriage return). If line is
   really an empty string, that means there are no more lines to read
   from the file.
#. When we reach the end of the file, we should close the file and
   raise the magic `StopIteration` exception. Remember, we got to this
   point because we needed a match and apply function for the next rule.
   The next rule comes from the next line of the file but there is no
   next line! Therefore, we have no value to return. The iteration is
   over. (♫ The partys over ♫)


Moving backwards all the way to the start of the `__next__()` method

::

        def __next__(self):
            self.cache_index += 1
            if len(self.cache) >= self.cache_index:
                return self.cache[self.cache_index - 1]     ①
    
            if self.pattern_file.closed:
                raise StopIteration                         ②
            .
            .
            .



#. `self.cache` will be a list of the functions we need to match and
   apply individual rules. (At least *that* should sound familiar!)
   `self.cache_index` keeps track of which cached item we should return
   next. If we havent exhausted the cache yet ( i.e. if the length of
   `self.cache` is greater than `self.cache_index`), then we have a cache
   hit! Hooray! We can return the match and apply functions from the
   cache instead of building them from scratch.
#. On the other hand, if we dont get a hit from the cache, *and* the
   file object has been closed (which could happen, further down the
   method, as you saw in the previous code snippet), then theres nothing
   more we can do. If the file is closed, it means weve exhausted itweve
   already read through every line from the pattern file, and weve
   already built and cached the match and apply functions for each
   pattern. The file is exhausted; the cache is exhausted; Im exhausted.
   Wait, what? Hang in there, were almost done.


Putting it all together, heres what happens when:

+ When the module is imported, it creates a single instance of the
  `LazyRules` class, called rules , which opens the pattern file but
  does not read from it.
+ When asked for the first match and apply function, it checks its
  cache but finds the cache is empty. So it reads a single line from the
  pattern file, builds the match and apply functions from those
  patterns, and caches them.
+ Lets say, for the sake of argument, that the very first rule
  matched. If so, no further match and apply functions are built, and no
  further lines are read from the pattern file.
+ Furthermore, for the sake of argument, suppose that the caller calls
  the `plural()` function *again* to pluralize a different word. The
  `for` loop in the `plural()` function will call `iter(rules)`, which
  will reset the cache index but will not reset the open file object.
+ The first time through, the `for` loop will ask for a value from
  rules , which will invoke its `__next__()` method. This time, however,
  the cache is primed with a single pair of match and apply functions,
  corresponding to the patterns in the first line of the pattern file.
  Since they were built and cached in the course of pluralizing the
  previous word, theyre retrieved from the cache. The cache index
  increments, and the open file is never touched.
+ Lets say, for the sake of argument, that the first rule does *not*
  match this time around. So the `for` loop comes around again and asks
  for another value from rules . This invokes the `__next__()` method a
  second time. This time, the cache is exhaustedit only contained one
  item, and were asking for a secondso the `__next__()` method
  continues. It reads another line from the open file, builds match and
  apply functions out of the patterns, and caches them.
+ This read-build-and-cache process will continue as long as the rules
  being read from the pattern file dont match the word were trying to
  pluralize. If we do find a matching rule before the end of the file,
  we simply use it and stop, with the file still open. The file pointer
  will stay wherever we stopped reading, waiting for the next
  `readline()` command. In the meantime, the cache now has more items in
  it, and if we start all over again trying to pluralize a new word,
  each of those items in the cache will be tried before reading the next
  line from the pattern file.


We have achieved pluralization nirvana.

#. Minimal startup cost. The only thing that happens on `import` is
   instantiating a single class and opening a file (but not reading from
   it).
#. Maximum performance. The previous example would read through the
   file and build functions dynamically every time you wanted to
   pluralize a word. This version will cache functions as soon as theyre
   built, and in the worst case, it will only read through the pattern
   file once, no matter how many words you pluralize.
#. Separation of code and data. All the patterns are stored in a
   separate file. Code is code, and data is data, and never the twain
   shall meet.


☞Is this really nirvana? Well, yes and no. Heres something to
consider with the `LazyRules` example: the pattern file is opened
(during `__init__()`), and it remains open until the final rule is
reached. Python will eventually close the file when it exits, or after
the last instantiation of the `LazyRules` class is destroyed, but
still, that could be a *long* time. If this class is part of a long-
running Python process, the Python interpreter may never exit, and the
`LazyRules` object may never get destroyed.

There are ways around this. Instead of opening the file during
`__init__()` and leaving it open while you read rules one line at a
time, you could open the file, read all the rules, and immediately
close the file. Or you could open the file, read one rule, save the
file position with the `tell() method`_, close the file, and later
re-open it and use the `seek() method`_ to continue reading where
you left off. Or you could not worry about it and just leave the file
open, like this example code does. Programming is design, and design
is all about trade-offs and constraints. Leaving a file open too long
might be a problem; making your code more complicated might be a
problem. Which one is the bigger problem depends on your development
team, your application, and your runtime environment.

⁂


Further Reading
---------------


+ `Iterator types`_
+ `PEP 234: Iterators`_
+ `PEP 255: Simple Generators`_
+ `Generator Tricks for Systems Programmers`_

200111 `Mark Pilgrim`_

.. _plural6.py: examples/plural6.py
.. _Fibonacci-as-a-generator: generators.html#a-fibonacci-generator
.. _Dive Into Python 3: table-of-contents.html#iterators
.. _Rudyard Kipling: http://en.wikiquote.org/wiki/Rudyard_Kipling
.. _Iterator types: http://docs.python.org/3.1/library/stdtypes.html#iterator-types
.. _fibonacci2.py: examples/fibonacci2.py
.. _More about special methods: special-method-names.html
.. _PEP 234: Iterators: http://www.python.org/dev/peps/pep-0234/
.. _ method: files.html#read
.. _Mark Pilgrim: about.html
.. _PEP 255: Simple Generators: http://www.python.org/dev/peps/pep-0255/
.. _Comprehensions: comprehensions.html
.. _Generator Tricks for Systems Programmers: http://www.dabeaz.com/generators/


