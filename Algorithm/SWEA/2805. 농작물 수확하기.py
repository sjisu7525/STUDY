T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n//2) :
        ans += sum(farm[i][n//2-i:n//2+i+1])
        ans += sum(farm[n-1-i][n//2-i:n//2+i+1])

    ans += sum(farm[n//2])
    print(f'#{tc} {ans}')
