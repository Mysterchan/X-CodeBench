# Read the input string
S = input().strip()

# Filter the string to keep only '2'
result = ''.join(c for c in S if c == '2')

# Print the result
print(result)