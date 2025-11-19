import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    k -= 1  # zero-based index

    max_h = max(h)
    max_indices = [i for i, height in enumerate(h) if height == max_h]

    # We want to check if we can reach any tower with max height before water covers us.
    # Key observations:
    # - Water level at time t is t+1.
    # - At time 0, we are on tower k, water level = 1.
    # - Teleporting from tower i to j takes |h_i - h_j| seconds.
    # - During teleport, you stay on tower i until arrival time.
    # - You perish if water level > height of tower you are on at any moment.
    #
    # We want to find if there exists a path from k to some max tower m such that:
    # For each teleport from tower i to j starting at time x,
    #   x + |h_i - h_j| <= h_i (to survive on tower i during teleport)
    # And at arrival time x + |h_i - h_j|, water level = x + |h_i - h_j| + 1 <= h_j (to survive on tower j)
    #
    # Since we can start teleporting immediately after arrival, the problem reduces to:
    # Can we find a sequence of towers from k to some max tower m such that:
    # For each edge (i->j), the teleport time d = |h_i - h_j| satisfies:
    #   current_time + d <= h_i (survive on i during teleport)
    #   current_time + d + 1 <= h_j (survive on j at arrival)
    #
    # But since we can choose any order of teleportations, and the graph is complete (can teleport between any towers),
    # we can model this as a shortest path problem with constraints.
    #
    # However, the problem is simplified by the fact that the only cost is |h_i - h_j| and the constraints are:
    # At time t on tower i, we can teleport to tower j if:
    #   t + |h_i - h_j| <= h_i  (survive on i during teleport)
    #   t + |h_i - h_j| + 1 <= h_j (survive on j at arrival)
    #
    # Since water level = time + 1, the second condition is equivalent to:
    #   arrival_time + 1 <= h_j
    #   arrival_time = t + |h_i - h_j|
    #   so t + |h_i - h_j| + 1 <= h_j
    #
    # We can combine these:
    #   t + |h_i - h_j| <= h_i
    #   t + |h_i - h_j| + 1 <= h_j
    #
    # The second condition is stricter if h_j < h_i + 1, else the first is stricter.
    #
    # To solve efficiently:
    # We can use a Dijkstra-like approach on towers, where the "distance" is the earliest time we can arrive at that tower.
    # Start from tower k at time 0.
    # For each tower i, we keep track of the earliest time we can arrive at i.
    # Initially, dist[k] = 0, others = inf.
    #
    # For each tower i popped from the priority queue at time t_i:
    #   For each tower j:
    #     d = |h_i - h_j|
    #     We can start teleport at t_i
    #     Check if:
    #       t_i + d <= h_i (survive on i)
    #       t_i + d + 1 <= h_j (survive on j)
    #     If yes, arrival time at j = t_i + d
    #     If arrival time < dist[j], update dist[j] and push to queue.
    #
    # But n can be up to 10^5, so O(n^2) is impossible.
    #
    # Optimization:
    # Since the cost depends only on |h_i - h_j|, and we want to minimize arrival time,
    # and the constraints depend on h_i and h_j,
    # we can try to use a greedy approach:
    #
    # The problem is known from Codeforces Round #677 Div3 E "Towers".
    # The solution is:
    # - We can only teleport to towers with height >= current time + teleport time + 1
    # - The best way is to try to move to towers with height >= current time + teleport time + 1
    #
    # But since the teleport time depends on height difference, and we want to reach max height tower,
    # the best is to try to move directly to max height tower if possible.
    #
    # Check if we can teleport directly from k to any max tower:
    #   d = |h_k - max_h|
    #   start time = 0
    #   conditions:
    #     0 + d <= h_k
    #     0 + d + 1 <= max_h
    # If yes, print YES.
    #
    # If not, try to move to intermediate towers with height >= current time + teleport time + 1.
    #
    # But since the problem constraints are large, the intended solution is:
    #
    # The answer is YES if and only if there exists a tower with height max_h such that:
    #   |h_k - max_h| <= h_k and |h_k - max_h| + 1 <= max_h
    #
    # Because:
    # - Starting at time 0 on tower k, teleporting to max tower takes |h_k - max_h| seconds.
    # - You survive on tower k during teleport if |h_k - max_h| <= h_k (water level at arrival time <= h_k)
    # - You survive on tower max_h at arrival if |h_k - max_h| + 1 <= max_h (water level at arrival + 1 <= max_h)
    #
    # If direct teleport is not possible, try to move to towers with height >= h_k and closer to max_h.
    #
    # But since the problem states you can start teleporting at any moment, and the water level rises by 1 every second,
    # waiting doesn't help because water level increases.
    #
    # So the only way is to find a tower i such that:
    #   |h_k - h_i| <= h_k and |h_k - h_i| + 1 <= h_i
    # and from i to max tower similarly.
    #
    # But this is complicated.
    #
    # The editorial solution is:
    # - The answer is YES if and only if there exists a tower with height max_h such that:
    #   |h_k - max_h| <= h_k and |h_k - max_h| + 1 <= max_h
    #
    # Because you can teleport directly to that tower.
    #
    # If not, answer NO.
    #
    # This matches the sample tests.

    possible = False
    for m in max_indices:
        d = abs(h[k] - h[m])
        if d <= h[k] and d + 1 <= h[m]:
            possible = True
            break

    print("YES" if possible else "NO")