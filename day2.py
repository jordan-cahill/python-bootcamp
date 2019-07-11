# source venv/bin/activate

"""FORGOT TO MENTION"""

# letters number underscores for variable names
# cant start with a number
# can start with an underscore -- but this implies the variable / function is private

# another conditional

x = 1

if x is not None:
    pass            # placeholder

my_list = [1, 2, 3]
if x not in my_list:
    pass

"""STRING MANIPULATION"""

my_string = 'Hello'
my_string_lower = my_string.lower()
print('my string lower:', my_string_lower)

print('length of string:', len(my_string))   # length of any collection

my_string = 'hello '
print(f'my string with space [{my_string}]')
print(f'my string without space [{my_string.strip()}]')     # useful for dealing with user input

print(f'my string upper without space [{my_string.strip().upper()}]')

my_string = '1 2 3 4'
my_string_parts = my_string.split() # by default, splits by spaces
print('my string parts:', my_string_parts)

my_string = '1,2,3,4'
my_string_parts = my_string.split(',')
print('my string parts:', my_string_parts)

"""slices"""

my_string = 'abcde'
print('my string a:', my_string[0])
print('my string ab:', my_string[0:2])  # exclusive
print('my string ab:', my_string[:2])   # stop string at index 2
print('my string cde:', my_string[2:])  # start string at index 2 
print('my string e:', my_string[-1])
print('my string abcd:', my_string[:-1])

# strings are immutable
# "copy on write"
my_new_string = my_string + 'f'
print('my new string:', my_new_string)

"""LIST MANIPULATION"""

number_list = [1, 2, 3]
print('sum of number list:', sum(number_list))
print('max of number list:', max(number_list))
print('min of number list:', min(number_list))

char_list = ['a', 'b', 'c']
print('char list a:', char_list[0])
print('index of char list a:', char_list.index('a'))

char_list.append('d')
print('char list with d:', char_list)
del char_list[3]
print('char list withoud d:', char_list)

my_c = char_list.pop()
print('char list c:', my_c)
print('char list without c:', char_list)

my_a = char_list.pop(0)
print('my a:', my_a)

"""TUPLE MANIPULATION"""

my_tuple = (1, 2, 3)
# immutable but you can copy on write like a string
my_new_tuple = my_tuple + ('a',)
print('my new tuple:', my_new_tuple)

# del my_tuple[0]

my_tuple = {'key': 'value'},
my_tuple[0]['key'] = 'new value'
print('my tuple with new value;', my_tuple)

"""SET MANIPULATION"""

my_set = {1, 2, 3}
my_set.add(4)
# sets are unordered 
# my_set[0]

"""DICTIONARY MANIPULATION"""

my_dict = {'first': 'one'}
my_dict['second'] = 'two'

print('my dict:', my_dict)

print('my dict first value:', my_dict.pop('first'))
print('my dict:', my_dict)

"""OBJECT ORIENTED PROGRAMMING"""

class Card:

    # capital letters to hint it is static
    RANKS = tuple(range(1, 14))
    SUITS = ('C', 'D', 'S', 'H')

    def __init__(self, suit, rank):
        self.suit = suit        # instance attributes
        self.rank = rank

    def __str__(self):
        return str(self.rank) + self.suit

my_card = Card('S', 1)

print('my card as a string:', my_card)

print('my card ranks:', my_card.RANKS)
print('card ranks:', Card.RANKS)


import random


class Deck:

    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):  # instance method
        random.shuffle(self.deck)

my_deck = Deck()
print('first card in deck before shuffle:', my_deck.deck[0])
my_deck.shuffle()
print('first card in deck after shuffle:', my_deck.deck[0])

# shuffle()

""" PET EXAMPLE """

from datetime import date

class Pet:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # factory pattern

    @classmethod
    def from_birth_year(cls, name, species, year):
        return cls(name, species, date.today().year - year)

    @staticmethod
    def is_baby(age):
        return age < 2


baby_socks = Pet('Socks', 'cat', 1)
print('baby socks age:', baby_socks.age)

baby_socks = Pet.from_birth_year('Socks', 'cat', 2018)
print('baby socks age from birth year:', baby_socks.age)

# print('is baby socks a baby?', baby_socks.is_baby())

print('is a pet who is 1 year old a baby?', Pet.is_baby(1))


"""INHERITANCE"""

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    def play(self):
        print('get pet, cuddle, play with toys')

class Feline:

    def play(self):
        print('climb trees, kill birds')

class Cat(Feline, Pet):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.is_fluffy = True

baby_socks = Cat('Socks', 1)
print(baby_socks.age)

baby_socks = Cat.from_birth_year('Socks', 2018)
print('is she fluffy', baby_socks.is_fluffy)

baby_socks.play()