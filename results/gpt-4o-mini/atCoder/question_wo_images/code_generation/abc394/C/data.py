def transform_string(s):
    while 'WA' in s:
        # Find the index of the leftmost occurrence of 'WA'
        index = s.index('WA')
        # Replace it with 'AC'
        s = s[:index] + 'AC' + s[index + 2:]
    return s

# Read input string
input_string = input().strip()
# Output the resulting string
print(transform_string(input_string))