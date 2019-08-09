Bakery
======
Description
-----------
This is education project.
The application helps to organise a business of the bakery shop.

Hints on requirements installation
----------------------------------
Make sure python2.7, pip and virtualenv are installed.

Tested on MacOS 10.14 using Homebrew tool.
Hints to install:
    | brew install python@2
    | pip install virtualenv

Hints to uninstall:
    | pip uninstall virtualenv
    | brew remove python@2

The way to run the app
----------------------
It is best to use a dedicated Python environment to not interfere with OS-wide one:

    | cd bakery
    | virtualenv -p /usr/bin/python2.7 venv
    | source venv/bin/activate

Run application

    | pip install .
    | python setup.py build
    | export FLASK_APP=build/lib/bakery/bakery.py
    | export FLASK_ENV=development
    | python -m flask run

When done

    | deactivate
