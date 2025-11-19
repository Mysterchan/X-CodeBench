import sys
def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    A = data[1].strip()
    # convert to list of ints
    s = [1 if ch=='1' else 0 for ch in A]
    # initial cost to flip a leaf is 1
    cost = [1] * (3**N)
    # bottom‐up collapse N times
    for _ in range(N):
        n3 = len(s)
        new_len = n3 // 3
        s2 = [0] * new_len
        c2 = [0] * new_len
        idx = 0
        # process each triple
        for i in range(0, n3, 3):
            b0, b1, b2 = s[i], s[i+1], s[i+2]
            c0, c1, c2c = cost[i], cost[i+1], cost[i+2]
            # majority bit
            cnt0 = (b0==0) + (b1==0) + (b2==0)
            if cnt0 >= 2:
                m = 0
            else:
                m = 1
            s2[idx] = m
            # target is opposite of majority
            t = 1 - m
            # cost for each child to become t
            d0 = 0 if b0==t else c0
            d1 = 0 if b1==t else c1
            d2 = 0 if b2==t else c2c
            tot = d0 + d1 + d2
            # need two smallest of d0,d1,d2 => sum - max
            mx = d0 if d0>=d1 and d0>=d2 else (d1 if d1>=d2 else d2)
            c2[idx] = tot - mx
            idx += 1
        s, cost = s2, c2
    # result is cost to flip the root
    sys.stdout.write(str(cost[0]))

if __name__ == "__main__":
    main()