class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.breadth + other.breadth)

    def __str__(self):
        return f"Length is {self.length} and Breadth is {self.breadth}"

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth

    def __lt__(self, other):
        return self.length * self.breadth < other.length * other.breadth

    def __gt__(self, other):
        return self.length * self.breadth > other.length * other.breadth

    def __ge__(self, other):
        return self.length * self.breadth >= other.length * other.breadth

    def __le__(self, other):
        return self.length * self.breadth <= other.length * other.breadth

r1 = Rectangle(length=20, breadth=10)
r2 = Rectangle(length=10, breadth=5)

r3 = r1 + r2

print(r3)

print(f"r1 == r2: {r1 == r2}")
print(f"r1 < r2: {r1 < r2}")
print(f"r1 > r2: {r1 > r2}")
print(f"r1 >= r2: {r1 >= r2}")
print(f"r1 <= r2: {r1 <= r2}")
