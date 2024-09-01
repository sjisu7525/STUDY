N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
idx = [5,3,4,1,2,0] # 마주보는 면
max_val = 0
def dice(lst,bot) :
    global s
    if bot == 0 or bot == 5 :
        s += max(lst[1:5])
    elif bot == 1 or bot == 3 :
        s += max(lst[0],lst[2],lst[4],lst[5])
    elif bot == 2 or bot == 4 :
        s += max(lst[0], lst[1], lst[3], lst[5])
    top = lst[idx[bot]] # 주사위 윗면의 숫자
    return top

for i in range(6) :
    s = 0
    top = dice(arr[0], i) # i번째 면을 바닥으로 시작
    for j in range(1,N) :
        bot = arr[j].index(top) # 다음 주사위, top 숫자가 적힌 곳 = 바닥면
        top = dice(arr[j], bot)
    if max_val < s :
        max_val = s

print(max_val)