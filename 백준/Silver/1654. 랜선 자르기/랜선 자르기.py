import sys
input=sys.stdin.readline

n,k=map(int,input().split(' '))
l=[int(input()) for i in range(n)]


sum=0
start=1
end=max(l)


while start <= end:
    sum=0
    mid=(start+end)//2

    for i in l:
        sum+=i//mid

    if sum>=k:
        start=mid+1
    else:
        end=mid-1


print(end)