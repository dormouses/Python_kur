s=raw_input()
k=1
l=len(s)
while (k<=l):
  p=s[:k:]
  i=1
  ans=0
  if (l%k!=0):
    k=k+1
    continue
  c=s.count(p)
  if c==l/k:
    print c
    exit()
  k=k+1
