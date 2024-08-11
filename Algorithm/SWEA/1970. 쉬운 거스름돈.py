T = int(input())
changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 거스름돈 리스트
for tc in range(1, T+1) :
    pay = int(input())
    result = [0] *8 # 거스름돈 개수
    i = 0
    while i < 8 :
        result[i] = pay//changes[i] # 몫 == 사용한 거스름돈 수
        pay %= changes[i]
        
        if pay == 0 :
            break
        i += 1
    print(f'#{tc}')
    print(*result)