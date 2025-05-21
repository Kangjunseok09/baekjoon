import sys
input = sys.stdin.readline
n = int(input())
input = sys.stdin.readline
w = []
h = []
grade = []
for i in range(n):
  a, b = map(int, input().split())
  w.append(a)
  h.append(b)
for i in range(n):
  rank = 1
  for j in range(n):
    if i != j:
      if w[i] < w[j] and h[i] < h[j]:
        rank += 1
  grade.append(rank)
for i in grade:
  print(i, end=" ")
