class Rectangle:
    def __eq__(self, o: object) -> bool:
        return self.get_square() == o.get_square()

    def __ne__(self, o: object) -> bool:
        return self.get_square() != o.get_square()

    def __lt__(self, o: object) -> bool:
        return self.get_square() < o.get_square()

    def __ge__(self, o: object) -> bool:
        return self.get_square() >= o.get_square()

    def __gt__(self, o: object) -> bool:
        return self.get_square() > o.get_square()

    def __le__(self, o: object) -> bool:
        return self.get_square() <= o.get_square()

    def __add__(self, other_rect):
        return self.get_square() + other_rect.get_square()

    def __mul__(self, n: float):
        return self.get_square() * n

    width = None
    height = None

    def get_square(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height


if __name__ == '__main__':
    rect = Rectangle(width=1, height=2)
    rect2 = Rectangle(width=2, height=1)
    print(rect*10)
