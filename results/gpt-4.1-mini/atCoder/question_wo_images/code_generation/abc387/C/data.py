def count_snake_up_to(X):
    if X < 10:
        return 0
    s = str(X)
    n = len(s)
    digits = list(map(int, s))

    from functools import lru_cache

    # dp(pos, top_digit, max_other, is_tight, started)
    # pos: current index in digits
    # top_digit: the first digit chosen (most significant digit)
    # max_other: max digit among other digits so far
    # is_tight: whether prefix is restricted by X's prefix
    # started: whether we have chosen the top digit yet (to handle leading zeros)
    @lru_cache(None)
    def dp(pos, top_digit, max_other, is_tight, started):
        if pos == n:
            # If started, top_digit must be > max_other
            return 1 if started and top_digit > max_other else 0

        limit = digits[pos] if is_tight else 9
        res = 0
        for d in range(limit + 1):
            new_started = started
            new_top_digit = top_digit
            new_max_other = max_other
            if not started:
                # We must pick the top digit at the first non-zero digit (pos=0)
                # But the problem states number >= 10, so first digit can't be zero
                # So if d == 0 and pos == 0, we can't start yet (leading zero)
                # But since number >= 10, first digit can't be zero
                # So if pos == 0 and d == 0, skip
                if pos == 0 and d == 0:
                    continue
                # If not started and d != 0, this is the top digit
                new_started = True
                new_top_digit = d
                new_max_other = 0
            else:
                # started == True, so this digit is one of the other digits
                # update max_other
                if d > new_max_other:
                    new_max_other = d

            # Prune: if top_digit <= max_other, no need to continue
            # But we only know top_digit after started == True
            # So if started and top_digit <= max_other, skip
            if new_started and new_top_digit <= new_max_other:
                continue

            new_is_tight = is_tight and (d == limit)
            res += dp(pos + 1, new_top_digit, new_max_other, new_is_tight, new_started)
        return res

    return dp(0, 0, 0, True, False)


L, R = map(int, input().split())
print(count_snake_up_to(R) - count_snake_up_to(L - 1))