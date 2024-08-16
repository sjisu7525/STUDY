T = int(input())
def coloring(col, lst):
    change = 0
    for row in lst : # 한 행씩
        for i in range(m) :
            if row[i] != col : # 색이 다르면 색칠
                change += 1
    return change


for tc in range(1, T+1) :
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n) ]
    min_cnt = n*m

    for i in range(1, n-1) : # i == 0인 경우 흰 색 없음
        for j in range(i+1,n) : # j == i인 경우
            cnt = 0
            cnt += coloring('W',arr[0:i])
            cnt += coloring('B',arr[i:j])
            cnt += coloring('R',arr[j:n])
            if min_cnt > cnt :
                min_cnt = cnt

    print(f'#{tc} {min_cnt}')