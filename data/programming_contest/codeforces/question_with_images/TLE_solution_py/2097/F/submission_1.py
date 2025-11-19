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

    results = []

    current_dp_states = {tuple(S_initial)}
    options_memo = {}

    def get_options_for_airport(S_j_val, idx_j, day_params_for_day):
        a_j_cap = day_params_for_day['a'][idx_j]
        b_j_thresh = day_params_for_day['b'][idx_j]
        c_j_cap = day_params_for_day['c'][idx_j]

        state_key_for_options = (S_j_val, a_j_cap, b_j_thresh, c_j_cap)
        if state_key_for_options in options_memo:
            return options_memo[state_key_for_options]

        options = []
        options.append((0, 0))

        la1 = min(S_j_val, a_j_cap)
        lc1 = min(S_j_val - la1, c_j_cap)
        options.append((la1, lc1))

        lc2 = min(S_j_val, c_j_cap)
        la2 = min(S_j_val - lc2, a_j_cap)
        options.append((la2, lc2))

        L_req = max(0, S_j_val - b_j_thresh)
        max_can_send_cap = a_j_cap + c_j_cap

        actual_L_to_send_strat3 = 0
        if L_req > min(S_j_val, max_can_send_cap):
            actual_L_to_send_strat3 = min(S_j_val, max_can_send_cap)
        else:
            actual_L_to_send_strat3 = L_req

        la3 = min(actual_L_to_send_strat3, a_j_cap)
        lc3 = actual_L_to_send_strat3 - la3
        options.append((la3, lc3))

        unique_options = sorted(list(set(options)))
        options_memo[state_key_for_options] = unique_options
        return unique_options

    for day_idx in range(M):
        day_params_current_day = days_data[day_idx]
        options_memo.clear()

        next_dp_states = set()

        chosen_la = [0] * N
        chosen_lc = [0] * N

        for current_s_tuple in current_dp_states:

            def generate_flight_configs_recursive(airport_k_idx):
                if airport_k_idx == N:
                    x_rem = [0] * N
                    for j_idx in range(N):
                        x_rem[j_idx] = current_s_tuple[j_idx] - (chosen_la[j_idx] + chosen_lc[j_idx])

                    s_prime = [0] * N
                    for j_idx in range(N):
                        s_prime[j_idx] = min(x_rem[j_idx], day_params_current_day['b'][j_idx])

                    s_final_day = list(s_prime)
                    for k_target_idx in range(N):
                        s_final_day[k_target_idx] += chosen_la[(k_target_idx + 1) % N]
                        s_final_day[k_target_idx] += chosen_lc[(k_target_idx - 1 + N) % N]

                    next_dp_states.add(tuple(s_final_day))
                    return

                airport_k_options = get_options_for_airport(current_s_tuple[airport_k_idx],
                                                            airport_k_idx,
                                                            day_params_current_day)


                for la_val, lc_val in airport_k_options:
                    chosen_la[airport_k_idx] = la_val
                    chosen_lc[airport_k_idx] = lc_val
                    generate_flight_configs_recursive(airport_k_idx + 1)

            generate_flight_configs_recursive(0)

        current_dp_states = next_dp_states

        max_total_luggage_this_day = 0
        if not current_dp_states:
             pass
        else:
            for s_tuple_final in current_dp_states:
                max_total_luggage_this_day = max(max_total_luggage_this_day, sum(s_tuple_final))
        results.append(max_total_luggage_this_day)

    sys.stdout.write(" ".join(map(str, results)) + "\n")

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()
