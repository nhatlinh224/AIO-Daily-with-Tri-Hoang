# Step 1: Define a function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to easily iterate over digits
    num_str = str(number)
    # Get the number of digits
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number


# Step 2: Given list of numbers
test_list = [153, 270, 153, 407, 177, 9474, 10000, 1634, 370]

# Step 3: Iterate through the list and collect Armstrong numbers
results = []
for num in test_list:
    if is_armstrong(num):
        results.append(num)

# Step 4: Print the result
# Expected output: [153, 407, 1634, 370]
print("Các số Armstrong có trong list là:", results)
