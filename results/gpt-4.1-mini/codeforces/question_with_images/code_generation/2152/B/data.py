import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, rK, cK, rD, cD = map(int, input().split())
    
    # Calculate Manhattan distance for Krug (since Krug moves only up/down/left/right or stay)
    dist_krug = abs(rK - rD) + abs(cK - cD)
    # Calculate Chebyshev distance for Doran (since Doran moves in 8 directions or stay)
    dist_doran = max(abs(rK - rD), abs(cK - cD))
    
    # If Doran is already adjacent or can catch Krug in the first move, survival time is 1
    # Otherwise, if Krug can keep distance indefinitely, print -1
    # Otherwise, survival time is the Manhattan distance (Krug's moves) because Krug moves first,
    # and Doran can close the distance faster or equal speed.
    
    # Key insight:
    # - Krug moves first, can move 0 or 1 step in Manhattan metric.
    # - Doran moves second, can move 0 or 1 step in Chebyshev metric.
    # - Chebyshev distance <= Manhattan distance always.
    # - If Doran's Chebyshev distance < Krug's Manhattan distance, Doran can catch Krug eventually.
    # - If Doran's Chebyshev distance == Krug's Manhattan distance, Doran can catch Krug in dist_krug turns.
    # - If Doran's Chebyshev distance > Krug's Manhattan distance, Krug can survive infinitely (-1).
    
    if dist_doran > dist_krug:
        print(-1)
    else:
        print(dist_krug)