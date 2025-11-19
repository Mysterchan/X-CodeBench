import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = {}
for i in range(1,n+1):
  graph[i] = []
for i in range(n-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
tree = {}
for i in range(1,n+1):
  tree[i] = []
from collections import deque
queue = deque()
queue.append(1)
visited = [False]*(n+1)
visited[1] = True
while queue:
  now = queue.popleft()
  for nei in graph[now]:
    if visited[nei] == False:
      tree[now].append(nei)
      visited[nei] = True
      queue.append(nei)

p = False
f_ans = 0
def dfs(node):
  global f_ans
  global p
  al = []
  for nei in tree[node]:
    al.append(dfs(nei))
  al.sort(reverse = True)

  al = al[:4]
  if len(al) == 4:
    p = True
    f_ans = max(f_ans,sum(al)+1)
  elif al != []:
    f_ans = max(f_ans,al[0]+1)
  al = al[:3]
  if len(al) == 3:
    return sum(al)+1
  else:
    return 1
ans = dfs(1)
f_ans = max(ans,f_ans)
if p==False:
  f_ans = -1
print(f_ans)