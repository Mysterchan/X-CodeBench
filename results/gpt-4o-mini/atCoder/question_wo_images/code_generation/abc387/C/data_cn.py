def is_snake_number(n):
    str_n = str(n)
    max_digit = str_n[0]
    for d in str_n[1:]:
        if d >= max_digit:
            return False
    return True

def count_snake_numbers(L, R):
    count = 0
    for n in range(L, R + 1):
        if is_snake_number(n):
            count += 1
    return count

L, R = map(int, input().split())
print(count_snake_numbers(L, R))