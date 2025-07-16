sum = 0
min = 0

for i in range(7):
  n = int(input())
  
  if n % 2:
    sum += n
    if min == 0:
      min = n
    elif n < min:
      min = n
if sum == 0:
  print(-1)
else:
  print(f"{sum}\n{min}")