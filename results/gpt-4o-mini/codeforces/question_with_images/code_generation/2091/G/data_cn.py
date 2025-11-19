def max_strength_after_trip(s, k):
    if k >= s:
        return k - (s - k)
    max_possible_strength = k
    distance_covered = 0
    while distance_covered < s:
        if max_possible_strength > 0:
            distance_covered += max_possible_strength
            max_possible_strength -= 1
        else:
            break
        if distance_covered >= s:
            break
        distance_covered += max_possible_strength
        if max_possible_strength > 0:
            max_possible_strength -= 1
        else:
            break
    return max(0, max_possible_strength)

t = int(input())
results = []
for _ in range(t):
    s, k = map(int, input().split())
    results.append(max_strength_after_trip(s, k))

print("\n".join(map(str, results)))