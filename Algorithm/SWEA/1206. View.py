for tc in range(1,11) :
    n = int(input())
    build = list(map(int, input().split()))
    ans = 0

    for i in range(2, n-2) :
        h = build[i] - max(build[i-2], build[i-1], build[i+1], build[i+2])
        if h > 0 :
            ans += h
    print(f'#{tc} {ans}')
