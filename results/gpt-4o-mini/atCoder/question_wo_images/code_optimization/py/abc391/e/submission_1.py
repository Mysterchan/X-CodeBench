import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = input()

# Precompute the number of changes needed to change the majority value
def compute_cost(A, length):
    cost = [0] * (length // 3)
    for i in range(length // 3):
        count_0 = A[3 * i:3 * i + 3].count('0')
        count_1 = 3 - count_0  # Since it's binary, total is 3
        if count_0 > count_1:
            cost[i] = count_1  # To change majority to 1
        else:
            cost[i] = count_0  # To change majority to 0
    return cost

# Iteratively reduce the string and compute costs
length = 3 ** N
cost = compute_cost(A, length)

for n in range(N - 1, 0, -1):
    new_length = length // 3
    new_cost = [0] * new_length
    A_new = []
    
    for i in range(new_length):
        count_0 = A[3 * i:3 * i + 3].count('0')
        count_1 = 3 - count_0
        if count_0 > count_1:
            A_new.append('0')
            new_cost[i] = cost[3 * i + 1] + cost[3 * i + 2]  # Change to 0
        else:
            A_new.append('1')
            new_cost[i] = cost[3 * i] + cost[3 * i + 1]  # Change to 1
    
    A = ''.join(A_new)
    cost = new_cost
    length = new_length

# The final cost to change the first element
final_count_0 = A.count('0')
final_count_1 = 3 - final_count_0
if final_count_0 > final_count_1:
    print(final_count_1)  # To change majority to 1
else:
    print(final_count_0)  # To change majority to 0