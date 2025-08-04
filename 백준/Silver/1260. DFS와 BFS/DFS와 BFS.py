n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort()

def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for next in graph[node]:
        if not visited[next]:
            dfs(next, visited)

def bfs(start):
    visited = [False] * (n + 1)
    queue = [start]
    visited[start] = True

    while queue:
        node = queue[0]
        del queue[0]
        print(node, end=' ')
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

visited_dfs = [False] * (n + 1)
dfs(v, visited_dfs)
print()
bfs(v)