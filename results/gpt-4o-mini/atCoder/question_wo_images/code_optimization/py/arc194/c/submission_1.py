N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total_cost = 0
cost_to_flip = 0

for i in range(N):
    if A[i] == 1:
        total_cost += C[i]  # If A[i] is 1, add its cost to the total
    if A[i] != B[i]:  # Needs flipping
        cost_to_flip += C[i]  # Accumulate flip costs

# After all necessary flips, A becomes identical to B
# The minimum cost is the total cost minus the cost of those elements in A that will be turned to 0
min_cost = total_cost - cost_to_flip

print(min_cost)