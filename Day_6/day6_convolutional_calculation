# Ma trận A và Kernel B
A = [[0, 0, 0],
     [0, 4, 0],
     [0, 1, 0]]

B = [[1, 1],
     [1, 1]]

# Hàm thêm zero padding xung quanh ma trận A


def add_padding(matrix, pad_width):
    rows = len(matrix)
    cols = len(matrix[0])
    padded_matrix = [[0] * (cols + 2 * pad_width)
                     for _ in range(rows + 2 * pad_width)]
    for i in range(rows):
        for j in range(cols):
            padded_matrix[i + pad_width][j + pad_width] = matrix[i][j]
    return padded_matrix

# Hàm thực hiện phép chập


def convolve(matrix, kernel):
    kernel_size = len(kernel)
    output_rows = len(matrix) - kernel_size + 1
    output_cols = len(matrix[0]) - kernel_size + 1
    output = [[0] * output_cols for _ in range(output_rows)]
    for i in range(output_rows):
        for j in range(output_cols):
            for m in range(kernel_size):
                for n in range(kernel_size):
                    output[i][j] += matrix[i + m][j + n] * kernel[m][n]
    return output


# Thêm zero padding xung quanh ma trận A
A_padded = add_padding(A, 1)

# Thực hiện phép chập
result = convolve(A_padded, B)

print("Kết quả sau khi chập với Kernel B và Zero Padding:")
for row in result:
    print(row)
