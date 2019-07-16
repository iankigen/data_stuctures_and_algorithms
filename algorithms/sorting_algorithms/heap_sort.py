"""
Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort
where we first find the maximum element and place the maximum element at the end. We repeat the same process for
remaining element.

A Binary Heap:  is a Complete Binary Tree where items are stored in a special order such that value in a parent node is
greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter is
 called min heap. The heap can be represented by binary tree or array.

Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based representation
is space efficient. If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right
child by 2 * I + 2 (assuming the indexing starts at 0).

overall time complexity of the Heap Sort algorithm is O(nlog(n)).


"""


def heapify(array, heap_size, root_index):
	# Assume the index of the largest element is the root index
	largest = root_index
	left_child = (2 * root_index) + 1
	right_child = (2 * root_index) + 2

	# If the left/right child of the root is a valid index, and the element is greater than the current largest
	# element then update the largest element
	if left_child < heap_size and array[left_child] > array[largest]:
		largest = left_child

	if right_child < heap_size and array[right_child] > array[largest]:
		largest = right_child

	# if the largest element is nolonger the root element, swap them
	if largest != root_index:
		array[root_index], array[largest] = array[largest], array[root_index]
		# heapify the new root element to ensure its the largest
		heapify(array, heap_size, largest)


def heap_sort(array):
	"""
	create a max heap
	range(n, -1, -1)
	2nd element means: we stop at the element before -1 ie the 1st element of the list
	"""
	n = len(array)
	for i in range(n, -1, -1):
		heapify(array, n, i)

	# move the root of the max heap to the end
	for i in range(n - 1, 0, -1):
		array[i], array[0] = array[0], array[i]
		heapify(array, i, 0)


nums_array = [35, 12, 43, 8, 51]
nums_array2 = [12, 11, 13, 5, 6, 7]
heap_sort(nums_array)
heap_sort(nums_array2)
print(nums_array)
print(nums_array2)
