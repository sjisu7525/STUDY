n,m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

q = [(0,0)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
while q :
    x, y = q.pop(0)

    if x == n-1 and y == m-1 : # 미로의 끝 도달
        print(visited[x][y]) # 거리 출력
        break

    for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]] :
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and miro[nx][ny] == 1 and visited[nx][ny] == 0 :
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))