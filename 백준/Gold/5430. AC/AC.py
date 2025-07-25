from collections import deque
import json
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
  s = input()
  size = int(input())
  arr = deque(json.loads(input()))

  reverse_flag = False
  error_flag = False

  for i in s:
    if i == "R":
      reverse_flag = not reverse_flag
    elif i == "D":
      if not arr:
        print("error")
        error_flag = True
        break
      if reverse_flag:
        arr.pop()
      else:
        arr.popleft()
  if not error_flag:
    if reverse_flag:
      arr.reverse()
    print("[" + ",".join(map(str, arr)) + "]")