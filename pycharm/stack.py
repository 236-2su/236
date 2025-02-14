import sys
sys.stdin = open("input.txt", "r")


def sum_pal_hor(y,x,n):
    sum_a = 0
    for i in range(-n,n+1):
        if y+i<0 or y+i >=n:
            pass
        else:
            sum_a += arr[y+i][x]
        if x + i < 0 or x + i >= n:
            continue
        else:
            sum_a += arr[y][x+i]
    sum_a -= arr[y][x]
    return sum_a

    return
T = int(input())
for tc in range(1,T+1):
    n= int(input())
    arr= [list(map(int,input().split())) for _ in range(n)]
    max_sum = float('-inf')
    min_sum = float('inf')
    for i in range(n):
        for j in range(n):
            sum_ =sum_pal_hor(i,j,n)
            if max_sum<sum_:
                max_sum=sum_
            if min_sum>sum_:
                min_sum=sum_

    print(f'#{tc} {max_sum-min_sum}')