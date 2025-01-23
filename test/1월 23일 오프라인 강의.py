# # 라이브러리 - 패키지 - 모듈
# # 1. 데이터 분석 - pandas 모듈 - 내부 패키지
# # 2. 인공지능 - open ai 모듈, 랭체인모듈 - 외부패키지
# # 3. request
# import requests
# import json
# url = "https://random-data-api.com/api/v2/users"

# response = requests.get(url).json()  # 딕셔너리로 변환(json())

# # 딕셔너리를 json변환
# response = json.dumps(response, indent=4)

# # 딕셔너리와 json의 차이
# # 1. json은 큰따옴표만 씁니다.
# # 2. key는 무조건 문자

# print(response)

# # 1. ctrl + shift +c 를 해서 json viewer에 붙여 넣어서 viewer로 보면 보기 쉬움
# # 2. response = json.dumps(response, indent=4), indent = 들여쓰기


# 도전 문제: 90점 이상 = A, 80점 이상 = B, 70점 이상 = C, 나머지 F 학점

# 정수를 입력받아 윤년인지 윤년이 아닌지 판별하는 프로그램
# 1. 4로 나누어 떨어지고, 100으로는 나누어 떨어지지 않는다
# 2. 400으로 나누어 떨어집니다.

# def def_leap_yer(number):
#     if (number % 4 == 0 and number % 100 != 0) or (number%400 ==0):
#         print(f"윤년이 아니다")
#     else:
#         print(f"윤년입니다.")


# year = int(input())
# def_leap_yer(year)

# <list+ for 문>
# indexing 방식, iterator  방식

# list_a = [0]*5
# a = 0
# for i in range(5):
#     list_a[i] = 5 + i

# print(*list_a)

# arr = [1, 5, 3, 4, 4, 2]
# sum_arr = 0
# for i in arr:
#     sum_arr += i
# print(f"{sum_arr}")

# num = 0
# max_arr = 0
# for i in range(0, len(arr)):
#     if num < arr[i]:
#         num = arr[i]


# print(num)

# def input_num():
#     a, b = map(int, input().split())

#     return a, b


# def output_num():
#     a, b = input_num()
#     for i in range(a, b+1):
#         print(i, end=" ")


# output_num()

# Dictionary + for 문

# a = [3, 3, 2, 6, 2]
# bucket = [0]*7

# for i in a:
#     bucket[i] += 1

# for i in range(1, 7):
#     print(str(i) + ':' + str(bucket[i]) + '개')


# # dictionary buildup
arr = ['MC', 'BTS', 'BTS', 'MC', 'BTS']

# di = dict()
# for i in arr:
#     di[i] = 0

# for i in arr:
#     di[i] += 1

# print(di)

# di = dict()
# for i in arr:
#     di[i] = 0

# for i in arr:
#     di[i] += 1
# num = 0
# max_dict = ''
# # di.keys() = key, di.values() = value, di.items() -> 두개를 한번에
# for key, value in di.items():
#     if num < value:
#         num = value
#         max_dict = key
# print(max_dict)


# break : 특정 조건에서 반복문을 종료(탈출)
# continue: 특정 조건에서 반복문 처음으로 돌아가기

# while 문 3가지
# 1. 초기식
# 2. 증감식
# 3. 조건식: 참인동안 반복
#     무한반복 while True:
#                  break


# # 중첩 for문 이용해서 출력해 보세요
# for i in range(2):

#     for j in range(3):
#         print('#', end="")
#     print()


# T = int(input())
# arr = []
# for i in range(1, T+1):
#     lst = list(map(int, input().split()))
#     arr.append(lst)

# print(arr)

# # 이 코드를 파이써닉하게 리스트컴프리헨션을 써서 소스 코드를 작성

# T = int(input())
# arr = [list(map(int, input().split())) for _ in range(T)]
# print(arr)

# enumerate(iterable, start=0) -> 중요
