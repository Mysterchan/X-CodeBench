def count_kagamimochi(N, sizes):
    count = 0
    j = 0
    
    for i in range(N):
        while j < N and sizes[j] <= 2 * sizes[i]:
            j += 1
        count += j - i - 1  # excluding the case where i == j
        
    return count

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
sizes = list(map(int, data[1:]))

# Get the result and print it
result = count_kagamimochi(N, sizes)
print(result)