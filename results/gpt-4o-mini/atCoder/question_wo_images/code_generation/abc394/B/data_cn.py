N = int(input())
strings = [input().strip() for _ in range(N)]

# Sort strings by length
strings.sort(key=len)

# Join the sorted strings into a single string
result = ''.join(strings)

print(result)