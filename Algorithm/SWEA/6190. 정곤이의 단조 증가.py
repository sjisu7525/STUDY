T = int(input())

def nonde(val) :
    lst = list(map(int,str(val))) # 28 : [2,8]
    for i in range(1,len(lst)) :
        if lst[i] < lst[i-1] :
            return False
    return True

for tc in range(1, T+1) :
    n = int(input())
    num = list(map(int, input().split()))
    max_num = -1
    for i in range(n) :
        for j in range(i+1, n) :
            val = num[i]*num[j] # 두 곱한 값이
            if nonde(val) : #단조증가이고
                if max_num < val : # 최대값이면 갱신
                    max_num = val
    print(f'#{tc} {max_num}')