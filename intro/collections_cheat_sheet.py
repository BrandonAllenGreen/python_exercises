#******************** COLLECTION TYPES ********************#

# lists are like JS arrays
junk = list()
junk = ['carrots', 'celery', 'kale', 2, ['peas', 'corn']]
junk.insert(1, 'kidney beans')
junk.extend([True, 'tornado'])
junk.append('hurricane')
print(junk)

# dictionaries are like JS objects
junk = dict()
junk = {'name': 'Steve', 'age': 47, 'role': 'Head Coach'}
junk['kids'] = 2
print(junk)

# set works like JS set
junk = set()
junk.add('Scott')
print(junk)
{'Scott'}

junk.add('Scott')
print(junk)
{'Scott'}

# tuple works like list but is immutable. you can't add/remove things but you can iterate over it faster than a list.
junk = tuple()
junk = ('Joe', 'Instructor', 'Awesome')
print(junk)

# functions use indentation rather than brackets. white space matters. define documentation for functions using docstrings.


def display_name(name):
    '''Displays a name
    Arguments:
    name -- a string to be printed
    '''
    print(name)


display_name('Josephina')

# access doc strings with __doc__
print(display_name.__doc__)


#******************** LOOPING ********************#
# basic for loops are slower than comprehensions


#///// lists /////#
flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']

large_flowers = list()
for f in flowers:
    large_flowers.append('a large ' + f)

print(large_flowers)


# ///// dictionaries /////#
# a for loop on a dictionary will loop over the keys
family = {'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'}

for f in family:
    print(f)

# if you want both the keys and values, loop over the items() property
family = {'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'}

for key, value in family.items():
    print(key, value)


#///// sets /////#
# looping over sets is identical to lists
cars = {'Lexus', 'Chevy', 'Jeep'}

for c in cars:
    print(c)


#******************** COMPREHENSION ********************#
# python comprehension is similar to map() and filter() in JS.  iterate over collection, perform logic, and return new collection.
# comprehension is faster than using a plain for loop and accomplishes same result.


#///// lists /////#
flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']

large_flowers = ['a large ' + f for f in flowers]

print(large_flowers)

#///// dictionaries /////#
family = {
    'mother': 'Jenine',
    'father': 'Bo',
    'brother': 'Taylor'
}

# need to use the items() property on the original dictionary for the iteration.
my_family = {'my ' + key + ' is ' + value for (key, value) in family.items()}

print(my_family)


#///// sets /////#
# set comprehensions are almost identical to list comprehensions.  punctuation is different
possible_ratings = set(range(100))

funky_ratings = {r/2 for r in possible_ratings}

print(funky_ratings)
