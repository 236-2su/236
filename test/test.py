import sys
sys.stdin = open("input.txt", "r")

# T = int(input())

# for test_case in range(1, T + 1):
#     N,K = map(int,input().split())
#     blank = []
#     for _ in range(1, N+1):
#         num = [list(map(int,input().split()))]
    
#     for i in range(0,N):
#         for j in range(0,N):
#             len_num = 0
#             if j==0 and num[i][j] ==1:              
#                 for k in range(0,N-j):
#                     if num[i][j+k] ==0:
#                         break
#                     else: 
#                         len_num+=1
#             elif num[i][j] ==1 and j>0 and num[i][j-1] == 0:
#                 for k in range(0, N-j):
#                     if num[i][j+k] ==0:
#                         break
#                     else:
#                         len_num +=1
#             blank.append(len_num)
#     count = blank.count(k)
#     print(f"#{test_case} {count}")                
