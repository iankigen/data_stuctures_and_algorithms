test_list = [1, 2, 'a', 'b', 'john', 'doe']

# Updating Lists

test_list[1] = 100

# Append Lists

test_list.append('python')

# Delete List Elements
# use the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know.

del test_list[1]
test_list.remove('python')

# Concatenation

new_list = [1, 2, 3] + [4, 5, 6]

# Repetition

repeat = ["Hello"] * 3


# Membership

exist = 1 in test_list


print(repeat)
print(test_list)
