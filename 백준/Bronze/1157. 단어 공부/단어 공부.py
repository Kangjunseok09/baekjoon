s = input()
s = s.upper()
char = [chr(n + 65) for n in range(26)]
cnt = 0
manyword = ""
for i in char:
  if s.count(i) > cnt:
    manyword = i
    cnt = s.count(i)
  if manyword != i and cnt == s.count(i):
    manyword = "?"
print(manyword)



