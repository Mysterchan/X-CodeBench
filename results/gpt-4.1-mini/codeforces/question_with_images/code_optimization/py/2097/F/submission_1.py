import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())
    S_initial = list(map(int, sys.stdin.readline().split()))

    days_data = []
    for _ in range(M):
        a_prefs = list(map(int, sys.stdin.readline().split()))
        b_lims = list(map(int, sys.stdin.readline().split()))
        c_prefs = list(map(int, sys.stdin.readline().split()))
        days_data.append({'a': a_prefs, 'b': b_lims, 'c': c_prefs})

    # Instead of exploring all states, we track the maximum possible luggage at each airport after each day.
    # This is possible because the problem asks for the maximum number of unfound luggage,
    # and the operations are linear and monotonic in terms of maximum luggage.

    current_max = S_initial[:]  # max luggage at each airport after day i

    results = []

    for day_idx in range(M):
        day = days_data[day_idx]
        a = day['a']
        b = day['b']
        c = day['c']

        # Step 1: Morning flights depart simultaneously.
        # Each airport j can send up to a[j] luggage to previous airport (j-1),
        # and up to c[j] luggage to next airport (j+1).
        # The total luggage sent from airport j cannot exceed current_max[j].

        # We want to maximize the total luggage remaining after the afternoon check,
        # so we want to minimize the luggage found (i.e., maximize luggage after check).

        # The afternoon check reduces luggage at airport j by max(0, x - b[j]),
        # so the luggage after check is min(x, b[j]).

        # The evening flights arrive: luggage sent from neighbors arrive at airport j.

        # We want to find the maximum luggage vector after day i.

        # To maximize luggage after check, we want to minimize luggage found,
        # which means we want to keep luggage at each airport after morning flights
        # as close to or below b[j] to avoid losing luggage.

        # However, we can send luggage away from airports with luggage > b[j] to neighbors,
        # but neighbors have capacity limits on how much they can receive (from their own sending limits).

        # Since the problem is small (N <= 12), we can solve a linear system or use a DP approach.

        # But to optimize, we use the following approach:

        # Let x_j = luggage remaining at airport j after morning flights depart (before check).
        # We have:
        # x_j = current_max[j] - la_j - lc_j
        # la_j <= a[j], lc_j <= c[j], la_j + lc_j <= current_max[j]

        # After check:
        # luggage_j_after_check = min(x_j, b[j])

        # After evening flights arrive:
        # luggage_j_next = luggage_j_after_check + la_{j+1} + lc_{j-1}
        # indices modulo N

        # We want to choose la_j, lc_j to maximize sum of luggage_j_next.

        # This is a linear optimization problem with constraints.

        # Since N is small, we can solve it by enumerating all possible la_j, lc_j for each airport,
        # but that is exponential.

        # Instead, we use a greedy approach:

        # For each airport j:
        # - The maximum luggage that can remain after morning flights is b[j].
        # - So we want to send away at least max(0, current_max[j] - b[j]) luggage.
        # - But we cannot send more than a[j] + c[j].
        # - So the luggage sent away from j is send_j = min(current_max[j], max(0, current_max[j] - b[j]), a[j] + c[j])

        # We split send_j into la_j and lc_j to maximize the total luggage after evening flights.

        # Since luggage_j_next = min(x_j, b_j) + la_{j+1} + lc_{j-1},
        # the sum over all j is sum(min(x_j, b_j)) + sum(la_j) + sum(lc_j) = sum(min(x_j, b_j)) + sum(send_j)

        # So total luggage after day i = sum(min(x_j, b_j)) + sum(send_j)

        # We want to maximize sum(min(x_j, b_j)) + sum(send_j)

        # But x_j = current_max[j] - send_j

        # So sum(min(current_max[j] - send_j, b[j])) + sum(send_j)

        # We want to choose send_j in [0, min(current_max[j], a[j] + c[j])] to maximize above.

        # For each j, we can try send_j = 0 or send_j = min(current_max[j], a[j] + c[j]) or send_j = max(0, current_max[j] - b[j]) capped by capacity.

        # We pick the send_j that maximizes min(current_max[j] - send_j, b[j]) + send_j.

        # This is a simple per-airport optimization.

        new_max = [0]*N
        for j in range(N):
            max_send = min(current_max[j], a[j] + c[j])
            need_send = max(0, current_max[j] - b[j])
            candidates = [0, max_send, need_send]
            candidates = [min(max_send, max(0, c)) for c in candidates]
            best_val = -1
            best_send = 0
            for send_j in candidates:
                remain = current_max[j] - send_j
                val = min(remain, b[j]) + send_j
                if val > best_val:
                    best_val = val
                    best_send = send_j
            new_max[j] = best_val

        # Now distribute send_j into la_j and lc_j to maximize next day luggage.

        # Since sum of send_j is fixed, and luggage_j_next = min(x_j, b_j) + la_{j+1} + lc_{j-1},
        # sum over all j is sum(new_max) + sum(send_j) = sum(new_max) + sum(send_j) (but send_j already counted in new_max)

        # Actually, we have new_max[j] = min(x_j, b_j) + send_j, so sum(new_max) = sum(min(x_j, b_j) + send_j)

        # But we need to compute the luggage vector after evening flights:

        # luggage_j_next = min(x_j, b_j) + la_{j+1} + lc_{j-1}

        # We know send_j = la_j + lc_j

        # To maximize luggage_j_next, we want to maximize la_{j+1} + lc_{j-1} for each j.

        # Since sum of la_j + lc_j = send_j, total sum of send_j is fixed.

        # The distribution of la_j and lc_j affects the distribution of luggage_j_next.

        # To maximize the sum of luggage_j_next, any distribution works since sum over all j of luggage_j_next = sum(new_max) + sum(send_j) = sum(new_max) + sum(send_j) (double counting send_j? No, send_j is included in new_max).

        # So sum of luggage_j_next = sum(new_max) + sum(send_j) = sum(min(x_j, b_j) + send_j) = sum(new_max)

        # So sum(new_max) is the maximum total luggage after day i.

        # But we need to update current_max for next day: current_max = luggage_j_next vector.

        # To get luggage_j_next vector, we need to distribute send_j into la_j and lc_j.

        # We choose la_j = min(a[j], send_j), lc_j = send_j - la_j (greedy).

        # Then:

        # luggage_j_next = min(x_j, b_j) + la_{j+1} + lc_{j-1}

        # Let's compute x_j = current_max[j] - send_j

        x = [current_max[j] - min(current_max[j], a[j] + c[j]) for j in range(N)]
        # But we used best_send above, so we must store best_send per airport.

        best_sends = [0]*N
        for j in range(N):
            max_send = min(current_max[j], a[j] + c[j])
            need_send = max(0, current_max[j] - b[j])
            candidates = [0, max_send, need_send]
            candidates = [min(max_send, max(0, c)) for c in candidates]
            best_val = -1
            best_send = 0
            for send_j in candidates:
                remain = current_max[j] - send_j
                val = min(remain, b[j]) + send_j
                if val > best_val:
                    best_val = val
                    best_send = send_j
            best_sends[j] = best_send
            x[j] = current_max[j] - best_send

        # Distribute best_sends into la and lc greedily
        la = [0]*N
        lc = [0]*N
        for j in range(N):
            la[j] = min(a[j], best_sends[j])
            lc[j] = best_sends[j] - la[j]

        # Compute luggage after check
        after_check = [min(x[j], b[j]) for j in range(N)]

        # Compute luggage after evening flights arrive
        next_max = [0]*N
        for j in range(N):
            next_max[j] = after_check[j] + la[(j+1)%N] + lc[(j-1)%N]

        current_max = next_max

        results.append(sum(current_max))

    print(" ".join(map(str, results)))


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    solve()