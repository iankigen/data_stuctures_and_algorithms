"""
Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is
sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a
merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed.
Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.

Time Complexity Of Merge Sort
Best Case	O(n log n)
Average Case	O(n log n)
Worst Case	O(n log n)
"""


def merge_sort(sort_list):
    print("Splitting ", sort_list)
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sort_list[k] = left_half[i]
                i += 1
            else:
                sort_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            sort_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            sort_list[k] = right_half[j]
            j += 1
            k += 1

    print("Merging ", sort_list)
    return sort_list


lst = [21, 19, 68, 1, 21, 37, 7, 5]
print(merge_sort(lst))
