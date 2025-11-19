N = int(input())
A = list(map(int, input().split()))

# Calculate the total number of moves
total_moves = sum(A)

# The winner is determined by the parity of the total moves
if total_moves % 2 == 1:
    print("Fennec")
else:
    print("Snuke")