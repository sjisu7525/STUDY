def coloring(paper,x1, y1, x2, y2, col) :
    for x in range(x1, x2+1) :
        for y in range(y1,y2+1) :
            paper[x][y] += col


T = int(input())
for tc in range(1,T+1) :
    n = int(input())
    paper = [[0]*10 for _ in range(10)]

    for _ in range(n) :
        x1, y1, x2, y2, col = map(int, input().split())
        coloring(paper, x1, y1, x2, y2, col)

    print(f'#{tc} {sum([row.count(3) for row in paper])}')
