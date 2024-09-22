from collections import deque
T = int(input())

def bfs(q) :
    while q :
        i, j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]] :
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0 :
                visited[ni][nj] = 1 # 방문
                q.append([ni,nj])


for _ in range(T) :
    m, n, k = map(int,input().split()) #가로, 세로, 배추개수
    arr = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    cnt = 0 # 지렁이 수
    for _ in range(k) :
        j, i = map(int,input().split())
        arr[i][j] = 1 # 배추가 있는 곳

    for i in range(n):
        for j in range(m) :
            if arr[i][j] == 1 and visited[i][j] == 0 : # 배추 있고 안본곳
                cnt += 1
                q = deque([[i,j]])
                visited[i][j] = 1
                bfs(q)

    print(cnt)
