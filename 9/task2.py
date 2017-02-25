import math 
class Trigon:
  def __init__(self, la, lb, lc):
    self.a=la
    self.b=lb
    self.c=lc

  def square(self):
    p=(self.a+self.b+self.c)/2
    return math.sqrt((p*(p-self.a)*(p-self.b)*(p-self.c)))

  def perimeter(self):
    return self.a+self.b+self.c

class Pea:
  def __init__(self, l1, l2, l3):
    self.a=l1
    self.b=l2
    self.c=l3

  def square(self):
    s=Trigon(self.a, self.b, self.c).square()
    r=self.a*self.b*self.c/(4*s)
    return math.pi*r*r

  def perimeter (self):
    s=Trigon(self.a, self.b, self.c).square()
    r=a*b*c/(4*s)
    return 2*math.pi*r

class TrigonPea(Trigon, Pea):
  def __init__(self, a, b, c):
    Trigon.__init__(self, a, b, c)
    Pea.__init__(self, a, b, c)

  def perimeter(self):
    return Trigon.perimeter(self)
  
  def squre (self):
    return Trigon.square(self)

  def volume (self):
    return Trigon.perimeter(self)*Pea.square(self)

