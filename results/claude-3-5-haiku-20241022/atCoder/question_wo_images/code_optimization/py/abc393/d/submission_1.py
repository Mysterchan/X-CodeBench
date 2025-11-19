N = int(input())
S = input()

count1 = S.count("1")

# Sliding window of size count1
max_ones = 0
current_ones = 0

# Initialize first window
for i in range(count1):
    if S[i] == "1":
        current_ones += 1
max_ones = current_ones

# Slide the window
for i in range(count1, N):
    if S[i] == "1":
        current_ones += 1
    if S[i - count1] == "1":
        current_ones -= 1
    max_ones = max(max_ones, current_ones)

# Answer is number of 0s in the best window
print(count1 - max_ones)