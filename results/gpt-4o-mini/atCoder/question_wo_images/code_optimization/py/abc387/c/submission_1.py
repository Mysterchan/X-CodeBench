L, R = map(int, input().split())
count = 0

def is_snake_number(x):
    str_x = str(x)
    top_digit = int(str_x[0])
    return top_digit > max(int(d) for d in str_x[1:])

# Count snake numbers in a more efficient way
for i in range(L, R + 1):
    if is_snake_number(i):
        count += 1

print(count)