# # import sys
# # sys.stdin = open("input.txt","r")
# n = int(input())
# path = []
# cnt=0
# sum= 0

# def KFC(lev,sum_v):
    
#     global cnt
#     if sum_v>10:
#         return
#     if lev == n:           
#         cnt +=1
#         return
            
#     for i in range(1,7):
#         path.append(i)
#         KFC(lev+1,sum_v+i)
#         path.pop()             
        
        


# KFC(0,0)
# print(cnt)

# # 두개의 탑

# def get_sum():
#     m1_lst = []
#     m2_lst = []
#     while True:
#         if lst and len(m1_lst) != m1:
#             m1_lst.append(lst.pop())
#         elif not lst: break

#         if lst and len(m2_lst) != m2:
#             m2_lst.append(lst.pop())
#         elif not lst: break

#         for i in range(m1):
#             m1_lst *= (i+1)
        
#         for i in range(m2):
#             m2_lst[i] *= (i+1)

#         return sum(m1_lst) + sum(m2_lst)
        
# T= int(input())
# for tc in range(1,T+1):
#     m1,m2,    


# # 계산식 후위표기법
# # 후위표기법 연산 함수

# exp ='(3+1)*3/4'
# print(eval(exp))      # 계산기 eval

# # 전략
# # 피연선자(숫자) 스택에 push 
# # 연산자를 만나면 스택에 두개의 숫자를 pop해서 계산
# # 계산 결과를 다시 스택에 push
# # 과정을 반복, 마지막에는 스택에는 딱 한개의 결과 값만

# # 예) 1 2 + 3 *
# # 1. '1' -> 스택에 push -> stack == [1]
# # 2. '2' -> 스택에 push -> stack == [1,2]
# # 3. '+' -> 두 개의 숫자를  pop -> 2,1을 계산 -> 3 
# # 4. 결과 3을 stack에 push -> stack == [3]
# # 5. '3'-> 스택에 push -> stack ==[3,3]
# # 6. '*'-> 두개의 숫자를 pop -> 3,3 을 계산 -> 9
# # 7. 결과 9를 stack에 push -> stack ==[9]
# # 8. '.' -> 종료, 결과 9를 return

# # 주의) 계산을 해야하는데 스택에 있는 숫자가 2개 미만 return 'error'
# # 주의) 마지막에 스택에 남아있는 숫자가 1개가 아니다. return 'error'

# def get_calculate(arr):
#     stack = []
#     for i in arr[:-1]: # '.' 제외하기 위해서
#         # 숫자면 스택에 push
#         if i.isdecimal():
#             stack.append(int(i))
#         # 연산자면 pop으로 빼서 연산하고, 다시 스택에 push
#         elif i in {'+','-','*','/'}:
#             if len(stack) <2: # 계산하려는데 숫자가 2개 미만
#                 return 'error'
#             b=stack.pop()
#             a=stack.pop()
#             if i =='+': stack.append(a+b)
#             elif i=='-': stack.append(a-b)
#             elif i=='*': stack.append(a*b)
#             elif i=='/': stack.append(a//b)

#     if len(stack) != 1:
#         return 'error'
#     return stack[0] # 남은 한개의 숫자를 return

# T= int(input())
# for tc in range(1,T+1):
#     Forth = input().split()
#     result = get_calculate(Forth)
#     print(f'#{tc} {result}')


