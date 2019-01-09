"""
Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is called
a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap.
"""

# Creating a Heap
"""
A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out 
various operations on heap data structure. Below is a list of these functions.

heapify - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to 
            the index position 0. But rest of the data elements are not necessarily sorted.
heappush – This function adds an element to the heap without altering the current heap.
heappop - This function returns the smallest data element from the heap.
heapreplace – This function replaces the smallest data element with a new value supplied in the function.
"""
import heapq

new_list = [12, 1, 48, 79, 3, 6]

heapq.heapify(new_list)

print(new_list)

# Inserting into heap

"""
Inserting a data element to a heap always adds the element at the last index. But you can apply heapify function again
to bring the newly added element to the first index only if it smallest in value.
"""
heapq.heappush(new_list, 8)
print(new_list)

# Removing from heap

"""
removes the element at first index
"""
heapq.heappop(new_list)
print(new_list)

