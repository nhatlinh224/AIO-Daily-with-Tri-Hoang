# Step 1: Create a list containing all even numbers from 1 to 12
lst_data = []
for i in range(1, 13):
    if i % 2 == 0:
        lst_data.append(i)
print("Câu 1:", lst_data)  # Expected output: [2, 4, 6, 8, 10, 12]

# Step 2: Remove all elements divisible by 3 from the list
new_lst_data = []
for x in lst_data:
    if x % 3 != 0:
        new_lst_data.append(x)
lst_data = new_lst_data
print("Câu 2:", lst_data)  # Expected output: [2, 4, 8, 10]

# Step 3: Add elements [0, 1, 2, 3] at the end of the list and insert the string 'a' at index 3
lst_data.extend([0, 1, 2, 3])  # Add elements to the end
lst_data.insert(3, 'a')  # Insert 'a' at index 3
print("Câu 3:", lst_data)  # Expected output: [2, 4, 8, 'a', 10, 0, 1, 2, 3]

# Step 4: Update the last 5 elements to 0 if the list contains numbers divisible by 2 or 3
contains_divisible_by_2_or_3 = False
for x in lst_data:
    if isinstance(x, int) and (x % 2 == 0 or x % 3 == 0):
        contains_divisible_by_2_or_3 = True
        break

if contains_divisible_by_2_or_3:
    for i in range(1, 6):
        lst_data[-i] = 0  # Update the last 5 elements to 0
print("Câu 4:", lst_data)  # Expected output: [2, 4, 8, 'a', 10, 0, 0, 0, 0, 0]
