n = int(input())
money = 1000 - n
coins = [500, 100, 50, 10, 5, 1]
i = 0
result = 0
while money > 0 :
  if money / coins[i] >= 1 :
    money -= coins[i]
    result += 1
  elif money / coins[i] < 1 :
    i += 1
  
print(result)



