croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
for pattern in croatia:
    s = s.replace(pattern, "A") 
print(len(s))
  