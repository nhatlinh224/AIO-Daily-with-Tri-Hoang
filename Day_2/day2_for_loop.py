import math


def compute_interest(money, period):
    daily_rate = 1 / 365  # Lãi suất hàng ngày
    for _ in range(period):
        money *= (1 + daily_rate)
    return money


# Ví dụ kiểm tra
print(compute_interest(1, 30))   # Test case 1
print(compute_interest(1, 365))  # Test case 2
print(compute_interest(1, 730))  # Test case 3
