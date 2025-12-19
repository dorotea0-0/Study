import math

class Figure3D:
    def __init__(self, name):
        self.name = name

    def surface_area(self):
        raise NotImplementedError("Метод surface_area должен быть реализован в подклассе")

    def volume(self):
        raise NotImplementedError("Метод volume должен быть реализован в подклассе")


class Cube(Figure3D):
    def __init__(self, side):
        super().__init__("Куб")
        self.side = side

    def surface_area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3


class Sphere(Figure3D):
    def __init__(self, radius):
        super().__init__("Сфера")
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3


class Cylinder(Figure3D):
    def __init__(self, radius, height):
        super().__init__("Цилиндр")
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


class Parallelepiped(Figure3D):
    def __init__(self, a, b, c):
        super().__init__("Параллелепипед")
        self.a = a
        self.b = b
        self.c = c

    def surface_area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.c * self.a)

    def volume(self):
        return self.a * self.b * self.c


class Ellipsoid(Figure3D):
    def __init__(self, a, b, c):
        super().__init__("Эллипсоид")
        self.a = a
        self.b = b
        self.c = c

    def surface_area(self):
        # Приближенная формула для площади поверхности эллипсоида
        p = 1.6075
        term1 = (self.a * self.b) ** p
        term2 = (self.b * self.c) ** p
        term3 = (self.c * self.a) ** p
        return 4 * math.pi * ((term1 + term2 + term3) / 3) ** (1/p)

    def volume(self):
        return (4/3) * math.pi * self.a * self.b * self.c


def find_largest_volume(figures):
    if not figures:
        return

    total_volume = sum(f.volume() for f in figures)
    largest_figures = []

    for fig in figures:
        if fig.volume() >= total_volume - fig.volume():
            largest_figures.append(fig)

    if largest_figures:
        print("Фигуры, объем которых равен или больше суммарного объема остальных:")
        for fig in largest_figures:
            print(f"  {fig.name}: объем = {fig.volume():.2f}")
    else:
        print("Нет фигур, удовлетворяющих условию.")


# Пример использования
if __name__ == "__main__":
    figures = [
        Cube(3),
        Sphere(2),
        Cylinder(2, 4),
        Parallelepiped(2, 3, 4),
        Ellipsoid(2, 3, 4)
    ]

    print("=== Площади поверхностей и объемы ===")
    for fig in figures:
        print(f"{fig.name}:")
        print(f"  Площадь поверхности: {fig.surface_area():.2f}")
        print(f"  Объем: {fig.volume():.2f}")
        print()

    print("=== Поиск фигуры с наибольшим объемом ===")
    find_largest_volume(figures)