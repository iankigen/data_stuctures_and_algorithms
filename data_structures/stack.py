"""
stack data strcuture allows operations at one end wich can be called top of the stack.
In a stack the element inserted last in sequence will come out first as we can remove only from the top of the stack.
Such feature is known as Last in First Out(LIFO) feature. The operations of adding and removing the elements is known
as PUSH and POP
"""


class Stack(object):
    def __init__(self):
        self.stack = []

    def push_data(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        return False

    def pop_data(self):
        return self.stack.pop() if len(self.stack) else False

    def peek(self):
        """
        :return: dataval on top of stack
        """
        return self.stack[0] if len(self.stack) else False

    def all(self):
        return self.stack


new_stack = Stack()
print(new_stack.push_data('Mon'))
print(new_stack.push_data('Tue'))
print(new_stack.peek())
print(new_stack.pop_data())
print(new_stack.all())
