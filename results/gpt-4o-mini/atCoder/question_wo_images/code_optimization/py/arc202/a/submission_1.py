def solve(N, A):
    A.sort()
    ans = 0
    current_value = 0
    
    for num in A:
        if num > current_value:
            current_value = num
        else:
            ans += current_value - num + 1
            current_value += 1
            
    return ans

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))