L, R = map(int, input().split())

def count_snake_up_to(X):
    if X < 10:
        return 0
    s = str(X)
    n = len(s)
    digits = list(map(int, s))

    from functools import lru_cache

    @lru_cache(None)
    def dp(pos, max_digit, is_tight, started):
        # pos: current position in number
        # max_digit: the top digit chosen (fixed at pos=0)
        # is_tight: whether prefix equals X's prefix so far
        # started: whether we have placed the top digit (pos=0)
        if pos == n:
            # All digits placed
            return 1 if started else 0

        limit = digits[pos] if is_tight else 9
        res = 0

        if pos == 0:
            # At first digit, choose top digit d in [1..limit]
            for d in range(1, limit + 1):
                # top digit must be strictly greater than all other digits
                # so max_digit = d
                res += dp(pos + 1, d, is_tight and (d == limit), True)
        else:
            # For other positions, digits must be < max_digit
            for d in range(0, limit + 1):
                if d < max_digit:
                    res += dp(pos + 1, max_digit, is_tight and (d == limit), started)
        return res

    return dp(0, 0, True, False)

print(count_snake_up_to(R) - count_snake_up_to(L - 1))