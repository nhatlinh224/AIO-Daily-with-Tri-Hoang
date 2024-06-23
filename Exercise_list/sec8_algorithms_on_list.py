# Step 1: Define the list
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

# Step 2: Find the indices of None values
none_indices = []
for index, value in enumerate(lst_data):
    if value is None:
        none_indices.append(index)
print("Vị trí None đầu tiên:", none_indices)  # Expected output: [2, 4, 6]

# Step 3: Create a new list excluding None values
filtered_list = [value for value in lst_data if value is not None]
# Expected output: [1, 1.1, 1.4, 1.5, 2.0]
print("Danh sách sau khi bỏ các giá trị None:", filtered_list)

# Final Output
print("Vị trí None đầu tiên:", none_indices)
print("Danh sách sau khi bỏ các giá trị None:", filtered_list)
