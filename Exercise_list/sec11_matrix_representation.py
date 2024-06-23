# Step 1: Define the matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [2, 4, 6],
    [1, 3, 5],
    [1, 0, 1]
]

# Step 2: Function to add two matrices


def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Step 3: Function to subtract two matrices


def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Step 4: Function to compute the dot product of two matrices


def dot_product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix1[0])):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result


# Calculate A + B
sum_matrix = add_matrices(A, B)

# Calculate A - B
difference_matrix = subtract_matrices(A, B)

# Calculate dot product of A and B
dot_product_matrix = dot_product(A, B)

# Print results
print("Sum (A + B):", sum_matrix)
print("Difference (A - B):", difference_matrix)
print("Dot Product (A * B):", dot_product_matrix)

# Final output format
# Expected output: [[3, 6, 9], [5, 8, 11], [8, 8, 10]]
print("Tổng:", sum_matrix)
# Expected output: [[-1, -2, -3], [3, 2, 1], [6, 8, 8]]
print("Hiệu:", difference_matrix)
# Expected output: [[7, 10, 19], [19, 31, 55], [31, 52, 91]]
print("Dot Product:", dot_product_matrix)
