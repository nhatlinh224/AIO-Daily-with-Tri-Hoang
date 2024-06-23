# Step 1: Define the list
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

# Step 2: Function to perform Nearest Neighbor interpolation


def nearest_neighbor_interpolation(data):
    # Iterate through the list to find None values
    for i in range(len(data)):
        if data[i] is None:
            # Find the nearest non-None value
            left = i - 1
            right = i + 1

            while left >= 0 and data[left] is None:
                left -= 1
            while right < len(data) and data[right] is None:
                right += 1

            # Determine which non-None value is closer
            if left >= 0 and (right >= len(data) or (i - left) <= (right - i)):
                data[i] = data[left]
            elif right < len(data):
                data[i] = data[right]

    return data


# Step 3: Apply the interpolation function to the list
interpolated_data = nearest_neighbor_interpolation(lst_data.copy())
# Expected output: [1, 1.1, 1.1, 1.4, 1.4, 1.5, 1.5, 2.0]
print("Interpolated Data:", interpolated_data)

# Final Output
print("Original Data:", lst_data)
print("Interpolated Data:", interpolated_data)
