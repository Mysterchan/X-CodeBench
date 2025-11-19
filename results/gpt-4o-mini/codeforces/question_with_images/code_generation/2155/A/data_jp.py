def total_matches(n):
    matches = 0
    winners = n
    losers = 0
    
    while winners > 1 or losers > 1:
        # Matches in the winners group
        matches += winners // 2
        winners = (winners + 1) // 2  # Update winners for next round
        
        # Matches in the losers group
        matches += losers // 2
        losers = (losers + 1) // 2  # Update losers for next round
        
        # Teams that lost in the winner group go to the loser group
        if winners < n:  # Only update losers if there are teams moving from winners to losers
            losers += n - winners
            
    return matches

t = int(input())
for _ in range(t):
    n = int(input())
    print(total_matches(n))