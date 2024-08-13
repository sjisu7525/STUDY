for _ in range(1,11) :
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    # 행/열
    for i in range(100):
        row = col = 0
        for j in range(100) :
            row += arr[i][j]
            col += arr[j][i]
        if row > result :
            result = row
        if col > result :
            result = col
    
    # 대각선
    c1 = c2 = 0
    for i in range(100) :
        c1 += arr[i][i]
        c2 += arr[i][99-i]
        if c1 > result :
            result = c1
        if c2 > result :
            result = c2    
    
    print(f'#{tc} {result}')
