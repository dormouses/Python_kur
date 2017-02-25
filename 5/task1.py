from math import *
s=raw_input()
l=input()
a=int(l[0])
b=int(l[1])
x=a
try:
  maxx=minn=eval(s)
except:
  x=b
  maxx=minn=eval(s)
for x in xrange(a, b+1):
  try:
    k=eval(s) 
    minn = min(minn, k)
    maxx = max(maxx, k)
  except:
    q = 'ququ'

print (' '.join([str(minn), str(maxx)]))
