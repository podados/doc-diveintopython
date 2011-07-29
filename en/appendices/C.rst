Appendix C. Tips and tricks
============================

Chapter 1. Installing Python
   
Chapter 2. Your First Python Program
   
  * 2.1. Diving in
        Tip: Running Programs on Windows
        In the ActivePython IDE on Windows, you can run the Python program
        you're editing by choosing File->Run... (Ctrl-R). Output is displayed
        in the interactive window.
        Tip: Running Programs on Mac OS
        In the Python IDE on Mac OS, you can run a Python program with Python->
        Run window... (Cmd-R), but there is an important option you must set
        first. Open the .py file in the IDE, pop up the options menu by
        clicking the black triangle in the upper-right corner of the window,
        and make sure the Run as __main__ option is checked. This is a per-file
        setting, but you'll only need to do it once per file.
        Tip: Running Programs in UNIX
        On UNIX-compatible systems (including Mac OS X), you can run a Python
        program from the command line: python odbchelper.py
   
   
  * 2.2. Declaring Functions
        Note: Python vs. Visual Basic: Return Values
        In Visual Basic, functions (that return a value) start with function,
        and subroutines (that do not return a value) start with sub. There are
        no subroutines in Python. Everything is a function, all functions
        return a value (even if it's None), and all functions start with def.
        Note: Python vs. Java: Return Values
        In Java, C++, and other statically-typed languages, you must specify
        the datatype of the function return value and each function argument.
        In Python, you never explicitly specify the datatype of anything. Based
        on what value you assign, Python keeps track of the datatype
        internally.
   
   
  * 2.3. Documenting Functions
        Note: Python vs. Perl: Quoting
        Triple quotes are also an easy way to define a string with both single
        and double quotes, like qq/.../ in Perl.
        Note: Why doc strings are a Good Thing
        Many Python IDEs use the doc string to provide context-sensitive
        documentation, so that when you type a function name, its doc string
        appears as a tooltip. This can be incredibly helpful, but it's only as
        good as the doc strings you write.
   
   
  * 2.4. Everything Is an Object
        Note: Python vs. Perl: import
        import in Python is like require in Perl. Once you import a Python
        module, you access its functions with module.function; once you require
        a Perl module, you access its functions with module::function.
   
   
  * 2.5. Indenting Code
        Note: Python vs. Java: Separating Statements
        Python uses carriage returns to separate statements and a colon and
        indentation to separate code blocks. C++ and Java use semicolons to
        separate statements and curly braces to separate code blocks.
   
   
  * 2.6. Testing Modules
        Note: Python vs. C: Comparison and Assignment
        Like C, Python uses == for comparison and = for assignment. Unlike C,
        Python does not support in-line assignment, so there's no chance of
        accidentally assigning the value you thought you were comparing.
        Tip: if __name__ on Mac OS
        On MacPython, there is an additional step to make the if __name__ trick
        work. Pop up the module's options menu by clicking the black triangle
        in the upper-right corner of the window, and make sure Run as __main__
        is checked.
   
   

Chapter 3. Native Datatypes
   
  * 3.1. Introducing Dictionaries
        Note: Python vs. Perl: Dictionaries
        A dictionary in Python is like a hash in Perl. In Perl, variables that
        store hashes always start with a % character. In Python, variables can
        be named anything, and Python keeps track of the datatype internally.
        Note: Python vs. Java: Dictionaries
        A dictionary in Python is like an instance of the Hashtable class in
        Java.
        Note: Python vs. Visual Basic: Dictionaries
        A dictionary in Python is like an instance of the Scripting.Dictionary
        object in Visual Basic.
   
   
  * 3.1.2. Modifying Dictionaries
        Note: Dictionaries are unordered
        Dictionaries have no concept of order among elements. It is incorrect
        to say that the elements are "out of order"; they are simply unordered.
        This is an important distinction that will annoy you when you want to
        access the elements of a dictionary in a specific, repeatable order
        (like alphabetical order by key). There are ways of doing this, but
        they're not built into the dictionary.
   
   
  * 3.2. Introducing Lists
        Note: Python vs. Perl: lists
        A list in Python is like an array in Perl. In Perl, variables that
        store arrays always start with the @ character; in Python, variables
        can be named anything, and Python keeps track of the datatype
        internally.
        Note: Python vs. Java: lists
        A list in Python is much more than an array in Java (although it can be
        used as one if that's really all you want out of life). A better
        analogy would be to the ArrayList class, which can hold arbitrary
        objects and can expand dynamically as new items are added.
   
   
  * 3.2.3. Searching Lists
        Note: What's True in Python?
        Before version 2.2.1, Python had no separate boolean datatype. To
        compensate for this, Python accepted almost anything in a boolean
        context (like an if statement), according to the following rules:


::

              o 0 is false; all other numbers are true.
              o An empty string ("") is false, all other strings are true.
              o An empty list ([]) is false; all other lists are true.
              o An empty tuple (()) is false; all other tuples are true.
              o An empty dictionary ({}) is false; all other dictionaries are
                true.
        These rules still apply in Python 2.2.1 and beyond, but now you can


        also use an actual boolean, which has a value of True or False. Note
        the capitalization; these values, like everything else in Python, are
        case-sensitive.
   
   
  * 3.3. Introducing Tuples
        Note: Tuples into lists into tuples
        Tuples can be converted into lists, and vice-versa. The built-in tuple
        function takes a list and returns a tuple with the same elements, and
        the list function takes a tuple and returns a list. In effect, tuple
        freezes a list, and list thaws a tuple.
   
   
  * 3.4. Declaring variables
        Note: Writing Multiline Commands
        When a command is split among several lines with the line-continuation
        marker ("\"), the continued lines can be indented in any manner; Python
        's normally stringent indentation rules do not apply. If your Python
        IDE auto-indents the continued line, you should probably accept its
        default unless you have a burning reason not to.
   
   
  * 3.5. Formatting Strings
        Note: Python vs. C: String Formatting
        String formatting in Python uses the same syntax as the sprintf
        function in C.
   
   
  * 3.7. Joining Lists and Splitting Strings
        Caution: You Can't join Non-Strings
        join works only on lists of strings; it does not do any type coercion.
        Joining a list that has one or more non-string elements will raise an
        exception.
        Tip: Searching with split
        anystring.split(delimiter, 1) is a useful technique when you want to
        search a string for a substring and then work with everything before
        the substring (which ends up in the first element of the returned list)
        and everything after it (which ends up in the second element).
   
   

Chapter 4. The Power Of Introspection
   
  * 4.2. Using Optional and Named Arguments
        Note: Calling Functions is Flexible
        The only thing you need to do to call a function is specify a value
        (somehow) for each required argument; the manner and order in which you
        do that is up to you.
   
   
  * 4.3.3. Built-In Functions
        Note: Python is self-documenting
        Python comes with excellent reference manuals, which you should peruse
        thoroughly to learn all the modules Python has to offer. But unlike
        most languages, where you would find yourself referring back to the
        manuals or man pages to remind yourself how to use these modules,
        Python is largely self-documenting.
   
   
  * 4.7. Using lambda Functions
        Note: lambda is Optional
        lambda functions are a matter of style. Using them is never required;
        anywhere you could use them, you could define a separate normal
        function and use that instead. I use them in places where I want to
        encapsulate specific, non-reusable code without littering my code with
        a lot of little one-line functions.
   
   
  * 4.8. Putting It All Together
        Note: Python vs. SQL: null value comparisons
        In SQL, you must use IS NULL instead of = NULL to compare a null value.
        In Python, you can use either == None or is None, but is None is
        faster.
   
   

Chapter 5. Objects and Object-Orientation
   
  * 5.2. Importing Modules Using from module import
        Note: Python vs. Perl: from module import
        from module import * in Python is like use module in Perl; import
        module in Python is like require module in Perl.
        Note: Python vs. Java: from module import
        from module import * in Python is like import module.* in Java; import
        module in Python is like import module in Java.
        Caution:
        Use from module import * sparingly, because it makes it difficult to
        determine where a particular function or attribute came from, and that
        makes debugging and refactoring more difficult.
   
   
  * 5.3. Defining Classes
        Note: Python vs. Java: pass
        The pass statement in Python is like an empty set of braces ({}) in
        Java or C.
        Note: Python vs. Java: Ancestors
        In Python, the ancestor of a class is simply listed in parentheses
        immediately after the class name. There is no special keyword like
        extends in Java.
   
   
  * 5.3.1. Initializing and Coding Classes
        Note: Python vs. Java: self
        By convention, the first argument of any Python class method (the
        reference to the current instance) is called self. This argument fills
        the role of the reserved word this in C++ or Java, but self is not a
        reserved word in Python, merely a naming convention. Nonetheless,
        please don't call it anything but self; this is a very strong
        convention.
   
   
  * 5.3.2. Knowing When to Use self and __init__
        Note: __init__ Methods
        __init__ methods are optional, but when you define one, you must
        remember to explicitly call the ancestor's __init__ method (if it
        defines one). This is more generally true: whenever a descendant wants
        to extend the behavior of the ancestor, the descendant method must
        explicitly call the ancestor method at the proper time, with the proper
        arguments.
   
   
  * 5.4. Instantiating Classes
        Note: Python vs. Java: Instantiating Classes
        In Python, simply call a class as if it were a function to create a new
        instance of the class. There is no explicit new operator like C++ or
        Java.
   
   
  * 5.5. Exploring UserDict: A Wrapper Class
        Tip:
        In the ActivePython IDE on Windows, you can quickly open any module in
        your library path by selecting File->Locate... (Ctrl-L).
        Note: Python vs. Java: Function Overloading
        Java and Powerbuilder support function overloading by argument list,
        i.e. one class can have multiple methods with the same name but a
        different number of arguments, or arguments of different types. Other
        languages (most notably PL/SQL) even support function overloading by
        argument name; i.e. one class can have multiple methods with the same
        name and the same number of arguments of the same type but different
        argument names. Python supports neither of these; it has no form of
        function overloading whatsoever. Methods are defined solely by their
        name, and there can be only one method per class with a given name. So
        if a descendant class has an __init__ method, it always overrides the
        ancestor __init__ method, even if the descendant defines it with a
        different argument list. And the same rule applies to any other method.
        Note:
        Guido, the original author of Python, explains method overriding this
        way: "Derived classes may override methods of their base classes.
        Because methods have no special privileges when calling other methods
        of the same object, a method of a base class that calls another method
        defined in the same base class, may in fact end up calling a method of
        a derived class that overrides it. (For C++ programmers: all methods in
        Python are effectively virtual.)" If that doesn't make sense to you (it
        confuses the hell out of me), feel free to ignore it. I just thought
        I'd pass it along.
        Caution:
        Always assign an initial value to all of an instance's data attributes
        in the __init__ method. It will save you hours of debugging later,
        tracking down AttributeError exceptions because you're referencing
        uninitialized (and therefore non-existent) attributes.
        Note: Historical Note
        In versions of Python prior to 2.2, you could not directly subclass
        built-in datatypes like strings, lists, and dictionaries. To compensate
        for this, Python comes with wrapper classes that mimic the behavior of
        these built-in datatypes: UserString, UserList, and UserDict. Using a
        combination of normal and special methods, the UserDict class does an
        excellent imitation of a dictionary. In Python 2.2 and later, you can
        inherit classes directly from built-in datatypes like dict. An example
        of this is given in the examples that come with this book, in
        fileinfo_fromdict.py.
   
   
  * 5.6.1. Getting and Setting Items
        Note:
        When accessing data attributes within a class, you need to qualify the
        attribute name: self.attribute. When calling other methods within a
        class, you need to qualify the method name: self.method.
   
   
  * 5.7. Advanced Special Class Methods
        Note: Python vs. Java equality and identity
        In Java, you determine whether two string variables reference the same
        physical memory location by using str1 == str2. This is called object
        identity, and it is written in Python as str1 is str2. To compare
        string values in Java, you would use str1.equals(str2); in Python, you
        would use str1 == str2. Java programmers who have been taught to
        believe that the world is a better place because == in Java compares by
        identity instead of by value may have a difficult time adjusting to
        Python's lack of such "gotchas".
        Note:
        While other object-oriented languages only let you define the physical
        model of an object ("this object has a GetLength method"), Python's
        special class methods like __len__ allow you to define the logical
        model of an object ("this object has a length").
   
   
  * 5.8. Introducing Class Attributes
        Note: Python vs. Java attribute definitions
        In Java, both static variables (called class attributes in Python) and
        instance variables (called data attributes in Python) are defined
        immediately after the class definition (one with the static keyword,
        one without). In Python, only class attributes can be defined here;
        data attributes are defined in the __init__ method.
        Note:
        There are no constants in Python. Everything can be changed if you try
        hard enough. This fits with one of the core principles of Python: bad
        behavior should be discouraged but not banned. If you really want to
        change the value of None, you can do it, but don't come running to me
        when your code is impossible to debug.
   
   
  * 5.9. Private Functions
        Note: Method Naming Conventions
        In Python, all special methods (like __setitem__) and built-in
        attributes (like __doc__) follow a standard naming convention: they
        both start with and end with two underscores. Don't name your own
        methods and attributes this way, because it will only confuse you (and
        others) later.
   
   

Chapter 6. Exceptions and File Handling
   
  * 6.1. Handling Exceptions
        Note: Python vs. Java exception handling
        Python uses try...except to handle exceptions and raise to generate
        them. Java and C++ use try...catch to handle exceptions, and throw to
        generate them.
   
   
  * 6.5. Working with Directories
        Note:
        Whenever possible, you should use the functions in os and os.path for
        file, directory, and path manipulations. These modules are wrappers for
        platform-specific modules, so functions like os.path.split work on UNIX
        , Windows, Mac OS, and any other platform supported by Python.
   
   

Chapter 7. Regular Expressions
   
  * 7.4. Using the {n,m} Syntax
        Note:
        There is no way to programmatically determine that two regular
        expressions are equivalent. The best you can do is write a lot of test
        cases to make sure they behave the same way on all relevant inputs.
        You'll talk more about writing test cases later in this book.
   
   

Chapter 8. HTML Processing
   
  * 8.2. Introducing sgmllib.py
        Important: Language evolution: DOCTYPE
        Python 2.0 had a bug where SGMLParser would not recognize declarations
        at all (handle_decl would never be called), which meant that DOCTYPEs
        were silently ignored. This is fixed in Python 2.1.
        Tip: Specifying command line arguments in Windows
        In the ActivePython IDE on Windows, you can specify command line
        arguments in the "Run script" dialog. Separate multiple arguments with
        spaces.
   
   
  * 8.4. Introducing BaseHTMLProcessor.py
        Important: Processing HTML with embedded script
        The HTML specification requires that all non-HTML (like client-side
        JavaScript) must be enclosed in HTML comments, but not all web pages do
        this properly (and all modern web browsers are forgiving if they
        don't). BaseHTMLProcessor is not forgiving; if script is improperly
        embedded, it will be parsed as if it were HTML. For instance, if the
        script contains less-than and equals signs, SGMLParser may incorrectly
        think that it has found tags and attributes. SGMLParser always converts
        tags and attribute names to lowercase, which may break the script, and
        BaseHTMLProcessor always encloses attribute values in double quotes
        (even if the original HTML document used single quotes or no quotes),
        which will certainly break the script. Always protect your client-side
        script within HTML comments.
   
   
  * 8.5. locals and globals
        Important: Language evolution: nested scopes
        Python 2.2 introduced a subtle but important change that affects the
        namespace search order: nested scopes. In versions of Python prior to
        2.2, when you reference a variable within a nested function or lambda
        function, Python will search for that variable in the current (nested
        or lambda) function's namespace, then in the module's namespace. Python
        2.2 will search for the variable in the current (nested or lambda)
        function's namespace, then in the parent function's namespace, then in
        the module's namespace. Python 2.1 can work either way; by default, it
        works like Python 2.0, but you can add the following line of code at
        the top of your module to make your module work like Python 2.2:
        from __future__ import nested_scopes
        Note: Accessing variables dynamically
        Using the locals and globals functions, you can get the value of
        arbitrary variables dynamically, providing the variable name as a
        string. This mirrors the functionality of the getattr function, which
        allows you to access arbitrary functions dynamically by providing the
        function name as a string.
   
   
  * 8.6. Dictionary-based string formatting
        Important: Performance issues with locals
        Using dictionary-based string formatting with locals is a convenient
        way of making complex string formatting expressions more readable, but
        it comes with a price. There is a slight performance hit in making the
        call to locals, since locals builds a copy of the local namespace.
   
   

Chapter 9. XML Processing
   
  * 9.2. Packages
        Note: What makes a package
        A package is a directory with the special __init__.py file in it. The
        __init__.py file defines the attributes and methods of the package. It
        doesn't need to define anything; it can just be an empty file, but it
        has to exist. But if __init__.py doesn't exist, the directory is just a
        directory, not a package, and it can't be imported or contain modules
        or nested packages.
   
   
  * 9.6. Accessing element attributes
        Note: XML attributes and Python attributes
        This section may be a little confusing, because of some overlapping
        terminology. Elements in an XML document have attributes, and Python
        objects also have attributes. When you parse an XML document, you get a
        bunch of Python objects that represent all the pieces of the XML
        document, and some of these Python objects represent attributes of the
        XML elements. But the (Python) objects that represent the (XML)
        attributes also have (Python) attributes, which are used to access
        various parts of the (XML) attribute that the object represents. I told
        you it was confusing. I am open to suggestions on how to distinguish
        these more clearly.
        Note: Attributes have no order
        Like a dictionary, attributes of an XML element have no ordering.
        Attributes may happen to be listed in a certain order in the original
        XML document, and the Attr objects may happen to be listed in a certain
        order when the XML document is parsed into Python objects, but these
        orders are arbitrary and should carry no special meaning. You should
        always access individual attributes by name, like the keys of a
        dictionary.
   
   

Chapter 10. Scripts and Streams
   
Chapter 11. HTTP Web Services
   
  * 11.6. Handling Last-Modified and ETag
        Note: Support Last-Modified and ETag
        In these examples, the HTTP server has supported both Last-Modified and
        ETag headers, but not all servers do. As a web services client, you
        should be prepared to support both, but you must code defensively in
        case a server only supports one or the other, or neither.
   
   

Chapter 12. SOAP Web Services
   
Chapter 13. Unit Testing
   
  * 13.2. Diving in
        Note: Do you have unittest?
        unittest is included with Python 2.1 and later. Python 2.0 users can
        download it from pyunit.sourceforge.net (http://pyunit.sourceforge.net/
        ).
   
   

Chapter 14. Test-First Programming
   
  * 14.3. roman.py, stage 3
        Note: Know when to stop coding
        The most important thing that comprehensive unit testing can tell you
        is when to stop coding. When all the unit tests for a function pass,
        stop coding the function. When all the unit tests for an entire module
        pass, stop coding the module.
   
   
  * 14.5. roman.py, stage 5
        Note: What to do when all of your tests pass
        When all of your tests pass, stop coding.
   
   

Chapter 15. Refactoring
   
  * 15.3. Refactoring
        Note: Compiling regular expressions
        Whenever you are going to use a regular expression more than once, you
        should compile it to get a pattern object, then call the methods on the
        pattern object directly.
   
   

Chapter 16. Functional Programming
   
  * 16.2. Finding the path
        Note: os.path.abspath does not validate pathnames
        The pathnames and filenames you pass to os.path.abspath do not need to
        exist.
        Note: Normalizing pathnames
        os.path.abspath not only constructs full path names, it also normalizes
        them. That means that if you are in the /usr/ directory,
        os.path.abspath('bin/../local/bin') will return /usr/local/bin. It
        normalizes the path by making it as simple as possible. If you just
        want to normalize a pathname like this without turning it into a full
        pathname, use os.path.normpath instead.
        Note: os.path.abspath is cross-platform
        Like the other functions in the os and os.path modules, os.path.abspath
        is cross-platform. Your results will look slightly different than my
        examples if you're running on Windows (which uses backslash as a path
        separator) or Mac OS (which uses colons), but they'll still work.
        That's the whole point of the os module.
   
   

Chapter 17. Dynamic functions
   
Chapter 18. Performance Tuning
   
  * 18.2. Using the timeit Module
        Tip:
        You can use the timeit module on the command line to test an existing
        Python program, without modifying the code. See http://docs.python.org/
        lib/node396.html for documentation on the command-line flags.
        Tip:
        The timeit module only works if you already know what piece of code you
        need to optimize. If you have a larger Python program and don't know
        where your performance problems are, check out the hotshot module. (
        http://docs.python.org/lib/module-hotshot.html)
   
   

