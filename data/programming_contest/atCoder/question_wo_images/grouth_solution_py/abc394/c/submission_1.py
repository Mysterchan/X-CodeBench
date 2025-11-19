s = input()
ans = []
for i in reversed(s):
    if i == 'W' and ans and ans[-1] == 'A':
        ans[-1] = 'C'
        ans.append('A')
    else:
        ans.append(i)

ans.reverse()

print(''.join(ans))