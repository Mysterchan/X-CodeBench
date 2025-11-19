import sys

def main():
    S = sys.stdin.readline().strip()
    n = len(S)
    count = 0
    # d is the distance between consecutive indices in the triple (i, j, k)
    # We need i + 2*d < n  =>  d < n/2
    for d in range(1, n // 2 + 1):
        for i in range(n - 2 * d):
            if S[i] == 'A' and S[i + d] == 'B' and S[i + 2*d] == 'C':
                count += 1
    print(count)

if __name__ == "__main__":
    main()