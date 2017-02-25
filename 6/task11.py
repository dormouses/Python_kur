s = raw_input()
ans = ''
maxLen = 0
n = len(s)
locans =s[0]
i=0
while i<n:
    if len(locans) == len(set(locans)):
        if len(ans) < len(locans):
            ans = locans
        i +=1
        if i< n:
          locans += s[i]
    else:
        locans = locans[1:]

print ans
