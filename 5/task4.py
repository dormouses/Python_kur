c=list(input())
k=input()
n=len(c)

q=c
for i in xrange (k, n):
  q[i]=min(q[i-k:i])+c[i]

print q[n-1]
