import sys
sys.stdin =open('input.txt', 'r')
def get_max_score(balloons, score=0):
    if not balloons:
        return score

    max_temp = float('inf')
    index = int()
    for i in range(len(balloons)):
        if i == 0:
            if len(balloons)>1:
                temp = balloons[i+1]
            else:
                temp = balloons[i] 
                
        elif i == len(balloons)-1 and len(balloons)>=2:
            temp = balloons[len(balloons)-2]
        else:
            temp = balloons[i-1]*balloons[i+1]
        if max_temp < temp:
            max_temp = temp
            index = i 
    temp_max = balloons.pop(index)
    get_max_score(balloons, score + temp_max)

    return


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    result = get_max_score(balloons)
    print(balloons)
    # print(f"#{tc} {result}")


