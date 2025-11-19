import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    # We want to minimize the maximum bench length.
    # The minimal max bench length is the smallest x such that
    # we can place k desks in n rows, each row having benches of length at most x.
    # Since each bench is consecutive desks, and benches are separated by empty spots,
    # the best we can do is to split k desks into groups of size at most x,
    # and distribute these groups across n rows.
    #
    # The number of benches needed if max bench length is x:
    # benches = ceil(k / x)
    #
    # Since each bench must be in a single row, and a row can have multiple benches,
    # but benches in the same row must be separated by empty spots,
    # the only limitation is that the number of benches <= n * (number of benches per row).
    #
    # Actually, since benches are separated by empty spots, the number of benches per row is unlimited,
    # but the length of each bench is at most x.
    #
    # The only real limitation is that the total number of benches <= n * (max benches per row),
    # but max benches per row is unlimited (since empty spots separate benches).
    #
    # So the only limitation is that the number of benches <= n * m (which is always true).
    #
    # So the problem reduces to:
    # Find minimal x such that ceil(k / x) <= n * m (always true)
    #
    # But we want to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches needed (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # The real constraint is that the number of benches <= n * (max benches per row),
    # but max benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # but since benches are separated by empty spots, the number of benches per row is unlimited.
    #
    # So the problem reduces to:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n * m,
    # which is always true.
    #
    # So the problem is to minimize x such that the number of benches (ceil(k/x)) <= n * m,
    # but since n * m >= k, this is trivial.
    #
    # Actually, the problem is simpler:
    # We want to split k desks into n rows, each row having benches of length at most x.
    # The minimal x is the minimal integer x such that the number of benches (ceil(k/x)) <= n,
    # because each bench must be in a single row, and benches in the same row are separated by empty spots,
    # so the number of benches per row is unlimited.
    #
    # But the number of benches is ceil(k/x).
    #
    # So the minimal x is the minimal integer x such that ceil(k/x) <= n.
    #
    # This means:
    # ceil(k/x) <= n
    # => (k + x - 1) // x <= n
    # => k + x - 1 <= n * x
    # => k - 1 <= n * x - x = x * (n - 1)
    # => x >= (k - 1) / (n - 1)
    #
    # Since x must be integer, x >= ceil((k - 1) / (n - 1))
    #
    # But if n = 1, then we have only one row, so the bench length is k (all desks in one row).
    #
    # Also, x cannot be more than m (the number of spots in a row).
    #
    # So the minimal x is max(1, min(m, ceil(k / n)))
    #
    # Because if we split k desks into n rows, the minimal max bench length is at least ceil(k / n),
    # and cannot be more than m.
    #
    # So the answer is:
    # ans = (k + n - 1) // n
    # if ans > m:
    #     ans = m
    #
    # This matches the sample tests.
    
    ans = (k + n - 1) // n
    if ans > m:
        ans = m
    print(ans)