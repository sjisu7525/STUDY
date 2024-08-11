T = int(input())
def find_word(lst, n, m) :
    global cnt
    for i in range(n) :
        seq = 0 # 연속 개수 판단
        for j in range(n) :
            if lst[i][j] == 1 : # 단어가 들어갈 수 있는 자리
                seq +=1 # 연속 수 증가
                if j == n-1 and seq == m : # 마지막 셀이라면 연속 m 인 경우 cnt 증가
                    cnt += 1
            else :
                if seq == m : # 앞의 연속이 m 이었다면
                    cnt += 1
                seq = 0
for tc in range(1, T+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n) ]
    cnt = 0 # 길이m의 단어가 들어갈 수 있는 자리의 수
    
    find_word(arr, n, m)
    find_word(list(zip(*arr)), n, m)
    print(f'#{tc} {cnt}')
    