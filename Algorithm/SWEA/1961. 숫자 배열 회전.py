T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    ## arr : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    first = list(zip(*arr[::-1]))  ## [(7, 4, 1), (8, 5, 2), (9, 6, 3)]
    second = arr[::-1] ## [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    third = list(zip(*arr))[::-1] ## [(3, 6, 9), (2, 5, 8), (1, 4, 7)]
    print(f'#{tc}')
    for i in range(n) :
        print(''.join(first[i]), ''.join(list(reversed(second[i]))), ''.join(third[i]))
    