number = list(map(int, input().split()))

if number == list(range(1, 9)):
  result = "ascending"
elif number == list(range(8, 0 ,-1)):
  result = "descending"
else:
  result = "mixed"
print(result)