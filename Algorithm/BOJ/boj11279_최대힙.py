from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n) :
    num = int(input())

    if num == 0 :
        if heap :
            print(heappop(heap)[1])
        else :
            print(0)
    else :
        heappush(heap,(-num, num))