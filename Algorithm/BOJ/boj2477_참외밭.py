## 참외
n = int(input())

## 방향을 인덱스로 하고 순서와 거리를 담을 이차원 리스트 생성
info = [[] for _ in range(5)]
info_full = [] # 들어오는 순서대로 길이만 담을 리스트
for i in range(6) :
    d, l = map(int, input().split())
    info[d] += [i,l]
    info_full += [l]

big = 1
idx = [] # 작은 사각형의 가로 세로 인덱스
for i in range(1,5) :
    if len(info[i]) == 2:
        big *= info[i][1]
        idx += [(info[i][0]+3)%6]

small = info_full[idx[0]]*info_full[idx[1]]

print((big-small)*n)