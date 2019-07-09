import math

"""
SET UP IDE
"""

# go to VS code extensions
# search for python
# install the python extension that is by Microsoft
# ctrl + shift + P --> to open text box @ top of screen
# type 'python: select linter'
# choose pep8
# accept the install prompt at the bottom of the screen to install pep8
# (this just runs 'pip install autopep8' for you)

# OR use PyCharm where all of this is already set up
# OR use whatever text editor you prefer :)


"""
ENTERING VIRTUAL ENVIRONMENT
"""

# pip install virtualenv

# create virtualenviornment for your new project:
# virtualenv venv

# if you run the above command your virtual environment
# will be named 'venv'
# can name it whatever you want but a lot of ppl call theirs
# for each project 'venv'

# if the virtual environment says python2 you can change it
# to python 3 by running:
# virtualenv -p /usr/bin/python3 venv

# but replace /usr/bin/python3 with the path to wherever
# your python is.
# to find where python is saved on your system:

# Mac
# which python

# Windows
# python
# (now you are in python repl)
# >>> import os
# >>> import sys
# >>> os.path.dirname(sys.executable)
# the above command will print your path
# >>> exit()

# activate your virtualenvironment:

# windows
# venv\Scripts\activate

# mac
# source venv/bin/activate

# to deactivate after you finish your coding sesh:
# deactivate


"""
PRIMITIVE TYPES
"""

my_int = 1
my_float = 1.1
my_string = 'hello'
my_bool = True
none_type = None

"""python is dynamically typed"""

# convert a float to an int
print('float:', my_float)       # this kind of string concatonation automatically converts
my_new_int = int(my_float)      # any type to a string (dynamic typing in action!)
print('my new int floor:', my_new_int)
my_new_int = round(my_float)
print('my new int rounded:', my_new_int)
my_new_int = math.ceil(my_float)
print('my new int ceiling:', my_new_int)


"""
COLLECTIONS
"""

"""dictionaries"""
my_empty_dict = {}
my_dict = {'key1': 'value1', 'key2': 'value2'}
# keys have to be unique
# values dont have to be unique

my_dict_with_keys_repeated = {'key1': 'value1', 'key1': 'value2'}
print('my_dict:', my_dict) 
# you will see one of the key/value pairs gets removed bc
# a key is duplicated (but no error is raised! be careful!)

# you can mix and match types
# dictionaries are unordered


"""lists"""
my_empty_list = []
my_list = ['item1', 'item2', 'item3']
# you can mix and match types
# values do not have to be unique

my_list_with_items_repeated = ['item1', 'item2', 'item2', 12]
print('my list:', my_list)  # no problems here!


"""getting values from dicts & lists"""
dict_value = my_dict['key1']        # must provide the key
# will raise KeyError if key is not in dict
# we will talk about errors more on day3

dict_value = my_dict.get('key7', 0)
# set to None as default value if you do not specify a default value
# here we specified a default value of 0 so dict_value will be 7

print('dict value:', dict_value)

list_value = my_list[0]             # must provide the index
print('list value:', list_value)

list_value = my_list[-1]            # you can index lists backwards!
print('list value:', list_value)


"""tuples"""

my_empty_tuple = ()
# immutable

my_fake_one_item_tuple = (1)     # this is not a tuple, python considers this an int
print('my fake one item tuple', type(my_fake_one_item_tuple))

my_one_item_tuple = (1,)
my_two_item_tuple = (1, 2,)

# a common use case for tuples in Python
def return_two_things():
    # do some logic ...
    this_thing = 1
    that_thing = 2
    return this_thing, that_thing   # as you can see ... the paren aren't required!

my_things = return_two_things()
print('my_things type', type(my_things))

this_thing, that_thing = return_two_things()
print('this thing that thing type', type(this_thing), type(that_thing))
# you can receive variables returned as a tuple separately

# bc the paren aren't required ... watch out for trailing commas!
my_one_item_tuple = 1,
my_tuple_with_one_item = {'key': 'value'},  # be careful!

triple = 1, 2, 3


"""sets"""

my_empty_set = set()
# cannot make an empty set like {} bc that is an empty dict

my_one_item_set = {1}
my_two_item_set = {1, 2}
# python knows these are sets bc no ':' separating keys & values

# sets cannot have duplicates
my_new_list = [1, 2, 3, 4, 4]
my_set = set(my_new_list)   # removes duplicate values
print('my_set:', my_set)

"""
MATH
"""

x = 1
y = 2
z = x + y
z = x - y
z = x * y
z = x / y

z = x ** y  # exponents
z = x % y   # remainder after division

x = 1.1
y = 1
z = x + y
print('z:', z)  # you can do math with floats & ints together

x += 1  # i remember that this is += instead of =+ bc if you typed
x -= 1  # x =+ 1 then Python thinks you are setting x to a positive 1

"""
CONDITIONALS
"""

x = 1

print('conditionals practice:')

if x == 1:  # equates type and value
    print('x is 1')
else:
    print('x is not 1')

if x >= 1:
    print('x greater than or equlal to 1')
elif x < 1:                     # this could be an else but it is my peresonal preference to
    print('x is less than 1')   # be specific about the condition after the if 
                                # IF the default behavior is specific and can be defined

if x == 1:
    y = 'one'
elif x == 2:
    y = 'two'
elif x == 3:
    y = 'three'

# no switch case statements in python
# this is a prettier syntax in certain situations
# than the equivilant if/elif above
example = {
    1: 'one',
    2: 'two',
    3: 'three'
}
if x in example:
    y = example[x]

"""
LOOPS / CONTROL FLOW
"""

# you can imagine that the i = 0 and i += 1
# is there but Python will imply that i starts
# at 0 and that you want to increase by 1
# each time if you do not specify these things
# explictly

# i = 0
for i in range(10):     # exclusive range
    print('loop #', i)
    # i += 1
print('after the loop:', i)

# the best way to specify your starting value explicitly
# and/or increment:

for j in range(4, 10, 2):     # start, stop (exclusive), increment
    print('loop #', j)
print('after the loop:', j)

# looping over a collection

for item in my_list:
    print('looping over list', item)

for key in my_dict:
    print('looping over dict', key)

for key, value in my_dict.items():
    print('looping over dict', key)

for value in my_dict.values():
    print('looping over dict', value)

k = 0       # while loops do require a starting point
while k < 5:
    print('loop number', k)
    k += 1

# use a while loop when you want to loop over
# something until a certain condition is met
# rather than looping over something a certain amount
# of times

my_list = [1, 2, 3]
value = my_list[0]
index = 1
while value != 3:
    value = my_list[index]
    index += 1

# the while loop can be re-written as a for loop but
# the while loop probably is more intuitive bc the
# idea is to continue looping until a condition is met
# (the purpose of a while loop)

for value in my_list:
    if value == 3:
        break       # also people don't like to 'break' out of loops
    else:           # a lot of the time bc if the code expands
        continue    # and someone doesn't notice the break it can cause bugs easily

# the 'else: continue' is useless in this situation but ...
# now you know about the continue keyword to 'continue' a for loop.
# if there were more logic after the continue, it would not execute
# during that iteration. 'continue' starts the next iteration

# while True:
    # this is commented out so the script will finish processing
    # BUT this is another example of a use case for a while loop
    # use 'while True' to begin long running processes
    # e.g. consuming from a queue


"""
STRING CONCATONATION
"""

name = 'Jordan'
print('hello', name)    # automatically converts to string
                        # adds a space

print('hello ' + str(name)) # does not convert to string (error will be raised otherwise)
                            # does not add a space

print(f'hello {name}')  # automatically converts to string
                        # prettiest and most preferred way to concatonate strings usually :)
