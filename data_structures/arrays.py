from array import array

# array_name = array(typecode, [Initializers])

"""
Typecode	Value
b	Represents signed integer of size 1 byte/td>
B	Represents unsigned integer of size 1 bytetest_array = array('i', [1, 2, 3])
c	Represents character of size 1 byte
i	Represents signed integer of size 2 bytes# Insertion Operation
I	Represents unsigned integer of size 2 bytes
f	Represents floating point of size 4 bytestest_array.insert(1, 100)
d	Represents floating point of size 8 bytes
"""
test_array = array('i', [1, 2, 3, 10, 20])

# Deletion Operation

test_array.remove(2)

# Update Operation

test_array[1] = 200

# Append Operation

test_array.append(1000)

print(test_array)
