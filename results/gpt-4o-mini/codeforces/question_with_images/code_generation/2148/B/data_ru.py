t = int(input())
results = []

for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Count the number of required crossings
    crossings = 0

    # If there are horizontal lasers, we need to cross at least one
    if n > 0:
        crossings += 1
    
    # If there are vertical lasers, we need to cross at least one
    if m > 0:
        crossings += 1

    # After crossing the first horizontal laser, we might need another one
    for level in a:
        if level > y:
            break
        crossings += 1

    # After crossing the first vertical laser, we might need another one
    for position in b:
        if position > x:
            break
        crossings += 1

    results.append(str(crossings))

print('\n'.join(results))