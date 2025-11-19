t = int(input())
for _ in range(t):
    s, k = map(int, input().split())
    # The maximum power after reaching s is max(1, k - number_of_turns)
    # Each turn reduces power by 1 (except when power is 1)
    # Number of turns needed is at least ceil((s - k) / (k - 1)) if k > 1
    # If k == 1, no turns possible, power remains 1
    if k == 1:
        print(1)
        continue
    # Calculate minimal turns needed
    turns = (s - k + (k - 2)) // (k - 1)  # ceil division for (s-k)/(k-1)
    # Power after turns cannot be less than 1
    ans = max(1, k - turns)
    print(ans)