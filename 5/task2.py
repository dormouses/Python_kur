def rand():
  xn=x0
  yield xn
  b=1
  while xn!=x0 or b==1:
    b=0
    xn=(a*xn+c) % m
    yield xn
   
s=input()
x0=s[0]
a=s[1]
c=s[2]
m=s[3]
n=input()
ans='NO'
for i in rand():
 # print i
  if i==n:
    ans='YES'
    break
print ans
