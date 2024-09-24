import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = [6] * self.sides_count
        self.filled = False
        self.set_sides(*sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides) if self.sides_count != 1 else self.__sides[0]

    def get_perimeter(self):
        return len(self)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)

    def set_sides(self, circumference):
        if isinstance(circumference, (int, float)) and circumference > 0:
            super().set_sides(circumference)
            self.__radius = circumference / (2 * math.pi)

    def get_sides(self):
        return [super().get_sides()[0]]

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def set_sides(self, a, b, c):
        if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and a > 0 and b > 0 and c > 0:
            super().set_sides(a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color, *[edge_length] * 12)

    def set_sides(self, *edges):
        if len(edges) == 1 and isinstance(edges[0], (int, float)) and edges[0] > 0:
            super().set_sides(*[edges[0]] * 12)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 15)
    cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())

    circle1.set_sides(15)
    print(circle1.get_sides())
    print(len(circle1))  # 15
    print(cube1.get_volume())