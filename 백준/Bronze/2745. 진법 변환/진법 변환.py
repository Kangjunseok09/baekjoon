list = [chr(i) for i in range(ord('0'), ord('9')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]

n, b = input().split()
b = int(b)
result = 0
for i in range(1, len(n)+1):
  result += (list.index(n[-i])) * (b ** (i-1))

print(result)