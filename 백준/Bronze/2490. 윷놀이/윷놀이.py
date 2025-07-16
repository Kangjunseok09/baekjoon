yutlist = ["D", "C", "B", "A", "E"]
for i in range(3):
  yut = list(map(int, input().split()))
  print(yutlist[sum(yut)])