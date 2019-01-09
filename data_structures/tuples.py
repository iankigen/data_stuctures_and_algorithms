"""
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples
 and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
"""
tup1 = ('tesla',)
tup2 = 'q', 'a'

# Accessing Values in Tuples

print(tup2[1])

# Basic tuple operations
'''
Python Expression	Results	Description
len((1, 2, 3))	3	Length
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	Concatenation
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	True	Membership
for x in (1, 2, 3): print x,	1 2 3	Iteration
'''

# Delete Tuple Elements
# Removing individual tuple elements is not possible.


# Updating Tuples
# Tuples are immutable which means you cannot update or change the values of tuple elements.
