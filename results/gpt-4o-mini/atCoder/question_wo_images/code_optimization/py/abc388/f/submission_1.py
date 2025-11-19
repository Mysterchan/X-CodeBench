import sys

def solve():
    input = sys.stdin.readline
    N, M, A, B = map(int, input().split())
    
    bad_intervals = []
    for _ in range(M):
        l, r = map(int, input().split())
        bad_intervals.append((l, r))
    
    # If there are no bad squares, we can easily reach N
    if M == 0:
        print("Yes")
        return

    # Mark bad squares in a range
    bad_set = set()
    for l, r in bad_intervals:
        for i in range(l, r + 1):
            bad_set.add(i)

    can_reach = [False] * (B + 1)
    can_reach[0] = True  # Starting point
    
    for pos in range(1, N + 1):
        if pos in bad_set:
            continue
        
        # Check if we can come to this position from any allowed move
        for move in range(A, B + 1):
            if pos - move >= 1 and can_reach[(pos - move) % (B + 1)]:
                can_reach[pos % (B + 1)] = True
                break
            
        # If we can reach pos, check if we reached N
        if pos == N and can_reach[pos % (B + 1)]:
            print("Yes")
            return
            
    print("No")

solve()