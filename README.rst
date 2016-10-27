renpy-requests
==============

This is an integration of the python requests module with Ren'Py.

It supports http and https, with a huge caveat - the https support is not
validated, which means that the request - and any passwords it contains - can
be read by someone trying to intercept the connection.

If that doesn't matter - for example, if you're sending high scores that
aren't that important - this might be the library for you. But don't use
to to send passwords or anything remotely important.


Using
-----

Copy the followin files and directories from game/ into your project's
game directory:

* cgi.py
* Cookie.py
* ecdsa/
* hmac.py
* Queue.py
* requests/
* tlslite/
* uuid.py

Then add to your script code like::

    init python:
        import requests

    label start:

        show text "Please wait..."
        pause 0

        python:
            try:
                response = requests.get("http://www.renpy.org/")
            except:
                response = None

        hide text

        "[response.text]"
