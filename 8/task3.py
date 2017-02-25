class Dot:
  def __init__(self, *args):
   # self.val=list(map(lambda x:float(x), args))
    self.val=args
  def __str__(self):
    l=list(map(lambda x: str(x), self.val))
    return ",".join(l)
  def distance(self, a):
    if len(self.val)!=len(a.val):
      raise ValueError
    l=list(map(lambda x, y:(x-y)*(x-y), self.val, a.val))
    import math
    return math.sqrt(reduce(lambda res, x: res+x, l))
      
  def middle (self, a):
    if len(self.val)!=len(a.val):
      raise ValueError
    l=list(map(lambda x, y:(float(x)+float(y))/2, self.val, a.val))
    return Dot(*l)
