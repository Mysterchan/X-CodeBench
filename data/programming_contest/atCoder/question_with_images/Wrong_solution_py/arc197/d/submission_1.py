import sys

input = sys.stdin.readline
MOD = 998244353

MAX_N = 401
fact = [1] * MAX_N
for i in range(2, MAX_N):
    fact[i] = (fact[i - 1] * i) % MOD

def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    P_sets = {}
    for i in range(1, N + 1):

        s = frozenset(j for j in range(1, N + 1) if A[i - 1][j - 1] == 1)
        P_sets[i] = s

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            is_comparable = P_sets[i].issubset(P_sets[j]) or P_sets[j].issubset(P_sets[i])
            if (A[i - 1][j - 1] == 1) != is_comparable:
                print(0)
                return

    groups = {}
    for v, p_set in P_sets.items():
        if p_set not in groups:
            groups[p_set] = []
        groups[p_set].append(v)

    total_ways = 1
    root_p_set_found = False

    for p_set, component in groups.items():
        size = len(component)

        if 1 in component:
            total_ways = (total_ways * fact[size - 1]) % MOD
            root_p_set_found = True
        else:

            total_ways = (total_ways * fact[size]) % MOD

    if not root_p_set_found and N > 0:

         print(0)
         return

    print(total_ways)

def main():
    try:
        T_str = input()
        if not T_str: return
        T = int(T_str)
        for _ in range(T):
            solve()
    except (IOError, ValueError):
        return

if __name__ == '__main__':
    main()