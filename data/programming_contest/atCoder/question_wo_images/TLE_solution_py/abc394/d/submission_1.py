colorful_brackets = {"()", "[]", "<>"}

S = input()

ans = False

while len(S) > 0:
    new_S = []
    i = 0
    while i < len(S) - 1:

        if S[i] + S[i + 1] not in colorful_brackets:
            new_S.append(S[i])
        else:
            i += 1
        i += 1

    if i == len(S) - 1:
        new_S.append(S[i])
    if S == new_S:
        break
    else:
        S = new_S
else:
    ans = True

if ans:
    print("Yes")
else:
    print("No")