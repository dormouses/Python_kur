s=raw_input()
l=s.split(' ')
st=[] 
try:
  for el in l:
    if el=='+' or el=='-' or el=='/' or el=='*':
      a=st.pop()
      b=st.pop()
      c=`eval(b+el+a)`
      st.append(c)
    else:
      st.append(el)
  if len(st)==1:
    print st[0]
  else:
    1/0
except Exception:
  print 'ERROR'
