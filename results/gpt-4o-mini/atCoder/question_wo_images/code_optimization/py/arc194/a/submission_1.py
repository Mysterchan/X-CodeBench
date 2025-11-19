n = int(input())
a_n = list(map(int, input().split()))

max_sum = current_sum = 0

for value in a_n:
    # If adding the current value does not reduce the sum, add it
    if current_sum + value > current_sum:
        current_sum += value
    # Update the maximum sum after each addition
    max_sum = max(max_sum, current_sum)

print(max_sum)