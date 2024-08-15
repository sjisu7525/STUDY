for _ in range(10) :
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 2 위치 찾기
    r = 99
    for i in range(100):
        if ladder[99][i] == 2 :
            c = i

    #
    dir = [[0,-1],[0,1],[-1,0]] # 이동 방향(좌우 이동 먼저)
    while r > 0 : # 0번행에 올때까지
        for x, y in dir :
            nr, nc = r + x, c + y
            if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1 :
                ladder[nr][nc] = 2 # 방문 표시
                r, c = nr, nc
                break

    print(f'#{tc} {c}')
