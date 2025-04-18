# # 트리!!
# # 트리  vs  그래프 
# # -> 트리의 특징
# # 1. cycle이 없다
# # 2. 부모 자식 관계가 있다.
# # 3. 단방향

# # 이진트리 : 트리인데 자식이 2개 이하면 이진트리
# #  - 특징 1. 최고 조상 노드를 1번으로 둔다
# #  - 특징 2. 왼쪽 자식은 *** 부모 index*2, 오른쪽 자식은 부목 index*2 + 1*** => 1차원 배열을 이용한다.
 

# # 전위순회
# bt = [0,'A','B','T','R','S','V']
# bt += [0]*100

# def dfs(now):

#     if bt[now] ==0 : return # 백트레킹

#     print(bt[now]) # 현재 노드 먼저 탐색
#     dfs(now*2) #왼쪽 자식 노드 탐색
#     dfs(now*2+1)# 오른쪽 자식 노드 탐색

# dfs(1) # 최고 조상 노드 root

# # 중위 순회
# bt = [0,'A','B','T','R','S','V']
# bt += [0]*100

# def dfs(now):

#     if bt[now] ==0 : return # 백트레킹

#     dfs(now*2) #왼쪽 자식 노드 탐색  
#     print(bt[now]) # 현재 노드 먼저 탐색
#     dfs(now*2+1)# 오른쪽 자식 노드 탐색

# dfs(1) # 최고 조상 노드 root

# # 후위 순회
# bt = [0,'A','B','T','R','S','V']
# bt += [0]*100

