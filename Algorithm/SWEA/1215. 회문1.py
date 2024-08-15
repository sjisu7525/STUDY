for tc in range(1, 11) :
    n = int(input())
    txt = [list(str(input())) for _ in range(8)]
    txt_trans = list(zip(*txt)) # 전치행렬
    cnt = 0
    for i in range(8) :
        for j in range(9-n) :
            if txt[i][j:j+n] == txt[i][j:j+n][::-1] :
                cnt += 1
            if txt_trans[i][j:j+n] == txt_trans[i][j:j+n][::-1] :
                cnt += 1

    print(f'#{tc} {cnt}')

##############################################################
for tc in range(1, 11) :
       n = int(input())
       txt = [list(str(input())) for _ in range(8)]
       cnt = 0
       for i in range(8) :
              for j in range(9-n) :
                     if txt[i][j:j+n//2] == txt[i][j+n//2+n%2:j+n][::-1] : # n%2 : 홀수 고려
                            cnt += 1

       txt_trans = list(zip(*txt))
       for i in range(8) :
              for j in range(9-n) :
                     if txt_trans[i][j:j+n//2] == txt_trans[i][j+n//2+n%2:j+n][::-1] :
                            cnt += 1

       print(f'#{tc} {cnt}')


##############################################################
for tc in range(1, 11):
       n = 8
       m = int(input())
       arr = [list(str(input())) for _ in range(n)]
       cnt = 0

       # 가로
       for i in range(n):
              for j in range(n - m + 1):
                     for k in range(m // 2):
                            if arr[i][j + k] != arr[i][j + m - 1 - k]:
                                   break  # 다음 글자로
                     else:  # for 문을 다 돌았다면 회문 존재
                            cnt += 1
       # 전치행렬
       for i in range(n):
              for j in range(n):
                     if i < j:
                            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
       # 세로
       for i in range(n):
              for j in range(n - m + 1):
                     for k in range(m // 2):
                            if arr[i][j + k] != arr[i][j + m - 1 - k]:
                                   break  # 다음 글자로
                     else:  # for 문을 다 돌았다면 회문 존재
                            cnt += 1
       print(f'#{tc} {cnt}')