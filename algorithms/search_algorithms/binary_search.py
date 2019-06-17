"""
In divide and conquer approach, the problem in hand, is divided into smaller sub-problems and then each problem is
solved independently. When we keep on dividing the sub problems into even smaller sub-problems, we may eventually reach
a stage where no more division is possible. Those "atomic" smallest possible sub-problem (fractions) are solved. The solution of all sub-problems is finally merged in order to obtain the solution of an original problem.
"""

# Binary search

'''
In binary search we take a sorted list of elements and start looking for an element at the middle of the list. If the 
search value matches with the middle value in the list we complete the search. Otherwise we eleminate half of the list 
of elements by choosing whether to procees with the right or left half of the list depending on the value of the item 
searched. This is possible as the list is sorted and it is much quicker than linear search. Here we divide the given 
list and conquer by choosing the proper half of the list. We repeat this approcah till we find the element or conclude 
about it's absence in the list.
'''

data = [2, 7, 19, 34, 53, 72]


def binary_search(data_list, val):
	first = 0
	last = len(data_list) - 1

	while first <= last:
		midpoint = (first + last) // 2

		if val == data_list[midpoint]:
			return True
		else:
			if val < data_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	if first > last:
		return False


print(binary_search(data, 34))
print(binary_search(data, 340))


def binary_search_recursion(sorted_list, value):
	midpoint_index = (len(sorted_list) // 2) - 1
	last_index = len(sorted_list) - 1
	first_index = 0

	if midpoint_index > last_index:
		return False
	if midpoint_index < first_index:
		return False

	if sorted_list[midpoint_index] == value:
		return True
	if sorted_list[midpoint_index] < value:
		return binary_search_recursion(sorted_list[(midpoint_index + 1):], value)
	else:
		return binary_search_recursion(sorted_list[:midpoint_index], value)


print(binary_search_recursion(data, 34))
print(binary_search_recursion(data, 340))
