s=raw_input()
try:
  m=__import__(s)
  i=0
  for el in dir(m):
    if str(type(eval('m.'+el)))=="<type 'module'>":
      i+=1
  print i
except Exception:
  print -1
