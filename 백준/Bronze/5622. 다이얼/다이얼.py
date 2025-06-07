word = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0
for i in range(len(word)):
  for j in range(len(dial)):
    if word[i] in dial[j]:
      time += j + 3
      break
print(time)

