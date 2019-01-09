"""
A linked list is a sequence of data elements, which are connected together via links. Each data element contains a
connection to another data element in form of a pointer. Python does not have linked lists in its standard library.
We implement the concept of linked lists using the concept of nodes
"""


# Creation of Linked list
class Node(object):
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList(object):
    def __init__(self):
        self.headval = None

    def print_list(self):
        val = self.headval
        while val:
            print(val.dataval)
            val = val.nextval

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.nextval = self.headval
        self.headval = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.headval:
            self.headval = new_node
            return
        headval = self.headval
        while headval.nextval:
            headval = headval.nextval
        headval.nextval = new_node

    def add(self, val, data):
        if not val:
            raise Exception('value does not exist')
        new_node = Node(data)
        nextval = val.nextval
        val.nextval = new_node
        new_node.nextval = nextval

    def remove(self, data):
        headval = self.headval
        if headval:
            if headval.dataval == data:
                self.headval = headval.nextval
                headval = None

            while headval:
                prev = headval
                headval = headval.nextval
                if headval.dataval == data:
                    prev.nextval = headval.nextval
                    return



val1, val2, val3 = Node('mon'), Node('tue'), Node('wed')
list1 = LinkedList()
list1.headval = val1
# Link first Node to second node
list1.headval.nextval = val2
# Link second Node to third node
val2.nextval = val3

# Traversing a Linked List
# Singly linked lists can be traversed in only forwrad direction starting form the first data element. We simply print
# the value of the next data element by assgining the pointer of the next node to the current data element.
list1.print_list()

# Insertion in a Linked List
# Inserting element in the linked list involves reassigning the pointers from the existing nodes to the newly inserted
# node. Depending on whether the new data element is getting inserted at the beginning or at the middle or at the end of
# the linked list,

# Inserting at the Beginning of the Linked List
# This involves pointing the next pointer of the new data node to the current head of the linked list. So the current
# head of the linked list becomes the second data element and the new node becomes the head of the linked list.
list1.add_beginning('sun')
print('-' * 10)
list1.print_list()

# Inserting at the End of the Linked List
# This involves pointing the next pointer of the the current last node of the linked list to the new data node.
# So the current last node of the linked list becomes the second last data node and the new node becomes the last
# node of the linked list.

list1.append('thur')
print('-' * 10)
list1.print_list()

# Inserting in between two Data Nodes
# This involves chaging the pointer of a specific node to point to the new node. That is possible by passing in both the
# new node and the existing node after which the new node will be inserted.

list1.add(list1.headval, 'fri')
print('-' * 10)
list1.print_list()

# Removing an Item form a Liked List
# We can remove an existing node using the key for that node.
list1.remove('thur')
print('-' * 10)
list1.print_list()


