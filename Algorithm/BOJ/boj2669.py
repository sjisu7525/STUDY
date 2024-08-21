arr = [[0]*100 for _ in range(100)]
for _ in range(4) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2) : # 행범위
        arr[i][x1:x2] = [1]*(x2-x1) # 열범위
print(sum([sum(row) for row in arr]))