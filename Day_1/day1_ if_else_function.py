def calculate_can_chi_calendar(year):
    # Tạo danh sách các Can và Chi
    can_list = ['Canh', 'Tân', 'Nhâm', 'Quý',
                'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    chi_list = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý',
                'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

    # Tính Can và Chi dựa vào phần dư
    can = can_list[year % 10]
    chi = chi_list[year % 12]

    # Kết quả
    result = f"{can} {chi}"
    return result


# Ví dụ:
print(calculate_can_chi_calendar(2024))  # Output: Giáp Thìn
print(calculate_can_chi_calendar(2023))  # Output: Quý Mão
print(calculate_can_chi_calendar(1997))  # Output: Đinh Sửu
