coordinates = [tuple(map(int, input().split())) for i in range(3)]
x, y = zip(*coordinates)
for i in x:
  if x.count(i) == 1:
    print(i, end=" ")
for i in y:
  if y.count(i) == 1:
    print(i)