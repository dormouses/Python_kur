import collections
d=collections.OrderedDict()

s=raw_input()
w=s.split()
for i in xrange(0, len(w)):
  if d.get(w[i])==None:
    d[w[i]]=0
  else:
    d[w[i]]=i

s=''
for i in d.keys():
  s+=str(i)
  if d[i]>0:
    s+='('+str(d[i])+')'
  s+=' '
print s
