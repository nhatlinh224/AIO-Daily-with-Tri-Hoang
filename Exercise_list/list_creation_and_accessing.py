# Task: Create a list and access elements using index

# Step 1: Create a list with numbers from 1 to 10
lst_data = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2: Print the first 5 elements of the list
first_5_elements = lst_data[:5]
print("Câu 2:", first_5_elements)  # Expected output: [1, 2, 3, 4, 5]

# Step 3: Print elements that have values not divisible by 2
not_divisible_by_2 = [x for x in lst_data if x % 2 != 0]
print("Câu 3:", not_divisible_by_2)  # Expected output: [1, 3, 5, 7, 9]

# Step 4: Print the sum of all elements in the list
sum_of_elements = sum(lst_data)
print("Câu 4:", sum_of_elements)  # Expected output: 55
