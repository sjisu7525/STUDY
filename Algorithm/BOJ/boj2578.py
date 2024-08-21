def nbingo(arr) :
    arr_trans = list(zip(*arr))
    cnt = 0 # 빙고 개수
    for i in range(5) :
        if sum(arr[i]) == 0 :
            cnt += 1
        if sum(arr_trans[i]) == 0 :
            cnt += 1
    # 대각선
    if sum([arr[i][i] for i in range(5)]) == 0 :
        cnt += 1
    if sum([arr[i][4-i] for i in range(5)]) == 0:
        cnt += 1
    return cnt

def rm(x):
    for i in range(5) :
        for j in range(5) :
            if my_bingo[i][j] == x :
                my_bingo[i][j] = 0
                return

my_bingo = [list(map(int, input().split())) for _ in range(5)]
seq = [] # 사회자가 말한 순서
for _ in range(5) :
    seq += list(map(int, input().split()))
cnt = 0

for x in seq :
    cnt += 1
    rm(x)
    n = nbingo(my_bingo)
    if n >= 3 :
        print(cnt)
        break