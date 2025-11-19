# Read the number of strings
N = int(input().strip())

# Read the strings into a list
strings = [input().strip() for _ in range(N)]

# Sort the strings by their lengths
strings.sort(key=len)

# Concatenate the sorted strings
result = ''.join(strings)

# Print the result
print(result)