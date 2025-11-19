import sys
input = sys.stdin.readline

def main():
    N, L = map(int, input().split())
    d = list(map(int, input().split()))

    # If L is not divisible by 3, no equilateral triangle can be formed
    if L % 3 != 0:
        print(0)
        return

    step = L // 3

    # Compute positions of points on the circle
    pos = [0] * N
    for i in range(1, N):
        pos[i] = (pos[i-1] + d[i-1]) % L

    # Map position to list of indices (points)
    pos_map = {}
    for i, p in enumerate(pos, 1):
        if p not in pos_map:
            pos_map[p] = []
        pos_map[p].append(i)

    ans = 0
    # For each point a, find points b and c such that:
    # pos[b] = (pos[a] + step) % L
    # pos[c] = (pos[a] + 2*step) % L
    # and a < b < c
    for a in range(1, N+1):
        p_a = pos[a-1]
        p_b = (p_a + step) % L
        p_c = (p_a + 2*step) % L

        if p_b in pos_map and p_c in pos_map:
            # We want to count triples (a,b,c) with a < b < c
            # pos_map[p_b] and pos_map[p_c] are sorted lists of points at those positions
            # Use binary search to find how many b > a and c > b
            b_list = pos_map[p_b]
            c_list = pos_map[p_c]

            # Find number of b > a
            import bisect
            b_start = bisect.bisect_right(b_list, a)
            for b_idx in range(b_start, len(b_list)):
                b = b_list[b_idx]
                # For each b, find number of c > b
                c_start = bisect.bisect_right(c_list, b)
                ans += len(c_list) - c_start

    print(ans)

if __name__ == "__main__":
    main()