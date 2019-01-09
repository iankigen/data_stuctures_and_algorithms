"""
A double-ended queue, or deque, has the feature of adding and removing elements from either end.
The Deque module is a part of collections library. It has the methods for adding and removing elements which can be
invoked directly with arguments.
"""
import collections

new_dequeue = collections.deque(['Mon', 'Tue', 'Wed'])
print(new_dequeue)

# Append to the right
new_dequeue.append('Thur')
print('Append to the right -> ', new_dequeue)

# Append to the left
new_dequeue.appendleft('Sun')
print('Append to the left -> ', new_dequeue)

# remove from right
new_dequeue.pop()
print('pop from the right -> ', new_dequeue)

# remove from left
new_dequeue.popleft()
print('pop from the left -> ', new_dequeue)

# reverse deque
new_dequeue.reverse()
print('reverse deque -> ', new_dequeue)
