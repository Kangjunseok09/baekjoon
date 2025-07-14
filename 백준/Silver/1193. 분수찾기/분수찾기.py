n = int(input())

sum = 0
i = 1
while True:
  sum += i 
  if n - sum <= 0:
    break
  i += 1

if i % 2 == 0:
  mom = i - (n - (sum - i)) + 1
  son = n - (sum - i)
else:
  mom = n - (sum - i)
  son = i - (n - (sum - i)) + 1
print(f"{son}/{mom}")
