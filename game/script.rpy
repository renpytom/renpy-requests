init python:
    import tlslite
    import requests


label main_menu:
    return



## The game starts here.


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
