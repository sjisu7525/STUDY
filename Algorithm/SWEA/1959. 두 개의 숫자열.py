T = int(input())

def find_max(lst_large, lst_small,n1, n2) :
    max_sum = 0
    for i in range(n1-n2+1) : # 큰 리스트의 자리 옮겨가며
        s = 0
        for j in range(n2) : 
            s += lst_large[i+j]*lst_small[j] # 곱하기
        if max_sum < s :
            max_sum = s
    return max_sum
            
for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split())) 
      
    if n >= m :
        result = find_max(lst1, lst2, n, m)
    else :
        result = find_max(lst2, lst1, m, n)
        
    print(f'#{tc} {result}')