"""
Sorting refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a
particular order.
"""

# Bubble Sort

"""
It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if
they are not in order.
Time Complexity of Bubble Sort
Best Case: O(n)

Average Case: O(n2)

Worst Case: O(n2)
"""


def bubble_sort(data_list):
    for n in range(len(data_list)):
        for i in range(len(data_list) - 1):
            if data_list[i] > data_list[i + 1]:
                data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]
    return data_list


data_list = [19, 2, 31, 45, 6, 11, 121, 27]
print(bubble_sort(data_list))
