import sys
input = sys.stdin.readline

n = int(input())
deque = []
for i in range(n):
  cmd = input().split()

  if cmd[0] == "push_front":
    deque.insert(0, int(cmd[1]))
  elif cmd[0] == "push_back":
    deque.append(int(cmd[1]))
  elif cmd[0] == "pop_front":
    if len(deque) == 0:
      print(-1)
    else:
      num = deque.pop(0)
      print(num)
  elif cmd[0] == "pop_back":
    if len(deque) == 0:
      print(-1)
    else:
      num = deque.pop(len(deque)-1)
      print(num)
  elif cmd[0] == "size":
    print(len(deque))
  elif cmd[0] == "empty":
    if len(deque) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == "front":
    if len(deque) == 0:
      print(-1)
    else:
      print(deque[0])
  elif cmd[0] == "back":
    if len(deque) == 0:
      print(-1)
    else:
      print(deque[len(deque)-1])
