# 1/3 + 2/3
class CorrectFraction:
    numerator = None
    denominator = None

    def get_float(self):
        return self.numerator / self.denominator

    def __init__(self, numerator, denominator):
        if numerator > denominator:
            raise ValueError('Numerator can not be grant than denominator')
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other_fraction):
        return self.get_float() + other_fraction.get_float()

    def __mul__(self, other_fraction):
        return self.get_float() * other_fraction.get_float()

    def __sub__(self, other_fraction):
        return self.get_float() - other_fraction.get_float()

    def __eq__(self, o) -> bool:
        return self.get_float() == o.get_float()

    def __ne__(self, o) -> bool:
        return self.get_float() != o.get_float()

    def __lt__(self, o: object) -> bool:
        return self.get_float() < o.get_float()

    def __ge__(self, o: object) -> bool:
        return self.get_float() >= o.get_float()

    def __gt__(self, o: object) -> bool:
        return self.get_float() > o.get_float()

    def __le__(self, o: object) -> bool:
        return self.get_float() <= o.get_float()

if __name__ == '__main__':
    fraction1 = CorrectFraction(1, 2) # 3/6
    fraction2 = CorrectFraction(2, 3) # 4/6 -> 7/6 1, 1/6
    print(fraction1 + fraction2)

