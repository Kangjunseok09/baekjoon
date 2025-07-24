from collections import deque
n, m = map(int, input().split())
dq = deque(range(1, n+1))
num = list(map(int, input().split()))
cnt = 0

for i in num:
  while dq[0] != i:
    idx = dq.index(i)
    if idx <= len(dq) // 2:
      dq.rotate(-1)
      cnt += 1
    else:
      dq.rotate(1)
      cnt += 1
  dq.popleft()

print(cnt)
    
