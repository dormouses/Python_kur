class MTuple:
  def __init__(self, value):
    self.val=tuple(value)
 
  def __str__(self):
    return self.val.__str__()
 
  def __neg__(self):
    return(MTuple(self.val[::-1]))

  def __getattr__(self, name):
    if hasattr(self.val, name):
      def wrapper(*args, **kwds):
        _args=[]
        _kwds={}
        for el in args:
          if type(el)==type(self):
            _args.append(el.val)
          else:
            _args.append(el)
        for key in kwds.keys():
          if type(kw[key])==type(self):
            _kw[key]=kw[key].val
          else:
            kw_new[key]=kw[key]
        ans=getattr(self.val, name)(*_args, **_kwds)
        if type(ans)==tuple:
          return MTuple(ans)
        else:
          return ans
      return wrapper
    raise AttributeError(name)

