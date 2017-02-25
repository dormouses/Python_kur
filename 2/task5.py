s=input()
x=s[0]
y=s[1]
r=s[2]

list=input()

l=len(list)
num=range(0,l, 2)
k=0
for i in num:
  if (x-list[i])*(x-list[i])+(y-list[i+1])*(y-list[i+1]) > r*r:
    k=1

if k==0:
  print 'YES'
else:
  print 'NO'
