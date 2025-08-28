import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}
for i in range(1, n+1):
  name = input().rstrip()
  dict[i] = name
  dict[name] = i

for i in range(m):
  cmd = input().rstrip()
  if cmd.isdigit():
    print(dict[int(cmd)])
  else:
    print(dict[cmd])