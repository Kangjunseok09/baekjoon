n = int(input())
cnt = 0

for i in range(n):
    word = input().strip()
    seen = set()     
    prev_char = ''   
    is_group = True  

    for j in word:
        if j != prev_char:       
            if j in seen:        
                is_group = False
                break               
            seen.add(j)          
        prev_char = j            

    if is_group:
        cnt += 1

print(cnt)