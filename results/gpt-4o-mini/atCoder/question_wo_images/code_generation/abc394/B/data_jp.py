N = int(input())
strings = [input().strip() for _ in range(N)]
strings.sort(key=len)
result = ''.join(strings)
print(result)