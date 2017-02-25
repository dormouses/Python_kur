from array import *
k=array('i',[])
inp=input()
l=array('i',inp)
s=l.tostring()
s=s[::-1]
k.fromstring(s)
print k.tolist()
