"""
In Linear search, we search an element or value in a given array by traversing the array from the starting, till the
desired element or value is found.
"""

data = [2, 7, 19, 34, 53, 72]


def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return True
    return False


print(linear_search(data, 72))
print(linear_search(data, 172))
