# Define the text corpus
text_corpus = "Tôi thích AI thích Toán"

# Tokenize the text into words
tokens = text_corpus.split()  # Tokenization by splitting the text by spaces
# Expected output: ['Tôi', 'thích', 'AI', 'thích', 'Toán']
print("Tokens:", tokens)

# Define the vocabulary list (as per the expected output)
vocabulary = ['AI', 'Toán', 'Tôi', 'môn', 'nhạc', 'thích', 'âm']

# Create a Bag-of-Words model
# Initialize a frequency vector with 0s
bow_vector = [0] * len(vocabulary)

# Populate the frequency vector based on the presence of words
for token in tokens:
    if token in vocabulary:
        index = vocabulary.index(token)
        bow_vector[index] += 1

# Expected output: [1, 1, 1, 0, 0, 2, 0]
print("Bag-of-Words Vector:", bow_vector)

# Display the tokenization and Bag-of-Words results
tokenization_output = tokens
bow_output = bow_vector

# Expected output: ['Tôi', 'thích', 'AI', 'thích', 'Toán']
print("Tokenization:", tokenization_output)
print("Bag-of-Words:", bow_output)  # Expected output: [1, 1, 1, 0, 0, 2, 0]
# Expected output: ['AI', 'Toán', 'Tôi', 'môn', 'nhạc', 'thích', 'âm']
print("Vocabulary:", vocabulary)
