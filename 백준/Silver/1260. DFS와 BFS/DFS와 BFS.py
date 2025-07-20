n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1, n+1):
  graph[i].sort()

def dfs(v):
  stack = [v]
  visited = [False] * (n+1)
  while stack:
    node = stack.pop()
    if not visited[node]:
      print(node, end=" ")
      visited[node] = True
      for next in reversed(graph[node]):
        if not visited[next]:
          stack.append(next)

def bfs(v):
  queue = [v]
  visited = [False] * (n+1)
  visited[v] = True
  
  while queue:
    q = queue.pop(0)
    print(q, end=" ")
    for next in graph[q]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)

dfs(v)
print()
bfs(v)