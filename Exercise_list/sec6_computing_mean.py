# Step 1: Create a list of numbers from 1 to 10
lst_data = list(range(1, 11))
print("Câu 1:", lst_data)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2: Calculate the mean of the list


def calculate_mean(data):
    return sum(data) / len(data)


mean_value = calculate_mean(lst_data)
print("Câu 2: Mean =", mean_value)  # Expected output: 5.5

# Step 3: Calculate the median of the list


def calculate_median(data):
    data_sorted = sorted(data)
    n = len(data_sorted)
    mid = n // 2

    if n % 2 == 0:  # Even number of elements
        median = (data_sorted[mid - 1] + data_sorted[mid]) / 2
    else:  # Odd number of elements
        median = data_sorted[mid]

    return median


median_value = calculate_median(lst_data)
# Expected output: Mean = 5.5, Median = 5.5
print("Câu 3: Mean =", mean_value, "Median =", median_value)
