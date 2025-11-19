def is_snake_number(n):
    s = str(n)
    top_digit = s[0]
    return all(top_digit > digit for digit in s[1:])

def count_snake_numbers(L, R):
    count = 0
    for num in range(L, R + 1):
        if is_snake_number(num):
            count += 1
    return count

import sys
input = sys.stdin.read
L, R = map(int, input().strip().split())
print(count_snake_numbers(L, R))