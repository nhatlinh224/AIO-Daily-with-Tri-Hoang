# Step 1: Create a list of numbers from 1 to 10
lst_data = list(range(1, 11))
print("Câu 1:", lst_data)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2: Calculate the median of the list


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
print("Câu 2: Median:", median_value)  # Expected output: 5.5

# Step 3: Filter the list to include only odd numbers and sort in descending order
lst_data_odd_descending = sorted(
    [x for x in lst_data if x % 2 != 0], reverse=True)
print("Câu 3:", lst_data_odd_descending)  # Expected output: [9, 7, 5, 3, 1]
