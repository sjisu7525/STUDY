T = int(input())
for tc in range(1, T+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    max_sum = 0
    for i in range(n-m+1) : # 행번호
        for j in range(n-m+1) : # 열번호
            s = 0
            for k in range(m) :
                s += sum(arr[i+k][j:j+m]) #sum 대신 for문 한번더 돌아도 가능..
            if max_sum < s :
                max_sum = s 
    print(f'#{tc} {max_sum}')