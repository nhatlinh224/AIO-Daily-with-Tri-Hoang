def find_squared_root(a):
    """
    Tìm căn bậc hai của số a bằng phương pháp Newton-Raphson
    """
    # Giá trị gần đúng ban đầu
    x_n = a
    epsilon = 0.001

    while True:
        # Tính giá trị x tiếp theo
        x_next = 0.5 * (x_n + a / x_n)

        # Kiểm tra điều kiện hội tụ
        if abs(x_next - x_n) < epsilon:
            return x_next

        # Cập nhật giá trị x_n
        x_n = x_next


# Test case 1: Tìm căn bậc hai của 2
result_1 = find_squared_root(2)
print(f"Test case 1: find_squared_root(2) = {result_1}")

# Test case 2: Tìm căn bậc hai của 3
result_2 = find_squared_root(3)
print(f"Test case 2: find_squared_root(3) = {result_2}")
