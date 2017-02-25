l=input()
m=l[0]
n=l[1]
len1=len(`n*m`)
len2=len(`n`)
len3=len(`m`)

for i in range(1, n+1):
 print ('{:_>{len1}}_=_{:_>{len2}}_*_{:_>{len3}}'.format(i*m,i,m, len1=len1, len2=len2, len3=len3))
