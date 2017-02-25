s=raw_input()
ans=s[0]
locans=s[0]
a=set(s[0])
for i in range(0,len(s)):
  a=set(s[i:i+1])
  for j in range(i+1,len(s)+1):
    a.add(s[j-1])
    if len(a)==(j-i):
      locans=s[i:j]
    else:
      a.remove(s[i])
      break;
  if len(ans)<len(locans):
    ans=locans
  if (len(s) - i) < len(ans):
    break

print ans
