# Getting Portable Graphics Library (PGL) to work on a Mac

Some Macs may currently be incompatible with one of the software libraries
used by the Portable Graphics Library (PGL). To test whether this is the
case, try the following:

1. Open the Terminal application.
2. Type the following:

    $ python
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tkinter
    >>> tkinter._test() 

If a friendly window pops up that says "This is Tcl/Tk..." and more, then
you're fine. Otherwise, you were probably automatically logged out and are
now facing the log in screen. Take a deep breath, log back in, and fix the
problem by taking the following steps:

1. Visit the website https://www.python.org/downloads/.
2. Click the yellow button "Download Python 3.7.4".
3. Wait for the download to complete. It should download a file called ```python-3.7.4-macosx10.9.pkg```.
4. Click on that file to start the installer, then go through the installation steps, accepting all default suggestions.
5. Open the Terminal application again.
6. Type the following:

    echo "alias python=/usr/local/bin/python3.7" >> ~/.bash_profile
    
7. Exit the Terminal by typing Cmd-Q.
8. Open the Terminal application again (!)
9. Now try the test again:

    $ python
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tkinter
    >>> tkinter._test() 
    
Hopefully you get the friendly pop-up window. If not, email me (hopkinsm@reed.edu)
for help.

