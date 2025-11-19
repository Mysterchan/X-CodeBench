t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    last_col = 0
    counts = [0] * m

    for _ in range(k):
        x, y = map(int, input().split())
        if y > last_col:
            last_col = y
        counts[y - 1] += 1

    if last_col == 1:
        print("Yuyu")
        continue

    if n > 1:
        if any(count % 2 for count in counts[1:last_col]):
            print("Mimo")
        else:
            print("Yuyu")
    else:
        print("Mimo" if counts[0] % 2 else "Yuyu")