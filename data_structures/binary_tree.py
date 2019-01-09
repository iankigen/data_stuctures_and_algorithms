"""
Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties.
- One node is marked as Root node.
- Every node other than the root is associated with one parent node.
- Each node can have an arbiatry number of chid node.


"""


class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Tree(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Tree(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


root = Tree(12)
root.insert(3)
root.insert(14)
root.insert(9)
root.print_tree()
