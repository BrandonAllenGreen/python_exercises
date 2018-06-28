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


# list comprehension is similar to map() and filter() in JS.  iterate over collection, perform logic, and return new collection.
flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']

# long way to write a  for loop
large_flowers = list()
for f in flowers:
    large_flowers.append('a large ' + f)

print(large_flowers)

# shorthand for loop
large_flowers = ['a large ' + f for f in flowers]

print(large_flowers)
