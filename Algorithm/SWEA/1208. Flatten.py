def counting_sort(lst) :
    cnt = [0]*101
    sort_lst = [0]*len(lst)
    for x in lst :
        cnt[x] += 1
    
    for i in range(1,101) :
        cnt[i] += cnt[i-1]
    
    for i in range(len(lst)-1, -1,-1) :
        sort_lst[cnt[lst[i]]-1] = lst[i]
        cnt[lst[i]] -= 1 
    return sort_lst


for tc in range(1,11) :
    dump = int(input())
    lst = list(map(int, input().split()))
    # lst.sort()
    lst = counting_sort(lst)
    print(lst)

    for i in range(dump) :
        lst[0] += 1
        lst[-1] -= 1
        lst.sort()
    
    print(f'#{tc} {lst[-1]-lst[0]}')
