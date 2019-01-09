"""
The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to
do this, a selection sort looks for the largest or smallest value as it makes a pass and, after completing the pass,
places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the
second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the
final item must be in place after the (n−1) st pass.

Time Complexity Of Selection Sort
Best Case	O(n2)
Average Case	O(n2)
Worst Case	O(n2)
"""


def selection_sort(sort_list):
    for i in range(len(sort_list)):
        smallest_element = min(sort_list[i:])
        index_of_smallest = sort_list.index(smallest_element)
        sort_list[i], sort_list[index_of_smallest] = sort_list[index_of_smallest], sort_list[i]
    return sort_list


lst = [1, 32, 43, 54, 4, 6, 5]

print(selection_sort(lst))
