list=input()
max=max2=list[0]
for i in list:
  if i>max:
    max2=max
    max=i
  elif i>max2 and i!=max or max==max2:
    max2=i

if max==max2:
  print 'NO'
else:
  print max2


