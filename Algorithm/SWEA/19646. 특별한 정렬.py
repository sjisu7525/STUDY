T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    num = list(map(int, input().split()))
    num.sort(reverse = True)
    new = [0]*n

    for i in range(n) :
        if i % 2 == 0 :
            new[i] = num[(i//2)]
        else :
            new[i] = num[n-1-(i//2)]
    print(f'#{tc}', *new)