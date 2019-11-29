class Complex:
    def __init__(self,C,D):
        self.C = C
        self.D = D

    def __add__(self,other):
        plus = self.C + other
        print(plus)

    def __sub__ (self,other):
        minus = self.C - other
        print(minus)

    def __mul__(self,other):
        umnojenie = self.C * other
        print(umnojenie)

    def __div__(self,other):
        delenie = self.C / other
        print(delenie)


complex = Complex(7,3j)
complex.__add__(3j)
complex.__sub__(3j)
complex.__mul__(3)
complex.__div__(3)
