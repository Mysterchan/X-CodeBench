N = int(input())
strings = [input() for _ in range(N)]

# Sort strings by their length
strings.sort(key=len)

# Concatenate and print the result
print("".join(strings))