n = int(input())
queue = [i for i in range(1, n+1)]
while len(queue) != 1:
  print(queue[0], end=" ")
  del queue[0]
  queue.append(queue.pop(0))
print(queue[0], end=" ")

