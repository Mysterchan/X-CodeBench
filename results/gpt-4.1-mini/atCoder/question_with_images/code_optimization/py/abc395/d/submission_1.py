import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# For each pigeon, store (nest, last_update_time)
Hato = [[i, -1] for i in range(N + 1)]

# For each Type 2 operation, store the pair of nests swapped
swap_ops = []

# For each nest, store the list of times when it was involved in a swap
nest_swaps = [[] for _ in range(N + 1)]

# Read all operations first
ops = [None] * Q
for i in range(Q):
    line = input().split()
    op = int(line[0])
    if op == 1:
        a, b = int(line[1]), int(line[2])
        ops[i] = (1, a, b)
    elif op == 2:
        a, b = int(line[1]), int(line[2])
        ops[i] = (2, a, b)
        swap_ops.append((a, b))
        nest_swaps[a].append(i)
        nest_swaps[b].append(i)
    else:
        a = int(line[1])
        ops[i] = (3, a)

import bisect

def get_final_nest(nest, start_time, end_time):
    # Find all swaps involving 'nest' between start_time+1 and end_time
    # For each such swap, if nest is swapped with another nest, update nest accordingly
    swaps = nest_swaps[nest]
    # Find the index of first swap after start_time
    idx = bisect.bisect_right(swaps, start_time)
    # Iterate over swaps until end_time
    for pos in range(idx, len(swaps)):
        t = swaps[pos]
        if t >= end_time:
            break
        a, b = swap_ops[t - (Q - len(swap_ops))] if t >= Q - len(swap_ops) else swap_ops[t]
        # Actually, swap_ops are stored in order of occurrence, but their indices correspond to the operation index
        # So swap_ops[t] corresponds to operation at time t
        # So we can just do a,b = swap_ops[t]
        a, b = swap_ops[t]
        if nest == a:
            nest = b
        elif nest == b:
            nest = a
    return nest

# The above function is still O(number_of_swaps_in_range), which can be large.
# We need a more efficient approach.

# Optimized approach:
# For each nest, we store the list of swap times and the corresponding partner nest at that time.
# Then, to find the final nest after all swaps between start_time and end_time,
# we can binary search the swaps in that interval and simulate the swaps.

# Let's precompute for each nest:
# nest_swaps_times[nest] = list of times when nest was swapped
# nest_swaps_partners[nest] = list of partner nests at those times

nest_swaps_times = [[] for _ in range(N + 1)]
nest_swaps_partners = [[] for _ in range(N + 1)]

for t, (a, b) in enumerate(swap_ops):
    nest_swaps_times[a].append(t)
    nest_swaps_partners[a].append(b)
    nest_swaps_times[b].append(t)
    nest_swaps_partners[b].append(a)

def get_final_nest(nest, start_time, end_time):
    times = nest_swaps_times[nest]
    partners = nest_swaps_partners[nest]
    # Find swaps in (start_time, end_time)
    # start_time and end_time are operation indices in [0, Q-1]
    # swap_ops are indexed from 0 to len(swap_ops)-1, corresponding to operation indices where op=2
    # We need to map operation indices to swap_ops indices:
    # Let's create a mapping from operation index to swap_ops index
    # We'll do this once before processing queries.

    # We'll do this outside the function.

    # For now, just return nest (placeholder)
    return nest

# Build a mapping from operation index to swap_ops index
opidx_to_swapidx = [-1] * Q
swap_idx = 0
for i in range(Q):
    if ops[i][0] == 2:
        opidx_to_swapidx[i] = swap_idx
        swap_idx += 1

def get_final_nest(nest, start_op_idx, end_op_idx):
    times = nest_swaps_times[nest]
    partners = nest_swaps_partners[nest]
    # We want to find all swaps with swap operation index in (start_swap_idx, end_swap_idx]
    # Convert start_op_idx and end_op_idx to swap indices
    # We want swaps with operation index > start_op_idx and < end_op_idx
    # So swap indices corresponding to operation indices in (start_op_idx, end_op_idx)
    # We'll find left and right indices in times array for swap indices corresponding to operation indices in that range

    # Since times stores swap indices (0-based), and swap_ops correspond to operation indices where op=2,
    # and opidx_to_swapidx maps operation index to swap index or -1

    # We need to find the swap indices corresponding to operation indices > start_op_idx and < end_op_idx

    # So for each swap index in times, get the operation index of that swap
    # We'll precompute swapidx_to_opidx for quick lookup

    # Precompute swapidx_to_opidx
    # We'll do this once outside the function

    # Then binary search times for swap indices with opidx in (start_op_idx, end_op_idx)

    # We'll do this outside the function for efficiency

    # So here, we just get the indices in times where swap operation index is in (start_swap_idx, end_swap_idx)

    # We'll implement this after precomputations

    # Placeholder
    return nest

# Precompute swapidx_to_opidx
swapidx_to_opidx = [0] * len(swap_ops)
idx = 0
for i in range(Q):
    if ops[i][0] == 2:
        swapidx_to_opidx[idx] = i
        idx += 1

# For each nest, we replace nest_swaps_times with the list of operation indices of swaps involving that nest
for nest in range(1, N + 1):
    times = nest_swaps_times[nest]
    for i in range(len(times)):
        times[i] = swapidx_to_opidx[times[i]]

def get_final_nest(nest, start_op_idx, end_op_idx):
    times = nest_swaps_times[nest]
    partners = nest_swaps_partners[nest]
    # Find swaps with operation index in (start_op_idx, end_op_idx)
    left = bisect.bisect_right(times, start_op_idx)
    right = bisect.bisect_left(times, end_op_idx)
    for i in range(left, right):
        # swap at times[i], partner is partners[i]
        nest = partners[i]
    return nest

output = []
for i in range(Q):
    op = ops[i]
    if op[0] == 1:
        # Type 1: move pigeon a to nest b at time i
        a, b = op[1], op[2]
        Hato[a] = [b, i]
    elif op[0] == 3:
        a = op[1]
        nest, last_time = Hato[a]
        # Apply swaps between last_time and i
        final_nest = get_final_nest(nest, last_time, i)
        Hato[a] = [final_nest, i]
        output.append(str(final_nest))

print('\n'.join(output))