import sys
input = sys.stdin.readline
basket = []

n, m = map(int,input().split())
for i in range(1, n+1):
  basket.append(i)

for i in range(m):
  f, s = map(int, input().split())
  basket[f-1:s] = basket[f-1:s][::-1]
      

    

for i in basket:
  print(i, end=" ")


