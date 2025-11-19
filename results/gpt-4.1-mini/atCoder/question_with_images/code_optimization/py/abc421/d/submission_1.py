import sys
input = sys.stdin.readline

Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

S_chars = []
S_counts = []
for _ in range(M):
    c, a = input().split()
    S_chars.append(c)
    S_counts.append(int(a))

T_chars = []
T_counts = []
for _ in range(L):
    c, b = input().split()
    T_chars.append(c)
    T_counts.append(int(b))

# Movement deltas
delta = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# We'll process the moves in a two-pointer manner over the compressed sequences
i, j = 0, 0  # indices for S and T
a_remain, b_remain = S_counts[0], T_counts[0]

# Current positions
rt, ct = Rt, Ct
ra, ca = Ra, Ca

ans = 0

while i < M and j < L:
    # Number of moves to process in this step
    step = min(a_remain, b_remain)

    # Movement deltas for this block
    drt, dct = delta[S_chars[i]]
    dra, dca = delta[T_chars[j]]

    # Relative movement per step
    ddr = drt - dra
    ddc = dct - dca

    # Current relative position
    rr = rt - ra
    rc = ct - ca

    if ddr == 0 and ddc == 0:
        # Relative position does not change during these steps
        # So if they are at the same cell now, they coincide for all steps
        if rr == 0 and rc == 0:
            ans += step
        # Update positions after these steps
        rt += drt * step
        ct += dct * step
        ra += dra * step
        ca += dca * step
    else:
        # We want to find all k in [1, step] such that:
        # rr + ddr * k == 0 and rc + ddc * k == 0
        # Both must be zero at the same k

        # Solve for k:
        # k = -rr / ddr = -rc / ddc
        # Check if such k exists and is integer in [1, step]

        # Handle cases where ddr or ddc is zero separately
        if ddr == 0:
            # Then rr must be zero for any k to satisfy rr + ddr*k=0
            if rr != 0:
                # No solution
                pass
            else:
                # rr=0 always, so check rc + ddc*k=0
                # k = -rc / ddc
                if ddc != 0:
                    k = -rc / ddc
                    if k.is_integer():
                        k = int(k)
                        if 1 <= k <= step:
                            ans += 1
                # else ddc=0 and rc !=0 => no solution
        elif ddc == 0:
            # Similarly
            if rc != 0:
                pass
            else:
                k = -rr / ddr
                if k.is_integer():
                    k = int(k)
                    if 1 <= k <= step:
                        ans += 1
        else:
            # Both ddr and ddc != 0
            # Check if -rr/ddr == -rc/ddc
            # To avoid floating point, cross multiply:
            # -rr * ddc == -rc * ddr
            if (-rr) * ddc == (-rc) * ddr:
                # Then k = -rr / ddr
                k = -rr / ddr
                if k.is_integer():
                    k = int(k)
                    if 1 <= k <= step:
                        ans += 1

        # Update positions after these steps
        rt += drt * step
        ct += dct * step
        ra += dra * step
        ca += dca * step

    # Decrease remaining counts
    a_remain -= step
    b_remain -= step

    if a_remain == 0:
        i += 1
        if i < M:
            a_remain = S_counts[i]
    if b_remain == 0:
        j += 1
        if j < L:
            b_remain = T_counts[j]

print(ans)