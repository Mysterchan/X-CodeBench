import sys

a = int(sys.stdin.read().strip())
n = 1
factorial = 1

while factorial < a:
    n += 1
    factorial *= n

print(n)