words = [input() for _ in range(5)]  # 5줄 입력

result = ''
for i in range(15):  # 최대 열 길이
    for j in range(5):  # 5줄
        if i < len(words[j]):
            result += words[j][i]  # 세로로 읽기

print(result)