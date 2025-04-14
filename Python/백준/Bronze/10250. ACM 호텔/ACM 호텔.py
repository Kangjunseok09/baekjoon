result = []
T = int(input())
for i in range(T):
  H, W, N = map(int, input().split())
  if N%H == 0:
    result.append((H * 100) + (N//H))
  else:
    result.append((N % H * 100) + (N//H+1))

for i in range(len(result)):
  print(result[i])