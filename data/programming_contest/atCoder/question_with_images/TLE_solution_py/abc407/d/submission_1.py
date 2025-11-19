import sys
read = sys.stdin.read
def error(*args, end='\n'): print(*args, end=end, file=sys.stderr)

from collections import defaultdict, deque
from itertools import chain
from functools import reduce
from operator import xor
from copy import deepcopy

def main():
    h, w = map(int, input().split())
    aa = [list(map(int, input().split())) for _ in range(h)]

    allxor = reduce(xor, chain.from_iterable(aa))
    ans = allxor

    nums = [(0, deepcopy(aa))]
    for y in range(h):
        for x in range(w):
            nums2 = deepcopy(nums)
            for p, bb in nums:
                if bb[y][x] > -1:
                    if x < w - 1:
                        q = p
                        cc = deepcopy(bb)
                        q ^= bb[y][x]
                        q ^= bb[y][x + 1]
                        ans = max(ans, allxor ^ q)
                        cc[y][x] = -1
                        cc[y][x + 1] = -1
                        nums2.append((q, cc))
                    if y < h - 1:
                        q = p
                        cc = deepcopy(bb)
                        q ^= bb[y][x]
                        q ^= bb[y + 1][x]
                        ans = max(ans, allxor ^ q)
                        cc[y][x] = -1
                        cc[y + 1][x] = -1
                        nums2.append((q, cc))
            nums = nums2
    print(ans)

if __name__ == '__main__':
    main()