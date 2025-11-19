import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    P = list(map(lambda x: int(x) - 1, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    visited = [False] * N
    cycles = []
    
    # Find all cycles in the permutation P
    for i in range(N):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = P[j]
            cycles.append(cycle)

    total_dp = {(0, 0): 0}

    # Evaluate contributions from cycles
    for cycle in cycles:
        m = len(cycle)

        current_dp = [[-1] * (m + 1) for _ in range(m + 1)]
        current_dp[0][0] = 0

        # Enumerate through all possible configurations for each cycle
        for mask in range(3 ** m):
            b = []
            a0 = a1 = a2 = 0
            t = mask
            for _ in range(m):
                v = t % 3
                t //= 3
                b.append(v)
                if v == 0: a0 += 1
                elif v == 1: a1 += 1
                else: a2 += 1
            score = 0
            
            # Compute the score for this particular configuration
            for i in range(m):
                x, y = b[i], b[(i + 1) % m]
                if (x == 0 and y == 1) or (x == 1 and y == 0):
                    score += 2
                elif x == 0 and y == 0:
                    score += 1
                elif (x == 0 and y == 2) or (x == 2 and y == 0):
                    score += 1
            
            if current_dp[a0][a1] < score:
                current_dp[a0][a1] = score

        new_dp = {}
        for (u0, u1), val in total_dp.items():
            for a0 in range(m + 1):
                for a1 in range(m + 1 - a0):
                    sc = current_dp[a0][a1]
                    if sc >= 0:
                        key = (u0 + a0, u1 + a1)
                        new_dp[key] = max(new_dp.get(key, -1), val + sc)
        
        total_dp = new_dp

    for a0, a1, a2 in queries:
        print(total_dp.get((a0, a1), 0))

if __name__ == "__main__":
    solve()