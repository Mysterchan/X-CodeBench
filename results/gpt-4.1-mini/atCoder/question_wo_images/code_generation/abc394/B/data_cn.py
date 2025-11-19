N = int(input())
strings = [input() for _ in range(N)]
strings.sort(key=len)
print("".join(strings))