class Vector:
  def __init__ (self, x, y):
    self.x=x
    self.y=y
  def __add__(self, a):
      return Vector(self.x+a.x, self.y+a.y)
  def __str__ (self):
    return '|'+str(self.x)+','+str(self.y)+'|'
  def __mul__(self, a):
    if str(type(a))=="<type 'int'>":
      return Vector (self.x*a,self.y*a) 
    else:
      return self.x*a.x+self.y*a.y
  def __rmul__(self, a): 
    if str(type(a))=="<type 'int'>":
      return Vector (self.x*a,self.y*a) 
    else:
      return self.x*a.x+self.y*a.y
#  def __rmul__(self, a):
 #   return Vector(self.x*a, self.y*a)
    
