T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    num = list(input())
    cnt = [0]*10
    # set,max 안쓰고 해보기
    for x in num :
        cnt[int(x)] += 1
    max_idx = 0
    max_cnt = 0
    for i in range(10) :
        if max_cnt <= cnt[i] :
            max_cnt = cnt[i]
            max_idx = i
    print(f'#{tc} {max_idx} {max_cnt}')