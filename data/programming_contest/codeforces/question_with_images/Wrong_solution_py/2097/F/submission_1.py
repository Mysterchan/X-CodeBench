def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = map(int, input[ptr:ptr+2])
        ptr +=2
        s = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        days = []
        for __ in range(m):
            a = list(map(int, input[ptr:ptr+n]))
            ptr +=n
            b = list(map(int, input[ptr:ptr+n]))
            ptr +=n
            c = list(map(int, input[ptr:ptr+n]))
            ptr +=n
            days.append((a, b, c))

        res = []
        current_s = s.copy()
        for i in range(m):
            a, b, c = days[i]
            new_s = [0]*n
            x = [0]*n
            y = [0]*n
            for j in range(n):
                max_x = min(a[j], current_s[j])
                remaining = current_s[j] - max_x
                max_y = min(c[j], remaining)
                x[j] = max_x
                y[j] = max_y

            remaining_after_check = [0]*n
            for j in range(n):
                rem = current_s[j] - x[j] - y[j]
                remaining_after_check[j] = min(rem, b[j])

            incoming_x = [0]*n
            incoming_y = [0]*n
            for j in range(n):
                p_j = (j -2) % n
                incoming_x[p_j] += x[j]
                q_j = (j) % n
                incoming_y[q_j] += y[j]

            for j in range(n):
                new_s[j] = remaining_after_check[j] + incoming_x[j] + incoming_y[j]

            current_s = new_s
            res.append(sum(current_s))

        print('\n'.join(map(str, res)))

solve()
