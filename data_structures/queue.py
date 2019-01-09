"""
queue data structure: data elements are arranged in a queue
queue can be implemented using python list where we can use the insert() and pop() methods to add and remove elements.
Their is no insertion as data elements are always added at the end of the queue.
"""


class Queue(object):
    def __init__(self):
        self.queue = list()

    def insert_data(self, datavalue):
        if datavalue not in self.queue:
            self.queue.insert(0, datavalue)
            return True
        return False

    def size(self):
        return len(self.queue)

    def pop_data(self):
        return self.queue.pop() if self.queue else False

    def all(self):
        return self.queue

new_queue = Queue()
print(new_queue.insert_data('Mon'))
print(new_queue.insert_data('Tue'))
print(new_queue.insert_data('Tue'))
print(new_queue.insert_data('Wed'))
print(new_queue.size())
print(new_queue.all())
print(new_queue.pop_data())
print(new_queue.all())
