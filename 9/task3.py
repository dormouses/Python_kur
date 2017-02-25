import itertools

def inc (k):
  k+=1
  if k==4:
    k=0

sp=input()
n=len(sp)
l=[0, 1]
ans=[]
for i in xrange(0, n):
  ans.append(l)
for p in itertools.product(*ans):
  if p.count(1)==4:
    i=0
    k=0
    sums=[0, 0, 0, 0, 0]
    while i!=n:
      sums[k]+=sp[i]
      if p[i]==1: k+=1
      i+=1
    if sums[0]==sums[2] and sums[1]==sums[3]:
      print 'YES'
      exit(0)
print 'NO'
