T = int(input())
for tc in range(1, T+1) :
    N, M, K = map(int, input().split())
    wait = list(map(int, input().split()))
    wait.sort()
    result = 'Possible'
    for i in range(N) :
        # 내가 왔을 때까지 만들어진 붕어빵 수 - 나 이전 손님 수
        if wait[i]//M * K - i < 1 : # 내 붕어빵은 없음
            result = 'Impossible'
            break

    print(f'#{tc} {result}')

######################################################
# T = int(input())
# for tc in range(1, T+1) :
#     N, M, K = map(int, input().split())
#     wait = list(map(int, input().split()))
#     wait.sort()
#
#     # 0초부터 만들기 시작, M초의 시간을 들이면 K개의 붕어빵
#     sec = 0 # 현재 시각
#     bung_num = 0 # 현재 있는 붕어빵 수
#     result = 'Possible'
#     while  wait :
#         sec += 1
#         if sec % M == 0 : # M초 후
#             bung_num += K # k개 붕어빵 만들어짐
#         if sec == wait[0] : # 손님이 도착하고
#             if bung_num > 0 : # 붕어빵이 있다면
#                 bung_num -= 1 #  붕어빵을 주고
#                 wait.pop(0) # 손님을 보낸다.
#             else : # 붕어빵이 없어
#                 result = 'Impossible'
#                 break
#     print(f'#{tc} {result}')

