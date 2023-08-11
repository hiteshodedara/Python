class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __mod__(self, other):
        return Vector(self.x % other, self.y % other)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Vector objects
v1 = Vector(3, 4)
v2 = Vector(2, 5)

v3 = v1 + v2

v4 = v1 * v2

# Print the results
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v3}")
print(f"v1 * 2: {v4}")
