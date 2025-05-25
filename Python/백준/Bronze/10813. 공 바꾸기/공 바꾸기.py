n, m = map(int, input().split())
basket = []
for _ in range(n):
  basket.append(_+1)

for _ in range (m):
  i, j  = map(int, input().split())
  basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for _ in basket:
  print(_, end=" ")

