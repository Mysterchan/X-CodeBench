import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arrays = []
    max_len = 0
    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        arr = data[1:]
        arrays.append(arr)
        if k > max_len:
            max_len = k

    # We want to find the lexicographically minimum bottom row after gravity.
    # Gravity causes elements to fall down to the bottom row.
    # The bottom row length = max length of any array.
    # Each column in the bottom row is formed by stacking all elements from arrays that have that column.
    # After gravity, the bottom row at position j contains all elements from arrays that have length > j.
    # The order of arrays affects the order of elements in each column.
    #
    # To get lex min bottom row, we want to arrange arrays so that for each column,
    # the elements that fall down form a lex min sequence.
    #
    # Observation:
    # The bottom row is formed by taking the last elements in each column after gravity.
    # Gravity stacks elements in each column from bottom to top.
    #
    # The bottom row at position j is the last element in the stack of column j.
    # The stack of column j is formed by taking the j-th element of all arrays that have length > j,
    # stacked in the order of arrays from bottom to top.
    #
    # So the bottom row at position j is the element from the array that is at the bottom of the stack for column j.
    #
    # To minimize lex order of bottom row, we want to minimize the bottom element in column 0,
    # then if tie, minimize bottom element in column 1, and so on.
    #
    # This means we want to sort arrays by their elements column-wise:
    # Compare arrays by their elements at position 0, then 1, then 2, ...
    # If an array is shorter and doesn't have element at position j, treat it as smaller (empty).
    #
    # But arrays are left aligned, so shorter arrays have fewer columns.
    # For comparison, shorter arrays are considered smaller if they run out of elements earlier.
    #
    # After sorting arrays by their elements lex order (with shorter arrays considered smaller),
    # stacking them from top to bottom in that order will produce the lex min bottom row.
    #
    # Why?
    # Because the bottom row at position j is the element of the bottom-most array that has length > j.
    # The bottom-most array is the last in the order.
    # So the bottom row at position j is the element at position j of the last array in the order that has length > j.
    #
    # To get lex min bottom row, we want the last array with length > j to have minimal element at j.
    # So sorting arrays lex order ascending and stacking top to bottom in that order,
    # the last array with length > j is the lex max among arrays with length > j.
    #
    # But we want lex min bottom row, so we want the last array with length > j to be lex min at position j.
    #
    # This suggests we should stack arrays in reverse lex order (descending),
    # so the last array with length > j is lex min at position j.
    #
    # Let's verify with sample:
    # Sample 2:
    # arrays:
    # [2,9]
    # [3,1,4]
    # Sorted lex ascending:
    # [2,9] < [3,1,4] because 2 < 3 at pos 0
    # Stack top to bottom: [2,9], [3,1,4]
    # bottom row pos 0: last array with length>0 is [3,1,4], element=3
    # pos1: last array with length>1 is [3,1,4], element=1
    # pos2: last array with length>2 is [3,1,4], element=4
    # bottom row: 3 1 4
    # But sample output is 2 9 4
    #
    # Stack in reverse order:
    # [3,1,4], [2,9]
    # bottom row pos0: last array with length>0 is [2,9], element=2
    # pos1: last array with length>1 is [2,9], element=9
    # pos2: last array with length>2 is [3,1,4], element=4
    # bottom row: 2 9 4 matches sample output.
    #
    # So we must sort arrays lex ascending and stack them bottom to top in that order,
    # i.e. print arrays in reverse order of lex ascending.
    #
    # Then bottom row at position j is element at j of the last array with length>j,
    # which is the lex min array at that position.
    #
    # Implementation:
    # Sort arrays lex ascending (shorter arrays considered smaller).
    # Then bottom row length = max_len.
    # For each position j in [0..max_len-1]:
    #   find last array in sorted order with length > j, take element at j.
    #
    # Since arrays are sorted lex ascending, last array with length>j is the last array in the list with length>j.
    #
    # We can precompute for each position j the last array with length>j by scanning from right to left.
    #
    # Then output bottom row.

    # Define a comparison key for lex order with shorter arrays smaller
    def lex_key(arr):
        return arr

    arrays.sort(key=lex_key)

    # For each position j, find last array with length > j
    # We'll create an array last_with_len_gt_j of length max_len
    # last_with_len_gt_j[j] = index of last array with length > j
    last_with_len_gt_j = [-1] * max_len

    # For each j, we scan arrays from right to left to find last array with length > j
    # To do efficiently, we can for each array mark all positions < length as candidate
    # But that is O(n * max_len) worst case, too large.
    #
    # Instead, for each array i, length = len(arrays[i])
    # For j in [0..length-1], last_with_len_gt_j[j] can be updated to i if i > current
    #
    # We can do this by iterating arrays from right to left:
    # For i in reversed(range(n)):
    #   length = len(arrays[i])
    #   for j in range(length):
    #       if last_with_len_gt_j[j] == -1:
    #           last_with_len_gt_j[j] = i
    #
    # This is O(n * max_len) worst case, too large.
    #
    # Optimization:
    # For each array, we only update last_with_len_gt_j for positions < length if last_with_len_gt_j[j] == -1
    # Once last_with_len_gt_j[j] is set, no need to update again.
    #
    # So total updates = max_len, since each position updated once.
    #
    # Implement this.

    for i in reversed(range(n)):
        length = len(arrays[i])
        for j in range(length):
            if last_with_len_gt_j[j] == -1:
                last_with_len_gt_j[j] = i

    # Now build bottom row
    bottom_row = []
    for j in range(max_len):
        idx = last_with_len_gt_j[j]
        if idx == -1:
            # no array has length > j, so no element in bottom row at j
            # problem states arrays left aligned, so bottom row length = max_len
            # but some columns may be empty? No, max_len is max length of arrays
            # so at least one array has length max_len, so idx != -1 always
            bottom_row.append(0)  # fallback, should not happen
        else:
            bottom_row.append(arrays[idx][j])

    print(*bottom_row)