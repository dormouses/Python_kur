import sys
from math import *
import itertools

s=raw_input()
sp=raw_input()
par=sp.replace('=',' ').split()
param=par[::2]
value=par[1::2]
params=', '.join(param)
f=eval('lambda '+ params+':'+s)
ans=[]

values=[]
for el in value:
  if ',' in el:
    bound=el.split(',')
    values.append(range(int(bound[0]), int(bound[1])+1))
  else:
    values.append([int(el)])

final_params=apply(itertools.product, values)
for el in final_params:
  try:
    ans.append(apply(f, el))
  except:
    continue

print max(ans)
