n, k = map(int, input().split())
temp = list(map(int, input().split()))
max_temp = sum(temp[0:k])
crr_temp = sum(temp[0:k])
for i in range(n-k) :
    crr_temp = crr_temp - temp[i] + temp[i+k] # 이전 합에서 앞에 제거 뒤에 추가
    if max_temp <  crr_temp :
        max_temp = crr_temp
print(max_temp)

########### 시간 초과 ########### 
n, k = map(int, input().split())
temp = list(map(int, input().split()))
max_temp = -100*n
for i in range(n-k+1) :
    seq_temp = sum(temp[i:i+k])
    if seq_temp > max_temp :
        max_temp = seq_temp
print(max_temp)