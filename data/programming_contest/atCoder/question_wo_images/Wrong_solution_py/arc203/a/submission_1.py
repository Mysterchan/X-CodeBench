T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    if M == 1:
        print(1)
    else:
        print(N*M//2)