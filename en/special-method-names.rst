
You are here: `Home`_ `Dive Into Python 3`_
Difficulty level: ♦♦♦♦♦


Special Method Names
====================

❝ My specialty is being right when other people are wrong.
❞
`George Bernard Shaw`_


Diving In
---------

Throughout this book, youve seen examples of special methodscertain
magic methods that Python invokes when you use certain syntax. Using
special methods, your classes can act like sets, like dictionaries,
like functions, like iterators, or even like numbers. This appendix
serves both as a reference for the special methods weve seen already
and a brief introduction to some of the more esoteric ones.


Basics
------

If youve read the `introduction to classes`_, youve already seen the
most common special method: the `__init__()` method. The majority of
classes I write end up needing some initialization. There are also a
few other basic special methods that are especially useful for
debugging your custom classes. Notes You Want So You Write And Python
Calls ① to initialize an instance `x = MyClass()` ` `x.
__init__ ()``_ ② the official representation as a string ` repr
(x)` ` `x. __repr__ ()``_ ③ the informal value as a string ` `
str (x)``_ `x. __str__ ()` ④ the informal value as a byte array
` bytes (x)` `x. __bytes__ ()` ⑤ the value as a formatted
string `format(x, format_spec )` ` `x. __format__ ( format_spec )``_

#. The `__init__()` method is called *after* the instance is created.
If you want to control the actual creation process, use the
`__new__()` method.
#. By convention, the `__repr__()` method should return a string that
is a valid Python expression.
#. The `__str__()` method is also called when you `print(x)`.
#. *New in Python 3*, since the `bytes` type was introduced.
#. By convention, format_spec should conform to the `Format
   Specification Mini-Language`_. `decimal.py` in the Python standard
   library provides its own `__format__()` method.




Classes That Act Like Iterators
-------------------------------

In `the Iterators chapter`_, you saw how to build an iterator from the
ground up using the `__iter__()` and `__next__()` methods. Notes You
Want So You Write And Python Calls ① to iterate through a
sequence ` iter (seq)` ` `seq. __iter__ ()``_ ② to get the next
value from an iterator ` next (seq)` ` `seq. __next__ ()``_ ③
to create an iterator in reverse order ` reversed (seq)` ` `seq.
__reversed__ ()``_

#. The `__iter__()` method is called whenever you create a new
iterator. Its a good place to initialize the iterator with initial
values.
#. The `__next__()` method is called whenever you retrieve the next
value from an iterator.
#. The `__reversed__()` method is uncommon. It takes an existing
   sequence and returns an iterator that yields the items in the sequence
   in reverse order, from last to first.


As you saw in `the Iterators chapter`_, a `for` loop can act on an
iterator. In this loop:

::

     `for x in seq:
        print(x)`


Python 3 will call `seq.__iter__()` to create an iterator, then call
the `__next__()` method on that iterator to get each value of x . When
the `__next__()` method raises a `StopIteration` exception, the `for`
loop ends gracefully.


Computed Attributes
-------------------
Notes You Want So You Write And Python Calls ① to get a
computed attribute (unconditionally) `x.my_property` ` `x.
__getattribute__ ( 'my_property' )``_ ② to get a computed
attribute (fallback) `x.my_property` ` `x. __getattr__ ( 'my_property'
)``_ ③ to set an attribute `x.my_property = value` ` `x.
__setattr__ ( 'my_property' , value )``_ ④ to delete an
attribute `del x.my_property` ` `x. __delattr__ ( 'my_property' )``_
⑤ to list all attributes and methods `dir(x)` ` `x. __dir__
()``_

#. If your class defines a `__getattribute__()` method, Python will
call it on *every reference to any attribute or method name* (except
special method names, since that would cause an unpleasant infinite
loop).
#. If your class defines a `__getattr__()` method, Python will call it
only after looking for the attribute in all the normal places. If an
instance x defines an attribute color , `x.color` will *not* call
`x.__getattr__('color')`; it will simply return the already-defined
value of x.color .
#. The `__setattr__()` method is called whenever you assign a value to
an attribute.
#. The `__delattr__()` method is called whenever you delete an
attribute.
#. The `__dir__()` method is useful if you define a `__getattr__()` or
   `__getattribute__()` method. Normally, calling `dir(x)` would only
   list the regular attributes and methods. If your `__getattr__()`
   method handles a color attribute dynamically, `dir(x)` would not list
   color as one of the available attributes. Overriding the `__dir__()`
   method allows you to list color as an available attribute, which is
   helpful for other people who wish to use your class without digging
   into the internals of it.


The distinction between the `__getattr__()` and `__getattribute__()`
methods is subtle but important. I can explain it with two examples:

::

    
     `class Dynamo:
        def __getattr__(self, key):
            if key == 'color':         ①
                return 'PapayaWhip'
            else:
                raise AttributeError   ②`
    
    >>> dyn = Dynamo()
    >>> dyn.color                      ③
    'PapayaWhip'
    >>> dyn.color = 'LemonChiffon'
    >>> dyn.color                      ④
    'LemonChiffon'



#. The attribute name is passed into the `__getattr__()` method as a
string. If the name is `'color'`, the method returns a value. (In this
case, its just a hard-coded string, but you would normally do some
sort of computation and return the result.)
#. If the attribute name is unknown, the `__getattr__()` method needs
to raise an `AttributeError` exception, otherwise your code will
silently fail when accessing undefined attributes. (Technically, if
the method doesnt raise an exception or explicitly return a value, it
returns `None`, the Python null value. This means that *all*
attributes not explicitly defined will be `None`, which is almost
certainly not what you want.)
#. The dyn instance does not have an attribute named color , so the
`__getattr__()` method is called to provide a computed value.
#. After explicitly setting dyn.color , the `__getattr__()` method
   will no longer be called to provide a value for dyn.color , because
   dyn.color is already defined on the instance.


On the other hand, the `__getattribute__()` method is absolute and
unconditional.

::

    
     `class SuperDynamo:
        def __getattribute__(self, key):
            if key == 'color':
                return 'PapayaWhip'
            else:
                raise AttributeError`
    
    >>> dyn = SuperDynamo()
    >>> dyn.color                      ①
    'PapayaWhip'
    >>> dyn.color = 'LemonChiffon'
    >>> dyn.color                      ②
    'PapayaWhip'



#. The `__getattribute__()` method is called to provide a value for
dyn.color .
#. Even after explicitly setting dyn.color , the `__getattribute__()`
   method *is still called* to provide a value for dyn.color . If
   present, the `__getattribute__()` method *is called unconditionally*
   for every attribute and method lookup, even for attributes that you
   explicitly set after creating an instance.


☞If your class defines a `__getattribute__()` method, you
probably also want to define a `__setattr__()` method and coordinate
between them to keep track of attribute values. Otherwise, any
attributes you set after creating an instance will disappear into a
black hole.
You need to be extra careful with the `__getattribute__()` method,
because it is also called when Python looks up a method name on your
class.

::

    
     `class Rastan:
        def __getattribute__(self, key):
            raise AttributeError           ①
        def swim(self):
            pass`
    
    >>> hero = Rastan()
    >>> hero.swim()                        ②
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 3, in __getattribute__
    AttributeError



#. This class defines a `__getattribute__()` method which always
raises an `AttributeError` exception. No attribute or method lookups
will succeed.
#. When you call `hero.swim()`, Python looks for a `swim()` method in
   the `Rastan` class. This lookup goes through the `__getattribute__()`
   method, *because all attribute and method lookups go through the
   `__getattribute__()` method*. In this case, the `__getattribute__()`
   method raises an `AttributeError` exception, so the method lookup
   fails, so the method call fails.




Classes That Act Like Functions
-------------------------------

You can make an instance of a class callableexactly like a function is
callableby defining the `__call__()` method. Notes You Want So You
Write And Python Calls to call an instance like a function
`my_instance()` ` `my_instance. __call__ ()``_
The ` `zipfile` module`_ uses this to define a class that can decrypt
an encrypted zip file with a given password. The zip decryption
algorithm requires you to store state during decryption. Defining the
decryptor as a class allows you to maintain this state within a single
instance of the decryptor class. The state is initialized in the
`__init__()` method and updated as the file is decrypted . But since
the class is also callable like a function, you can pass the instance
as the first argument of the `map()` function, like so:

::

     `# excerpt from zipfile.py
    class _ZipDecrypter:
    .
    .
    .
        def __init__(self, pwd):
            self.key0 = 305419896               ①
            self.key1 = 591751049
            self.key2 = 878082192
            for p in pwd:
                self._UpdateKeys(p)
    
        def __call__(self, c):                  ②
            assert isinstance(c, int)
            k = self.key2 | 2
            c = c ^ (((k * (k^1)) >> 8) & 255)
            self._UpdateKeys(c)
            return c
    .
    .
    .
    zd = _ZipDecrypter(pwd)                    ③
    bytes = zef_file.read(12)
    h = list(map(zd, bytes[0:12]))             ④`



#. The `_ZipDecryptor` class maintains state in the form of three
rotating keys, which are later updated in the `_UpdateKeys()` method
(not shown here).
#. The class defines a `__call__()` method, which makes class
instances callable like functions. In this case, the `__call__()`
method decrypts a single byte of the zip file, then updates the
rotating keys based on the byte that was decrypted.
#. zd is an instance of the `_ZipDecryptor` class. The pwd variable is
passed to the `__init__()` method, where it is stored and used to
update the rotating keys for the first time.
#. Given the first 12 bytes of a zip file, decrypt them by mapping the
   bytes to zd , in effect calling zd 12 times, which invokes the
   `__call__()` method 12 times, which updates its internal state and
   returns a resulting byte 12 times.




Classes That Act Like Sets
--------------------------

If your class acts as a container for a set of valuesthat is, if it
makes sense to ask whether your class contains a valuethen it should
probably define the following special methods that make it act like a
set. Notes You Want So You Write And Python Calls the number of items
` len (s)` ` `s. __len__ ()``_ to know whether it contains a specific
value `x in s` ` `s. __contains__ ( x )``_
The ` `cgi` module`_ uses these methods in its `FieldStorage` class,
which represents all of the form fields or query parameters submitted
to a dynamic web page.

::

     `# A script which responds to http://example.com/search?q=cgi
    import cgi
    fs = cgi.FieldStorage()
    if 'q' in fs:                                               ①
      do_search()
    
    # An excerpt from cgi.py that explains how that works
    class FieldStorage:
    .
    .
    .
        def __contains__(self, key):                            ②
            if self.list is None:
                raise TypeError('not indexable')
            return any(item.name == key for item in self.list)  ③
    
        def __len__(self):                                      ④
            return len(self.keys())                             ⑤`



#. Once you create an instance of the `cgi.FieldStorage` class, you
can use the `in` operator to check whether a particular parameter was
included in the query string.
#. The `__contains__()` method is the magic that makes this work. When
you say `if 'q' in fs`, Python looks for the `__contains__()` method
on the fs object, which is defined in `cgi.py`. The value `'q'` is
passed into the `__contains__()` method as the key argument.
#. The `any()` function takes a `generator expression`_ and returns
`True` if the generator spits out any items. The `any()` function is
smart enough to stop as soon as the first match is found.
#. The same `FieldStorage` class also supports returning its length,
so you can say `len( fs )` and it will call the `__len__()` method on
the `FieldStorage` class to return the number of query parameters that
it identified.
#. The `self.keys()` method checks whether `self.list is None`, so the
   `__len__` method doesnt need to duplicate this error checking.




Classes That Act Like Dictionaries
----------------------------------

Extending the previous section a bit, you can define classes that not
only respond to the `in` operator and the `len()` function, but they
act like full-blown dictionaries, returning values based on keys.
Notes You Want So You Write And Python Calls to get a value by its key
`x[key]` ` `x. __getitem__ ( key )``_ to set a value by its key
`x[key] = value` ` `x. __setitem__ ( key , value )``_ to delete a key-
value pair `del x[key]` ` `x. __delitem__ ( key )``_ to provide a
default value for missing keys `x[nonexistent_key]` ` `x. __missing__
( nonexistent_key )``_
The `FieldStorage` class from the ` `cgi` module`_ also defines these
special methods, which means you can do things like this:

::

     `# A script which responds to http://example.com/search?q=cgi
    import cgi
    fs = cgi.FieldStorage()
    if 'q' in fs:
      do_search(fs['q'])                              ①
    
    # An excerpt from cgi.py that shows how it works
    class FieldStorage:
    .
    .
    .
        def __getitem__(self, key):                   ②
            if self.list is None:
                raise TypeError('not indexable')
            found = []
            for item in self.list:
                if item.name == key: found.append(item)
            if not found:
                raise KeyError(key)
            if len(found) == 1:
                return found[0]
            else:
                return found`



#. The fs object is an instance of `cgi.FieldStorage`, but you can
still evaluate expressions like `fs['q']`.
#. `fs['q']` invokes the `__getitem__()` method with the key parameter
   set to `'q'`. It then looks up in its internally maintained list of
   query parameters ( self.list ) for an item whose `.name` matches the
   given key.




Classes That Act Like Numbers
-----------------------------

Using the appropriate special methods, you can define your own classes
that act like numbers. That is, you can add them, subtract them, and
perform other mathematical operations on them. This is how fractions
are implementedthe ` Fraction ` class implements these special
methods, then you can do things like this:

::

    
    >>> from fractions import Fraction
    >>> x = Fraction(1, 3)
    >>> x / 3
    Fraction(1, 9)


Here is the comprehensive list of special methods you need to
implement a number-like class. Notes You Want So You Write And Python
Calls addition `x + y` ` `x. __add__ ( y )``_ subtraction `x - y` `
`x. __sub__ ( y )``_ multiplication `x * y` ` `x. __mul__ ( y )``_
division `x / y` ` `x. __truediv__ ( y )``_ floor division `x // y` `
`x. __floordiv__ ( y )``_ modulo (remainder) `x % y` ` `x. __mod__ ( y
)``_ floor division & modulo `divmod(x, y)` ` `x. __divmod__ ( y )``_
raise to power `x ** y` ` `x. __pow__ ( y )``_ left bit-shift `x << y`
` `x. __lshift__ ( y )``_ right bit-shift `x >> y` ` `x. __rshift__ (
y )``_ bitwise `and` `x & y` ` `x. __and__ ( y )``_ bitwise `xor` `x ^
y` ` `x. __xor__ ( y )``_ bitwise `or` `x | y` ` `x. __or__ ( y )``_
Thats all well and good if x is an instance of a class that implements
those methods. But what if it doesnt implement one of them? Or worse,
what if it implements it, but it cant handle certain kinds of
arguments? For example:

::

    
    >>> from fractions import Fraction
    >>> x = Fraction(1, 3)
    >>> 1 / x
    Fraction(3, 1)


This is *not* a case of taking a `Fraction` and dividing it by an
integer (as in the previous example). That case was straightforward:
`x / 3` calls `x.__truediv__(3)`, and the `__truediv__()` method of
the `Fraction` class handles all the math. But integers dont know how
to do arithmetic operations with fractions. So why does this example
work?
There is a second set of arithmetic special methods with reflected
operands . Given an arithmetic operation that takes two operands (
e.g. `x / y`), there are two ways to go about it:

#. Tell x to divide itself by y , or
#. Tell y to divide itself into x


The set of special methods above take the first approach: given `x /
y`, they provide a way for x to say I know how to divide myself by y .
The following set of special methods tackle the second approach: they
provide a way for y to say I know how to be the denominator and divide
myself into x . Notes You Want So You Write And Python Calls addition
`x + y` ` `y. __radd__ ( x )``_ subtraction `x - y` ` `y. __rsub__ ( x
)``_ multiplication `x * y` ` `y. __rmul__ ( x )``_ division `x / y` `
`y. __rtruediv__ ( x )``_ floor division `x // y` ` `y. __rfloordiv__
( x )``_ modulo (remainder) `x % y` ` `y. __rmod__ ( x )``_ floor
division & modulo `divmod(x, y)` ` `y. __rdivmod__ ( x )``_ raise to
power `x ** y` ` `y. __rpow__ ( x )``_ left bit-shift `x << y` ` `y.
__rlshift__ ( x )``_ right bit-shift `x >> y` ` `y. __rrshift__ ( x
)``_ bitwise `and` `x & y` ` `y. __rand__ ( x )``_ bitwise `xor` `x ^
y` ` `y. __rxor__ ( x )``_ bitwise `or` `x | y` ` `y. __ror__ ( x )``_
But wait! Theres more! If youre doing in-place operations, like `x /=
3`, there are even more special methods you can define. Notes You Want
So You Write And Python Calls in-place addition `x += y` ` `x.
__iadd__ ( y )``_ in-place subtraction `x -= y` ` `x. __isub__ ( y
)``_ in-place multiplication `x *= y` ` `x. __imul__ ( y )``_ in-place
division `x /= y` ` `x. __itruediv__ ( y )``_ in-place floor division
`x //= y` ` `x. __ifloordiv__ ( y )``_ in-place modulo `x %= y` ` `x.
__imod__ ( y )``_ in-place raise to power `x **= y` ` `x. __ipow__ ( y
)``_ in-place left bit-shift `x <<= y` ` `x. __ilshift__ ( y )``_ in-
place right bit-shift `x >>= y` ` `x. __irshift__ ( y )``_ in-place
bitwise `and` `x &= y` ` `x. __iand__ ( y )``_ in-place bitwise `xor`
`x ^= y` ` `x. __ixor__ ( y )``_ in-place bitwise `or` `x |= y` ` `x.
__ior__ ( y )``_
Note: for the most part, the in-place operation methods are not
required. If you dont define an in-place method for a particular
operation, Python will try the methods. For example, to execute the
expression `x /= y`, Python will:

#. Try calling `x.__itruediv__( y )`. If this method is defined and
returns a value other than `NotImplemented`, were done.
#. Try calling `x.__truediv__( y )`. If this method is defined and
returns a value other than `NotImplemented`, the old value of x is
discarded and replaced with the return value, just as if you had done
` x = x / y` instead.
#. Try calling `y.__rtruediv__( x )`. If this method is defined and
   returns a value other than `NotImplemented`, the old value of x is
   discarded and replaced with the return value.


So you only need to define in-place methods like the `__itruediv__()`
method if you want to do some special optimization for in-place
operands. Otherwise Python will essentially reformulate the in-place
operand to use a regular operand + a variable assignment.
There are also a few unary mathematical operations you can perform on
number-like objects by themselves. Notes You Want So You Write And
Python Calls negative number `-x` ` `x. __neg__ ()``_ positive number
`+x` ` `x. __pos__ ()``_ absolute value `abs(x)` ` `x. __abs__ ()``_
inverse `~x` ` `x. __invert__ ()``_ complex number `complex(x)` ` `x.
__complex__ ()``_ integer `int(x)` ` `x. __int__ ()``_ floating point
number `float(x)` ` `x. __float__ ()``_ number rounded to nearest
integer `round(x)` ` `x. __round__ ()``_ number rounded to nearest n
digits `round(x, n)` ` `x. __round__ (n)``_ smallest integer `>= x`
`math.ceil(x)` ` `x. __ceil__ ()``_ largest integer `<= x`
`math.floor(x)` ` `x. __floor__ ()``_ truncate `x` to nearest integer
toward 0 `math.trunc(x)` ` `x. __trunc__ ()``_ `PEP 357`_ number as a
list index `a_list[ x ]` ` `a_list[x. __index__ ()]``_


Classes That Can Be Compared
----------------------------

I broke this section out from the previous one because comparisons are
not strictly the purview of numbers. Many datatypes can be
comparedstrings, lists, even dictionaries. If youre creating your own
class and it makes sense to compare your objects to other objects, you
can use the following special methods to implement comparisons. Notes
You Want So You Write And Python Calls equality `x == y` ` `x. __eq__
( y )``_ inequality `x != y` ` `x. __ne__ ( y )``_ less than `x < y` `
`x. __lt__ ( y )``_ less than or equal to `x <= y` ` `x. __le__ ( y
)``_ greater than `x > y` ` `x. __gt__ ( y )``_ greater than or equal
to `x >= y` ` `x. __ge__ ( y )``_ truth value in a boolean context `if
x:` ` `x. __bool__ ()``_
☞If you define a `__lt__()` method but no `__gt__()` method,
Python will use the `__lt__()` method with operands swapped. However,
Python will not combine methods. For example, if you define a
`__lt__()` method and a `__eq__()` method and try to test whether `x
<= y`, Python will not call `__lt__()` and `__eq__()` in sequence. It
will only call the `__le__()` method.


Classes That Can Be Serialized
------------------------------

Python supports `serializing and unserializing arbitrary objects`_.
(Most Python references call this process pickling and unpickling.)
This can be useful for saving state to a file and restoring it later.
All of the `native datatypes`_ support pickling already. If you create
a custom class that you want to be able to pickle, read up on `the
pickle protocol`_ to see when and how the following special methods
are called. Notes You Want So You Write And Python Calls a custom
object copy `copy.copy(x)` ` `x. __copy__ ()``_ a custom object
deepcopy `copy.deepcopy(x)` ` `x. __deepcopy__ ()``_ * to get an
objects state before pickling `pickle.dump(x, file )` ` `x.
__getstate__ ()``_ * to serialize an object `pickle.dump(x, file )` `
`x. __reduce__ ()``_ * to serialize an object (new pickling protocol)
`pickle.dump(x, file , protocol_version )` ` `x. __reduce_ex__ (
protocol_version )``_ * control over how an object is created during
unpickling `x = pickle.load( file )` ` `x. __getnewargs__ ()``_ * to
restore an objects state after unpickling `x = pickle.load( file )` `
`x. __setstate__ ()``_
* To recreate a serialized object, Python needs to create a new object
that looks like the serialized object, then set the values of all the
attributes on the new object. The `__getnewargs__()` method controls
how the object is created, then the `__setstate__()` method controls
how the attribute values are restored.


Classes That Can Be Used in a `with` Block
------------------------------------------

A `with` block defines a `runtime context`_; you enter the context
when you execute the `with` statement, and you exit the context after
you execute the last statement in the block. Notes You Want So You
Write And Python Calls do something special when entering a `with`
block `with x:` ` `x. __enter__ ()``_ do something special when
leaving a `with` block `with x:` ` `x. __exit__ ( exc_type , exc_value
, traceback )``_
This is how the ` `with file ` idiom`_ works.

::

     `# excerpt from io.py:
    def _checkClosed(self, msg=None):
        '''Internal: raise an ValueError if file is closed
        '''
        if self.closed:
            raise ValueError('I/O operation on closed file.'
                             if msg is None else msg)
    
    def __enter__(self):
        '''Context management protocol.  Returns self.'''
        self._checkClosed()                                ①
        return self                                        ②
    
    def __exit__(self, *args):
        '''Context management protocol.  Calls close()'''
        self.close()                                       ③`



#. The file object defines both an `__enter__()` and an `__exit__()`
method. The `__enter__()` method checks that the file is open; if its
not, the `_checkClosed()` method raises an exception.
#. The `__enter__()` method should almost always return self this is
the object that the `with` block will use to dispatch properties and
methods.
#. After the `with` block, the file object automatically closes. How?
   In the `__exit__()` method, it calls `self.close()`.


☞The `__exit__()` method will always be called, even if an
exception is raised inside the `with` block. In fact, if an exception
is raised, the exception information will be passed to the
`__exit__()` method. See `With Statement Context Managers`_ for more
details.
For more on context managers, see `Closing Files Automatically`_ and
`Redirecting Standard Output`_.


Really Esoteric Stuff
---------------------

If you know what youre doing, you can gain almost complete control
over how classes are compared, how attributes are defined, and what
kinds of classes are considered subclasses of your class. Notes You
Want So You Write And Python Calls a class constructor `x = MyClass()`
` `x. __new__ ()``_ * a class destructor `del x` ` `x. __del__ ()``_
only a specific set of attributes to be defined ` `x. __slots__ ()``_
a custom hash value `hash(x)` ` `x. __hash__ ()``_ to get a propertys
value `x.color` ` `type(x). __dict__ ['color'].__get__(x, type(x))``_
to set a propertys value `x.color = 'PapayaWhip'` ` `type(x). __dict__
['color'].__set__(x, 'PapayaWhip')``_ to delete a property `del
x.color` ` `type(x). __dict__ ['color'].__del__(x)``_ to control
whether an object is an instance of your class `isinstance(x,
MyClass)` ` `MyClass. __instancecheck__ (x)``_ to control whether a
class is a subclass of your class `issubclass(C, MyClass)` ` `MyClass.
__subclasscheck__ (C)``_ to control whether a class is a subclass of
your abstract base class `issubclass(C, MyABC)` ` `MyABC.
__subclasshook__ (C)``_
* Exactly when Python calls the `__del__()` special method `is
incredibly complicated`_. To fully understand it, you need to know how
`Python keeps track of objects in memory`_. Heres a good article on
`Python garbage collection and class destructors`_. You should also
read about `weak references`_, the ` `weakref` module`_, and probably
the ` `gc` module`_ for good measure.


Further Reading
---------------

Modules mentioned in this appendix:

+ ` `zipfile` module`_
+ ` `cgi` module`_
+ ` `collections` module`_
+ ` `math` module`_
+ ` `pickle` module`_
+ ` `copy` module`_
+ ` `abc` (Abstract Base Classes) module`_


Other light reading:

+ `Format Specification Mini-Language`_
+ `Python data model`_
+ `Built-in types`_
+ ` PEP 357: Allowing Any Object to be Used for Slicing`_
+ ` PEP 3119: Introducing Abstract Base Classes`_


`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _serializing and unserializing arbitrary objects: serializing.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__delattr__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__lt__
.. _['color'].__del__(x): http://www.python.org/doc/3.1/reference/datamodel.html#object.__delete__
.. _(): http://docs.python.org/3.1/library/math.html#math.trunc
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__iadd__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__delitem__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__imul__
.. _Python garbage collection and class destructors: http://www.electricmonk.nl/log/2008/07/07/python-destructor-and-garbage-collection-notes/
.. _Mark Pilgrim: about.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__gt__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ifloordiv__
.. _is incredibly complicated: http://www.python.org/doc/3.1/reference/datamodel.html#object.__del__
.. _runtime context: http://www.python.org/doc/3.1/library/stdtypes.html#typecontextmanager
.. _Python keeps track of objects in memory: http://www.python.org/doc/3.1/reference/datamodel.html#objects-values-and-types
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__iand__
.. _ module: http://docs.python.org/3.1/library/weakref.html
.. _(x): http://docs.python.org/3.1/reference/datamodel.html#object.__str__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rrshift__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__eq__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__pow__
.. _['color'].__get__(x, type(x)): http://www.python.org/doc/3.1/reference/datamodel.html#object.__get__
.. _the Iterators chapter: iterators.html#a-fibonacci-iterator
.. _weak references: http://mindtrove.info/articles/python-weak-references/
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__next__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__hash__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__getattribute__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__exit__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__xor__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__itruediv__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__invert__
.. _introduction to classes: iterators.html#divingin
.. _ module: http://docs.python.org/3.1/library/copy.html
.. _(): http://docs.python.org/3.1/library/math.html#math.ceil
.. _the Iterators chapter: iterators.html
.. _(): http://docs.python.org/3.1/library/pickle.html#pickle-state
.. _ 357: Allowing Any Object to be Used for Slicing: http://www.python.org/dev/peps/pep-0357/
.. _ module: http://docs.python.org/3.1/library/pickle.html
.. _(): http://docs.python.org/3.1/reference/datamodel.html#object.__repr__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__float__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rpow__
.. _x261C;: porting-code-to-python-3-with-2to3.html
.. _Redirecting Standard Output: files.html#redirect
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__add__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__getitem__
.. _['color'].__set__(x, 'PapayaWhip'): http://www.python.org/doc/3.1/reference/datamodel.html#object.__set__
.. _ 3119: Introducing Abstract Base Classes: http://www.python.org/dev/peps/pep-3119/
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rand__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__slots__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__truediv__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__bool__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__abs__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__new__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__floordiv__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__setitem__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__neg__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ne__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__le__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ipow__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__divmod__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rshift__
.. _(): http://docs.python.org/3.1/library/math.html#math.floor
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__int__
.. _With Statement Context Managers: http://www.python.org/doc/3.1/reference/datamodel.html#with-statement-context-managers
.. _Built-in types: http://www.python.org/doc/3.1/library/stdtypes.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__mul__
.. _x261E;: where-to-go-from-here.html
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__call__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ior__
.. _(): http://docs.python.org/3.1/reference/datamodel.html#object.__init__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__setattr__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__contains__
.. _George Bernard Shaw: http://en.wikiquote.org/wiki/George_Bernard_Shaw
.. _(n): http://www.python.org/doc/3.1/reference/datamodel.html#object.__round__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ilshift__
.. _ module: http://www.python.org/doc/3.1/library/gc.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rdivmod__
.. _ module: http://docs.python.org/3.1/library/zipfile.html
.. _) module: http://docs.python.org/3.1/library/abc.html
.. _generator expression: advanced-iterators.html#generator-expressions
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__isub__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rsub__
.. _Dive Into Python 3: table-of-contents.html#special-method-names
.. _(C): http://www.python.org/dev/peps/pep-3119/#overloading-isinstance-and-issubclass
.. _Home: index.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rfloordiv__
.. _()]: http://www.python.org/doc/3.1/reference/datamodel.html#object.__index__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__dir__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__enter__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rmul__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ror__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__mod__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ge__
.. _Format Specification Mini-Language: http://www.python.org/doc/3.1/library/string.html#formatspec
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rmod__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rxor__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__len__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__pos__
.. _ module: http://www.python.org/doc/3.1/library/collections.html
.. _Python data model: http://www.python.org/doc/3.1/reference/datamodel.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__ixor__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__getattr__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rtruediv__
.. _ module: http://docs.python.org/3.1/library/math.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__or__
.. _): http://docs.python.org/3.1/library/collections.html#collections.defaultdict.__missing__
.. _): http://docs.python.org/3.1/reference/datamodel.html#object.__format__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__lshift__
.. _ module: http://docs.python.org/3.1/library/cgi.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__imod__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__sub__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__rlshift__
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__and__
.. _(C): http://docs.python.org/3.1/library/abc.html#abc.ABCMeta.__subclasshook__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__complex__
.. _native datatypes: native-datatypes.html
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__radd__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__iter__
.. _(): http://www.python.org/doc/3.1/reference/datamodel.html#object.__reversed__
.. _Closing Files Automatically: files.html#with
.. _): http://www.python.org/doc/3.1/reference/datamodel.html#object.__irshift__
.. _(): http://docs.python.org/3.1/library/pickle.html#pickling-class-instances


