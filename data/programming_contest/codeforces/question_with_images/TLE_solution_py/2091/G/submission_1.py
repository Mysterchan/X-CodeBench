n = int(input())

for _ in range(n):
    s, k = map(int, input().rstrip().split())

    movements = 0
    power = k
    pos = 0

    while pos != s:
        if (pos + power) < s and (pos + power) >= 0:
            pos = pos + power
            movements+=1
        elif (pos + power) < 0 or (pos + power) > s:
            if power < 0:
                if power + 1 == 0:
                    power = 1
                else:
                    power = -1 * (power+1)
            elif power > 0:
                if power - 1 == 0:
                    power = -1
                else:
                    power = -1 * (power-1)
        else:
            print(power)
