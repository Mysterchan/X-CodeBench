t = int(input())
results = []

for _ in range(t):
    h, w = map(int, input().split())
    s = input()

    # Count the number of 'D' and 'R' in the string
    count_R = s.count('R')
    count_D = s.count('D')

    # Calculate the maximum possible cells painted
    # Total cells traceable in the given HxW grid
    total_paintable_cells = h * w

    # Cells that cannot be painted are because of the restrictions
    # If we have `count_R` Rs and `count_D` Ds, the remaining `?` can be used
    # We can calculate how many rows and columns are completely blocked
    remaining_R = (w - 1) - count_R  # Remaining Rs can fill columns
    remaining_D = (h - 1) - count_D  # Remaining Ds can fill rows

    # Each '?' can be translatable to either D or R
    max_black_cells = total_paintable_cells - remaining_R - remaining_D

    results.append(max_black_cells)

# Print all results at once
print('\n'.join(map(str, results)))