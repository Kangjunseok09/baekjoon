n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))

rank = {j: i for i, j in enumerate(sort_arr)}

print(*(rank[i] for i in arr))