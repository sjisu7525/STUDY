for _ in range(10) :
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 시작점들 위치 찾기
    start = [i for i in range(100) if ladder[0][i] == 1]
    min_len = 10000

    # 이동 : 한칸씩 할 필요가 없음★
    for s in start : # 각 시작점들에 대해서
        len_cnt = 0 # 거리 측정
        r, c = 0, s
        while r < 99 : # 마지막 행에 올때까지
            # 왼쪽이동
            if c - 1 >= 0 and ladder[r][c-1] == 1 :
                while c - 1 >= 0 and ladder[r][c-1] == 1: # 왼쪽 이동이 가능할 때 까지
                    c -= 1 # 왼쪽으로 이동
                    len_cnt += 1
            # 오른쪽이동
            elif c + 1 <= 99 and ladder[r][c+1] == 1 :
                while c + 1 <= 99 and ladder[r][c+1] == 1: # 오른쪽 이동이 가능할 때 까지
                    c += 1 # 오른쪽으로 이동
                    len_cnt += 1
            r += 1 # 이동 후 아래로
            len_cnt += 1
        if len_cnt < min_len  :
            min_len = len_cnt
            min_start = s

    print(f'#{tc} {min_start}')



##########################################################
# for _ in range(10):
#     tc = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#
#     # 시작점들 위치 찾기
#     start = [i for i in range(100) if ladder[0][i] == 1]
#     # 이동
#     dir = [[0,-1],[0,1],[1,0]] # 이동 방향(좌우 이동 먼저)
#     min_len = 10000
#     for c in start : # 각 시작점들에 대해서
#         len_cnt = 0 # 거리 측정
#         r = 0
#         while r < 99 : # 마지막 행에 올때까지
#             if len_cnt >= min_len : # 도착을 못했는데 이미 최소 거리보다 크거나 같은 경우
#                 break
#             for x, y in dir :
#                 nr, nc = r + x, c + y
#                 if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1 :
#                     ladder[nr][nc] = 2 # 방문 표시
#                     len_cnt += 1
#                     r, c = nr, nc
#                     break
#         if len_cnt < min_len  :
#             min_len = len_cnt
#             min_start = c
#     print(f'#{tc} {min_start}')
