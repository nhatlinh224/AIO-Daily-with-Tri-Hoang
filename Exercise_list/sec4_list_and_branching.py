# Function to determine if each person can have the most candies after receiving extra candies
def kids_with_candies(candies, extra_candies):
    # Calculate the current maximum number of candies any person has
    max_candies = max(candies)

    # Initialize an empty list to store the result
    result = []

    # Iterate through the list of candies
    for candy in candies:
        # Check if the current person can have the most candies after receiving extra candies
        if candy + extra_candies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    return result


# Test case
test_candies = [2, 3, 5, 1, 3]
extra_candies = 3

# Get the result
result = kids_with_candies(test_candies, extra_candies)

# Print the result
print(result)  # Expected output: [True, True, True, False, True]
