def replace_wa_with_ac(s):
    while 'WA' in s:
        s = s.replace('WA', 'AC', 1)
    return s

input_string = input().strip()
result = replace_wa_with_ac(input_string)
print(result)