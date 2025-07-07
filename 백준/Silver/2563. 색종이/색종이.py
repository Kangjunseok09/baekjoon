n = int(input())
colorpaper = []
paper = [[0] * 100 for i in range(100)]

for i in range(n):
  x, y = map(int, input().split())
  colorpaper.append((x, y))

for h, w in colorpaper:
  for i in range(10):
    for j in range(10):
      paper[i+h][j+w] = 1

area = sum(sum(i) for i in paper)
print(area)
