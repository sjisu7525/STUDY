for tc in range(1, 11) :
    tc = int(input())
    txt = [list(str(input())) for _ in range(100)]
    txt_trans = list(zip(*txt)) # 전치행렬
    max_num = 0
    for i in range(100) :
        for j in range(100) :
            for k in range(j+1, 101) :
                if txt[i][j:k] == txt[i][j:k][::-1] :
                    if len(txt[i][j:k]) > max_num :
                        max_num = len(txt[i][j:k])
                if txt_trans[i][j:k] == txt_trans[i][j:k][::-1] :
                    if len(txt_trans[i][j:k]) > max_num :
                        max_num = len(txt_trans[i][j:k])

    print(f'#{tc} {max_num}')