import copy
# import sys
# sys.stdin = open('input.txt ','r')

n,q = map(int,input().split())
arr= [[] for _ in range(n+1)]
question = [[] for _ in range(q)]
for i in range(1,n+1):
    arr[i] = list(map(int,input().split()))

for i in range(q):
    question[i] = list(map(int,input().split()))


for i in range(q):
    start_start = question[i][0]
    end_end = question[i][1]

    check_start = arr[start_start]
    check_start_end = check_start[1]
    check_end = arr[end_end]
    check_end_start = check_end[0]
    count= 0
    if check_start_end < check_end_start:
        while check_start[1] < check_end[1]:

            count = 0
            max_end = 0
            temp_start =0

            for j in range(1, n+1):
                if j == start_start: continue
                if check_start[1] >= arr[j][0] and check_start[1] <= arr[j][1]:
                    if max_end < arr[j][1]:
                        max_end = arr[j][1]
                        count += 1
                        temp_start = arr[j]
                        start_start = j
                    else: continue

            check_start = copy.deepcopy(temp_start)

            if count != 0:
                continue
            else:
                break

    if count == 0:
        print(count)
    else:
        print(1)