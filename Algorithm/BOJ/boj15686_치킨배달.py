def chicken(start):
    global min_dis
    if len(stores) == m : # 상점의 개수가 m개인 경우
        tmp_dis = min_distance(homes,stores)
        min_dis = min(min_dis, tmp_dis)
        return

    for i in range(start, len(chicken_stores)) : # 치킨 집 조합
        stores.append(chicken_stores[i])
        chicken(i+1)
        stores.pop()

def distance(a,b) :
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def min_distance(homes, stores) : # 집과 가장 가까운 치킨집 거리들의 합
    total = 0
    for h in homes :
        total += min(distance(h, s) for s in stores)
    return total

## 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

homes = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 1] # 집 위치
chicken_stores = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 2] # 치킨 집 위치

stores = []
min_dis = 2*n*len(homes)

chicken(0)

print(min_dis)
