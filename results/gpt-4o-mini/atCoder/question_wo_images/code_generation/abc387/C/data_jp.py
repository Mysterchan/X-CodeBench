def is_hebi(num):
    digits = str(num)
    first_digit = digits[0]
    return all(first_digit > d for d in digits[1:])

def count_hebi_in_range(L, R):
    count = 0
    for num in range(L, R + 1):
        if is_hebi(num):
            count += 1
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    L, R = map(int, input().split())
    result = count_hebi_in_range(L, R)
    print(result)