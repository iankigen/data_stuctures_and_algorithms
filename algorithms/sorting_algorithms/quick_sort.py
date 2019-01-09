"""
Quick sort is an in-place sorting algorithm, which means it does not require any extra/temporary list to perform sorting,
everything will be done on the original list itself. Here in this sorting technique we will select a pivot element and
arrange all the items to the right are greater than pivot and elements to the left are lesser than the pivot. Again we
do the same step for the left and right elements of the pivot as sublists until all the elements are sorted.

Time Complexity Of QuickSort
Best Case	O(n log n)
Average Case	O(n log n)
Worst Case	O(n2)
"""


def quick_sort(sort_list):
    less = []
    equal = []
    greater = []

    if sort_list:
        pivot = sort_list[0]

        for x in sort_list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return sort_list


data_list = [109, 109, 19, 2, 31, 45, 6, 11, 121, 27]
print(quick_sort(data_list))
