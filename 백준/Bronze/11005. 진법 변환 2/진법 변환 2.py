n, b = map(int, input().split())

list = [chr(i) for i in range(ord('0'), ord('9')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]

result = []
while n > 0:
  result.append(list[n%b])
  n //= b
for i in range(len(result)-1, -1, -1):
  print(result[i], end="")