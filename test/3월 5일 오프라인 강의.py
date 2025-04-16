# 이진 탐색트리(BST)
# 1. 이진 트리의 특성(2개 이하의 자식노드를 가진다.)
# 2. 왼쪽 자식 노드의 값은 항상 부모 노드보다 작다.
# 3. 오른쪽 자식 노드의 값은 항상 부모 노드보다 크다.


# 트리에 데이터가 저장되는 과정
# 1. 루트 노드부터 시작
# 2. 삽입할 값과 현재 노드의 값을 비교
#     2-1. 현재 노드보다 작은면 왼쪽으로
#     2-2. 현재 노드보다 크면 오른쪽으로
# 3. 자식노드가 그 방향에 없다면 (빈자리면)저장
# 4. 자식노드가 그 방향에 있다면 2번, 3번 과정 다시 반복


# # queue 복습
# from collections import deque
# q= deque([5,4,3])
# flag = 0 
# while flag<5:
#     flag +=1 
    
#     temp = q.popleft()
#     temp =(temp * 55 + 17) % 11
#     q.append(temp) 

# while q:
#     temp_q = q.popleft()
#     print(temp_q)


# # 알고리즘 1. 방향배열, 알고리즘 2. BFS(큐, visited배열)
# # BFS 특징
# # BFS는 두개의 과정으로 나눠짐
# # 1번 과정 - 큐에서 뺀다(탐색)
# # 2번 과정 - 다음 갈 수 있는 노드 예약 걸기(큐 등록)
# # 과정 2번을 실행할 때 조건 3가지
# # 조건 1. 미로내부, 조건2. 벽이 아니고, 조건3. 최초 방문(visited) ---> 방문을 하면 방문 기록

# # 함수 2개 만들기
# # 1번 함수 BFS함수
# # 2번 함수 find_start함수(출발점 찾기)

# # # 인접 리스트
# # from collections import deque

# alist = [[] for _ in range(7)]
# alist[5] =[3,1]
# alist[3] =[2]
# alist[1] =[4]
# alist[4] =[0,6]

# q = deque()
# # 항상 q에 start 노드 값을 넣어준다.
# q.append(5)

# while q:
#     # 과정 1번. 큐에서 뺀다(탐색)
#     now = q.popleft()
#     print(now, end = ' ')

#     # 과정 2번. 다음 갈곳 예약 걸기(큐등록)
#     for i in range(len(alist[now])):
#         next = alist[now][i]
#         q.append(next)

# def dfs(now):

#     if bt[now] ==0 : return # 백트레킹

#     dfs(now*2) # 왼쪽 자식 노드 탐색  
#     dfs(now*2+1)# 오른쪽 자식 노드 탐색
#     print(bt[now]) # 현재 노드 마지막 탐색

# # dfs(1) # 최고 조상 노드 root

# def bfs():
#     q =[]
#     # visited 배열 초기화
#     visited = [[0] *N for _ in range(N)]
#     # 시작점을 큐에 등록
#     q.append((y,x))
#     visited[y][x] = 1
#     while q:
#         # bfs의 1번과정. 큐에서 뺀다(탐색)
#         ty,tx = q.pop(0)
#         if arr[ty][tx] == 3:
#             return visitied[ty][tx] # 최단 경로의 길이
#         # 방향 배열 알고리즘
#         for dy,dx in [(0,1),(0,-1),(-1,0),(1,0)]:
#             k = 1 
#             if arr[ty][tx] ==4:
#                 k=2 # 점프대인 경우
#             ny,nx = ty+dy *k, tx+dx *k
#         # bfs의 2번과정. 다음 갈 곳 예약걸기(큐등록)
#         # 조건 3가지(1. 미로내부 2. 벽이 아니고 3. 최초 방문)
#             if 0<=ny<N and 0<=nx<n and arr[ny][nx] != 1 and visited[ny][nx] ==0:
#                 q.append((ny,nx))
#                 # 최초 방문일 경우 방문하고, 방문기록
#                 visited[ny][nx] = visited[ty][tx] + 1
    
#     return -1            

# def find_start(): # 출발점 찾기
#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] ==2:
#                 return y,x

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split()) for _ in range(N))]
#     sty,stx = find_start()
#     result = bfs(sty,stx)
#     print(f'{tc} {result}')


# # 슬라이딩 윈도우 준비
# arr =[4,5,1,1,5,4,-3,-13,9,20,13]
# idx = int(input())

# def get_sum(idx):
#     sum_v = 0 
#     for i in range(5): # i값이 0,1,2,3,4
#         sum_v += arr[idx+i]
#     return sum_v

# ret = get_sum(idx)
# print(ret)

# 슬라이딩 윈도우 쓰는 이유는? 빠르기 떄문!!

# n,m= map(int,input().split())
# arr = list(map(int,input().split()))
# def find_max():
#     max_sum = float('-inf')
#     sum_temp = sum(arr[:5])
    
#     for i in range(n-m):
#         sum_temp -= arr[i]
#         sum_temp += arr[i+m]
    
#         if max_sum < sum_temp:
#             max_sum = sum_temp
#             temp_i = i+1
#     return temp_i

# result = find_max()
    
# print(result)


