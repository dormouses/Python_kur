s=raw_input()
ans=s[0]
locans=s[0]
a = set()
for i in range(0,len(s)):
  a.add(s[i])
  for j in range(i+1,len(s)+1):
    a.add(s[j-1])
    if len(a)==(j-i):
      locans=s[i:j]
  if len(ans)<len(locans):
    ans=locans
  if (len(s) - i) < len(ans):
    break
  a.remove(s[i])

print ans
