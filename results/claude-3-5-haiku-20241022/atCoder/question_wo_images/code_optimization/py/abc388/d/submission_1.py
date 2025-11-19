def solve(N, C):
    contributors = 0  # Number of adults with stones
    
    for i in range(N):
        # Alien i becomes adult and receives stones from all contributors
        C[i] += contributors
        
        # If this alien has stones, they can contribute to future aliens
        if C[i] > 0:
            # They will give 1 stone to the next C[i] aliens (or until we run out of aliens)
            remaining_aliens = N - i - 1
            stones_to_give = min(C[i], remaining_aliens)
            
            # Update their final count
            C[i] -= stones_to_give
            
            # If they still have stones after giving to all remaining aliens, they remain a contributor
            if C[i] > 0:
                contributors += 1
    
    return " ".join(map(str, C))

N = int(input())
C = list(map(int, input().split()))
print(solve(N, C))