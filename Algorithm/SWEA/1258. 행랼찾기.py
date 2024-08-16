T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    row = [] # 행 길이
    col = [] # 열 길이
    s = [] # 넓이

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] > 0 : # 용기의 시작
                # 용기의 시작이 아니라 이어지는 부분인 경우
                if (0 <= i-1 < n and arr[i-1][j] != 0) or (0 <= j-1 < n and arr[i][j-1] != 0)  :
                    continue
                tmp = 1
                for di, dj in [[1,0] , [0,1]] :
                    ni, nj = i + di, j + dj
                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 0 : # 용기가 끝날 때까지 
                        ni, nj = ni + di, nj + dj
                    if di == 1 : # 행방향
                        row += [ni-i]
                        tmp *= ni-i
                    else :
                        col += [nj-j]
                        tmp *= nj-j
                s += [tmp]
    info = list(zip(s,row, col))
    info.sort()
    print(f'#{tc} {len(info)}' , end =' ')
    for s,r,c in info :
        print(r,c, end =' ')
    print()