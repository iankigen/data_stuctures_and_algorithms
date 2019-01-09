"""
Traversal is a process to visit all the nodes of a tree and may print their values too. Because, all nodes are connected
via links we always start from the root node.

There are three ways which we use to traverse a tree −

- In-order Traversal
- Pre-order Traversal
- Post-order Traversal
"""


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if not self.data:
            self.data = data
        else:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, root):
        # In-order Traversal
        # In this traversal method, the left subtree is visited first, then the root and later the right sub-tree.
        # Left -> Root -> Right
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res

    def pre_order_traversal(self, root):
        # Pre-order Traversal
        # In this traversal method, the root node is visited first, then the left subtree and finally the right subtree.
        # Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        # Post-order Traversal
        # In this traversal method, the root node is visited last, hence the name. First we traverse the left subtree,
        #  then the right subtree and finally the root node.
        # Left ->Right -> Root
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res


tree = Node(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)

tree.print_tree()
print(tree.inorder_traversal(tree))
print(tree.pre_order_traversal(tree))
print(tree.post_order_traversal(tree))
