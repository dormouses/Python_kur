str = raw_input()
end = 0
best = ''
maxLen = 0
StrLen = len(str)
temp = str[0]
while True :
    if len(temp) == len(set(temp)):
        if maxLen < len(temp):
            maxLen = len(temp)
            best = temp
        end +=1
        if end >= StrLen:
            break
        temp += str[end]
    else:
        temp = temp[1:]
 
print best