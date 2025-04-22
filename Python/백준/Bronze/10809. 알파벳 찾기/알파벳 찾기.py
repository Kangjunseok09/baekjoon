str = input()
result = [-1]*26
for i in range(26):
  for j in range(len(str)):
    if chr(97 + i) == str[j]:
      result[i] = j
      break

    


for i in range(len(result)):
  print(result[i], end=" ")