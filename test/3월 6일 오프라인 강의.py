# 문제 푸는 방식

# 0<= n<= 20 -> 재귀부터 가장 먼저 생각해 본다.
# n이 커지면 한 500 이면 재귀는 생각도하지마라!

# n =50 ~ 100정도이고, 최소값 또는 최대값을 찾아라
# => BFS로 풀어라

# n = 10만 -> 2중 for 조차 생각 x => 1중 for문

# # 투포인터 알고리즘 시작
# def two_pointer():
#     left = 0 # 왼쪽 포인터는 0에서 시작
#     right = len(arr) -1 # 오른쪽 포인터는 배열의 긑에서 시작

#     while left < right: # 두포이터가 만나면 반복문 종료
#         sum_v = arr[left] + arr[right]

#         if sum_v == m:
#             print(left, right)
#             return
#         elif sum_v<m: # 현재의 합이 타겟합(m)보다 작으면
#             left +=1 # 왼쪽 포인터를 오른쪽으로 이동시켜서(합을 증가시키기 위해)
#         else:
#             right -= 1 # 오른쪽 포인터를 왼쪽으로 이동(합을 감소시키기 위해)
#     print("찾을 수 없음")

# n,m = map(int,input().split())
# arr = list(map(int, input().split()))
# two_pointer()

# n, target = map(int(int,input().split()))
# arr = list(map(int, input().split()))
# cnt , sum_v = 0,0
# left, right = 0, 0 # left의 시작점도 0,right 의 시작점도 0

# while True:
#     # 합이 타겟 이상이거나 끝에 도달했을 때
#     if sum_v >= target or right ==n:
#         sum_v -= arr[left] # 구간 축소니깐 sum_v에서 left값 빼기
#         left += 1
#     elif sum_v < target:
#         sum_v += arr[right] # 구간 확대니까 sum_v에서 right값 더하기
#         right += 1 # 구간 확대
#     # 현재 합이 target과 같으면 카운팅
#     if sum_v == target:
#         cnt += 1
#     if left == n: break
# print(count)

1.sort : 선수들의 실력을 오름차순 정렬
2. 투포인터 : left, right
    2-1. 실력차이가 k 초과면 ---> 범위를 좁힘(left증가)
    2-2. 실력차이가 k 이하면 ---> 범위르 넓힘(right증가)
