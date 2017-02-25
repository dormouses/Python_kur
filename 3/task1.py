s=input()
x1=s[0]
y1=s[1]
x2=s[2]
y2=s[3]
x3=s[4]
y3=s[5]
x4=s[6]
y4=s[7]

if x2==x1 and x4==x3:
  print 'YES'
elif x2==x1 or x4==x3:
  print' NO'
else:
  if (y2-y1)*(x4-x3)==(y4-y3)*(x2-x1):
    print 'YES'
  else:
    print' NO'
