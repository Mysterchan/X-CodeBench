n = int(input())
a = list(map(int, input().split()))

distinct_values = set(a)
count = len(distinct_values)

# Count sequences formed by setting A[L:R] to A[L]
result = count * (count + 1) // 2

# Add the count of sequences formed by equal segments
for value in distinct_values:
    occurrences = a.count(value)
    if occurrences > 1:
        result += occurrences * (occurrences - 1) // 2

print(result)