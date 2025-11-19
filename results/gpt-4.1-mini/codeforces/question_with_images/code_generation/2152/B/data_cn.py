import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, rK, cK, rD, cD = map(int, input().split())
    # Krug moves like a rook (up/down/left/right + stay)
    # Doran moves like a king (8 directions + stay)
    # Both cannot leave the grid [0, n] x [0, n]
    # Krug starts first, then Doran, alternating turns.
    # We want the minimal number of turns until Doran catches Krug,
    # or -1 if Krug can survive infinitely.

    # Distance metrics:
    # Krug moves 1 step in 4 directions or stay => Manhattan distance changes by at most 1 per Krug move.
    # Doran moves 1 step in 8 directions or stay => Chebyshev distance changes by at most 1 per Doran move.

    # Turn order: Krug moves first (turn 1), then Doran (turn 1), then Krug (turn 2), then Doran (turn 2), ...
    # Capture occurs if after any move both are on the same cell.

    # Key insight:
    # Let distM = Chebyshev distance between Doran and Krug start positions
    # Let distK = Manhattan distance between Doran and Krug start positions

    # Krug tries to maximize survival time, Doran tries to minimize it.

    # Because Doran moves like a king, he can reduce Chebyshev distance by 1 each Doran turn.
    # Krug moves like a rook, can increase Manhattan distance by at most 1 each Krug turn.

    # If Doran is initially closer or equal in Chebyshev distance than Krug in Manhattan distance,
    # Doran can catch Krug quickly.

    # The minimal number of full turns (Krug+Doran) to catch is:
    # If distM <= distK, then survival time = distM
    # Else survival time = distK + (distM - distK + 1) // 2

    # But from the sample and problem, the survival time is exactly the Chebyshev distance between them.

    # Actually, from the sample and problem explanation, the survival time equals the Chebyshev distance between start positions.

    # Because:
    # - Doran can move diagonally and reduce Chebyshev distance by 1 each Doran turn.
    # - Krug can only move orthogonally, so Manhattan distance changes by at most 1 each Krug turn.
    # - Since Krug moves first, the minimal number of turns until capture is the Chebyshev distance.

    # Check if Krug can survive infinitely:
    # Since the grid is finite and Doran moves faster (in terms of distance metric),
    # Krug cannot survive infinitely.

    # So survival time = Chebyshev distance between start positions.

    distM = abs(rK - rD) + abs(cK - cD)
    distC = max(abs(rK - rD), abs(cK - cD))

    # Output the survival time = distC
    print(distC)