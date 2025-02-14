import sys
sys.stdin = open("input.txt","r")
n = int(input())
path = []
arr=[]
used =[0]*7
def KFC(x,n):

    if x == n:

        return

    for i in range(1,7):
        if used[i] == 1:continue
        used[i] = 1
        path.append(i)
        KFC(x+1,n)
        path.pop()              # 백트래킹
        used[i] = 0

arr=[]

print(KFC(0,n))




