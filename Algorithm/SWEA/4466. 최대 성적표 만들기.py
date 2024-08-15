T = int(input())
for tc in range(1, T+1) :
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse= True)

    print(f'#{tc} {sum(score[:k])}')

#################################################
def dfs(i, s, depth):
    global max_score
    if depth == k:  # 종료 조건: 선택한 원소의 개수가 k일 때
        if max_score < s:  # 점수 갱신
            max_score = s
        return
    for j in range(n):
        if visited[j] == 0:  # 방문하지 않은 원소를 선택
            visited[j] = 1
            dfs(j, s + score[j], depth + 1)
            visited[j] = 0  # 백트래킹: 방문 해제

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    max_score = 0
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        dfs(i, score[i], 1)
        visited[i] = 0  # 백트래킹: 방문 해제
    print(f'#{tc} {max_score}')