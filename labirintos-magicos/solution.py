adj = dict()
vis = dict()

p = int(input())
for i in range (p):
  name = input()
  adj[name] = []
  vis[name] = False

a = int(input())
for i in range(a):
  x,y = input().split()
  adj[x].append(y)
  adj[y].append(x)


def connected(a,b):
  global adj
  if vis[a]:return False
  vis[a]=True
  if a == b:
    return True
  for nb in adj[a]:
    ans = connected(nb,b)
    if ans: return ans

  return False

input()

x,y = input().split()
if connected(x,y):print('SIM')
else:print('NAO')
