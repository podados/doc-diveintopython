
You are here: `Home`_ `Dive Into Python 3`_
Difficulty level: ♦♢♢♢♢


Installing Python
=================

❝ Tempora mutantur nos et mutamur in illis. (Times change, and
we change with them.) ❞
ancient Roman proverb


Diving In
---------

Before you can start programming in Python 3, you need to install it.
Or do you?


Which Python Is Right For You?
------------------------------

If you're using an account on a hosted server, your ISP may have
already installed Python 3. If youre running Linux at home, you may
already have Python 3, too. Most popular GNU/Linux distributions come
with Python 2 in the default installation; a small but growing number
of distributions also include Python 3. Mac OS X includes a command-
line version of Python 2, but as of this writing it does not include
Python 3. Microsoft Windows does not come with any version of Python.
But dont despair! You can point-and-click your way through installing
Python, regardless of what operating system you have.
The easiest way to check for Python 3 on your Linux or Mac OS X system
is `from the command line`_. Once youre at a command line prompt, just
type python3 (all lowercase, no spaces), press ENTER , and see what
happens. On my home Linux system, Python 3.1 is already installed, and
this command gets me into the Python interactive shell .

::

    
    mark@atlantis:~$ python3
    Python 3.1 (r31:73572, Jul 28 2009, 06:52:23) 
    [GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


(Type exit() and press ENTER to exit the Python interactive shell.)
My `web hosting provider`_ also runs Linux and provides command-line
access, but my server does not have Python 3 installed. (Boo!)

::

    
    mark@manganese:~$ python3
    bash: python3: command not found


So back to the question that started this section, Which Python is
right for you? Whichever one runs on the computer you already have.
[Read on for Windows instructions, or skip to Installing on Mac OS X,
Installing on Ubuntu Linux, or Installing on Other Platforms.]
⁂


Installing on Microsoft Windows
-------------------------------

Windows comes in two architectures these days: 32-bit and 64-bit. Of
course, there are lots of different versions of WindowsXP, Vista,
Windows 7but Python runs on all of them. The more important
distinction is 32-bit v. 64-bit. If you have no idea what architecture
youre running, its probably 32-bit.
Visit ` `python.org/download/``_ and download the appropriate Python 3
Windows installer for your architecture. Your choices will look
something like this:

+ **Python 3.1 Windows installer** (Windows binarydoes not include
source)
+ **Python 3.1 Windows AMD64 installer** (Windows AMD64 binarydoes not
  include source)


I dont want to include direct download links here, because minor
updates of Python happen all the time and I dont want to be
responsible for you missing important updates. You should always
install the most recent version of Python 3.x unless you have some
esoteric reason not to.

#. Once your download is complete, double-click the `.msi` file.
Windows will pop up a security alert, since youre about to be running
executable code. The official Python installer is digitally signed by
the `Python Software Foundation`_, the non-profit corporation that
oversees Python development. Dont accept imitations!Click the `Run`
button to launch the Python 3 installer.
#. The first question the installer will ask you is whether you want
to install Python 3 for all users or just for you. The default choice
is install for all users, which is the best choice unless you have a
good reason to choose otherwise. (One possible reason why you would
want to install just for me is that you are installing Python on your
companys computer and you dont have administrative rights on your
Windows account. But then, why are you installing Python without
permission from your companys Windows administrator? Dont get me in
trouble here!)Click the `Next` button to accept your choice of
installation type.
#. Next, the installer will prompt you to choose a destination
directory. The default for all versions of Python 3.1.x is
`C:\Python31\`, which should work well for most users unless you have
a specific reason to change it. If you maintain a separate drive
letter for installing applications, you can browse to it using the
embedded controls, or simply type the pathname in the box below. You
are not limited to installing Python on the `C:` drive; you can
install it on any drive, in any folder.Click the `Next` button to
accept your choice of destination directory.
#. The next page looks complicated, but its not really. Like many
   installers, you have the option not to install every single component
   of Python 3. If disk space is especially tight, you can exclude
   certain components.

    + **Register Extensions** allows you to double-click Python scripts (
    `.py` files) and run them. Recommended but not required. (This option
    doesnt require any disk space, so there is little point in excluding
    it.)
    + **Tcl/Tk** is the graphics library used by the Python Shell, which
    you will use throughout this book. I strongly recommend keeping this
    option.
    + **Documentation** installs a help file that contains much of the
    information on ` `docs.python.org``_. Recommended if you are on dialup
    or have limited Internet access.
    + **Utility Scripts** includes the `2to3.py` script which youll learn
    about `later in this book`_. Required if you want to learn about
    migrating existing Python 2 code to Python 3. If you have no existing
    Python 2 code, you can skip this option.
    + **Test Suite** is a collection of scripts used to test the Python
      interpreter itself. We will not use it in this book, nor have I ever
      used it in the course of programming in Python. Completely optional.

#. If youre unsure how much disk space you have, click the `Disk
Usage` button. The installer will list your drive letters, compute how
much space is available on each drive, and calculate how much would be
left after installation.Click the `OK` button to return to the
Customizing Python page.
#. If you decide to exclude an option, select the drop-down button
before the option and select Entire feature will be unavailable. For
example, excluding the test suite will save you a whopping 7908 KB of
disk space.Click the `Next` button to accept your choice of options.
#. The installer will copy all the necessary files to your chosen
destination directory. (This happens so quickly, I had to try it three
times to even get a screenshot of it!)
#. Click the `Finish` button to exit the installer.
#. In your `Start` menu, there should be a new item called `Python
   3.1`. Within that, there is a program called IDLE . Select this item
   to run the interactive Python Shell.


[Skip to using the Python Shell]
⁂


Installing on Mac OS X
----------------------

All modern Macintosh computers use the Intel chip (like most Windows
PCs). Older Macs used PowerPC chips. You dont need to understand the
difference, because theres just one Mac Python installer for all Macs.
Visit ` `python.org/download/``_ and download the Mac installer. It
will be called something like **Python 3.1 Mac Installer Disk Image**,
although the version number may vary. Be sure to download version 3.x,
not 2.x.

#. Your browser should automatically mount the disk image and open a
Finder window to show you the contents. (If this doesnt happen, youll
need to find the disk image in your downloads folder and double-click
to mount it. It will be named something like `python-3.1.dmg`.) The
disk image contains a number of text files ( `Build.txt`,
`License.txt`, `ReadMe.txt`), and the actual installer package,
`Python.mpkg`.Double-click the `Python.mpkg` installer package to
launch the Mac Python installer.
#. The first page of the installer gives a brief description of Python
itself, then refers you to the `ReadMe.txt` file (which you didnt
read, did you?) for more details.Click the `Continue` button to move
along.
#. The next page actually contains some important information: Python
requires Mac OS X 10.3 or later. If you are still running Mac OS X
10.2, you should really upgrade. Apple no longer provides security
updates for your operating system, and your computer is probably at
risk if you ever go online. Also, you cant run Python 3.Click the
`Continue` button to advance.
#. Like all good installers, the Python installer displays the
software license agreement. Python is open source, and its license is
`approved by the Open Source Initiative`_. Python has had a number of
owners and sponsors throughout its history, each of which has left its
mark on the software license. But the end result is this: Python is
open source, and you may use it on any platform, for any purpose,
without fee or obligation of reciprocity.Click the `Continue` button
once again.
#. Due to quirks in the standard Apple installer framework, you must
agree to the software license in order to complete the installation.
Since Python is open source, you are really agreeing that the license
is granting you additional rights, rather than taking them away.Click
the `Agree` button to continue.
#. The next screen allows you to change your install location. You
must install Python on your boot drive, but due to limitations of the
installer, it does not enforce this. In truth, I have never had the
need to change the install location.From this screen, you can also
customize the installation to exclude certain features. If you want to
do this, click the `Customize` button; otherwise click the `Install`
button.
#. If you choose a Custom Install, the installer will present you with
   the following list of features:

    + **Python Framework**. This is the guts of Python, and is both
    selected and disabled because it must be installed.
    + **GUI Applications** includes IDLE, the graphical Python Shell which
    you will use throughout this book. I strongly recommend keeping this
    option selected.
    + **UNIX command-line tools** includes the command-line `python3`
    application. I strongly recommend keeping this option, too.
    + **Python Documentation** contains much of the information on `
    `docs.python.org``_. Recommended if you are on dialup or have limited
    Internet access.
    + **Shell profile updater** controls whether to update your shell
    profile (used in `Terminal.app`) to ensure that this version of Python
    is on the search path of your shell. You probably dont need to change
    this.
    + **Fix system Python** should not be changed. (It tells your Mac to
      use Python 3 as the default Python for all scripts, including built-in
      system scripts from Apple. This would be very bad, since most of those
      scripts are written for Python 2, and they would fail to run properly
      under Python 3.)
Click the `Install` button to continue.
#. Because it installs system-wide frameworks and binaries in
`/usr/local/bin/`, the installer will ask you for an administrative
password. There is no way to install Mac Python without administrator
privileges.Click the `OK` button to begin the installation.
#. The installer will display a progress meter while it installs the
features youve selected.
#. Assuming all went well, the installer will give you a big green
checkmark to tell you that the installation completed
successfully.Click the `Close` button to exit the installer.
#. Assuming you didnt change the install location, you can find the
newly installed files in the `Python 3.1` folder within your
`/Applications` folder. The most important piece is IDLE , the
graphical Python Shell.Double-click IDLE to launch the Python Shell.
#. The Python Shell is where you will spend most of your time
   exploring Python. Examples throughout this book will assume that you
   can find your way into the Python Shell.


[Skip to using the Python Shell]
⁂


Installing on Ubuntu Linux
--------------------------

Modern Linux distributions are backed by vast repositories of
precompiled applications, ready to install. The exact details vary by
distribution. In Ubuntu Linux, the easiest way to install Python 3 is
through the `Add/Remove` application in your `Applications` menu.

#. When you first launch the `Add/Remove` application, it will show
you a list of preselected applications in different categories. Some
are already installed; most are not. Because the repository contains
over 10,000 applications, there are different filters you can apply to
see small parts of the repository. The default filter is Canonical-
maintained applications, which is a small subset of the total number
of applications that are officially supported by Canonical, the
company that creates and maintains Ubuntu Linux.
#. Python 3 is not maintained by Canonical, so the first step is to
drop down this filter menu and select All Open Source applications.
#. Once youve widened the filter to include all open source
applications, use the Search box immediately after the filter menu to
search for Python 3 .
#. Now the list of applications narrows to just those matching Python
3 . Youre going to check two packages. The first is `Python (v3.0)`.
This contains the Python interpreter itself.
#. The second package you want is immediately above: `IDLE (using
Python-3.0)`. This is a graphical Python Shell that you will use
throughout this book.After youve checked those two packages, click the
`Apply Changes` button to continue.
#. The package manager will ask you to confirm that you want to add
both `IDLE (using Python-3.0)` and `Python (v3.0)`.Click the `Apply`
button to continue.
#. The package manager will show you a progress meter while it
downloads the necessary packages from Canonicals Internet repository.
#. Once the packages are downloaded, the package manager will
automatically begin installing them.
#. If all went well, the package manager will confirm that both
packages were successfully installed. From here, you can double-click
IDLE to launch the Python Shell, or click the `Close` button to exit
the package manager.You can always relaunch the Python Shell by going
to your `Applications` menu, then the `Programming` submenu, and
selecting IDLE .
#. The Python Shell is where you will spend most of your time
   exploring Python. Examples throughout this book will assume that you
   can find your way into the Python Shell.


[Skip to using the Python Shell]
⁂


Installing on Other Platforms
-----------------------------

Python 3 is available on a number of different platforms. In
particular, it is available in virtually every Linux, BSD , and
Solaris-based distribution. For example, RedHat Linux uses the `yum`
package manager. FreeBSD has its `ports and packages collection`_,
SUSE has `zypper`, and Solaris has `pkgadd`. A quick web search for
`Python 3` + your operating system should tell you whether a Python 3
package is available, and if so, how to install it.
⁂


Using The Python Shell
----------------------

The Python Shell is where you can explore Python syntax, get
interactive help on commands, and debug short programs. The graphical
Python Shell (named IDLE ) also contains a decent text editor that
supports Python syntax coloring and integrates with the Python Shell.
If you dont already have a favorite text editor, you should give IDLE
a try.
First things first. The Python Shell itself is an amazing interactive
playground. Throughout this book, youll see examples like this:

::

    
    >>> 1 + 1
    2


The three angle brackets, >>> , denote the Python Shell prompt. Dont
type that part. Thats just to let you know that this example is meant
to be followed in the Python Shell.
1 + 1 is the part you type. You can type any valid Python expression
or command in the Python Shell. Dont be shy; it wont bite! The worst
that will happen is youll get an error message. Commands get executed
immediately (once you press ENTER ); expressions get evaluated
immediately, and the Python Shell prints out the result.
2 is the result of evaluating this expression. As it happens, 1 + 1 is
a valid Python expression. The result, of course, is 2 .
Lets try another one.

::

    
    >>> print('Hello world!')
    Hello world!


Pretty simple, no? But theres lots more you can do in the Python
shell. If you ever get stuckyou cant remember a command, or you cant
remember the proper arguments to pass a certain functionyou can get
interactive help in the Python Shell. Just type help and press ENTER .

::

    
    >>> help
    Type help() for interactive help, or help(object) for help about object.


There are two modes of help. You can get help about a single object,
which just prints out the documentation and returns you to the Python
Shell prompt. You can also enter help mode , where instead of
evaluating Python expressions, you just type keywords or command names
and it will print out whatever it knows about that command.
To enter the interactive help mode, type help() and press ENTER .

::

    
    >>> help()
    Welcome to Python 3.0!  This is the online help utility.
    
    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/tutorial/.
    
    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".
    
    To get a list of available modules, keywords, or topics, type "modules",
    "keywords", or "topics".  Each module also comes with a one-line summary
    of what it does; to list the modules whose summaries contain a given word
    such as "spam", type "modules spam".
    
    help> 


Note how the prompt changes from >>> to help> . This reminds you that
youre in the interactive help mode. Now you can enter any keyword,
command, module name, function namepretty much anything Python
understandsand read documentation on it.

::

    
    help> print                                                                 ①
    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file: a file-like object (stream); defaults to the current sys.stdout.
        sep:  string inserted between values, default a space.
        end:  string appended after the last value, default a newline.
    
    help> PapayaWhip                                                            ②
    no Python documentation found for 'PapayaWhip'
    
    help> quit                                                                  ③
    
    You are now leaving help and returning to the Python interpreter.
    If you want to ask for help on a particular object directly from the
    interpreter, you can type "help(object)".  Executing "help('string')"
    has the same effect as typing a particular string at the help> prompt.
    >>>                                                                         ④



#. To get documentation on the `print()` function, just type print and
press ENTER . The interactive help mode will display something akin to
a man page: the function name, a brief synopsis, the functions
arguments and their default values, and so on. If the documentation
seems opaque to you, dont panic. Youll learn more about all these
concepts in the next few chapters.
#. Of course, the interactive help mode doesnt know everything. If you
type something that isnt a Python command, module, function, or other
built-in keyword, the interactive help mode will just shrug its
virtual shoulders.
#. To quit the interactive help mode, type quit and press ENTER .
#. The prompt changes back to >>> to signal that youve left the
   interactive help mode and returned to the Python Shell.


IDLE , the graphical Python Shell, also includes a Python-aware text
editor.
⁂


Python Editors and IDEs
-----------------------

IDLE is not the only game in town when it comes to writing programs in
Python. While its useful to get started with learning the language
itself, many developers prefer other text editors or Integrated
Development Environments ( IDE s). I wont cover them here, but the
Python community maintains `a list of Python-aware editors`_ that
covers a wide range of supported platforms and software licenses.
You might also want to check out the `list of Python-aware IDE s`_,
although few of them support Python 3 yet. One that does is `PyDev`_,
a plugin for `Eclipse`_ that turns Eclipse into a full-fledged Python
IDE . Both Eclipse and PyDev are cross-platform and open source.
On the commercial front, there is ActiveStates `Komodo IDE `_. It has
per-user licensing, but students can get a discount, and a free time-
limited trial version is available.
Ive been programming in Python for nine years, and I edit my Python
programs in `GNU Emacs`_ and debug them in the command-line Python
Shell. Theres no right or wrong way to develop in Python. Find a way
that works for you!
`☜`_ `☞`_
200111 `Mark Pilgrim`_

.. _from the command line: troubleshooting.html#getting-to-the-command-line
.. _Python Software Foundation: http://www.python.org/psf/
.. _Home: index.html
.. _Dive Into Python 3: table-of-contents.html#installing-python
.. _ports and packages collection: http://www.freebsd.org/ports/
.. _docs.python.org: http://docs.python.org/
.. _s: http://wiki.python.org/moin/IntegratedDevelopmentEnvironments
.. _x261E;: your-first-python-program.html
.. _IDE: http://www.activestate.com/komodo/
.. _GNU Emacs: http://www.gnu.org/software/emacs/
.. _PyDev: http://pydev.sourceforge.net/
.. _Eclipse: http://eclipse.org/
.. _approved by the Open Source Initiative: http://opensource.org/licenses/
.. _a list of Python-aware editors: http://wiki.python.org/moin/PythonEditors
.. _web hosting provider: http://cornerhost.com/
.. _Mark Pilgrim: about.html
.. _python.org/download/: http://python.org/download/
.. _x261C;: whats-new.html
.. _later in this book: case-study-porting-chardet-to-python-3.html


