dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

def good(x,y):
  if x>=0 and x<l and y>=0 and y<l and maze[x][y]=='.':
    return 1
  else:
    return 0

def go(x,y,n):
  maze[x][y]=n
  for d in range(4):
    if good(x+dx[d],y+dy[d]):
      go(x+dx[d],y+dy[d],n+1)


l = list(raw_input())
if len(l)==1:
  print 'YES'
  exit()
maze = []
maze.append(l)
l = len(l)
for i in xrange(l-1) :
  maze.append(list(raw_input()))

go(0,0,0)

if maze[l-1][l-1]=='.':
  print 'NO'
else:
  print 'YES'

