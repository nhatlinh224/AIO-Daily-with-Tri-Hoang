# Step 1: Define the list of stopwords
stop_words = ["I", "love", "and", "to"]

# Step 2: Define the sentence and split it into words
sentence = "I love AI and listen to music"
words = sentence.split()  # Split sentence into words

# Step 3: Use a for-loop to filter out the stopwords and keep only required words
filtered_words = []
for word in words:
    if word not in stop_words:
        filtered_words.append(word)

# Keep only unique words and order as per the expected output
final_filtered_words = []
for word in filtered_words:
    if word not in final_filtered_words:
        final_filtered_words.append(word)

# Print the result
# Expected output: ['AI', 'listen', 'music']
print("Filtered words:", final_filtered_words)

# Final Output
# Expected output: ['AI', 'listen', 'music']
print("Output:", final_filtered_words)
