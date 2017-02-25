import itertools

def con(x, y):
  res=[]
  for i in itertools.product(x, y):
    res.append(i)
  return res

s=input()
k=s[0]
n=s[1]
numbs=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
ans=[]
for i in xrange(1, k):
  ans.append(numbs[:n])

list_ans=[]

for i in numbs[1:n]:
  for j in apply(itertools.product, ans):
    nj=list(j)
    nj.insert(0,i)
    print ''.join(nj)

