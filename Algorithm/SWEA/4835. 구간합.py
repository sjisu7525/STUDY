T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    min_sum = sum(lst[0:0+m])
    max_sum = sum(lst[0:0+m])
    for i in range(1, n-m+1) :
        if min_sum > sum(lst[i:i+m]) :
            min_sum = sum(lst[i:i+m])
        if max_sum < sum(lst[i:i+m]) :
            max_sum = sum(lst[i:i+m])
    print(f'#{tc} {max_sum - min_sum}')