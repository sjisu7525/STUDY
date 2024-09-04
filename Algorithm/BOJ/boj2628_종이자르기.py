m, n = map(int, input().split())
w, l = [0], [0]
T = int(input())

w = w + [m]
l = l + [n]

for _ in range(T) :
  a, b = map(int, input().split())

  if a == 1 :
    w.append(b)
  else :
    l.append(b)


w.sort()
l.sort()

max_w = 0
max_l = 0
 
tmp = []
for i in range(len(w)-1) :
    for j in range(len(l)-1) :
        tmp.append((w[i+1]-w[i])*(l[j+1]-l[j]))
    
print(max(tmp))