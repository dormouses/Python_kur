p=input()
n=len(p)
s=reduce(lambda res, x: res+x, p)
if s % 2 == 1:
  exit()
s=s/2
p=p+p
l=0;
while l<n:
  l+=1
  cur_s=0
  i=l
  while i<n+l and cur_s<s:
    cur_s+=p[i]
    i+=1
  if cur_s!=s: continue
  j=l-1
  cur_s1=0
  cur_s2=0
  while j<i:
    j+=1
    cur_s1+=p[j]
    k=i
    while cur_s2<cur_s1 and k<n+l:
      cur_s2+=p[k]
      k+=1
    if cur_s1!=cur_s2 or cur_s1==s: 
      cur_s2=0
      continue
    print 'YES'
    exit()
print 'NO'
