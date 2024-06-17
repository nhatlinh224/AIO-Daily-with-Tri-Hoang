# Hàm tính tích chập (convolution) cho ma trận
def convolution_2d(matrix, kernel):
    m, n = len(matrix), len(matrix[0])
    km, kn = len(kernel), len(kernel[0])
    output = []

    for i in range(m - km + 1):
        row = []
        for j in range(n - kn + 1):
            sum = 0
            for ki in range(km):
                for kj in range(kn):
                    sum += matrix[i + ki][j + kj] * kernel[ki][kj]
            row.append(sum)
        output.append(row)
    return output


# Ma trận đầu vào A
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Kernel B
kernel_b = [
    [2, 4],
    [4, 3]
]

# Kernel C
kernel_c = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Tính toán Convolutional cho câu A
result_a = convolution_2d(matrix_a, kernel_b)
print("Câu A: Kết quả tích chập của A và Kernel B:")
for row in result_a:
    print(row)

# Tính toán Convolutional cho câu B
result_b = convolution_2d(matrix_a, kernel_c)
print("Câu B: Kết quả tích chập của A và Kernel C:")
for row in result_b:
    print(row)
