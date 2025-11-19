N = int(input())
S = input()

# Find first and last occurrence of '1'
first_one = S.index('1')
last_one = S.rindex('1')

# Count zeros between first and last '1'
zeros_between = S[first_one:last_one+1].count('0')

print(zeros_between)