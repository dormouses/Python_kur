def chek():
  ans=''
  for i in xrange (0, n):
    ans+=a[i]+zn[i]
  if eval(ans):
    print 'YES'
    exit()

def dozn (k, c):
  if k==n-1:
    zn[k]=' '
    if c==1:
      chek()
  else:
    for j in xrange(0, 2):
      zn[k]=z[j]
      dozn(k+1,0)
    if c==0:
      zn[k]='=='
      dozn(k+1, 1)

s=raw_input()
a=s.split(' ')
n=len(a)
z="+-"
zn=[0]*(n+1)
dozn(0, 0)
print 'NO'
