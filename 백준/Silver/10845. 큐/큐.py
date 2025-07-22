import sys
input = sys.stdin.readline
n = int(input())
queue = []
for i in range(n):
  cmd = input().split()
  if cmd[0] == "push":
    queue.append(int(cmd[1]))
  elif cmd[0] == "pop":
    if len(queue) == 0:
      print(-1)
    else:
      num = queue.pop(0)
      print(num)
  elif cmd[0] == "size":
    print(len(queue))
  elif cmd[0] == "empty":
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == "front":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif cmd[0] == "back":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[len(queue)-1])
