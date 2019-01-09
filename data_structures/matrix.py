"""
Matrix is a special case of two dimensional array where each data element is of strictly same size. So every matrix is
also a two dimensional array but not vice versa
"""
from numpy import append, insert, delete, reshape

# axis = 0 for a row, 1 for a column

# temprature for 1 week measured in the morning, mid-day, evening and mid-night.
week_temp = [
    ['Mon', 18, 20, 22, 17],
    ['Tue', 11, 18, 21, 18],
    ['Wed', 15, 21, 20, 19],
    ['Thu', 11, 20, 22, 21],
    ['Fri', 18, 17, 23, 22],
    ['Sat', 12, 22, 20, 18],
    ['Sun', 13, 15, 19, 16]
]
m = reshape(week_temp, (7, 5))
print(m)

# Accessing Values in a Matrix

# Print data for Wednesday
print(m[2])

# Print data for friday evening
print(m[4][3])

# Adding a row
# We can add column to a matrix using the insert() method. here we have to mention the index where we want to add the
#  column and a array containing the new values of the columns added.
week_temp_with_avg = append(m, [['Avg', 12, 15, 13, 11]], 0)
print(week_temp_with_avg)

week_temp_with_col = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
print(week_temp_with_col)

# Delete a row from a Matrix
# We can delete a row from a matrix using the delete() method. We have to specify the index of the row and also the
#  axis value which is 0 for a row and 1 for a column.
week_temp_delete_row = delete(m, [2], 0)

print(week_temp_delete_row)

# Delete a column from a Matrix
week_temp_delete_col = delete(m, [2], 1)

print(week_temp_delete_col)

# Update a row in in a Matrix
m[3] = ['Thu', 10, 10, 10, 10]
print(m)
