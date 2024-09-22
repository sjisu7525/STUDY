import sys
input = sys.stdin.readline

n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m) :
    i,j = map(int,input().split())
    adj[i].append(j)
    adj[j].append(i)

min_cnt = 1e9  # 베이컨의 수
ans = 0 # 베이컨의 수가 가장 작은 사람
for i in range(1, n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    q = [[i, 0]]
    cnt = 0
    while q :
        now, c = q.pop(0)
        for next in adj[now] :
            if visited[next] == 0 : # 방문안한 친구
                visited[next] = 1
                q.append([next,c+1])
                cnt += c + 1
    if min_cnt > cnt : # 최소값 갱신
        min_cnt = cnt
        ans = i
print(ans)