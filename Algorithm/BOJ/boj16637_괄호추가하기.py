def cal(a,b,op) :
    if op == '+' :
        return a+b
    if op == '-' :
        return a-b
    if op == '*' :
        return a*b

def func(num, i) : # num : 연산자 앞의 숫자 i : 연산자가 있는 위치
    global max_val
    if i >= n : # 연산이 끝난 경우
        max_val = max(max_val, num) # 최대값 갱신
        return

    # 연산자 뒤에 괄호가 없는 경우
    func(cal(num, int(f[i+1]), f[i]), i+2)

    # 연산자 뒤에 괄호가 있는 경우
    if i+3 < n :
        func(cal(num, cal(int(f[i+1]), int(f[i+3]), f[i+2]), f[i]), i+4)

n = int(input())
f = list(str(input()))
max_val = -(2**31)
func(int(f[0]), 1)
print(max_val)