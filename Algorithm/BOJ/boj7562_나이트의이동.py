from collections import deque

T = int(input())
dir = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

def bfs(q) :
    global min_cnt
    while q :
        r, c, cnt = q.popleft()
        if cnt >= min_cnt:  # 이미 횟수가 최소가 아닌 경우
            continue
        if r == last_r and c == last_c:  # 도착
            min_cnt = min(min_cnt, cnt)
        for dr, dc in dir :
            nr, nc = r+dr, c+dc
            if 0<=nr<l and 0<=nc<l and visited[nr][nc] == 0 :
                visited[nr][nc] = 1
                q.append([nr,nc,cnt+1])

for _ in range(T) :
    l = int(input())
    r, c = map(int, input().split())
    last_r, last_c = map(int,input().split())
    visited = [[0]*l for _ in range(l)]
    min_cnt = l*l

    q = deque([[r,c,0]]) # 시작 위치, 횟수
    bfs(q)
    print(min_cnt)