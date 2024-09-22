num_list = list(range(1,10001))

for n in range(1, 10000) :
    dn = n + n//1000 + (n//100)%10 + (n//10)%10 + n%10
    if dn in num_list:
        num_list.remove(dn)

num_list.sort()
for num in num_list :
    print(num)