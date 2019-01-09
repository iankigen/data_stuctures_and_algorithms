"""
Mathematically a set is a collection of items not in any particular order. A Python set is similar to this mathematical
definition with below additional conditions:
The elements in the set cannot be duplicates.
The elements in the set are immutable but the set as a whole is mutable.
There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.
"""

# Creating a set
# A set is created by using the set() function or placing all the elements within a pair of curly braces.


days = {'mon', 'tue', 'wed', 'thur', 'fri', 'sat'}

print(days)

# Adding Items to a Set
# We can add elements to a set by using add() method.
days.add('sun')

print(days)

# Removing Item from a Set
# We can remove elements from a set by using discard() method.
days.discard('mon')

print(days)

# Union of Sets
# The union operation on two sets produces a new set containing all the distinct elements from both the sets.

hello = {'hello'}
world = {'world'}

hello_world = hello | world

print(hello_world)

# Intersection of Sets
# The intersection operation on two sets produces a new set containing only the common elements from both the sets.

days_a = {'mon', 'tue', 'wed'}
days_b = {'wed', 'thur', 'fri'}
common_day = days_a & days_b

print(common_day)

# Difference of Sets
# The difference operation on two sets produces a new set containing only the elements from the first set and none
# from the second set.
days_a = {'mon', 'tue', 'wed'}
days_b = {'wed', 'thur', 'fri'}
uncommon_day = days_a - days_b

print(uncommon_day)

# Compare Sets
# We can check if a given set is a subset or superset of another set. The result is True or False depending on the
# elements present in the sets.

days_a = {'mon', 'tue', 'wed'}
days_b = {'mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun'}

days_a_subset_b = days_a <= days_b
days_b_superset_b = days_b >= days_a

print(days_a_subset_b)
print(days_b_superset_b)
