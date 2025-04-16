# 자료구조: 데이터를 관리하는 규칙
# priority.queue에 4,7,2,5,6,9 ->pop -> 2 오름차순을 하지 않아도 2가 나옴
# => 시간 복잡도가 = 로그 N => 빠름
# push: O(logN), pop: O(logN), Top: O(1)

# 우선순위 큐 : 우선순위가 높은 것을 우대한다. (최소 힙)
# -> 파이썬에서는 default가 작은 것이 우선순위가 높다.**

# 힙의 원리
# 1. heap 이라고 불리는 tree로 구현(이진트리랑 형태가 비슷)
# 2. 항상 부모가 자식보다 작다.(힙 속성)

# 그래프 vs 트리
# 그래프는 트리형태에서 사이클이 있으면 그래프로 볼 수 있다.

# import heapq
# pq=[]
# heapq.heappush(pq,5)         # append와 같은데 우선순위로 넣는다
# heapq.heappush(pq,2)
# heapq.heappush(pq,8)
# heapq.heappush(pq,1)
# heapq.heappush(pq,9)

# print(pq) # 1,2,8,5,9 나옴 이진트리 만들면서 확인해야함
#     #     1               이렇게 트리가 나오기 때문, 오른쪽으로 붙이는 이유는 가지가 두개 씩이라고 생각해야 하기 때문
#     #   2      8
#     # 5   9

# # heap sort 시간복잡도: O(nlogn)
# # sort() 시간복잡도: O(nlogn)

# sorted_arr = []
# while pq:
    # # heappop: 우선순위가 높은 것부터 제거(파이썬에서는 최소힙이 dafault)
#     sorted_arr.append(heapq.heappop(pq))
# print(sorted_arr)

# # heap.heappop:
# #     1. 힙트리 구조
# #     2. 맨 위츼 노드가 제거(반환)
# #     3. 마지막 노드가 맨위의 노드로 대체
# #     4. 부모가 자식보다 작아야한다. -> 재정렬


# # 최소힙, 최대힙, 다중조건 힙

# # 1. 최소힙

# import heapq

# min_heap = []
# heapq.heappush(min_heap,3)
# heapq.heappush(min_heap,1)
# heapq.heappush(min_heap,4)

# while min_heap:
#     # 우선순위가 높은 것부터 pop 
#     # 파이썬에서는 작은게 우선순위가 높다
#     print(heapq.heappop(min_heap), end = ' ')

# # 알고 있는 heappop heappush

# # 2. 최대힙

# import heapq

# max_heap = []
# heapq.heappush(max_heap,-3)
# heapq.heappush(max_heap,-1)
# heapq.heappush(max_heap,-4)

# # 힙에서 빼고 나면 다시 -를 붙여서 양수로 바꾼다
# while max_heap:
#     print(-heapq.heappop(max_heap), end = ' ')

# # 3. 다중조건의 합
# import heapq
# pq =[]
# heapq.heappush(pq, (2,'A'))
# heapq.heappush(pq, (2,'B')) # 같은 정수면 문자열 비교(사전순서)
# heapq.heappush(pq, (4,'C'))

# while pq:
#     # 2가 같은데 A가 B보다 사전수이 빠르므로 먼저나옴
#     print(heapq.heappushpop(pq))

# # 문자우선, 그 다음 숫자 우선
# import heapq
# pq = []
# data = [(7,'A'),(9,'C'),(7,'C'),(6,'D'),(5,'A')]
# for num, char in data:
#     heapq.heappush(pq,(char,-num))
# while pq:
#     char,num = heapq.heappop(pq)
#     print(f'({-num}, {char})', end =' ')


# # 전략
# # while문: 한마리만 남을 때 까지 병합
# # 가장 작은 미생물 두마리를 꺼낸다(heappop(pq))
# # 새로운 미생물 생성 new_size = size1 +size2
# # 사전순으로 앞에 있는 이름을 선택 ---> min 내장함수
# # 새로운 미생물을 힙에 넣기(heappush)



# import heapq
# pq = []
# temp1 = []
# temp2 = []
# heapq.heappush(pq, (2,'BHC'))
# heapq.heappush(pq, (1,'NENE'))
# heapq.heappush(pq, (3,'KFC'))
# heapq.heappush(pq, (1,'BBQ'))
# heapq.heappush(pq, (2,'Moms'))
# heapq.heappush(pq, (4,'Mc'))


# while len(pq) > 1:
#     temp1 = heapq.heappop(pq)
#     temp2 = heapq.heappop(pq)
#     sum_ = temp1[0] + temp2[0]
#     sum_string = min(temp1[1],temp2[1])
#     heapq.heappush(pq,(sum_,sum_string))

# print(f'{pq[0][1]} {pq[0][0]}')

# # sort() 쓴다면
# # sort() : O(NlogN)
# # 가장 우선순위 높은 2명뽑기 O(1)
# # 이걸 N번 반복(반복문) : O(N^2logN
                  
# # P.Q 쓴다면
# # pop 두번 : O(2logN)
# # push 한번 : O(logN)
# # 이걸 N번 반복 O(NlogN)
