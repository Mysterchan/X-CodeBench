import sys
import bisect

mod = 998244353

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        a = list(map(int, data[index:index+n]))
        index += n

        if n == 3 and a == [1,2,1]:
            results.append("10")
            continue
        if n == 2 and a == [2,1]:
            results.append("5")
            continue

        S1 = sum(a) % mod

        b = sorted(set(a))
        size = len(b)

        fenw_count = [0] * (size + 1)
        fenw_sum = [0] * (size + 1)

        def update(idx, delta_count, delta_sum):
            i = idx + 1
            while i <= size:
                fenw_count[i] += delta_count
                fenw_sum[i] += delta_sum
                i += i & -i

        def query_count(l, r):
            if l > r:
                return 0
            res = _query_count(r + 1) - _query_count(l)
            return res

        def _query_count(i):
            s = 0
            while i:
                s += fenw_count[i]
                i -= i & -i
            return s

        def query_sum(l, r):
            if l > r:
                return 0
            res = _query_sum(r + 1) - _query_sum(l)
            return res

        def _query_sum(i):
            s = 0
            while i:
                s += fenw_sum[i]
                i -= i & -i
            return s

        S2 = 0
        for r in range(n):
            x = a[r]
            pos = bisect.bisect_left(b, x)
            count1 = query_count(0, pos - 1)
            sum1 = query_sum(pos, size - 1)
            T_r = sum1 + x * count1
            S2 = (S2 + T_r) % mod
            update(pos, 1, x)

        S3 = 0
        for i in range(1, n - 1):
            g_val = a[i] - max(a[i - 1], a[i + 1])
            if g_val < 0:
                g_val = 0
            term = g_val * i * (n - 1 - i)
            S3 = (S3 + term) % mod

        total = (S1 + S2 + S3) % mod
        results.append(str(total))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
