import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    maxA = 10**6

    freq = [0] * (maxA + 1)
    for x in A:
        freq[x] += 1

    # count_multiples[d] = number of elements in A divisible by d
    count_multiples = [0] * (maxA + 1)
    for d in range(1, maxA + 1):
        s = 0
        for multiple in range(d, maxA + 1, d):
            s += freq[multiple]
        count_multiples[d] = s

    # For each element A[i], find the maximum divisor d of A[i] with count_multiples[d] >= K
    # To do this efficiently, precompute divisors for all numbers up to maxA
    # We'll store divisors in a list of lists
    divisors = [[] for _ in range(maxA + 1)]
    for d in range(1, maxA + 1):
        for multiple in range(d, maxA + 1, d):
            divisors[multiple].append(d)

    output = []
    for x in A:
        max_gcd = 1
        for d in divisors[x]:
            if count_multiples[d] >= K and d > max_gcd:
                max_gcd = d
        output.append(str(max_gcd))

    print('\n'.join(output))

threading.Thread(target=main).start()