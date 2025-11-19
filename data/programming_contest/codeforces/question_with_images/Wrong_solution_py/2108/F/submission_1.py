import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n

        operations = [0] * (n + 2)

        for i in range(n):
            if a[i] > 0:
                start = i + 1
                end = min(n, i + a[i])
                if start <= end:
                    operations[start] += 1
                    operations[end + 1] -= 1

        current = 0
        op_count = [0] * n
        for i in range(n):
            current += operations[i]
            op_count[i] = current

        final = [0] * n
        for i in range(n):
            final[i] = op_count[i]
            if a[i] > 0:
                pass

        op_count.sort()

        target = 0
        for val in op_count:
            if val >= target:
                target += 1

        results.append(str(target))

    print("\n".join(results))

if __name__ == "__main__":
    solve()
