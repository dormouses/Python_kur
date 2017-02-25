s=raw_input()
d={}
while s != "" :
  words = s.split(' ')
  if len(words)==1:
    d[words[0]]=1
  else:
    try:
      d[words[0]]=-1
    except Exception:
      k=1
   # print words
    for el in words[1:]:
      if not d.has_key(el) and el!='':
        d[el]=0
 # print d
  s = raw_input()

#print d
for el in d.values():
  if el==0:
    print 'NO'
    exit()
print 'YES'

