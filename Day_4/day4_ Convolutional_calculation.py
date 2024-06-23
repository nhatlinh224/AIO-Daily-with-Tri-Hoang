# Ma trận A và Kernel B
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 4],
     [1, 3]]

# Hàm thực hiện phép chập


def convolve(matrix, kernel):
    kernel_size = len(kernel)
    output_rows = len(matrix) - kernel_size + 1
    output_cols = len(matrix[0]) - kernel_size + 1
    output = []
    for i in range(output_rows):
        new_row = []
        for j in range(output_cols):
            sum_value = 0
            for m in range(kernel_size):
                for n in range(kernel_size):
                    sum_value += matrix[i + m][j + n] * kernel[m][n]
            new_row.append(sum_value)
        output.append(new_row)
    return output


# Thực hiện phép chập
result = convolve(A, B)

# In kết quả
print("Kết quả sau khi chập với Kernel B:")
for row in result:
    print(row)

# Kernel C
C = [[1, 1, 1],
     [0, 0, 0],
     [1, 1, 1]]

# Thực hiện phép chập
result_2 = convolve(A, C)

# In kết quả
print("Kết quả sau khi chập với Kernel C:")
for row in result_2:
    print(row)
