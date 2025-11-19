def count_snake_numbers_up_to(x: int) -> int:
    if x < 10:
        return 0
    s = str(x)
    n = len(s)
    first_digit = int(s[0])
    rest_digits = s[1:]

    # Count snake numbers with fewer digits than n
    # For length d (2 <= d < n):
    # first digit: 1..9
    # other digits: 0..(first_digit-1)
    # count = sum_{d=2}^{n-1} sum_{f=1}^9 (f)^{d-1}
    total = 0
    for length in range(2, n):
        for f in range(1, 10):
            total += f ** (length - 1)

    # Count snake numbers with length == n and first digit < first_digit
    for f in range(1, first_digit):
        total += f ** (n - 1)

    # Count snake numbers with length == n and first digit == first_digit
    # Need to count numbers <= x with first digit == first_digit and
    # all other digits < first_digit
    # Use digit DP on rest_digits with max digit = first_digit - 1
    limit = first_digit - 1
    digits = list(map(int, rest_digits))
    length = len(digits)

    from functools import lru_cache

    @lru_cache(None)
    def dfs(pos, is_limit):
        if pos == length:
            return 1
        up = digits[pos] if is_limit else limit
        res = 0
        for d in range(up + 1):
            if d <= limit:
                res += dfs(pos + 1, is_limit and (d == up))
        return res

    total += dfs(0, True)
    return total


L, R = map(int, input().split())
print(count_snake_numbers_up_to(R) - count_snake_numbers_up_to(L - 1))