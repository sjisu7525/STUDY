n = int(input())
max_len = 1
for i in range(n//2,n+1) :
    lst = [n]
    v1, v2 = n, i # 첫번째, 두번째 수
    while v2 >= 0 :
        lst += [v2]
        v1,v2 = v2, v1-v2
    if max_len < len(lst) :
        max_len = len(lst)
        ans = lst
print(max_len)
print(*ans)