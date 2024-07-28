import sys
from collections import deque
import heapq
input = sys.stdin.readline
'''
deque를 쓰면 시간초과가 난다
heapq를 써야 통과한다
'''
count = 1
l_x = [0,1,0,-1]
l_y = [1,0,-1,0]
while True:
    n = int(input())
    if n==0:
        break
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    
    R = [[float("inf") for _ in range(n)] for _ in range(n)]
    R[0][0] = L[0][0]
    deq = []
    heapq.heappush(deq,(L[0][0],0,0))
    '''
    deq = deque()
    deq.append((L[0][0],0,0))
    '''
    while deq:
        val, a, b = heapq.heappop(deq)

        for i in range(4):
            ca, cb = a+l_x[i], b+l_y[i]
            if ca>=0 and cb>=0 and ca<n and cb<n:
                value = val+L[ca][cb]
                if value<R[ca][cb]:
                    R[ca][cb]=value
                    heapq.heappush(deq,(value, ca,cb))
    print("Problem {}: {}".format(count, R[-1][-1]))
    count+=1
