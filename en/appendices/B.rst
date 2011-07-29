Appendix B. A 5-minute review
==============================

Chapter 1. Installing Python
   
  * 1.1. Which Python is right for you?
       
        The first thing you need to do with Python is install it. Or do you?
   
  * 1.2. Python on Windows
       
        On Windows, you have a couple choices for installing Python.
   
  * 1.3. Python on Mac OS X
       
        On Mac OS X, you have two choices for installing Python: install it, or
        don't install it. You probably want to install it.
   
  * 1.4. Python on Mac OS 9
       
        Mac OS 9 does not come with any version of Python, but installation is
        very simple, and there is only one choice.
   
  * 1.5. Python on RedHat Linux
       
        Download the latest Python RPM by going to http://www.python.org/ftp/
        python/ and selecting the highest version number listed, then selecting
        the rpms/ directory within that. Then download the RPM with the highest
        version number. You can install it with the rpm command, as shown here:
   
  * 1.6. Python on Debian GNU/Linux
       
        If you are lucky enough to be running Debian GNU/Linux, you install
        Python through the apt command.
   
  * 1.7. Python Installation from Source
       
        If you prefer to build from source, you can download the Python source
        code from http://www.python.org/ftp/python/. Select the highest version
        number listed, download the .tgz file), and then do the usual configure
        , make, make install dance.
   
  * 1.8. The Interactive Shell
       
        Now that you have Python installed, what's this interactive shell thing
        you're running?
   
  * 1.9. Summary
       
        You should now have a version of Python installed that works for you.
   

Chapter 2. Your First Python Program
   
  * 2.1. Diving in
       
        Here is a complete, working Python program.
   
  * 2.2. Declaring Functions
       
        Python has functions like most other languages, but it does not have
        separate header files like C++ or interface/implementation sections
        like Pascal. When you need a function, just declare it, like this:
   
  * 2.3. Documenting Functions
       
        You can document a Python function by giving it a doc string.
   
  * 2.4. Everything Is an Object
       
        A function, like everything else in Python, is an object.
   
  * 2.5. Indenting Code
       
        Python functions have no explicit begin or end, and no curly braces to
        mark where the function code starts and stops. The only delimiter is a
        colon (:) and the indentation of the code itself.
   
  * 2.6. Testing Modules
       
        Python modules are objects and have several useful attributes. You can
        use this to easily test your modules as you write them. Here's an
        example that uses the if __name__ trick.
   

Chapter 3. Native Datatypes
   
  * 3.1. Introducing Dictionaries
       
        One of Python's built-in datatypes is the dictionary, which defines
        one-to-one relationships between keys and values.
   
  * 3.2. Introducing Lists
       
        Lists are Python's workhorse datatype. If your only experience with
        lists is arrays in Visual Basic or (God forbid) the datastore in
        Powerbuilder, brace yourself for Python lists.
   
  * 3.3. Introducing Tuples
       
        A tuple is an immutable list. A tuple can not be changed in any way
        once it is created.
   
  * 3.4. Declaring variables
       
        Python has local and global variables like most other languages, but it
        has no explicit variable declarations. Variables spring into existence
        by being assigned a value, and they are automatically destroyed when
        they go out of scope.
   
  * 3.5. Formatting Strings
       
        Python supports formatting values into strings. Although this can
        include very complicated expressions, the most basic usage is to insert
        values into a string with the %s placeholder.
   
  * 3.6. Mapping Lists
       
        One of the most powerful features of Python is the list comprehension,
        which provides a compact way of mapping a list into another list by
        applying a function to each of the elements of the list.
   
  * 3.7. Joining Lists and Splitting Strings
       
        You have a list of key-value pairs in the form key=value, and you want
        to join them into a single string. To join any list of strings into a
        single string, use the join method of a string object.
   
  * 3.8. Summary
       
        The odbchelper.py program and its output should now make perfect sense.
   

Chapter 4. The Power Of Introspection
   
  * 4.1. Diving In
       
        Here is a complete, working Python program. You should understand a
        good deal about it just by looking at it. The numbered lines illustrate
        concepts covered in Chapter 2, Your First Python Program. Don't worry
        if the rest of the code looks intimidating; you'll learn all about it
        throughout this chapter.
   
  * 4.2. Using Optional and Named Arguments
       
        Python allows function arguments to have default values; if the
        function is called without the argument, the argument gets its default
        value. Futhermore, arguments can be specified in any order by using
        named arguments. Stored procedures in SQL Server Transact/SQL can do
        this, so if you're a SQL Server scripting guru, you can skim this part.
   
  * 4.3. Using type, str, dir, and Other Built-In Functions
       
        Python has a small set of extremely useful built-in functions. All
        other functions are partitioned off into modules. This was actually a
        conscious design decision, to keep the core language from getting
        bloated like other scripting languages (cough cough, Visual Basic).
   
  * 4.4. Getting Object References With getattr
       
        You already know that Python functions are objects. What you don't know
        is that you can get a reference to a function without knowing its name
        until run-time, by using the getattr function.
   
  * 4.5. Filtering Lists
       
        As you know, Python has powerful capabilities for mapping lists into
        other lists, via list comprehensions (Section 3.6, ??Mapping Lists??).
        This can be combined with a filtering mechanism, where some elements in
        the list are mapped while others are skipped entirely.
   
  * 4.6. The Peculiar Nature of and and or
       
        In Python, and and or perform boolean logic as you would expect, but
        they do not return boolean values; instead, they return one of the
        actual values they are comparing.
   
  * 4.7. Using lambda Functions
       
        Python supports an interesting syntax that lets you define one-line
        mini-functions on the fly. Borrowed from Lisp, these so-called lambda
        functions can be used anywhere a function is required.
   
  * 4.8. Putting It All Together
       
        The last line of code, the only one you haven't deconstructed yet, is
        the one that does all the work. But by now the work is easy, because
        everything you need is already set up just the way you need it. All the
        dominoes are in place; it's time to knock them down.
   
  * 4.9. Summary
       
        The apihelper.py program and its output should now make perfect sense.
   

Chapter 5. Objects and Object-Orientation
   
  * 5.1. Diving In
       
        Here is a complete, working Python program. Read the doc strings of the
        module, the classes, and the functions to get an overview of what this
        program does and how it works. As usual, don't worry about the stuff
        you don't understand; that's what the rest of the chapter is for.
   
  * 5.2. Importing Modules Using from module import
       
        Python has two ways of importing modules. Both are useful, and you
        should know when to use each. One way, import module, you've already
        seen in Section 2.4, ??Everything Is an Object??. The other way
        accomplishes the same thing, but it has subtle and important
        differences.
   
  * 5.3. Defining Classes
       
        Python is fully object-oriented: you can define your own classes,
        inherit from your own or built-in classes, and instantiate the classes
        you've defined.
   
  * 5.4. Instantiating Classes
       
        Instantiating classes in Python is straightforward. To instantiate a
        class, simply call the class as if it were a function, passing the
        arguments that the __init__ method defines. The return value will be
        the newly created object.
   
  * 5.5. Exploring UserDict: A Wrapper Class
       
        As you've seen, FileInfo is a class that acts like a dictionary. To
        explore this further, let's look at the UserDict class in the UserDict
        module, which is the ancestor of the FileInfo class. This is nothing
        special; the class is written in Python and stored in a .py file, just
        like any other Python code. In particular, it's stored in the lib
        directory in your Python installation.
   
  * 5.6. Special Class Methods
       
        In addition to normal class methods, there are a number of special
        methods that Python classes can define. Instead of being called
        directly by your code (like normal methods), special methods are called
        for you by Python in particular circumstances or when specific syntax
        is used.
   
  * 5.7. Advanced Special Class Methods
       
        Python has more special methods than just __getitem__ and __setitem__.
        Some of them let you emulate functionality that you may not even know
        about.
   
  * 5.8. Introducing Class Attributes
       
        You already know about data attributes, which are variables owned by a
        specific instance of a class. Python also supports class attributes,
        which are variables owned by the class itself.
   
  * 5.9. Private Functions
       
        Unlike in most languages, whether a Python function, method, or
        attribute is private or public is determined entirely by its name.
   
  * 5.10. Summary
       
        That's it for the hard-core object trickery. You'll see a real-world
        application of special class methods in Chapter 12, which uses getattr
        to create a proxy to a remote web service.
   

Chapter 6. Exceptions and File Handling
   
  * 6.1. Handling Exceptions
       
        Like many other programming languages, Python has exception handling
        via try...except blocks.
   
  * 6.2. Working with File Objects
       
        Python has a built-in function, open, for opening a file on disk. open
        returns a file object, which has methods and attributes for getting
        information about and manipulating the opened file.
   
  * 6.3. Iterating with for Loops
       
        Like most other languages, Python has for loops. The only reason you
        haven't seen them until now is that Python is good at so many other
        things that you don't need them as often.
   
  * 6.4. Using sys.modules
       
        Modules, like everything else in Python, are objects. Once imported,
        you can always get a reference to a module through the global
        dictionary sys.modules.
   
  * 6.5. Working with Directories
       
        The os.path module has several functions for manipulating files and
        directories. Here, we're looking at handling pathnames and listing the
        contents of a directory.
   
  * 6.6. Putting It All Together
       
        Once again, all the dominoes are in place. You've seen how each line of
        code works. Now let's step back and see how it all fits together.
   
  * 6.7. Summary
       
        The fileinfo.py program introduced in Chapter 5 should now make perfect
        sense.
   

Chapter 7. Regular Expressions
   
  * 7.1. Diving In
       
        If what you're trying to do can be accomplished with string functions,
        you should use them. They're fast and simple and easy to read, and
        there's a lot to be said for fast, simple, readable code. But if you
        find yourself using a lot of different string functions with if
        statements to handle special cases, or if you're combining them with
        split and join and list comprehensions in weird unreadable ways, you
        may need to move up to regular expressions.
   
  * 7.2. Case Study: Street Addresses
       
        This series of examples was inspired by a real-life problem I had in my
        day job several years ago, when I needed to scrub and standardize
        street addresses exported from a legacy system before importing them
        into a newer system. (See, I don't just make this stuff up; it's
        actually useful.) This example shows how I approached the problem.
   
  * 7.3. Case Study: Roman Numerals
       
        You've most likely seen Roman numerals, even if you didn't recognize
        them. You may have seen them in copyrights of old movies and television
        shows ("Copyright MCMXLVI" instead of "Copyright 1946"), or on the
        dedication walls of libraries or universities ("established
        MDCCCLXXXVIII" instead of "established 1888"). You may also have seen
        them in outlines and bibliographical references. It's a system of
        representing numbers that really does date back to the ancient Roman
        empire (hence the name).
   
  * 7.4. Using the {n,m} Syntax
       
        In the previous section, you were dealing with a pattern where the same
        character could be repeated up to three times. There is another way to
        express this in regular expressions, which some people find more
        readable. First look at the method we already used in the previous
        example.
   
  * 7.5. Verbose Regular Expressions
       
        So far you've just been dealing with what I'll call "compact" regular
        expressions. As you've seen, they are difficult to read, and even if
        you figure out what one does, that's no guarantee that you'll be able
        to understand it six months later. What you really need is inline
        documentation.
   
  * 7.6. Case study: Parsing Phone Numbers
       
        So far you've concentrated on matching whole patterns. Either the
        pattern matches, or it doesn't. But regular expressions are much more
        powerful than that. When a regular expression does match, you can pick
        out specific pieces of it. You can find out what matched where.
   
  * 7.7. Summary
       
        This is just the tiniest tip of the iceberg of what regular expressions
        can do. In other words, even though you're completely overwhelmed by
        them now, believe me, you ain't seen nothing yet.
   

Chapter 8. HTML Processing
   
  * 8.1. Diving in
       
        I often see questions on comp.lang.python (http://groups.google.com/
        groups?group=comp.lang.python) like "How can I list all the [headers|
        images|links] in my HTML document?" "How do I parse/translate/munge the
        text of my HTML document but leave the tags alone?" "How can I add/
        remove/quote attributes of all my HTML tags at once?" This chapter will
        answer all of these questions.
   
  * 8.2. Introducing sgmllib.py
       
        HTML processing is broken into three steps: breaking down the HTML into
        its constituent pieces, fiddling with the pieces, and reconstructing
        the pieces into HTML again. The first step is done by sgmllib.py, a
        part of the standard Python library.
   
  * 8.3. Extracting data from HTML documents
       
        To extract data from HTML documents, subclass the SGMLParser class and
        define methods for each tag or entity you want to capture.
   
  * 8.4. Introducing BaseHTMLProcessor.py
       
        SGMLParser doesn't produce anything by itself. It parses and parses and
        parses, and it calls a method for each interesting thing it finds, but
        the methods don't do anything. SGMLParser is an HTML consumer: it takes
        HTML and breaks it down into small, structured pieces. As you saw in
        the previous section, you can subclass SGMLParser to define classes
        that catch specific tags and produce useful things, like a list of all
        the links on a web page. Now you'll take this one step further by
        defining a class that catches everything SGMLParser throws at it and
        reconstructs the complete HTML document. In technical terms, this class
        will be an HTML producer.
   
  * 8.5. locals and globals
       
        Let's digress from HTML processing for a minute and talk about how
        Python handles variables. Python has two built-in functions, locals and
        globals, which provide dictionary-based access to local and global
        variables.
   
  * 8.6. Dictionary-based string formatting
       
        There is an alternative form of string formatting that uses
        dictionaries instead of tuples of values.
   
  * 8.7. Quoting attribute values
       
        A common question on comp.lang.python (http://groups.google.com/groups?
        group=comp.lang.python) is "I have a bunch of HTML documents with
        unquoted attribute values, and I want to properly quote them all. How
        can I do this?"[4] (This is generally precipitated by a project manager
        who has found the HTML-is-a-standard religion joining a large project
        and proclaiming that all pages must validate against an HTML validator.
        Unquoted attribute values are a common violation of the HTML standard.)
        Whatever the reason, unquoted attribute values are easy to fix by
        feeding HTML through BaseHTMLProcessor.
   
  * 8.8. Introducing dialect.py
       
        Dialectizer is a simple (and silly) descendant of BaseHTMLProcessor. It
        runs blocks of text through a series of substitutions, but it makes
        sure that anything within a <pre>...</pre> block passes through
        unaltered.
   
  * 8.9. Putting it all together
       
        It's time to put everything you've learned so far to good use. I hope
        you were paying attention.
   
  * 8.10. Summary
       
        Python provides you with a powerful tool, sgmllib.py, to manipulate
        HTML by turning its structure into an object model. You can use this
        tool in many different ways.
   

Chapter 9. XML Processing
   
  * 9.1. Diving in
       
        There are two basic ways to work with XML. One is called SAX ("Simple
        API for XML"), and it works by reading the XML a little bit at a time
        and calling a method for each element it finds. (If you read Chapter 8,
        HTML Processing, this should sound familiar, because that's how the
        sgmllib module works.) The other is called DOM ("Document Object Model
        "), and it works by reading in the entire XML document at once and
        creating an internal representation of it using native Python classes
        linked in a tree structure. Python has standard modules for both kinds
        of parsing, but this chapter will only deal with using the DOM.
   
  * 9.2. Packages
       
        Actually parsing an XML document is very simple: one line of code.
        However, before you get to that line of code, you need to take a short
        detour to talk about packages.
   
  * 9.3. Parsing XML
       
        As I was saying, actually parsing an XML document is very simple: one
        line of code. Where you go from there is up to you.
   
  * 9.4. Unicode
       
        Unicode is a system to represent characters from all the world's
        different languages. When Python parses an XML document, all data is
        stored in memory as unicode.
   
  * 9.5. Searching for elements
       
        Traversing XML documents by stepping through each node can be tedious.
        If you're looking for something in particular, buried deep within your
        XML document, there is a shortcut you can use to find it quickly:
        getElementsByTagName.
   
  * 9.6. Accessing element attributes
       
        XML elements can have one or more attributes, and it is incredibly
        simple to access them once you have parsed an XML document.
   
  * 9.7. Segue
       
        OK, that's it for the hard-core XML stuff. The next chapter will
        continue to use these same example programs, but focus on other aspects
        that make the program more flexible: using streams for input
        processing, using getattr for method dispatching, and using
        command-line flags to allow users to reconfigure the program without
        changing the code.
   

Chapter 10. Scripts and Streams
   
  * 10.1. Abstracting input sources
       
        One of Python's greatest strengths is its dynamic binding, and one
        powerful use of dynamic binding is the file-like object.
   
  * 10.2. Standard input, output, and error
       
        UNIX users are already familiar with the concept of standard input,
        standard output, and standard error. This section is for the rest of
        you.
   
  * 10.3. Caching node lookups
       
        kgp.py employs several tricks which may or may not be useful to you in
        your XML processing. The first one takes advantage of the consistent
        structure of the input documents to build a cache of nodes.
   
  * 10.4. Finding direct children of a node
       
        Another useful techique when parsing XML documents is finding all the
        direct child elements of a particular element. For instance, in the
        grammar files, a ref element can have several p elements, each of which
        can contain many things, including other p elements. You want to find
        just the p elements that are children of the ref, not p elements that
        are children of other p elements.
   
  * 10.5. Creating separate handlers by node type
       
        The third useful XML processing tip involves separating your code into
        logical functions, based on node types and element names. Parsed XML
        documents are made up of various types of nodes, each represented by a
        Python object. The root level of the document itself is represented by
        a Document object. The Document then contains one or more Element
        objects (for actual XML tags), each of which may contain other Element
        objects, Text objects (for bits of text), or Comment objects (for
        embedded comments). Python makes it easy to write a dispatcher to
        separate the logic for each node type.
   
  * 10.6. Handling command-line arguments
       
        Python fully supports creating programs that can be run on the command
        line, complete with command-line arguments and either short- or
        long-style flags to specify various options. None of this is XML
        -specific, but this script makes good use of command-line processing,
        so it seemed like a good time to mention it.
   
  * 10.7. Putting it all together
       
        You've covered a lot of ground. Let's step back and see how all the
        pieces fit together.
   
  * 10.8. Summary
       
        Python comes with powerful libraries for parsing and manipulating XML
        documents. The minidom takes an XML file and parses it into Python
        objects, providing for random access to arbitrary elements.
        Furthermore, this chapter shows how Python can be used to create a
        "real" standalone command-line script, complete with command-line
        flags, command-line arguments, error handling, even the ability to take
        input from the piped result of a previous program.
   

Chapter 11. HTTP Web Services
   
  * 11.1. Diving in
       
        You've learned about HTML processing and XML processing, and along the
        way you saw how to download a web page and how to parse XML from a URL,
        but let's dive into the more general topic of HTTP web services.
   
  * 11.2. How not to fetch data over HTTP
       
        Let's say you want to download a resource over HTTP, such as a
        syndicated Atom feed. But you don't just want to download it once; you
        want to download it over and over again, every hour, to get the latest
        news from the site that's offering the news feed. Let's do it the
        quick-and-dirty way first, and then see how you can do better.
   
  * 11.3. Features of HTTP
       
        There are five important features of HTTP which you should support.
   
  * 11.4. Debugging HTTP web services
       
        First, let's turn on the debugging features of Python's HTTP library
        and see what's being sent over the wire. This will be useful throughout
        the chapter, as you add more and more features.
   
  * 11.5. Setting the User-Agent
       
        The first step to improving your HTTP web services client is to
        identify yourself properly with a User-Agent. To do that, you need to
        move beyond the basic urllib and dive into urllib2.
   
  * 11.6. Handling Last-Modified and ETag
       
        Now that you know how to add custom HTTP headers to your web service
        requests, let's look at adding support for Last-Modified and ETag
        headers.
   
  * 11.7. Handling redirects
       
        You can support permanent and temporary redirects using a different
        kind of custom URL handler.
   
  * 11.8. Handling compressed data
       
        The last important HTTP feature you want to support is compression.
        Many web services have the ability to send data compressed, which can
        cut down the amount of data sent over the wire by 60% or more. This is
        especially true of XML web services, since XML data compresses very
        well.
   
  * 11.9. Putting it all together
       
        You've seen all the pieces for building an intelligent HTTP web
        services client. Now let's see how they all fit together.
   
  * 11.10. Summary
       
        The openanything.py and its functions should now make perfect sense.
   

Chapter 12. SOAP Web Services
   
  * 12.1. Diving In
       
        You use Google, right? It's a popular search engine. Have you ever
        wished you could programmatically access Google search results? Now you
        can. Here is a program to search Google from Python.
   
  * 12.2. Installing the SOAP Libraries
       
        Unlike the other code in this book, this chapter relies on libraries
        that do not come pre-installed with Python.
   
  * 12.3. First Steps with SOAP
       
        The heart of SOAP is the ability to call remote functions. There are a
        number of public access SOAP servers that provide simple functions for
        demonstration purposes.
   
  * 12.4. Debugging SOAP Web Services
       
        The SOAP libraries provide an easy way to see what's going on behind
        the scenes.
   
  * 12.5. Introducing WSDL
       
        The SOAPProxy class proxies local method calls and transparently turns
        then into invocations of remote SOAP methods. As you've seen, this is a
        lot of work, and SOAPProxy does it quickly and transparently. What it
        doesn't do is provide any means of method introspection.
   
  * 12.6. Introspecting SOAP Web Services with WSDL
       
        Like many things in the web services arena, WSDL has a long and
        checkered history, full of political strife and intrigue. I will skip
        over this history entirely, since it bores me to tears. There were
        other standards that tried to do similar things, but WSDL won, so let's
        learn how to use it.
   
  * 12.7. Searching Google
       
        Let's finally turn to the sample code that you saw that the beginning
        of this chapter, which does something more useful and exciting than get
        the current temperature.
   
  * 12.8. Troubleshooting SOAP Web Services
       
        Of course, the world of SOAP web services is not all happiness and
        light. Sometimes things go wrong.
   
  * 12.9. Summary
       
        SOAP web services are very complicated. The specification is very
        ambitious and tries to cover many different use cases for web services.
        This chapter has touched on some of the simpler use cases.
   

Chapter 13. Unit Testing
   
  * 13.1. Introduction to Roman numerals
       
        In previous chapters, you "dived in" by immediately looking at code and
        trying to understand it as quickly as possible. Now that you have some
        Python under your belt, you're going to step back and look at the steps
        that happen before the code gets written.
   
  * 13.2. Diving in
       
        Now that you've completely defined the behavior you expect from your
        conversion functions, you're going to do something a little unexpected:
        you're going to write a test suite that puts these functions through
        their paces and makes sure that they behave the way you want them to.
        You read that right: you're going to write code that tests code that
        you haven't written yet.
   
  * 13.3. Introducing romantest.py
       
        This is the complete test suite for your Roman numeral conversion
        functions, which are yet to be written but will eventually be in
        roman.py. It is not immediately obvious how it all fits together; none
        of these classes or methods reference any of the others. There are good
        reasons for this, as you'll see shortly.
   
  * 13.4. Testing for success
       
        The most fundamental part of unit testing is constructing individual
        test cases. A test case answers a single question about the code it is
        testing.
   
  * 13.5. Testing for failure
       
        It is not enough to test that functions succeed when given good input;
        you must also test that they fail when given bad input. And not just
        any sort of failure; they must fail in the way you expect.
   
  * 13.6. Testing for sanity
       
        Often, you will find that a unit of code contains a set of reciprocal
        functions, usually in the form of conversion functions where one
        converts A to B and the other converts B to A. In these cases, it is
        useful to create a "sanity check" to make sure that you can convert A
        to B and back to A without losing precision, incurring rounding errors,
        or triggering any other sort of bug.
   

Chapter 14. Test-First Programming
   
  * 14.1. roman.py, stage 1
       
        Now that the unit tests are complete, it's time to start writing the
        code that the test cases are attempting to test. You're going to do
        this in stages, so you can see all the unit tests fail, then watch them
        pass one by one as you fill in the gaps in roman.py.
   
  * 14.2. roman.py, stage 2
       
        Now that you have the framework of the roman module laid out, it's time
        to start writing code and passing test cases.
   
  * 14.3. roman.py, stage 3
       
        Now that toRoman behaves correctly with good input (integers from 1 to
        3999), it's time to make it behave correctly with bad input (everything
        else).
   
  * 14.4. roman.py, stage 4
       
        Now that toRoman is done, it's time to start coding fromRoman. Thanks
        to the rich data structure that maps individual Roman numerals to
        integer values, this is no more difficult than the toRoman function.
   
  * 14.5. roman.py, stage 5
       
        Now that fromRoman works properly with good input, it's time to fit in
        the last piece of the puzzle: making it work properly with bad input.
        That means finding a way to look at a string and determine if it's a
        valid Roman numeral. This is inherently more difficult than validating
        numeric input in toRoman, but you have a powerful tool at your
        disposal: regular expressions.
   

Chapter 15. Refactoring
   
  * 15.1. Handling bugs
       
        Despite your best efforts to write comprehensive unit tests, bugs
        happen. What do I mean by "bug"? A bug is a test case you haven't
        written yet.
   
  * 15.2. Handling changing requirements
       
        Despite your best efforts to pin your customers to the ground and
        extract exact requirements from them on pain of horrible nasty things
        involving scissors and hot wax, requirements will change. Most
        customers don't know what they want until they see it, and even if they
        do, they aren't that good at articulating what they want precisely
        enough to be useful. And even if they do, they'll want more in the next
        release anyway. So be prepared to update your test cases as
        requirements change.
   
  * 15.3. Refactoring
       
        The best thing about comprehensive unit testing is not the feeling you
        get when all your test cases finally pass, or even the feeling you get
        when someone else blames you for breaking their code and you can
        actually prove that you didn't. The best thing about unit testing is
        that it gives you the freedom to refactor mercilessly.
   
  * 15.4. Postscript
       
        A clever reader read the previous section and took it to the next
        level. The biggest headache (and performance drain) in the program as
        it is currently written is the regular expression, which is required
        because you have no other way of breaking down a Roman numeral. But
        there's only 5000 of them; why don't you just build a lookup table
        once, then simply read that? This idea gets even better when you
        realize that you don't need to use regular expressions at all. As you
        build the lookup table for converting integers to Roman numerals, you
        can build the reverse lookup table to convert Roman numerals to
        integers.
   
  * 15.5. Summary
       
        Unit testing is a powerful concept which, if properly implemented, can
        both reduce maintenance costs and increase flexibility in any long-term
        project. It is also important to understand that unit testing is not a
        panacea, a Magic Problem Solver, or a silver bullet. Writing good test
        cases is hard, and keeping them up to date takes discipline (especially
        when customers are screaming for critical bug fixes). Unit testing is
        not a replacement for other forms of testing, including functional
        testing, integration testing, and user acceptance testing. But it is
        feasible, and it does work, and once you've seen it work, you'll wonder
        how you ever got along without it.
   

Chapter 16. Functional Programming
   
  * 16.1. Diving in
       
        In Chapter 13, Unit Testing, you learned about the philosophy of unit
        testing. In Chapter 14, Test-First Programming, you stepped through the
        implementation of basic unit tests in Python. In Chapter 15,
        Refactoring, you saw how unit testing makes large-scale refactoring
        easier. This chapter will build on those sample programs, but here we
        will focus more on advanced Python-specific techniques, rather than on
        unit testing itself.
   
  * 16.2. Finding the path
       
        When running Python scripts from the command line, it is sometimes
        useful to know where the currently running script is located on disk.
   
  * 16.3. Filtering lists revisited
       
        You're already familiar with using list comprehensions to filter lists.
        There is another way to accomplish this same thing, which some people
        feel is more expressive.
   
  * 16.4. Mapping lists revisited
       
        You're already familiar with using list comprehensions to map one list
        into another. There is another way to accomplish the same thing, using
        the built-in map function. It works much the same way as the filter
        function.
   
  * 16.5. Data-centric programming
       
        By now you're probably scratching your head wondering why this is
        better than using for loops and straight function calls. And that's a
        perfectly valid question. Mostly, it's a matter of perspective. Using
        map and filter forces you to center your thinking around your data.
   
  * 16.6. Dynamically importing modules
       
        OK, enough philosophizing. Let's talk about dynamically importing
        modules.
   
  * 16.7. Putting it all together
       
        You've learned enough now to deconstruct the first seven lines of this
        chapter's code sample: reading a directory and importing selected
        modules within it.
   
  * 16.8. Summary
       
        The regression.py program and its output should now make perfect sense.
   

Chapter 17. Dynamic functions
   
  * 17.1. Diving in
       
        I want to talk about plural nouns. Also, functions that return other
        functions, advanced regular expressions, and generators. Generators are
        new in Python 2.3. But first, let's talk about how to make plural
        nouns.
   
  * 17.2. plural.py, stage 1
       
        So you're looking at words, which at least in English are strings of
        characters. And you have rules that say you need to find different
        combinations of characters, and then do different things to them. This
        sounds like a job for regular expressions.
   
  * 17.3. plural.py, stage 2
       
        Now you're going to add a level of abstraction. You started by defining
        a list of rules: if this, then do that, otherwise go to the next rule.
        Let's temporarily complicate part of the program so you can simplify
        another part.
   
  * 17.4. plural.py, stage 3
       
        Defining separate named functions for each match and apply rule isn't
        really necessary. You never call them directly; you define them in the
        rules list and call them through there. Let's streamline the rules
        definition by anonymizing those functions.
   
  * 17.5. plural.py, stage 4
       
        Let's factor out the duplication in the code so that defining new rules
        can be easier.
   
  * 17.6. plural.py, stage 5
       
        You've factored out all the duplicate code and added enough
        abstractions so that the pluralization rules are defined in a list of
        strings. The next logical step is to take these strings and put them in
        a separate file, where they can be maintained separately from the code
        that uses them.
   
  * 17.7. plural.py, stage 6
       
        Now you're ready to talk about generators.
   
  * 17.8. Summary
       
        You talked about several different advanced techniques in this chapter.
        Not all of them are appropriate for every situation.
   

Chapter 18. Performance Tuning
   
  * 18.1. Diving in
       
        There are so many pitfalls involved in optimizing your code, it's hard
        to know where to start.
   
  * 18.2. Using the timeit Module
       
        The most important thing you need to know about optimizing Python code
        is that you shouldn't write your own timing function.
   
  * 18.3. Optimizing Regular Expressions
       
        The first thing the Soundex function checks is whether the input is a
        non-empty string of letters. What's the best way to do this?
   
  * 18.4. Optimizing Dictionary Lookups
       
        The second step of the Soundex algorithm is to convert characters to
        digits in a specific pattern. What's the best way to do this?
   
  * 18.5. Optimizing List Operations
       
        The third step in the Soundex algorithm is eliminating consecutive
        duplicate digits. What's the best way to do this?
   
  * 18.6. Optimizing String Manipulation
       
        The final step of the Soundex algorithm is padding short results with
        zeros, and truncating long results. What is the best way to do this?
   
  * 18.7. Summary
       
        This chapter has illustrated several important aspects of performance
        tuning in Python, and performance tuning in general.
   

