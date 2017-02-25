s=raw_input()
arr_str=s.split(' ')
dic=dict()
for s in arr_str:
  tmp=set(s)
  ind=len(tmp)
  if dic.get(ind)==None:
    dic[ind]=[]
  dic[ind]+=[s]
l=dic.keys()
l.sort()

output = ""

b=True
for el in l:
  for i in dic[el]:
    if not b: 
      output += " "+i
    else:
      output+=i
      b=False
print output
