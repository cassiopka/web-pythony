import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def add(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def sub(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
                
    def mul(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + self.imaginary * no.real)
        
    def truediv(self, no):
        den = pow(no.real, 2) + pow(no.imaginary, 2)
        real = (self.real * no.real + self.imaginary * no.imaginary) / den
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / den
        return Complex(real, imaginary)
        
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = list(map(float, input().split()))
    d = list(map(float, input().split()))
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x.add(y), x.sub(y), x.mul(y), x.truediv(y), x.mod(), y.mod()]), sep='\n')