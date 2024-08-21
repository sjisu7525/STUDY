def flat_line(lst) :
    dir, val = lst[0], lst[1]
    # 0,0을 기준으로 쫙 펼치기
    if dir == 2 : # 남
        return val
    if dir == 4 : # 동
        return x + (y-val)
    if dir == 1 : # 북
        return x + y + (x-val)
    if dir == 3 : # 서
        return 2*x + y + val

x, y = map(int, input().split())
store_num = int(input())
store = [flat_line(list(map(int, input().split()))) for _ in range(store_num)]
dong = flat_line(list(map(int, input().split())))

s = 0
for val in store :
    diff = abs(dong - val)
    s += min(diff, 2*x + 2*y - diff)
print(s)