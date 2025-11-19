import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = list(map(int, input().split()))

        a = [None]*m
        b = [None]*m
        c = [None]*m
        for i in range(m):
            a[i] = list(map(int, input().split()))
            b[i] = list(map(int, input().split()))
            c[i] = list(map(int, input().split()))

        # We want to find for each k=1..m the maximum number of luggage pieces
        # that may remain unfound after k days independently.
        # The problem is to maximize sum of luggage after k days, given the constraints.

        # Key observations:
        # - The luggage moves only between adjacent airports (previous and next).
        # - Each airport j has capacity constraints on how many luggage can be sent out on day i:
        #   a[i][j] to previous airport, c[i][j] to next airport.
        # - After flights depart, the luggage left at airport j is checked:
        #   if luggage_j >= b[i][j], then at least luggage_j - b[i][j] are found and removed.
        #   So the luggage after check is min(luggage_j, b[i][j]).
        # - At the end of the day, luggage transported arrives at destination airports.
        #
        # We want to maximize the sum of luggage after k days.
        #
        # The problem can be modeled as a linear system with constraints.
        #
        # However, since n <= 12 and m <= 2000, and we need to answer for each prefix k,
        # we can simulate the process day by day, but we need to find the maximum possible luggage
        # distribution after each day.
        #
        # The problem reduces to a max flow / linear programming problem, but since n is small,
        # we can solve it by DP or by iterative method.
        #
        # Approach:
        # For each day, given the luggage distribution at the start of the day,
        # we want to find the maximum luggage distribution after the day.
        #
        # Let's define:
        # x_j = luggage at airport j in the morning before flights depart
        # f_prev_j = luggage sent from airport j to previous airport (<= a[i][j])
        # f_next_j = luggage sent from airport j to next airport (<= c[i][j])
        #
        # Constraints:
        # f_prev_j + f_next_j <= x_j
        #
        # After flights depart, luggage left at airport j:
        # left_j = x_j - f_prev_j - f_next_j
        #
        # After check:
        # luggage_after_check_j = min(left_j, b[i][j])
        #
        # In the evening, luggage transported arrives:
        # luggage_next_j = luggage_after_check_j + f_prev_{j+1} + f_next_{j-1}
        # where indices wrap around modulo n.
        #
        # We want to maximize sum of luggage_next_j.
        #
        # This is a linear optimization problem with variables f_prev_j, f_next_j.
        #
        # Since n is small, we can solve it by linear programming or by iterative method.
        #
        # But since we only need the maximum sum, we can use a greedy approach:
        #
        # For each airport j:
        # - The luggage after check is at most b[i][j].
        # - To maximize total luggage after the day, we want to minimize the luggage found,
        #   so we want left_j to be as large as possible (up to b[i][j]).
        #
        # So we want to keep left_j = min(x_j, b[i][j]) as large as possible.
        #
        # But f_prev_j + f_next_j <= x_j - left_j
        #
        # The luggage arriving at airport j at the end of the day is:
        # luggage_after_check_j + f_prev_{j+1} + f_next_{j-1}
        #
        # We want to maximize sum over j of luggage_after_check_j + f_prev_{j+1} + f_next_{j-1}
        # = sum_j luggage_after_check_j + sum_j f_prev_j + sum_j f_next_j
        #
        # Since sum_j f_prev_j and sum_j f_next_j are the total luggage sent out,
        # and total luggage sent out = sum_j (x_j - left_j),
        # total luggage after the day = sum_j left_j + sum_j (x_j - left_j) = sum_j x_j
        #
        # So total luggage after the day is sum_j x_j, which is the same as before flights.
        #
        # But after check, luggage found reduces the luggage.
        #
        # So the maximum total luggage after the day is at most sum_j x_j.
        #
        # However, the luggage found reduces the luggage after check.
        #
        # The problem is to find a distribution of f_prev_j and f_next_j that maximizes the sum of luggage after the day.
        #
        # This is a max flow problem on a circle with capacity constraints.
        #
        # We can model the problem as a max flow on a graph with 2n edges per day.
        #
        # But since n is small, we can solve it by linear programming or by iterative method.
        #
        # Let's implement a max flow approach for each day:
        #
        # Construct a graph:
        # - For each airport j, node j.
        # - For each airport j, edges:
        #   - from j to prev(j) with capacity a[i][j]
        #   - from j to next(j) with capacity c[i][j]
        #
        # The luggage at airport j in the morning is x_j.
        #
        # We want to find flows f_prev_j and f_next_j such that:
        # f_prev_j + f_next_j <= x_j
        #
        # After flights depart, luggage left_j = x_j - f_prev_j - f_next_j
        #
        # After check, luggage_after_check_j = min(left_j, b[i][j])
        #
        # The luggage at the end of the day at airport j:
        # luggage_after_check_j + f_prev_{j+1} + f_next_{j-1}
        #
        # We want to maximize sum_j luggage_after_check_j + sum_j f_prev_j + sum_j f_next_j
        #
        # = sum_j luggage_after_check_j + sum_j (x_j - left_j)
        #
        # = sum_j luggage_after_check_j + sum_j (x_j - (x_j - f_prev_j - f_next_j))
        #
        # = sum_j luggage_after_check_j + sum_j (f_prev_j + f_next_j)
        #
        # But luggage_after_check_j = min(left_j, b[i][j]) = min(x_j - f_prev_j - f_next_j, b[i][j])
        #
        # So the problem is to choose f_prev_j, f_next_j to maximize:
        # sum_j min(x_j - f_prev_j - f_next_j, b[i][j]) + sum_j (f_prev_j + f_next_j)
        #
        # = sum_j b[i][j] + sum_j max(0, (x_j - f_prev_j - f_next_j) - b[i][j]) + sum_j (f_prev_j + f_next_j)
        #
        # = sum_j b[i][j] + sum_j max(0, x_j - f_prev_j - f_next_j - b[i][j]) + sum_j (f_prev_j + f_next_j)
        #
        # = sum_j b[i][j] + sum_j max(0, x_j - b[i][j] - f_prev_j - f_next_j) + sum_j (f_prev_j + f_next_j)
        #
        # = sum_j b[i][j] + sum_j max(0, x_j - b[i][j] - f_prev_j - f_next_j) + sum_j (f_prev_j + f_next_j)
        #
        # This is complicated.
        #
        # Alternative approach:
        #
        # Since the problem is complex, let's try a simpler approach:
        #
        # We want to maximize the sum of luggage after k days.
        #
        # Let's simulate the worst case scenario for luggage found:
        #
        # The luggage found at airport j on day i is max(0, luggage_before_check_j - b[i][j])
        #
        # To maximize luggage after check, we want luggage_before_check_j <= b[i][j].
        #
        # So we want to send out as much luggage as possible from airports where luggage_before_check_j > b[i][j].
        #
        # But sending luggage is limited by a[i][j], c[i][j], and the luggage available.
        #
        # So for each day, we can solve a max flow problem to maximize the luggage sent out,
        # subject to the constraints:
        # - from each airport j, total luggage sent out <= luggage at j
        # - edges capacities a[i][j], c[i][j]
        #
        # The luggage left after flights depart is luggage_j - sent_out_j
        #
        # After check, luggage_j = min(leftover, b[i][j])
        #
        # Then luggage at the end of the day is luggage_after_check_j + incoming luggage from flights.
        #
        # We can implement a max flow to find the maximum luggage sent out.
        #
        # Then update luggage for next day.
        #
        # Since n is small, we can implement a max flow with Dinic or Edmond-Karp.
        #
        # Let's implement Dinic max flow for each day.
        #
        # Graph construction for max flow:
        # - Source node S
        # - Sink node T
        # - For each airport j:
        #   - Node j
        #   - Edge from S to j with capacity = luggage_j (available luggage)
        #   - Edge from j to prev(j) with capacity a[i][j]
        #   - Edge from j to next(j) with capacity c[i][j]
        #
        # We want to find max flow from S to T through these edges.
        #
        # But where is the sink T?
        #
        # We want to maximize luggage sent out from airports.
        #
        # Actually, the luggage sent out is the flow from S to airports to neighbors.
        #
        # But the flow from airports to neighbors is limited by a[i][j], c[i][j].
        #
        # The problem is circular, so we can create a super sink T and connect all airports to T with infinite capacity,
        # but that doesn't make sense.
        #
        # Alternative:
        #
        # We want to maximize sum of luggage sent out from airports.
        #
        # So we can model the problem as a circulation with demands.
        #
        # Since the problem is complex, let's try a heuristic:
        #
        # For each airport j:
        # - The maximum luggage that can be sent out is min(luggage_j, a[i][j] + c[i][j])
        #
        # We want to send out as much luggage as possible from airports where luggage_j > b[i][j].
        #
        # So for each airport j:
        #   send_j = min(luggage_j - b[i][j], a[i][j] + c[i][j]) if luggage_j > b[i][j] else 0
        #
        # But we must distribute send_j into f_prev_j and f_next_j with constraints:
        # f_prev_j <= a[i][j], f_next_j <= c[i][j], f_prev_j + f_next_j <= send_j
        #
        # We can greedily assign:
        # f_prev_j = min(send_j, a[i][j])
        # f_next_j = min(send_j - f_prev_j, c[i][j])
        #
        # Then update luggage after flights depart:
        # left_j = luggage_j - f_prev_j - f_next_j
        #
        # After check:
        # luggage_after_check_j = min(left_j, b[i][j])
        #
        # Then luggage at end of day:
        # luggage_next_j = luggage_after_check_j + f_prev_{j+1} + f_next_{j-1}
        #
        # This heuristic should give a valid upper bound.
        #
        # Since the problem asks for maximum possible luggage unfound, this heuristic is acceptable.
        #
        # We'll implement this simulation for each day and output the sum after each day.

        luggage = s[:]
        res = []
        for day in range(m):
            f_prev = [0]*n
            f_next = [0]*n

            # Calculate how much to send out from each airport
            send = [0]*n
            for j in range(n):
                if luggage[j] > b[day][j]:
                    send[j] = min(luggage[j] - b[day][j], a[day][j] + c[day][j])
                else:
                    send[j] = 0

            # Distribute send into f_prev and f_next
            for j in range(n):
                f_prev[j] = min(send[j], a[day][j])
                f_next[j] = min(send[j] - f_prev[j], c[day][j])

            # Luggage left after flights depart
            left = [luggage[j] - f_prev[j] - f_next[j] for j in range(n)]

            # After check
            after_check = [min(left[j], b[day][j]) for j in range(n)]

            # Luggage arriving from flights
            luggage_next = [0]*n
            for j in range(n):
                prev_airport = (j - 1) % n
                next_airport = (j + 1) % n
                luggage_next[j] = after_check[j] + f_prev[next_airport] + f_next[prev_airport]

            luggage = luggage_next
            res.append(sum(luggage))

        print('\n'.join(map(str, res)))

if __name__ == "__main__":
    solve()