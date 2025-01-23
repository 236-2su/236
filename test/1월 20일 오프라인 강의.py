# 1월 20일

import sys
sys.stdin = open("input.txt", "r")
# 오프라인 파이썬 정리
# 1월 20일
# <

# 알트 쉬프트 방향키 
# 	한줄 복사


# 단축키 바꾸기
# 	VS Code 메뉴에서 File > Preferences > Keyboard Shortcuts로 이동.
# 	"Run Python File" 또는 "Debug Python File"을 검색하여 단축키를 확인하거	나 변경할 수 있습니다.

# \n = 줄바꿈
# \' = 따옴표를 나타냄

# variable = expressions
# 	할당 연산자


# 변수명 규칙
# 	알파벳, 문자, 숫자 가능
# 	숫자 시작은 안됨 123x a_123 O
# 	대시 사용불가
# 	대소문자 구분
# 	내장 함수, 메서드, 파이썬은 사용 불가


# f-sting 출력


# pi = 3.141592
# print(f"{pi:.2f}")
# 그냥 외우고 
# 2f = 소수 둘째 자리

# id(a) =>  a 메모리 주소를 가르키는 함수

# deep copy/ shallow copy에서 할당이라는 개념이 필요함... ---- 나중에 배움


# 복소수 = 3+ 3j ----실수 + 허수


# a= 15
# b=[15]
# c=(1,2,3,4)
# d= 'string'
# e=2.3
# f= 3+3j
# g = True
# h = None
# print(type(a), type(b),type(c),type(d),type(e),type(f),type(g),type(h))




# a= 10
# a += 4



# n = input()
# print(n)



# a,b = map(int,input().split())
# print(a,b)



# c= list(map(int,input().split()))
# print(c)



# a= list(map(int, input().split()))
# print(a)
# a,b,c,d,e = map(int,input().split())
# print(a,b,c,d,e)



# string[start:end:step]
# 1. start> end
# start부터 end -1까지 step만큼 증가
# 2. end>start
# start 부터 end+1 까지  step 만큼 감소
# start가 생략되면 0부터
# end가 생략되면 끝까지
# step이 생략되면 step은 1
