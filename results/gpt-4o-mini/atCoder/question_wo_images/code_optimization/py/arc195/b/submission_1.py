n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Count -1 occurrences
cnt_a = a.count(-1)
cnt_b = b.count(-1)

# Calculate the sum of fixed values and gather them for processing
sum_a = sum(x for x in a if x != -1)
sum_b = sum(y for y in b if y != -1)

# The number of pairs with non-negative sums must be equal to n
target_sum = (sum_a + sum_b + cnt_a + cnt_b) // n

# Check if target sum is achievable
if (sum_a + sum_b + cnt_a + cnt_b) % n != 0 or target_sum < 0:
    print('No')
    exit()

# We can find the pairs
needed_for_a = 0
needed_for_b = 0

for num in a:
    if num == -1:
        needed_for_a += target_sum
    else:
        if num > target_sum:
            needed_for_a -= (num - target_sum)

for num in b:
    if num == -1:
        needed_for_b += target_sum
    else:
        if num > target_sum:
            needed_for_b -= (num - target_sum)

# The needs must not exceed the respective counts of -1
if needed_for_a <= cnt_a and needed_for_b <= cnt_b:
    print('Yes')
else:
    print('No')