# list나 튜플은 안에 요소가 바뀌어도 주소가 바뀌지않음


# 할당은 몇번 이뤄졌을까?
# a=[]
# a= [1,1,1]
# a.append(1)
# a=[2,2,2,6]
# a.append(5)
# print(a)
# -> 3번 이뤄 졌음 append는 요소 값을 추가 한 것

#  리스트
#   - 리스트는 가변이다
#   - iterable

#  -리스트에서 마지막 값을 출력
# arr = [1, 5, 2, 7, 3, 6]
# a = arr[0]
# a.append(arr[len(arr)-1])
# a.append(arr[-1])
# a = arr[::2]
# a = arr[3:]
# print(a)

# arr= []                         vs              arr=[0]*6
# for i in range(6):
#     arr.append(0)

#                                                 파이써닉하다(간결하고 명확하게 의도가 표현되고 가독성이 좋은 코드)

# tuple
# 내부 값을 정의할 수 없는 하나의 값 덩어리이다

# a= 1,2,3
# a=(1,2,3)
# 둘다 모두 튜플

# list              vs               tuple
#     공통점: 두개 모두 여러개의 Elements로 구성된 하나의 객체

#                   차이점
# 값 수정가능                         값 수정 불가
# 나이키 박스                         나이키 박스 + 나이키 신발

# **튜플을 써야하는 이유?
# 성능: 성능이 훨씬 빠르다
# 안전성: 안정성 내부 값을 수정할 수 없어 안전한 프로그래밍 가능


# range(start,end,step)

# 딕셔너리(dictionary)
#  1. 하드코딩 my_dict={'apple': 12,'list':[1,2,3]} --> 하드 코딩할 때 중괄호를 사용
#  2. my_dict={} my_dict=dict()--> 딕셔너리
#     my_dict=set()
#     my_dict=['apple']=12


# {
# abc = [1, 2, ('A', 'B'), [1, 2, [('kfc', 'moms', 'bhc')]]]

# print(abc[0])
# print(abc[2])
# print(abc[2][0])
# print(abc[3][2][0])  # kfc moms bhc
#                                                                   }

# {
# d = dict()
# d["hi"] = [1, 2, 3, "kfc1"]
# d["oh"] = [1, 5, {"ho": 14, "my": 119, "qq": "kfc2"}]
# d[-153] = [(1, 2, (5, 6, "kfc3"))]
# # kfc1~3을 출력
# print(f'{d["hi"][3]}')
# print(f'{d["oh"][2]["qq"]}')
# print(f'{d[-153][0][2][2]}')
# }

# boolean -True,False
# True =1 False =0

# 부호는 등호 앞에쓴다 <=, >=, ==
# not =! ->a!=b

# a=[1,2,3]
# b=[1,2,3]
# 서로 다른 객체(메모리 주소가 다름)

# b=a 를 하면 메모리 주소가 같아져서 True로 나와서 is사용가능 a is b


#단축평가
#if 조건식에 활용이 많이됨
#and 는 모두다 참이어야 참이다.
#or 은 하나라도 참이면 참이다.

