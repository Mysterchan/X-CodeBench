import sys

def read_input():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip())
    ranges = []
    for i in range(1, n + 1):
        l, r = map(int, lines[i].strip().split())
        ranges.append((l, r))
    q = int(lines[n + 1].strip())
    queries = []
    for i in range(n + 2, n + q + 2):
        queries.append(int(lines[i].strip()))
    return n, ranges, q, queries

def solve(n, ranges, q, queries):
    diff = [0] * (5 * 10**5 + 2)
    for l, r in ranges:
        diff[l] += 1
        diff[r + 1] -= 1
    for i in range(1, len(diff)):
        diff[i] += diff[i - 1]
    for i in range(1, len(diff)):
        diff[i] += diff[i - 1]
    ans = []
    for x in queries:
        ans.append(diff[x] + x)
    return ans

def main():
    n, ranges, q, queries = read_input()
    ans = solve(n, ranges, q, queries)
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()