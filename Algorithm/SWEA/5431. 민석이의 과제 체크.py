T = int(input())
for tc in range(1, T+1) :
    n, k = map(int, input().split())
    s = set(map(int, input().split()))
    student = set(range(1, n+1))
    print(f'#{tc}', *list(student-s))