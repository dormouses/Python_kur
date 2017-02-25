set_n=set()
n=input()
l=input()
tmp=set()
for numb in l:
  for el in set_n:
    tmp.add(el+numb)
  tmp.add(numb)
  set_n.update(tmp)
if n in set_n:
  print('YES')
else:
  print ('NO')
