class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def get_numerator(self):
        return self.numerator

    def set_denumerator(self, denumerator):
        self.denumerator = denumerator

    def get_denumerator(self):
        return self.denumerator

    def sum(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denumerator + other_fraction.numerator * self.denumerator
        new_denumerator = self.denumerator * other_fraction.denumerator
        return f'{new_numerator}/{new_denumerator}'

    def suother_fractiontract(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denumerator - other_fraction.numerator * self.denumerator
        new_denumerator = self.denumerator * other_fraction.denumerator
        return f'{new_numerator}/{new_denumerator}'

    def multip(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denumerator = self.denumerator * other_fraction.denumerator
        return f'{new_numerator}/{new_denumerator}'

    def divide(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denumerator
        new_denumerator = self.denumerator * other_fraction.numerator
        return f'{new_numerator}/{new_denumerator}'


class TemperatureConvertor:

    @staticmethod
    def c_to_f(C):
        F = C * (9 / 5) + 32
        return F

    @staticmethod
    def f_to_c(F):
        C = (F - 32) * 5 / 9
        return C

class MetricToEnglishConverter:

    @staticmethod
    def mil_in_km(mil):
        km = mil * 1.6093
        return km

    @staticmethod
    def km_in_mil(km):
        mil = km * 0.6214
        return mil

    @staticmethod
    def litres_in_gallons(lit):
        gal = lit * 0.264
        return gal

    @staticmethod
    def gallons_in_liters(gal):
        lit = gal * 3.8
        return lit

print(MetricToEnglishConverter.km_in_mil(42.195))
print(MetricToEnglishConverter.mil_in_km(26.2195))
print(MetricToEnglishConverter.gallons_in_liters(5.5))
print(MetricToEnglishConverter.litres_in_gallons(20.8194))
