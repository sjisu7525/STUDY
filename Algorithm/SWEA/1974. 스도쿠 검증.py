T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    arr_trans = list(zip(*arr)) # 전치행렬
    result = 1
    # 행/ 열 검사
    for i in range(9):
        if len(set(arr[i])) != 9 : # 1~9가 모두 없다면
            result = 0
            break
        if len(set(arr_trans[i])) != 9 :
            result = 0
            break

    # 네모 검사
    if result == 1 :
        for i in range(0,9,3): 
            for j in range(0,9,3): # arr[i][j] : 3 x 3 크기의 작은 격자의 왼쪽 상단 셀 위치
                check = []
                for k in range(3) : # 3 x 3 크기의 작은 격자 내부 순환
                    for l in range(3) :
                        if arr[i+k][j+l] not in check : # 전에 없던 숫자라면 추가
                            check += [arr[i+k][j+l]]
                        else : # 전에 있던 숫자가 있다면
                            result = 0 
                            break # for l문 중단(함수로 하면 for i,j,k에 대해서 안돌아서 더 빠르게 탐색 가능할 듯)
    print(f'#{tc} {result}')