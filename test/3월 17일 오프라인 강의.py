# # 분할, 정복, 병합
# def merge_sort(arr):
#     # 정복
#     if len(arr) <= 1:
#         return arr
#     # 분할
#     mid = len(arr)//2
#     # 왼쪽
#     left = merge_sort(arr[:mid])
#     # 오른쪽
#     right = merge_sort(arr[mid:])
#     # 병합 함수 호출
#     result = merge(left,right)
#     return result

# def merge(left,right):
#     result = []
#     i,j = 0,0
#     while i<len(left) and j < len(right):
#         if left[i] <= right[j]:
#             # 왼쪽 요소가 작거나 같다.
#             result.append(left[i])
#             i += 1
#         else:
#             # 오른쪽 요소가 작다
#             result.append(right[j])
#             j += 1
#     # while문 끝나면 남은 배열들, 남은 배열은 extend
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# arr= [64,34,25,12,22,11,90]
# sorted_arr=merge_sort(arr)
# print(sorted_arr)



# # quick 정렬
# # 분할
# # 1-1. 피벗 선택(len(arr)//2)
# # 1-2. 피벗 보다 작은 건 left, 같은건 middle, 큰건 right
# # 2. 정복: 길이가 1 이하면 return
# # 3. 병합: 순서대로 병함(left + middle + right)

# def quick_sort(arr):
#     # 정복
#     if len(arr) <= 1: return arr
#     # 피벗: len(arr)//2
#     pivot = arr[len(arr)//2]
#     # 피벗 보다 작은 element를 left 리스트에 담는다
#     left = [x for x in arr if x<pivot]
#     # 피벗과 같은 element를 middle 리스트에 담는다
#     middle = [x for x in arr if x == pivot]
#     # 피벗보다 큰 element는 right 리스트에 담는다
#     right = [x for x in arr if x>pivot]

#     result = quick_sort(left) + middle + quick_sort(right)

#     return result

# arr = [64,34,25,12,22,11,90]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)