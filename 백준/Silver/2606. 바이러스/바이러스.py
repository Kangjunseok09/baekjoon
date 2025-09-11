computer = int(input())
n = int(input())
graph = [[] for i in range(computer+1)]
cnt = 0
visited = [False]*(computer+1)
for i in range(n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
dfs(1)
print(sum(visited)-1)
