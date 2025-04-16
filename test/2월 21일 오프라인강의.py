# # DFS vs BFS
# # BFS -> level단위로 탐색

# # DFS => 재귀호출, 백트래킹
# # BFS => queue로 구현

# # 미로는 보통은 BFS가 더 효율적
# # 하지만, DFS로 구현해야 해를 찾을 수 있는 문제들이 존재

# # heapq 정중앙 대학 전략
# # 1. mid(중간값) 보다 작은 값들은 최대힙, 큰 값들은 최소힙에 저장
# # 2. 두 힙의 크기 차이가 1이상 나지 않도록 유지
# # 3. 항상 mid(중간값)을 별도로 관리, 실시간으로 중앙값을 찾는다.

# import heapq
# max_heap = []
# min_heap = []
# mid = 500

# def push(v):
#     # 중간값이랑 비교해서 작으면 최대힙에, 크면 최소힙에
#     if mid >v:
#         heapq.heappush(max_heap, -v)
#     else:
#         heapq.heappop(min_heap, v)


# n= int(input())

# for _ in range(n):
#     # 두 점수
#     a,b = map(int,input().split())
#     # 두 점수를 힙에 push
#     push(a)
#     push(b)

#     # 최대힙의 크기가 더 클경우(mid 기준으로 왼쪽이 더 많을 경우)
#     # 최대힙의 최대값 == mid
#     if len(max_heap)>len(min_heap):
#         heapq.heappush(min_heap, mid)
#         mid = -heapq.heappop(max_heap)
#     elif len(max_heap) < len(min_heap):
#         heap.heappush(max_heap, -mid)
#         mid = heapq.heappop(min_heap)       
#     print(mid)
# #     # 최소힙의 크기가 더 클경우(mid 기준으로 오른쪽이 더 많을 경우)
# #     #최소힙의 최소값 == mid
    
# # 최소힙을 사용해서 가장 작은 어글리 넘버 찾기
# # 힙에 넣을 때 2,3,5를 곱한 수를 힙에 넣어 자동으로 정렬
# # 중복된 숫자가 생긴다.
# # ugly = [], 이 리스트를 통해서 이미 사용된 수 건너뛰기

# import heapq
# n = int(input())
# k = list(map(int, input().split()))
# ugly = []
# heap = [1] # 최소힙, 초기값 1넣기
# # 2,3,5 를 힙에 넣기
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 5)

# while len(ugly) < max(k):
#     n = heapq.heappop(heap) # 힙에서 가장 작은수 꺼냄
#     if n in ugly: continue # 중복방지
#     # ugly  리스트에 추가
#     ugly.append(n)
#     heapq.heappush(heap, n * 2)
#     heapq.heappush(heap, n * 3)
#     heapq.heappush(heap, n * 5)

# for i in k:
#     # k는 1부터고 이덱스는 0 부터니까
#     print(ugly[i-1], end = ' ')

