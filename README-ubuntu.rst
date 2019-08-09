Bakery
======
Description
-----------
This is education project.
The application helps to organise a business of the bakery shop.

Hints on requirements installation
----------------------------------
Make sure python2.7, pip and virtualenv are installed.

Tested on Ubuntu 18.04 LTS.
Hints to install:
    | sudo apt install python2.7 python-pip
    | sudo pip install virtualenv

Hints to uninstall:
    | sudo pip uninstall virtualenv
    | sudo apt remove python-pip python2.7

The way to run the app
----------------------
It is best to use a dedicated Python environment to not interfere with OS-wide one:

    | cd bakery
    | virtualenv -p /usr/bin/python2.7 venv
    | source venv/bin/activate

Run application

    | pip install .
    | python setup.py build
    | export FLASK_APP=build/lib.linux-x86_64-2.7/bakery/bakery.py
    | export FLASK_ENV=development
    | python -m flask run

When done

    | deactivate
