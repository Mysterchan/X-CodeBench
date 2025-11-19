import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    visited = [False] * N
    cycles = []
    for i in range(N):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = P[j]
            cycles.append(cycle)

    contribs = []
    for cyc in cycles:
        m = len(cyc)
        
        # dp[pos][a0][a1][last] = max score
        # last is the value assigned to position 0 (for cycle closure)
        INF = -10**9
        dp = [[[[INF]*3 for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+1)]
        
        # Initialize: position 0, try each value
        for v0 in range(3):
            dp[1][int(v0==0)][int(v0==1)][v0] = 0
        
        # Fill positions 1 to m-1
        for pos in range(1, m):
            for a0 in range(pos+1):
                for a1 in range(pos+1-a0):
                    for last in range(3):
                        if dp[pos][a0][a1][last] == INF:
                            continue
                        curr_score = dp[pos][a0][a1][last]
                        
                        # Try assigning each value to position pos
                        for v in range(3):
                            # MEX contribution from edge (pos-1, pos)
                            if last == 0 and v == 1 or last == 1 and v == 0:
                                edge_score = 2
                            elif last == 0 and v == 0:
                                edge_score = 1
                            elif last == 0 and v == 2 or last == 2 and v == 0:
                                edge_score = 1
                            elif last == 1 and v == 1:
                                edge_score = 2
                            elif last == 1 and v == 2 or last == 2 and v == 1:
                                edge_score = 0
                            elif last == 2 and v == 2:
                                edge_score = 1
                            else:
                                edge_score = 0
                            
                            new_a0 = a0 + (1 if v == 0 else 0)
                            new_a1 = a1 + (1 if v == 1 else 0)
                            if new_a0 <= m and new_a1 <= m:
                                dp[pos+1][new_a0][new_a1][v] = max(
                                    dp[pos+1][new_a0][new_a1][v],
                                    curr_score + edge_score
                                )
        
        # Build result: need to close the cycle from position m-1 back to position 0
        result = [[INF]*(m+1) for _ in range(m+1)]
        for a0 in range(m+1):
            for a1 in range(m+1-a0):
                for v0 in range(3):
                    if dp[m][a0][a1][v0] == INF:
                        continue
                    # v0 is the value at position m-1, need to find value at position 0
                    # and add the closing edge score
                    for a0_last in range(a0+1):
                        for a1_last in range(a1+1):
                            last_val = 0 if a0_last < a0 else (1 if a1_last < a1 else 2)
                            if (a0_last + (1 if last_val==0 else 0) == a0 and
                                a1_last + (1 if last_val==1 else 0) == a1):
                                # Compute closing edge score
                                if v0 == 0 and last_val == 1 or v0 == 1 and last_val == 0:
                                    close_score = 2
                                elif v0 == 0 and last_val == 0:
                                    close_score = 1
                                elif v0 == 0 and last_val == 2 or v0 == 2 and last_val == 0:
                                    close_score = 1
                                elif v0 == 1 and last_val == 1:
                                    close_score = 2
                                elif v0 == 1 and last_val == 2 or v0 == 2 and last_val == 1:
                                    close_score = 0
                                elif v0 == 2 and last_val == 2:
                                    close_score = 1
                                else:
                                    close_score = 0
                                result[a0][a1] = max(result[a0][a1], dp[m][a0][a1][v0] + close_score)
        
        contribs.append(result)

    total_dp = {(0,0): 0}
    for result in contribs:
        m = len(result)-1
        new_dp = {}
        for (u0,u1), val in total_dp.items():
            for a0 in range(m+1):
                for a1 in range(m+1-a0):
                    if result[a0][a1] > INF:
                        key = (u0+a0, u1+a1)
                        new_dp[key] = max(new_dp.get(key, 0), val+result[a0][a1])
        total_dp = new_dp

    for a0,a1,a2 in queries:
        print(total_dp.get((a0,a1),0))

if __name__ == "__main__":
    solve()