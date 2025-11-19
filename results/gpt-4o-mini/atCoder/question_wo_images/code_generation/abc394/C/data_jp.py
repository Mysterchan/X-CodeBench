def replace_wa_with_ac(s):
    while 'WA' in s:
        s = s.replace('WA', 'AC', 1)
    return s

# 入力の読み込み
s = input().strip()
# WA を AC に置換した結果を出力
print(replace_wa_with_ac(s))