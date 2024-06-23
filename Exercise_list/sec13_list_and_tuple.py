import math

# Create tuples
my_tuple1 = (2, 3)
my_tuple2 = (3, 6)

# Question 2: Calculate sum and product of vectors
result_vector1 = tuple(x + y for x, y in zip(my_tuple1, my_tuple2))
result_vector2 = tuple(x * y for x, y in zip(my_tuple1, my_tuple2))
print("Câu 2: Result_vector1=", result_vector1,
      ", Result_vector2=", result_vector2)

# Question 3: Calculate distance between vectors
distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(my_tuple1, my_tuple2)))
print("Câu 3:", distance)

# Question 4: Find index of element 3
index1 = my_tuple1.index(3)
index2 = my_tuple2.index(3)
print("Câu 4: index=(", index1, ",", index2, ")")
