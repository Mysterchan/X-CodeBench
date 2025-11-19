from __future__ import annotations

import math
import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from collections.abc import Callable, Iterable, Iterator
from functools import cache
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations, product
from math import acos, asin, atan, ceil, cos, floor, gcd, isqrt, log2, perm, pi, sin, tan
from typing import Any, ClassVar, Generic, Protocol, TypeVar

CT = TypeVar("CT")

sys.setrecursionlimit(1000000)

def getint() -> int:
    return int(sys.stdin.readline().rstrip())

def getints() -> list[int]:
    return list(map(int, sys.stdin.readline().rstrip().split()))

def getstr() -> str:
    return sys.stdin.readline().rstrip()

def getstrs() -> list[str]:
    return list(sys.stdin.readline().rstrip().split())

def getfloat() -> float:
    return float(sys.stdin.readline().rstrip())

def getfloats() -> list[float]:
    return list(map(float, sys.stdin.readline().rstrip().split()))

def all_primes_le(limit: int) -> list[int]:

    if limit < 2:
        return []
    if limit == 2:
        return [2]

    n_odds = (limit - 3) // 2 + 1
    sieve = bytearray(b"\x01") * n_odds
    r = math.isqrt(limit)
    last_i_to_check = (r - 3) // 2

    for i in range(last_i_to_check + 1):
        if sieve[i]:
            p = 2 * i + 3
            start = (p * p - 3) // 2
            step = p
            if start < n_odds:
                sieve[start::step] = b"\x00" * ((n_odds - 1 - start) // step + 1)

    primes = [2]
    primes.extend(2 * i + 3 for i, v in enumerate(sieve) if v)
    return primes

if True:
    _SMALL_PRIMES = all_primes_le(10000)
    _SMALL_PRIME_SET = set(_SMALL_PRIMES)

    _MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

    def _is_prime_64(n: int) -> bool:
        if n < 2:
            return False

        for p in _SMALL_PRIMES[:12]:
            if n % p == 0:
                return n == p

        d = n - 1
        s = (d & -d).bit_length() - 1
        while d % 2 == 0:
            d //= 2
        for a in _MR_BASES:
            if a % n == 0:
                return True
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            passed = False
            for _ in range(s - 1):
                x = (x * x) % n
                if x == n - 1:
                    passed = True
                    break
            if not passed:
                return False
        return True

    _PR_SEEDS = (
        (2, 1),
        (2, 3),
        (2, 5),
        (2, 7),
        (2, 11),
        (3, 1),
        (5, 1),
        (7, 1),
        (11, 1),
        (13, 1),
    )

    def _f_brent(x: int, c: int, mod: int) -> int:
        return (x * x + c) % mod

    def _pollard_rho_brent(n: int) -> int:

        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3

        for x0, c in _PR_SEEDS:
            y, r, q = x0, 1, 1
            g = 1
            while g == 1:
                x = y
                for _ in range(r):
                    y = _f_brent(y, c, n)
                k = 0
                while k < r and g == 1:
                    ys = y
                    m = 128
                    for _ in range(min(m, r - k)):
                        y = _f_brent(y, c, n)

                        q = (q * (x - y) % n) % n
                    g = math.gcd(q, n)
                    k += m
                r <<= 1
            if g == n:

                g = 1
                while g == 1:
                    ys = _f_brent(ys, c, n)
                    g = math.gcd(abs(x - ys), n)
            if 1 < g < n:
                return g

        i = 5
        while i * i <= n:
            if n % i == 0:
                return i
            if n % (i + 2) == 0:
                return i + 2
            i += 6
        return n

    def factorize(n: int, out: list[int] | None = None) -> list[int]:

        if out is None:
            out = []
        if n < 0:
            out.append(-1)
            n = -n
        if n in (0, 1):
            return out

        for p in _SMALL_PRIMES:
            if p * p > n:
                break
            if n % p == 0:
                cnt = 0
                while n % p == 0:
                    n //= p
                    cnt += 1
                out.extend([p] * cnt)
        if n == 1:
            return out

        if _is_prime_64(n):
            out.append(n)
        else:
            d = _pollard_rho_brent(n)
            if d == n:
                out.append(n)
            else:
                factorize(d, out)
                factorize(n // d, out)
        return out

    def pf(n: int) -> dict[int, int]:

        fs = factorize(n)
        fs.sort()
        res: dict[int, int] = {}
        for p in fs:
            res[p] = res.get(p, 0) + 1
        return res

    def divisors_from_pf(pf: dict[int, int], need_sort: bool = True) -> list[int]:

        divs = [1]
        for p, a in pf.items():
            base = divs[:]
            mul = 1
            for _ in range(a):
                mul *= p
                divs.extend(d * mul for d in base)
        if need_sort:
            divs.sort()
        return divs

N, K = getints()
A = getints()

divisors = [divisors_from_pf(pf(A[i])) for i in range(N)]