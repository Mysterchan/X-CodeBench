def determine_winner(N, A):
    # Calculate the total number of moves needed to fill S
    total_moves = sum(A)
    
    # The number of unique indices that need to be filled in S is N
    # The winner is determined by the parity of the total moves
    if total_moves % 2 == 1:
        return "Fennec"
    else:
        return "Snuke"

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

# Determine and print the winner
print(determine_winner(N, A))