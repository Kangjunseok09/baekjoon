n = int(input())
a = list(map(str, input()))
result = 0
for i in range(len(a)):
  t = ord(a[i]) - 96
  result += (t * 31 ** i )

print(result % 1234567891)
