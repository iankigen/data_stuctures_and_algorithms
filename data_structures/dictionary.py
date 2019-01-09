"""
In Dictionary each key is separated from its value by a colon (:), the items are separated by commas, and the whole
thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys
must be of an immutable data type such as strings, numbers, or tuples.
"""

dict = {'name': 'Ken', 'age': 100}

# Accessing Values in Dictionary

print(dict.get('name'))
print(dict['age'])

# Updating Dictionary

dict['age'] = 25

# Delete Dictionary Elements
del dict['name']  # remove entry with key 'Name'
print(dict)

dict.clear()  # remove all entries in dict
print(dict)

del dict  # delete entire dictionary
print(dict)
