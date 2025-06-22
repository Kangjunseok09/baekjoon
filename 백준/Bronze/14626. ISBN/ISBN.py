s = list(input())
sum = 0
for i in range(13):
  if s[i] == "*":
    idx = i
    continue
  if i % 2 == 1:
    sum += int(s[i]) * 3
  else :
    sum += int(s[i])

for i in range(10):
  weight = 3 if idx % 2 == 1 else 1

  if (sum + i * weight) % 10 == 0:
    print(i)
    break


