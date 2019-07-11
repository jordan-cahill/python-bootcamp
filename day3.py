
# windows
# venv\Scripts\activate

# mac
# source venv/bin/activate

"""ABSTRACT CLASSES"""

from abc import (
    ABC,
    abstractmethod
)

class Pet:

    def play(self):
        raise NotImplementedError

class Pet(ABC):

    @abstractmethod
    def play(self):
        """
        All pets should be able to play

        :param name_of_param: desc
        :return: what gets returned
        :raises: what error might get raised
        """
        print('get pet, cuddle, play with toys')

class Cat(Pet):

    def play(self):
        super().play()
        print('climb trees, kill birds')

class Dog(Pet):

    def play(self):
        super().play()
        print('fetch, swim, tug of war')

class Bird(Pet):
    pass

#amy_belle = Bird()      # ABC will raise an error when you try to instanciate
                        # an object that does not follow the abstract class rules
#amy_belle.play()        # not implemtned errror will be raised when you
                        # call the method you are trying to enforce

bowie = Dog()
bowie.play()

"""ARGS KWARGS OPTIONAL PARAMS"""

def required_positional_arguments_function(one, two, three):
    print(one, two, three)

print(1)
required_positional_arguments_function('hello', 'sogeti', 'austin')
#required_positional_arguments_function('hello', 'sogeti')

def optional_positional_arguments_function(*args):
    # one star (splat) means tuple of arguments
    my_string = ''
    for arg in args:
        my_string += arg + ' '
    print(my_string)
    print('args type:', type(args))

print(2)
optional_positional_arguments_function('hello', 'sogeti')

print(3)
args = ['hello', 'sogeti']
optional_positional_arguments_function(*args)

print(4)
# required_positional_arguments_function(*args) looks confusing

def optional_keyword_arguments_function_1(one='unknown', two='not sure', three='n/a'):
    print(one, two, three)

print(5)
optional_keyword_arguments_function_1('hello', 'sogeti')

print(6)
optional_keyword_arguments_function_1(one='hello', three='austin', two='sogeti')

print(7)
required_positional_arguments_function(one='hello', three='austin', two='sogeti')

print(8)
kwargs = {
    'one': 'hello',
    'two': 'sogeti'
}
optional_keyword_arguments_function_1(**kwargs)  # double splat lets you pass dictionary as keyword arguments

def optional_keyword_arguments_function_2(**kwargs):    # double splat
    my_string = ''
    for value in kwargs.values():
        my_string += value + ' '
    print(my_string)

print(9)
optional_keyword_arguments_function_2(**kwargs)

"""CAT EXAMPLE"""

from datetime import date

class Pet:

    def __init__(self, name, age, *args):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year, *args):
        return cls(name, date.today().year - year, *args)

    def play(self):
        print('get pet, cuddle, play with toys')

class Cat(Pet):

    def __init__(self, name, age, is_fluffy):
        super().__init__(name, age)
        self.is_fluffy = is_fluffy

    def jordans_magical_method(**kwargs):
        pass

baby_socks = Cat('Socks', 1, True)
print('is she fluffy?', baby_socks.is_fluffy)

baby_socks = Cat.from_birth_year('Socks', 2018, True)
print('is she fluffy?', baby_socks.is_fluffy)

"""EXCEPTION HANDLING"""

#make an exception happen
def raise_type_error():
    raise TypeError

try:
    raise_type_error()
except TypeError:
    print('an error occurred!')

def raise_type_error():
    1 + 'two'

try:
    raise_type_error()
except TypeError as e:  # __str__
    print('TypeError message:', e)
else:
    print('no error occured!')
finally:
    print('finally, the try except block is over!')

try:
    raise_type_error()
except Exception as e:
    print('TypeError message:', e)

""" do not ever do this
try:
    raise_type_error()
except:
    pass
"""

"""CUSTOM ERRORS"""

class NotEnoughCookiesError(Exception):

    def __init__(self, num_friends, num_cookies):
        super().__init__(f'We have {num_friends} friends and only {num_cookies} cookies')

def snack_time(num_friends, num_cookies):
    if num_cookies >= num_friends:
        return 'nom nom nom'
    raise NotEnoughCookiesError(num_friends, num_cookies)

try:
    print(snack_time(5, 4))
except NotEnoughCookiesError as e:
    print('NotEnoughCookiesError message:', e)

"""DECORATORS"""

# decorator = a function that gets called by another function
# allows you to execute code before & after a certain function executes

import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('Before the decorator!')
        func()
        print('After the decorator!')
    return function_that_runs_func

@my_decorator
def my_function():
    print('I am the function')

my_function()

"""VIRTUAL ENVIRONMENTS DISCUSSION"""

# virtualenv
# pipenv
# conda