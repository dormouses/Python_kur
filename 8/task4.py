class Vovel:
  def __getattr__(self, name):
    __a=set("aeiouy")
    k=True
    for e in name:
      if not (e in __a):
        k=False
    if k: 
      return name.upper()
    else:
      raise AttributeError("Vovel instance  has no attribute %r" %
                               ( name))
