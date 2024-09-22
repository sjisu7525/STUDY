import heapq

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
ans = 0

while len(card) > 1:
    a = heapq.heappop(card)  # 가장 작은 값
    b = heapq.heappop(card)
    ans += a + b
    heapq.heappush(card, a + b) 
print(ans)