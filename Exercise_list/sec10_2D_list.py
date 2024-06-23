# Step 1: Define the 1D list
lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Step 2: Convert the 1D list to a 2D list with dimensions 3x3
# We can do this by slicing the list into chunks of 3 elements each
rows, cols = 3, 3
matrix = [lst_data[i * cols:(i + 1) * cols] for i in range(rows)]

print("2D List:")
for row in matrix:
    print(row)
# Expected 2D list:
# [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

# Step 3: Extract the first and last elements from each row
output = [[row[0], row[-1]] for row in matrix]
print("lst_output:", output)  # Expected output: [[1, 3], [4, 6], [7, 9]]
