num_dict = {
    "ZRO" : 0, 
    "ONE" : 1, 
    "TWO" : 2, 
    "THR" : 3, 
    "FOR" : 4, 
    "FIV" : 5, 
    "SIX" : 6, 
    "SVN" : 7, 
    "EGT" : 8, 
    "NIN" : 9
}
T = int(input())
for tc in range(1, T+1) :
    tc, N = map(str,input().split())
    N = int(N)
    num = list(map(str,input().split()))
    cnt = [0]*10
    ans = [0]*N

    for n in num :
        cnt[num_dict[n]] += 1
    
    for i in range(1,10) :
        cnt[i] += cnt[i-1]

    for i in range(N-1, -1, -1) :
        ans[cnt[num_dict[num[i]]]-1] = num[i]
        cnt[num_dict[num[i]]] -= 1
    print(tc)
    print(*ans)