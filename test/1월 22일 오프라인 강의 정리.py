# data = [{'has_more': False,
#          'next_cursor': None,
#          'object': 'list',
#          'page_or_database': {},
#          'request_id': 'a5163fff-758f-45ea-b6fb',
#          'results': [{'archived': False,
#                       'cover': None,
#                       'created_by': {'object': 'user'},
#                       'created_time': '2023-06-15T04:29:00.000Z',
#                       'icon': None,
#                       'last_edited_by': {'object': 'user'},
#                       'last_edited_time': '2023-12-12T09:19:00.000Z',
#                       'object': 'page',
#                       'parent': {'type': 'database_id'},
#                       'properties': {'setNum': {'id': '%7DK%40%5C',
#                                                 'number': 1,
#                                                 'type': 'number'},
#                                      '과목': {'id': 'YuIE',
#                                             'multi_select': [{'color': 'default',
#                                                               'name': 'Python'}],
#                                             'type': 'multi_select'},
#                                      '구분': {'id': '%40%3EmR',
#                                             'select': {'color': 'purple',
#                                                        'name': '실습'},
#                                             'type': 'select'},
#                                      '단계': {'id': 'T%7B%7BP',
#                                             'select': {'color': 'default',
#                                                        'name': '3'},
#                                             'type': 'select'},
#                                      '문제번호': {'id': 'uEBt',
#                                               'number': 1431,
#                                               'type': 'number'},
#                                      '제목': {'id': 'title',
#                                             'title': [{'annotations': {'bold': False,
#                                                                        'code': False,
#                                                                        'color': 'default',
#                                                                        'italic': False,
#                                                                        'strikethrough': False,
#                                                                        'underline': False},
#                                                        'href': None,
#                                                        'plain_text': '복잡한 자료구조',
#                                                        'text': {'content': '복잡한 자료구조',
#                                                                 'link': None},
#                                                        'type': 'text'}],
#                                             'type': 'title'},
#                                      '일차': {'id': 'nWnH',
#                                             'number': '2',
#                                             'type': 'number'},
#                                      '커리큘럼': {'id': 'T%3AR_',
#                                               'multi_select': [{'color': 'default',
#                                                                 'name': 'fundamentals-of-python'}],
#                                               'type': 'multi_select'}},
#                       'public_url': None
#                       }],
#          'type': 'page_or_database'}]


# target = data[0]['results'][0]['properties']

# 딕셔너리를 생성하는 2가지 방법
# 1. 하드코딩
# first_data ={
#     '제목' = target['제목']['title'][0]['plain_text']
# }
# 2. first_daya[key] =value
# first_data={}
# first_data['제목'] = target['제목']['title'][0]['plain_text']

# ===================================================================


# 알고리즘에서 함ㅅ를 사용하는 이유?(pycharm)
# -디버깅(유지 보수성)

# 웹에서 함수를 사용하는 이유? (현업)
# - 클라이언트의 요청에 따라 맞는 함수를 호출하기 위해서

# 함수 정의·선언
#   def 함수명(매개변수-parameter):
#   매개변수 없어도 됨
#   return 도 없어도됨

# 함수 호출
#   함수명(함수인자-argument)

# def get_sum():
#     num1 = 5
#     num2 = 3
#     sum_result = num1 + num2
#     print(sum_result)
# get_sum()

# 키워드 인자는 위치 인자 뒤에 위치해야함

# 함수를 재귀함수로 정의할 수 있는 근거 2가지
#  1. 재귀 호출(자기 자신을 호출)
#  2. 기저조건(종료 조건)


# 내장함수
#     map함수
#         map(function, iterable)
#         a=list(map(int,input().split()))

#     zip(*interable)


# x = 10  # global scope


# def outer_funtion():
#     x = 1  # outer_funtion 기준에서 x는 local scope

#     def inner_funtion():
#         y = 2  # inner_funtion 기준에서 y는 local scope

#         # inner_funtion 기준에서 outer_funtion의 변수 x에 접근 할 수 있는 범위
#         # enclosed scope
#         result = x + y

#         print(result)  # print 함수가 built-in scope

#     inner_funtion()


# outer_funtion()


# packing & unpacking
#   packing
# 하나의 변수에 묶는다 - tuple

# sep: str| None=" "       ===      print(1,2,3) => 1, 2, 3
#   ㄴ> 문자열을 " "으로 나눠서 출력


# iterable을 문자열로 출려
#     1. join 메서드
#     2. unpacking => * ,  **

# lambda함수를 쓰는 이유?
# 1. 일회성으로 사용할 때 효율적이다.(재사용 필요 없을 때)
# -> map함수랑 lambda함수랑 같이 쓰는 경우


# arr = [1, 2, 3, 4, 5]
# # 문제: 각각의 요소를 제곱해서 arr 출력
# # map, lambda함수 사용

# print(list(map(lambda x: x**2, arr)))
