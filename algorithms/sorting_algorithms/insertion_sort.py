"""
Insertion Sort is an in-place sorting algorithm. Here a sub-list is maintained which always sorted, as the iterations go
on, the sorted sub-list grows until all the elements are sorted. In each iteration, an element in the main
list(unsorted list) is picked and placed correctly in the sorted list by shifting elements to the right which are
greater than the element picked from the unsorted sub-list.

Time Complexity Of Insertion Sort
Best Case	O(n2)
Average Case	O(n)
Worst Case	O(n2)
"""


def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j = j - 1
        sort_list[j + 1] = key
    return sort_list


lst = [2, 9, 8, 5, 1, 3]
print(insertion_sort(lst))
