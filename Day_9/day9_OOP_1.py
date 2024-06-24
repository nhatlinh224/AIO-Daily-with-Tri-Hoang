import math
from sympy import sqrt


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance_to_origin(self):
        return sqrt(self.__x**2 + self.__y**2)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


# Creating two point objects
point_a = Point(1, 2)
point_b = Point(4, 5)

# Calculating the distance of each point from the origin
distance_a = point_a.distance_to_origin()
distance_b = point_b.distance_to_origin()

print(f"d(A, O) = {distance_a} và d(B, O) = {distance_b}")
