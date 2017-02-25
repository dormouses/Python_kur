def gen(k, i):
  if i==k:
    print ''.join(ans)
  else:
    if (i!=0):
      ans.append(ch[0])
      gen(k, i+1)
      ans.pop()
    for j in xrange(1,n+1):
      ans.append(ch[j])
      gen(k, i+1)
      ans.pop()

s=input()
ans=[]
k=s[0]
n=s[1]
ch=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
n=n-1
gen(k, 0)

