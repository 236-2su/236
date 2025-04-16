# # 완전 탐색으로 부분집합 구하기

# arr = ['O', 'X']
# path = []
# name = ['Luffy', 'Zoro', 'sanji']

# def print_name():
#     for i in range(3):
#         if path[i] == 'O': print(name[i], end = ' ')
#     print() # 줄바꿈

# def dfs(lev):
#     if lev == 3:
#         # print(path)
#         print_name()
#         return

#     for i in range(2):
#         path.append(arr[i])
#         dfs(lev + 1)
#         path.pop()
# dfs(0)


# # ['A','B','c']
# # 1. 집합의 총개수 -> 2의 n승
# # -> 비트연산 1<<n
# #     1<<3 : 왼쪽으로 3번 밀어라
# #     1000 -> 2의 3승 -> 8
# #     8421
# # 2. 소스코드: 오른쪽으로 한번 씩 밀면서 마지막 자리가 1인지 0인지 확인



# # 부분 집합 구하기
# # 바이너리 카운팅
# # 비트 연산

# arr = ['A','B','C']
# n = len(arr)
# # 0b110(이진수) ---->6(십진수)
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1: # 이 연산은 비트연산입니다라는 가독성 그냥 1로 해도 상관없음
#             print(arr[i], end='')
#         tar >>=1 # 오른쪽으로 한번씩 민다.
# for tar in range(1<<n): # 모든 경우의 수 2의 n 제곱
#     print('{', end = '')
#     get_sub(tar)
#     print('}')


# # 조합 만들기
# arr=['A','B','C','D','E']

# for a in range(5):
#     start1 = a+1
#     for b in range(start1,5): # a에서 뽑은건 포함하면 안된다.
#         start2 = b+1
#         for c in range(start2,5):
#             print(arr[a],arr[b],arr[c])


# arr=['A','B','C','D','E']
# path=[]
# def dfs(lev,start):
#     if lev ==n:
#         print(path)
#         return
#     for i in range(start,5):
#         path.append(arr[i])
#         dfs(lev+1,i+1)
#         path.pop()
# dfs(0,0)


# # queue - 선입선출
# # 메서드 두개 사용 : append(), pop(0)

# from collections import deque

# T= int(input())

# for tc in range(1,T+1):
#     n,m = map(int,input().split())
#     arr =deque(map(int,input().split()))
#     for i in range(m):
#         arr.append(arr.popleft())


#         result = arr[0]
#         print(f'#{tc} {result}')

# # 피자굽기 문제파악
# # 1. N개의 피자를 동시에 구울 수 있는 화덕
# # 2. 1번 위치에서만 피자를 넣거나 뺄 수 있음
# # 3. 치즈가 0이되면 피자를 꺼내고, 새피자를 넣음
# # 4. 치즈가 남아있으면 다시 뒤에 넣기
# # 5. 마지막까지 남은 피자 번호를 찾아야함


# # 전략
# # 초기값 화던 채우기: N개 피자 넣기
# # 시뮬레이션
# # - 맨 앞의 피자 꺼내서 치즈 확인(popleft())
# # - 치즈의 양 반으로 줄이기(//:몫)
# # - 치즈가 0이면 새 피자 넣기
# # - 치즈가 남아있으면 다시 뒤에 넣기
# # - 한개 남을 때까지 반복(while 문)


# from collections import deque
# import sys
# sys.stdin =open('input.txt','r')


# T= int(input())
# for tc in range(1,T+1):
#     n,m = map(int,input().split())
#     cheeses = list(map(int, input().split()))
#     pizzas = deque([i+1,p] for i, p in enumerate(cheeses))
#     oven = deque()

#     for _ in range(n):
#         if pizzas:
#             oven.append(pizzas.popleft())
#     while len(oven)>1:
#         now = oven.popleft()
#         now[1]//=2
        
#         if now[1] == 0:
#             if pizzas:
#                 oven.append(pizzas.popleft())
#         else:
#             oven.append(now)
    
#     print(f'#{tc} {oven[0][0]}')