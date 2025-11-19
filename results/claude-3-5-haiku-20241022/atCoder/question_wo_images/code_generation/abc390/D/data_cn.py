from collections import deque

N = int(input())
A = list(map(int, input().split()))

# Initial state: each bag is separate
initial = tuple(frozenset([i]) for i in range(N))

visited = set()
xor_values = set()

queue = deque([initial])
visited.add(initial)

def compute_xor(partition):
    result = 0
    for group in partition:
        group_sum = sum(A[i] for i in group)
        result ^= group_sum
    return result

while queue:
    state = queue.popleft()
    xor_values.add(compute_xor(state))
    
    # Try merging any two groups
    state_list = list(state)
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            # Merge group i and j
            new_group = state_list[i] | state_list[j]
            new_state = []
            for k in range(len(state_list)):
                if k != i and k != j:
                    new_state.append(state_list[k])
            new_state.append(new_group)
            new_state = tuple(sorted(new_state, key=lambda x: min(x)))
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

print(len(xor_values))