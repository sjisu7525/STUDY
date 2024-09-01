import sys
n, p = map(int, sys.stdin.readline().split())
c = [[0] for _ in range(7)]  # 6줄
cnt = 0
for _ in range(n):
    line, fret = map(int, sys.stdin.readline().split())

    # 같은 줄에 나보다 높은 음이 있는 경우
    while c[line][-1] > fret:
        c[line].pop()
        cnt += 1

    # 높은 음을 다 뗀 후, 마지막 음이 나보다 작은 경우 눌러줘야함.
    if c[line][-1] < fret:
        c[line] += [fret]
        cnt += 1

print(cnt)

############# 시간초과 ############# 
n, p = map(int, input().split())
c = [[0] for _ in range(7)]  # 6줄
cnt = 0
for _ in range(n):
    line, fret = map(int, input().split())

    while c[line][-1] > fret:
        c[line].pop()
        cnt += 1

    if c[line][-1] < fret:
        c[line] += [fret]
        cnt += 1

print(cnt)