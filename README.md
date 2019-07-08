# Sogeti Python Bootcamp

Welcome to Sogeti Python Bootcamp! This bootcamp is designed for people with some programming experience
who want to learn Python. If you do not have a programming background, the course may feel like it is moving
a bit quickly. Regardless of experience there will be plenty of Python concepts to be learned from this course.
We will begin with Python syntax and basic logic, followed by advanced Python concepts, and then we will
then we will build a REST API with the Flask framework.

Before the bootcamp begins, please install both pip Python and add Python to your path. Pip is the Python
library installer. It should come with Python for most installations. Below you will find instructions on how
to install pip and Python. Also, make sure you bring your computer with you to the bootcamp, and be prepared
to follow along coding as I code and executing your code as I execute my code. It will be helpful for you
to also take notes as comments in your own Python documents for each day.

## Agenda
The workshop is a 5 day workshop, 1 hour per day.

### DAY 1 _Introduction to Python_

- text editors - vs code & pycharm
- set up pylint & autopep8 in vs code
- primitive types
- example: Dynamically typed
- variable assignment
- variable naming - pep8
- mathematical operators
- conditionals & boolean operators
- collection types
- loops / control flow
- functions - hello world

### DAY 2 _Object Oriented Programming with Python_

- common data manipulation methods
	- working with lists, dicts, etc (pop, append, index, etc)
	- string concatonation
- object oriented programming
- discussion: in Python classes aren't needed
- example: Poker game
	- objects & classes
	- `__init__` and `__str__`
	- object - identity, state, behavior
- example: Pet classes
	- classes - can also have class attributes & class methods & static methods
	- `__class__` and `__class__.__name__`
	- inheritance & multiple inheritance

### DAY 3 _Advanced Python Concepts_

- example: Pet classes continued
	- interfaces in python (ABC library)
	- exception handling
	- args, kwargs, optional params
	- decorators
- discussion: you can have classes in modules or functions in modules
    - when to use a class vs when to do procedural programming
    - consider state + the 4 principles of object oriented programming
- functional programming in python
	- iterators, generators, filter, map, lambda, list comprehension
	- passing functions as arguments
- discussion: virtual environments
- mention: import logging for logging
- mention: shallow copy / deep copy / references to objects passed to
  functions not copies

### DAY 4 _Python REST API with Flask_

- pip install flask
- hello world with flask
- intro to REST API
	- server side vs client side processes
	- HTTP verbs
	- endpoints as urls
	- resources, organization similar to OOP
	- stateless
- example: Store API 
	- implement endpoints with data stored in memory in dictionary
	- call Store API with JavaScript
    - test API with PostMan

### DAY 5 _Python REST API with Flask RESTful_

- example: create new Store API with Flask RESTful
    - Flask RESTful enforces REST standards are followed but it is more
      intimidating so we will begin just with using Flask on day 4
    - authentication with JWT token
    - add request parsing to ensure data is proper before adding the
      data from the client to the database & return unsuccessful HTTP response
        - could use marshmallow or jsonschema
    - connect Flask RESTful API to SQLite database

## Installing Python

### _Mac Users_

If you are using a Mac, I would recommend to install Python via Homebrew. By uisng Homebrew, pip will
automatically be installed when you install Python. First you'll have to install Homebrew. To install
Homebrew, open up your terminal and run this command:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Now you can install Python and pip by running the command:
```
brew install python
```
To make sure it worked, try running the commands:
```
python3 --version
pip3 --version
```
Mac will probably refer to the Python you install as `python3` to not mix up the Python you have installed
with the operating system Python. If a version number prints out, then Python has been added to your path and
you are good to go. If you have some sort of `python is not defined` error, some troubleshooting will be requried.

### _Windows Users_

To install Python and pip on Windows, scroll to the bottom of this web page `https://www.python.org/downloads/release/python-373/`
to see your installation options. I would recommend the `Windows x86-64 executable installer`. Before you begin the
installation, __select the check box__ on the executable installer that gives you the option to `add Python to
your PATH`. You can add it manually but this is the easiest way. Adding python to your path gives you the ability
to execute Python scripts via the command line.

Pip should be included with this installation. To confirm the installation was successful, open up command prompt and run:
```
python --version
pip --version
```
Both should print a version number.

## Using virtualenv



## Questions / Feedback / Further Disission

At the end of each topic I will ask for questions. If you have a question, please write it down so you don't forget,
then you can ask the question between topics. Certain questions may be out of the scope of the course, for example,
questions on how to clone this GitHub repo. If you feel your question is out of the scope of the course, do not
hesitate to talk to me after the course or send me an email.

If there is a Python topic you would like to discuss that may be a bit too involved to discuss between topics
during the course, I encourage you to meet up with me after the course or send me an email. I would love to hear
feedback or differing opinions or learn something new about Python -->

jordan.cahill@us.sogeti.com