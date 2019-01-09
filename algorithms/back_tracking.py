"""
Backtracking is a form of recursion. But it involves choosing only option out of any possibilities. We begin by choosing
an option and backtrack from it, if we reach a state where we conclude that this specific option does not give the
required solution. We repeat these steps by going across each available option until we get the desired solution.

Example of finding all possible order of arrangements of a given set of letters. When we choose a pair we apply
to verify if that exact pair has already been created or not. If not already created, the pair is added to the answer
list else it is ignored.
"""


def permute(no_of_combination, data_list):
    if no_of_combination == 1:
        return data_list
    else:
        return [
            y + x for y in permute(1, data_list) for x in permute(no_of_combination - 1, data_list)
        ]


print(permute(1, ['a', 'b']))
print(permute(2, ['a', 'b']))
print(permute(3, ['a', 'b']))
