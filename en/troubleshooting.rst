
You are here: `Home`_ `Dive Into Python 3`_


Troubleshooting
===============

❝ Wheres the ANY key? ❞
`variously attributed`_



Diving In
---------

FIXME


Getting to the Command Line
---------------------------

Throughout this book, there are examples of executing Python programs
from the command line. Where is the command line?
On Linux, look in your ** `Applications`** menu for a program called
** `Terminal`**. (It may be in a submenu like ** `Accessories`** or **
`System`**.)
On Mac OS X, there is an application called ** `Terminal`** in your
`/Applications/Utilities/` folder. To get there, click on your
desktop, open the ** `Go`** menu, select ** `Go to folder...`**, and
type /Applications/Utilities/ . Then double-click the ** `Terminal`**
program.
On Windows, click ** `Start`**, select ** `Run...`**, type cmd , and
press ENTER .


Running Python on the command line
----------------------------------

Once you get to the command line, you should be able to run the Python
interactive shell. On the Linux or Mac OS X command line, type python3
and press ENTER . On the Windows command line, type c:\python31\python
and press ENTER . If all goes well, you should see something like
this:

::

    
    you@localhost:~$ python3
    Python 3.1 (r31:73572, Jul 28 2009, 06:52:23) 
    [GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


(Type exit() and press ENTER to exit the Python interactive shell and
go back to the command line. This works on all platforms.)
If you get a command not found error, it probably means you `dont have
Python 3 installed`_.

::

    
    you@localhost:~$ python3
    bash: python3: command not found


On the other hand, if you get into a Python interactive shell but the
version number is not what you expected, you may have more than one
version of Python installed. This happens most often on Linux and Mac
OS X systems, where an older version of Python is pre-installed. You
can install the latest version without deleting the older version
(they will live side-by-side in peace), but you will need to be more
specific when you run Python from the command line.
For example, on my home Linux box, I have several versions of Python
installed so I can test the Python software that I write. To run a
specific version, I can type `python3.0`, `python3.1`, or `python2.6`.

::

    
    mark@atlantis:~$ python3.0
    Python 3.0.1+ (r301:69556, Apr 15 2009, 17:25:52)
    [GCC 4.3.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()
    mark@atlantis:~$ python3.1
    Python 3.1 (r31:73572, Jul 28 2009, 06:52:23) 
    [GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()
    mark@atlantis:~$ python2.6
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()


`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _Home: index.html
.. _variously attributed: http://www.wherestheanykey.co.uk
.. _x261C;: where-to-go-from-here.html
.. _x261E;: blank.html
.. _Mark Pilgrim: about.html
.. _Dive Into Python 3: table-of-contents.html#troubleshooting
.. _t have Python 3 installed: installing-python.html


