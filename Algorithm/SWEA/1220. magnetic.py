for tc in range(1, 11) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    # 1 : S극(아래)에 끌림, 2 : N극(위)에 끌림
    # 빨간색을 아예 내려버리기
    for i in range(100) :
        for j in range(100) :
            if arr[i][j] == 1 :
                if i == n-1 : # 끝에 도달
                    arr[i][j] = 0
                else :
                    if arr[i+1][j] == 0 : # 자성체가 없는 경우
                        arr[i][j] = 0
                        arr[i+1][j] = 1 # 이동
                    elif arr[i+1][j] == 2 : # 반대 자성체인 경우 교착
                        cnt += 1
    print(f'#{tc} {cnt}')