def min_bench_length(n, m, k):
    # Calculate the minimum possible longest bench length
    # We need to determine how many benches are required
    # It's calculated as:
    # The maximum number of desks that can be seated in one row is 'm'.
    # So we can spread 'k' desks over 'n' rows.
    # Thus we need at least ceil(k / m) benches in total,
    # and distribute those benches as evenly as possible over 'n' rows.
    
    # Minimum benches needed
    benches_needed = (k + m - 1) // m  # equivalent to ceil(k / m)
    # Distributing benches across rows
    # The minimal maximum length of the benches will be ceil(benches_needed / n)
    return (benches_needed + n - 1) // n  # equivalent to ceil(benches_needed / n)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, m, k = map(int, data[i].split())
        results.append(min_bench_length(n, m, k))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()