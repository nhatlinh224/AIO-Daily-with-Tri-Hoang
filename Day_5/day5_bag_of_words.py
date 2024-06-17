# Bước 1: Tạo corpus
corpus = [
    "Tôi thích môn Toán",
    "Tôi thích AI",
    "Tôi thích âm nhạc"
]

# Bước 2: Tokenization


def tokenize(sentence):
    return sentence.split()


# Tạo từ vựng (vocabulary) từ corpus
vocabulary = set()
for document in corpus:
    words = tokenize(document)
    vocabulary.update(words)
vocabulary = sorted(vocabulary)

# Tạo dictionary để mapping từ vựng với chỉ số
vocab_dict = {word: idx for idx, word in enumerate(vocabulary)}

# Bước 3: Biểu diễn văn bản dưới dạng BoW


def vectorize(sentence):
    words = tokenize(sentence)
    vector = [0] * len(vocabulary)
    for word in words:
        if word in vocab_dict:
            index = vocab_dict[word]
            vector[index] += 1
    return vector


# Ví dụ sử dụng:
sentence = "Tôi thích AI thích Toán"
bow_vector = vectorize(sentence)

print("Vocabulary:", vocabulary)
print("BoW Vector:", bow_vector)
