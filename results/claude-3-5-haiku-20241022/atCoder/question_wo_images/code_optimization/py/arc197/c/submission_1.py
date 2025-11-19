import sys
input = sys.stdin.readline

MAX_N = 200005
s = list(range(MAX_N))
removed = [False] * MAX_N

q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    
    if a < MAX_N:
        for i in range(a, MAX_N, a):
            removed[i] = True
    
    count = 0
    idx = 0
    while count < b:
        if not removed[idx]:
            count += 1
            if count == b:
                print(idx)
                break
        idx += 1