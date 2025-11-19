def max_strength_after_trip(s, k):
    if k >= s:
        return k - (s - 1)
    
    # To reach exactly s, we can use up our strength efficiently
    remaining_distance = s - k  # This is the distance we need to cover after initially going k meters
    
    # The maximum strength we could still have if we made ideal turns
    # Turn each time we would hit the boundary, which begins at s
    # When we turn at full strength, we lose 1 strength, leading to:
    # Remaining strength = k - number_of_turns_used
    
    # We need to know how many turns we can make before running out of strength
    # The maximum turns we can make is limited by (total distance covered - first move)
    # Each turn needs at least one up/down to use it, meaning we need 2 units of distance for each turn
    turns_can_make = min(k, (remaining_distance + 1)//2)
    
    # After making the maximum amount of turns possible, compute the remaining strength
    remaining_strength = k - turns_can_make
    
    return remaining_strength

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s, k = map(int, data[i].split())
        max_strength = max_strength_after_trip(s, k)
        results.append(max_strength)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()