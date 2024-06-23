import math

# Define the vectors
vector_a = [1, 2]
vector_b = [4, 5]

# Function to compute the dot product of two vectors


def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))

# Function to compute the magnitude (length) of a vector


def magnitude(vec):
    return math.sqrt(sum(x ** 2 for x in vec))


# Compute the dot product of vector_a and vector_b
dot_prod = dot_product(vector_a, vector_b)

# Compute the magnitudes of vector_a and vector_b
magnitude_a = magnitude(vector_a)
magnitude_b = magnitude(vector_b)

# Compute the Cosine Similarity
cosine_similarity = dot_prod / (magnitude_a * magnitude_b)

# Print the result
print("Cosine Similarity:", cosine_similarity)
