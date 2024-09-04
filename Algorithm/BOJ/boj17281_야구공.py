N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
max_s = 0 # 최대 득점


# 1번 선수를 제외한 순열생성
perm = []
visited = [0]*9
def permutaion(i): # 타자 순서로 가능한 순열
    if len(perm) == 8 : # 순서가 다 정해짐
        perm.insert(3, 0)  # 1번 선수를 4번 타자로 미리 결정
        order = perm[:]
        # print("======start=======")
        # print(order)
        playing(order)
        perm.pop(3)
        return

    for i in range(1,9) :
        if not visited[i] :
            visited[i] = 1
            perm.append(i)
            permutaion(i+1)
            perm.pop()
            visited[i] = 0


def playing(order):
    global max_s
    s = 0 # 득점수
    batter = 0 # 타자
    for n in range(N): # 각 이닝에 대해
        out = 0
        ru = [0, 0, 0] # 1,2,3루
        while out < 3:  # 삼진 아웃이 될 때까지
            result = scores[n][order[batter]]
            if result == 0: # 아웃
                out += 1
            elif result == 1: # 안타
                s += ru[2]
                ru = [1] + ru[:2]
            elif result == 2: # 2루타
                s += ru[1] + ru[2]
                ru = [0, 1] + ru[:1]
            elif result == 3: # 3루타
                s += sum(ru)
                ru = [0, 0, 1]
            elif result == 4: # 홈런
                s += sum(ru) + 1
                ru = [0, 0, 0]

            batter = (batter + 1) % 9 # 다음 타자

    max_s = max(max_s, s)

permutaion(1)
print(max_s)



############ 정답 ############
from itertools import permutations

N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
max_s = 0 # 최대 득점


# 1번 선수를 제외한 순열생성
o = [1,2,3,4,5,6,7,8]
orders = permutations(o,8)

for order in orders :
    order = list(order)
    order.insert(3,0)
    s = 0 # 득점수
    batter = 0 # 타자
    inning = 0
    out = 0
    ru = [0, 0, 0]  # 1,2,3루
    while inning < N :
        result = scores[inning][order[batter]]
        if result == 0: # 아웃
            out += 1
            if out == 3 :
                inning += 1
                out = 0
                ru = [0,0,0]
        elif result == 1: # 안타
            s += ru[2]
            ru[2] = 0
            if ru[1] == 1 :
                ru[2] = 1
                ru[1] = 0
            if ru[0] == 1:
                ru[1] = 1
            ru[0] = 1
        elif result == 2: # 2루타
            s += ru[1] + ru[2]
            ru[2], ru[1] = 0, 0
            if ru[0] == 1:
                ru[2] = 1
                ru[0] = 0
            ru[1] = 1
        elif result == 3: # 3루타
            s += ru[0] + ru[1] + ru[2]
            ru = [0,0,1]
        elif result == 4: # 홈런
            s += ru[0] + ru[1] + ru[2] + 1
            ru = [0, 0, 0]

        batter = (batter + 1) % 9 # 다음 타자

    max_s = max(max_s, s)

print(max_s)