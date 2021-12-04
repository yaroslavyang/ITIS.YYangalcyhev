#теперь знаю ваши F-строки -_-
#ComplexNumber
from math import atan

class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self, sec):
        thirdC.a = self.a + sec.a
        thirdC.b = self.b + sec.b
        if thirdC.b < 0:
            return f"Sum = {thirdC.a} - {abs(thirdC.b)} * i"
        elif thirdC.b > 0:
            return f"Sum = {thirdC.a} + {thirdC.b} * i"
        else:
            return f"Sum = {thirdC.a}"

    def add2(self, sec):
        self.a += sec.a
        self.b += sec.b

    def sub(self, sec):
        thirdC.a = self.a - sec.a
        thirdC.b = self.b - sec.b
        if thirdC.b < 0:
            return f"Difference = {thirdC.a} - {abs(thirdC.b)} * i"
        elif thirdC.b > 0:
            return f"Difference = {thirdC.a} + {thirdC.b} * i"
        else:
            return f"Difference = {thirdC.a}"

    def sub2(self, sec):
        self.a -= sec.a
        self.b -= sec.b

    def mult_number(self, x):
        thirdC.a = self.a * x
        thirdC.b = self.a * x
        if thirdC.b < 0:
            return f"{x} * vector = {thirdC.a} - {thirdC.b} * i"
        elif thirdC.b > 0:
            return f"{x} * vector = {thirdC.a} + {thirdC.b} * i"
        else:
            return f"{0}"

    def mult_number2(self, x):
        self.a *= x
        self.b *= x

    def mult(self, sec):
        thirdC.a = self.a * sec.a - self.b * sec.b
        thirdC.b = self.a * sec.b + self.b * sec.a
        if thirdC.b < 0:
            return f"Multiplication = {thirdC.a} - {abs(thirdC.b)} * i"
        elif thirdC.b > 0:
            return f"Multiplication = {thirdC.a} + {thirdC.b} * i"
        else:
            return f"Multiplication = {thirdC.a}"

    def mult2(self, sec):
        re = self.a * sec.a - self.b * sec.b
        im = self.a * sec.b + self.b * sec.a
        self.a = re
        self.b = im

    def div(self, sec):
        denom = sec.a**2 + sec.b**2
        numer_re = self.a * sec.a - self.b * -sec.b
        numer_im = self.a * -sec.b + self.b * sec.a
        thirdC.a = numer_re / denom
        thirdC.b = numer_im / denom
        if thirdC.b < 0:
            return f"Quotient = {thirdC.a} - {abs(thirdC.b)}i"
        elif thirdC.b > 0:
            return f"Quotient = {thirdC.a} + {thirdC.b}i"
        else:
            return f"Quotient = {thirdC.a}"

    def div2(self, sec):
        denom = sec.a2 + sec.b2
        numer_re = self.a * sec.a - self.b * -sec.b
        numer_im = self.a * -sec.b + self.b * sec.a
        self.a = numer_re / denom
        self.b = numer_im / denom

    def len1(self):
        return (self.a**2 + self.b**2)**0.5

    def str1(self):
        if thirdC.b < 0:
            return f"{self.a} - {abs(self.b)}i"
        elif thirdC.b > 0:
            return f"{self.a} + {self.b}i"
        else:
            return f"{self.a}"

    def arg(self):
        return atan(self.b / self.a)

    def pow1(self, n):
        r = (self.a**2 + self.b**2)**0.5
        c = self.a / r
        s = self.b / r
        return f"{r**n*c*n} + {r**n*s*n}i"

    def equals(self, sec):
        mod1 = (self.a**2 + self.b**2)**0.5
        mod2 = (sec.a**2 + sec.b**2)**0.5
        if mod1 > mod2:
            return ">"
        elif mod2 > mod1:
            return "<"
        else:
            return "="
            
#Vector2D
class Vector2D:
    def init(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, second):
        thirdV.x = self.x + second.x
        thirdV.y = self.y + second.y
        return thirdV.x, thirdV.y

    def add2(self, second):
        self.x += second.x
        self.y += second.y
        pass

    def sub(self, second):
        thirdV.x = self.x - second.x
        thirdV.y = self.y - second.y
        return thirdV.x, thirdV.y

    def sub2(self, second):
        self.x -= second.x
        self.y -= second.y

    def mult(self, a):
        thirdV.x = self.x * a
        thirdV.y = self.y * a
        return thirdV.x, thirdV.y

    def mult2(self, a):
        self.x *= a
        self.y *= a

    def str1(self):
        return f"({str(self.x)};{str(self.y)})"

    def len1(self):
        return f"Vector length: {(self.x**2 + self.y**2)**0.5}"

    def scalar_product(self, second):
        return f"Vector * vector: {(self.x * second.x) + (self.y * second.y)}"

    def cos(self, second):
        cos_ang = ((self.x * second.x + self.y * second.y) /
                   (((self.x**2 + self.y**2)**0.5)*((second.x**2 + second.y**2)**0.5)))
        return f"Cosine: {cos_ang}"

    def equals(self, second):
        len1 = (self.x**2 + self.y**2)**0.5
        len2 = (second.x**2 + second.y**2)**0.5
        if len1 > len2:
            return '>'
        elif len1 < len2:
            return '<'
        else:
            return '='

#RationalFraction
import math

def red(x, y):
    n = math.gcd(x, y)
    x //= n
    y //= n
    return f"{x}/{y}"

class RationalFraction:
    def init(self, x=0, y=0):
        self.x = x
        self.y = y

    def reduce(self):
        nod = math.gcd(self.x, self.y)
        self.x //= nod
        self.y //= nod

    def add(self, sec):
        thirdF.y = self.y * sec.y
        thirdF.x = self.x * sec.y + sec.x * self.y
        return f"Sum = {red(thirdF.x, thirdF.y)}"

    def add2(self, sec):
        self.x = (self.x * sec.y) + (sec.x * self.y)
        self.y *= sec.y
        self.reduce()

    def sub(self, sec):
        thirdF.y = self.y * sec.y
        thirdF.x = self.x * sec.y - sec.x * self.y
        return f"Difference = {red(thirdF.x, thirdF.y)}"

    def sub2(self, sec):
        self.x = self.x * sec.y - sec.x * self.y
        self.y *= sec.y
        self.reduce()

    def mult(self, sec):
        thirdF.y = self.y * sec.y
        thirdF.x = self.x * sec.x
        return f"Multiplication = {red(thirdF.x, thirdF.y)}"

    def mult2(self, sec):
        self.x *= sec.x
        self.y *= sec.y
        self.reduce()

    def div(self, sec):
        thirdF.y = self.y * sec.x
        thirdF.x = self.x * sec.y
        return f"Quotient = {red(thirdF.x, thirdF.y)}"

    def div2(self, sec):
        self.x *= sec.y
        self.y *= sec.x
        self.reduce()

    def str1(self):
        return f"{self.x}/{self.y}"

    def value(self):
        return self.x/self.y

    def equals(self, sec):
        val1 = self.x / self.y
        val2 = sec.x / sec.y
        if val1 > val2:
            return f"{self.x}/{self.y} > {sec.x}/{sec.y}"
        elif val1 < val2:
            return f"{self.x}/{self.y} < {sec.x}/{sec.y}"
        else:
            return f"{self.x}/{self.y} = {sec.x}/{sec.y}"

    def number_part(self):
        return self.x // self.y