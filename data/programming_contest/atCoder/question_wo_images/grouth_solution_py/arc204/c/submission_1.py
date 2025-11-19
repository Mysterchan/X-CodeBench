from bisect import bisect
from collections import defaultdict
from itertools import accumulate

def get_cycle(n, ppp):
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        s = i
        i = ppp[i]
        tmp = [s]
        used[s] = True
        while i != s:
            tmp.append(i)
            used[i] = True
            i = ppp[i]
        yield tmp

def solve(n, ppp, q, queries):
    ppp = [p - 1 for p in ppp]
    size_count = defaultdict(int)
    for cycle in get_cycle(n, ppp):
        size_count[len(cycle)] += 1

    odd_cycles = []
    even_partial_sums = {0}
    iso_total_v = 0
    odd_total_c = 0
    odd_total_v = 0
    even_total_c = 0
    even_total_v = 0
    for s, c in size_count.items():
        if s % 2 == 0:
            even_total_c += c
            even_total_v += s * c
            b = (c + 1).bit_length() - 1
            for i in range(b):
                weight = (1 << i) * (s // 2)
                even_partial_sums.update({c + weight for c in even_partial_sums})
            r = c - (1 << b) + 1
            if r > 0:
                weight = r * (s // 2)
                even_partial_sums.update({c + weight for c in even_partial_sums})
        else:
            if s == 1:
                iso_total_v += c
            else:
                odd_total_c += c
                odd_total_v += s * c
                odd_cycles.extend([s // 2] * c)

    even_cycles = [0] * (n + 1)
    for c in even_partial_sums:
        even_cycles[c] = c
    for i in range(n):
        even_cycles[i + 1] = max(even_cycles[i + 1], even_cycles[i])

    odd_cycles.sort(reverse=True)
    odd_cycle_no_adjacent_max = sum(odd_cycles)
    odd_cycle_count = [0] * (n + 1)
    acc = 0
    for c in odd_cycles:
        odd_cycle_count[acc + 1] += 1
        acc += c
    for i in range(n):
        odd_cycle_count[i + 1] += odd_cycle_count[i]

    def put_zero(x):
        tmp = x * 2
        if even_cycles[x] == x:
            return tmp, x, 0
        if even_cycles[x] < even_cycles[-1]:
            return tmp, x - 1, 2
        p2 = even_cycles[x]
        x -= even_cycles[x]
        if x <= odd_cycle_no_adjacent_max:
            occ = odd_cycle_count[x]
            return tmp, p2 + x - occ, occ * 2
        p2 += odd_cycle_no_adjacent_max - odd_cycle_count[-1]
        p1 = odd_cycle_count[-1] * 2
        x -= odd_cycle_no_adjacent_max

        if x <= odd_cycle_count[-1]:
            return tmp - x, p2 + x, p1 - x * 2
        tmp -= odd_cycle_count[-1]
        p2 += odd_cycle_count[-1]
        p1 -= odd_cycle_count[-1] * 2
        x -= odd_cycle_count[-1]

        if x <= iso_total_v:
            return tmp - x, p2, p1
        tmp -= iso_total_v
        x -= iso_total_v

        return tmp - x * 2, p2 - x, p1

    ans = []
    for x, y, z in queries:
        score, p2, p1 = put_zero(x)

        score += min(p2, y) * 2
        y -= min(y, p2)
        score += min(p1, y)
        ans.append(score)

    return ans

n = int(input())
ppp = list(map(int, input().split()))
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]
ans = solve(n, ppp, q, queries)
print('\n'.join(map(str, ans)))