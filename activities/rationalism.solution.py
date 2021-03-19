class Fraction:

    def initialize(self, n, d):
        self.numer = n
        self.denom = d

    def numerator(self):
        return self.numer

    def denominator(self):
        return self.denom

    def multiply_by(self, other_frac):
        self.numer = self.numerator() * other_frac.numerator()
        self.denom = self.denominator() * other_frac.denominator()
