import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    a = Vector2D(3, 4)
    b = Vector2D(1, -2)

    print("Вектор a:", a)
    print("Длина a:", a.length())
    print("Угол a (в радианах):", a.angle())
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("Скалярное произведение a·b =", a.dot_product(b))