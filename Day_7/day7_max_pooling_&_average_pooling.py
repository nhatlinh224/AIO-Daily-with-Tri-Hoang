def max_pooling(matrix):
    """
    Perform max pooling on a given 2D matrix using a 2x2 kernel.

    Parameters:
    matrix (list of list of int): The input 2D matrix to apply max pooling on.

    Returns:
    list of list of int: The max-pooled 2D matrix.
    """
    # Initialize an empty list to store the pooled values
    pooled_matrix = []

    # Iterate over the matrix with a step of 2 to apply the 2x2 kernel
    for i in range(0, len(matrix), 2):
        row = []  # Initialize a new row for the pooled matrix
        for j in range(0, len(matrix[0]), 2):
            # Find the maximum value in the 2x2 block
            max_val = max(matrix[i][j], matrix[i][j+1],
                          matrix[i+1][j], matrix[i+1][j+1])
            row.append(max_val)  # Append the max value to the current row
        # Append the completed row to the pooled matrix
        pooled_matrix.append(row)
    return pooled_matrix  # Return the pooled matrix


# Define the input matrix A
A = [
    [0, 0, 0, 4],
    [0, 4, 0, 2],
    [0, 1, 0, 2],
    [0, 3, 0, 2]
]

# Perform max pooling on matrix A
max_pooled_A = max_pooling(A)
print("Max Pooling Result:", max_pooled_A)


# Task: Average Pooling - Apply a 2x2 kernel to perform average pooling on a 2D matrix without using NumPy

def average_pooling(matrix):
    """
    Perform average pooling on a given 2D matrix using a 2x2 kernel.

    Parameters:
    matrix (list of list of int): The input 2D matrix to apply average pooling on.

    Returns:
    list of list of int: The average-pooled 2D matrix.
    """
    # Initialize an empty list to store the pooled values
    pooled_matrix = []

    # Iterate over the matrix with a step of 2 to apply the 2x2 kernel
    for i in range(0, len(matrix), 2):
        row = []  # Initialize a new row for the pooled matrix
        for j in range(0, len(matrix[0]), 2):
            # Calculate the average value in the 2x2 block
            avg_val = (matrix[i][j] + matrix[i][j+1] +
                       matrix[i+1][j] + matrix[i+1][j+1]) / 4
            row.append(avg_val)  # Append the average value to the current row
        # Append the completed row to the pooled matrix
        pooled_matrix.append(row)
    return pooled_matrix  # Return the pooled matrix


# Perform average pooling on matrix A
average_pooled_A = average_pooling(A)
print("Average Pooling Result:", average_pooled_A)
