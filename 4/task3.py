s = raw_input()
dic = {}

while s != "" :
  words = s.split()
  for el in words:
    if not dic.has_key(el):
      dic[el] = 0
    dic[el] += 1
  s = raw_input()

mmax=0;
c=-1;
for el in dic.keys():
  if dic[el]>mmax:
    mmax=dic[el]
    s=el
    c=1
  elif dic[el]==mmax:
    c+=1
if c==1:
  print s
else:
  print "---"
