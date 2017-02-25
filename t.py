s=raw_input()
m=s.split()
l=[]
for el in m:
  if not el in l:
    l.append(el)
l.sort(reverse=True)
print l
