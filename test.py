import numpy as np
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
result=np.zeros((N,N), dtype= int)
for test_case in range(1, T + 1):
    N = int(input())
    for i in range(1, N+1):
        for j in range(1, i+1):
            if j== 1 or j==i:
                result[i,j] = 1
            else:
                result[i,j] = result[i-1,j-1]+result[i-1,j]

    print(f"#{test_case}")
    for i in range(N):
     	 print(" ".join(map(str,result[i,:i+1])))
      
      