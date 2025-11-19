import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = input().rstrip()

length = 3**N
cost = [1]*length

for n in range(N, 0, -1):
    length //= 3
    new_cost = [0]*length
    for i in range(length):
        idx = 3*i
        zeros = (A[idx] == '0') + (A[idx+1] == '0') + (A[idx+2] == '0')
        majority = '0' if zeros >= 2 else '1'

        # Collect costs of children that match majority
        children_costs = []
        for j in range(3):
            if A[idx+j] == majority:
                children_costs.append(cost[idx+j])
        # To flip majority, must flip all but one child (the one with max cost)
        max_cost = max(children_costs)
        new_cost[i] = sum(children_costs) - max_cost

    # Build new A string for next iteration
    A = ''.join('0' if (A[3*i] == '0') + (A[3*i+1] == '0') + (A[3*i+2] == '0') >= 2 else '1' for i in range(length))
    cost = new_cost

print(cost[0])