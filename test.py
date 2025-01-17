import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    num =[]
    for i in range(0,N):
        row= list(map(int,input().split()))
        num.append(row)
print(N,M)
        
print(num)