# json 문법

# 유효성검사
# https: // jsonlint.com/

# json viewer
# http: // jsonviewer.stack.hu/

# 파이썬      json
# 딕셔너리    객체    {}
# 리스트      배열    []
# jsone에서 key는 반드시 문자열이여야 하며, 큰따옴표("")로 감싸야 한다.
# 다양한 타입의 값을 섞어서 사용가능하다.

# json에서 false, true - 소문자로 사용함
# json에서 None 은 null로 표현

# 중첩구조 - 객체 안의 배열, 배열안의 객체 중첩되어 있음
# 주석 사용 불가능
# 마지막 뒤에 , 사용 불가
# 들여쓰기는 가독성을 위한 선택사항항

# import json

# a = dict()
# a['name'] = 'sanghi'
# a['price'] = 4900
# a['brand'] = 'mcdonald'

# # Encoding 메서드 json.dump()
# b = json.dump(a, indent=2)
# # Decoding 메서드 json.loads()
# c = json.loads(b)
# print(c)

# json 파일 공유하는 사이트
# https: // github.com/jdorfman/awesome-json-datasets

# import requests
# import json
# url = 'https://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes'
# r = requests.get(url).text
# print(r)
