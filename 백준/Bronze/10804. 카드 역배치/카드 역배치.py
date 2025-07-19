card = [i for i in range(1,21)]
numbers = []
for i in range(10):
  x, y = map(int,input().split())
  for i in range((y-x+1) // 2):
    card[x-1+i], card[y-1-i] = card[y-1-i], card[x-1+i]
for i in card:
  print(i, end=" ")
