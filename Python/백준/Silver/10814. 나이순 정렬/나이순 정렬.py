import sys
input = sys.stdin.readline
ageNamelist = []
n = int(input())
for i in range(n):
  age, name = input().strip().split()
  age = int(age)
  ageNamelist.append((age, name))
ageNamelist.sort(key=lambda x: x[0])
for age, name in ageNamelist:
  print(age, name)
