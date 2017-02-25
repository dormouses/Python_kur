class Comparator:
  def __init__ (self, x):
    self.value=x
  def compare (self, x):
    try:
      return cmp(self.value, x.value)
    except:
      return 1
