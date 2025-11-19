import sys
input = sys.stdin.readline

from collections import defaultdict, deque
from functools import lru_cache

n, m = map(int, input().split())
roads = defaultdict(set)
for i in range(m):
    s1, s2 = map(int, input().split())
    roads[s1].add(s2)
    roads[s2].add(s1)

MAX = 10000000

def get_best_without_road(start, blocked):
    q = deque([(start, 0)])
    seen = set()
    while q:
        cur, d = q.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        if cur == n:
            return d
        for other in roads[cur]:
            if cur == blocked[0] and other == blocked[1]:
                continue
            q.append((other, d + 1))
    return MAX

@lru_cache(None)
def citizen(cur, seen, used):
    if cur == n:
        return 0
    if used:
        return get_best_without_road(cur, used)

    seen = set(seen)
    seen.add(cur)
    best = MAX
    for other in roads[cur]:
        if other in seen:
            continue
        best = min(best, police(other, frozenset(seen)) + 1)
    return best

@lru_cache(None)
def police(cur, seen):
    best = citizen(cur, seen, False)
    for other in roads[cur]:
        best = max(best, citizen(cur, seen, (cur, other)))
    return best

print(police(1, frozenset()))
