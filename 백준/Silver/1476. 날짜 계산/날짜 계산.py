e, s, m = map(int, input().split())
year = 1
while True:
  if year % 15 == e % 15 and year % 28 == s % 28 and year % 19 == m % 19:
    break
  year += 1
print(year)