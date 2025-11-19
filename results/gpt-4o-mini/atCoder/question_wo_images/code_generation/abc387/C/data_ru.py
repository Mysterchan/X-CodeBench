def is_snake_number(num):
    str_num = str(num)
    leading_digit = int(str_num[0])
    return all(leading_digit > int(digit) for digit in str_num[1:])

def count_snake_numbers(L, R):
    count = 0
    for number in range(L, R + 1):
        if is_snake_number(number):
            count += 1
    return count

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    L, R = map(int, input_data.split())
    result = count_snake_numbers(L, R)
    print(result)