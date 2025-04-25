n = int(input())
result = 1
i = 0
while True:
  result += 6 * i
  if result >= n:
    print(i+1)
    break
  i += 1