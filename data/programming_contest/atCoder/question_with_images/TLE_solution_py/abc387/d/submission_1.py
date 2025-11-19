import copy
H, W = map(int, input().split())
S = []
p = []
st = []
g = []
s = []

for i in range(H):
    s = input()
    s1 = []
    for j in range(len(s)):
        s1.append(s[j])
    S.append(s1)
    if 'S' in s:
        st.append([i, s.index('S')])
    if 'G' in s:
        g.append([i, s.index('G')])
s2 = copy.deepcopy(s1)
oldS = copy.deepcopy(S)

S = copy.deepcopy(oldS)
p = []
p.append(['V', st[0][0], st[0][1]])
z = 1
while True:
    f = False
    f1 = False
    q = []
    for i in range(len(p)):
        if p[i][0] == 'G':
            q1 = []
            q1 = copy.deepcopy(p[i])
            q.append(q1)

        if p[i][0] == 'H':
            if p[i][1] > 0 and S[p[i][1] - 1][p[i][2]] == '.':
                S[p[i][1] - 1][p[i][2]] = str(z)
                q1 = ['V', p[i][1] - 1, p[i][2]]
                q.append(q1)
                f = True
            if p[i][1] > 0 and S[p[i][1] - 1][p[i][2]] == 'G':
                f1 = True
                break

            if p[i][1] < H - 1 and S[p[i][1] + 1][p[i][2]] == '.':
                S[p[i][1] + 1][p[i][2]] = str(z)
                q1 = ['V', p[i][1] + 1, p[i][2]]
                q.append(q1)
                f = True
            if p[i][1] < H - 1 and S[p[i][1] + 1][p[i][2]] == 'G':
                f1 = True
                break

        if p[i][0] == 'V':
            if p[i][2] > 0 and S[p[i][1]][p[i][2] - 1] == '.':
                S[p[i][1]][p[i][2] - 1] = str(z)
                q1 = ['H', p[i][1], p[i][2] - 1]
                q.append(q1)
                f = True
            if p[i][2] > 0 and S[p[i][1]][p[i][2] - 1] == 'G':
                f1 = True
                break

            if p[i][2] < W - 1 and S[p[i][1]][p[i][2] + 1] == '.':
                S[p[i][1]][p[i][2] + 1] = str(z)
                q1 = ['H', p[i][1], p[i][2] + 1]
                q.append(q1)
                f = True
            if p[i][2] < W - 1 and S[p[i][1]][p[i][2] + 1] == 'G':
                f1 = True
                break
    if f1 == True:
        break
    p = copy.deepcopy(q)
    z += 1
    if f == False:
        break
if f1 == True:
    mV = z
else:
    mV = -1

S = copy.deepcopy(oldS)
p = []
p.append(['H', st[0][0], st[0][1]])
z = 1
while True:
    f = False
    f1 = False
    q = []
    for i in range(len(p)):
        if p[i][0] == 'G':
            q1 = []
            q1 = copy.deepcopy(p[i])
            q.append(q1)

        if p[i][0] == 'H':
            if p[i][1] > 0 and S[p[i][1] - 1][p[i][2]] == '.':
                S[p[i][1] - 1][p[i][2]] = str(z)
                q1 = ['V', p[i][1] - 1, p[i][2]]
                q.append(q1)
                f = True
            if p[i][1] > 0 and S[p[i][1] - 1][p[i][2]] == 'G':
                f1 = True
                break

            if p[i][1] < H - 1 and S[p[i][1] + 1][p[i][2]] == '.':
                S[p[i][1] + 1][p[i][2]] = str(z)
                q1 = ['V', p[i][1] + 1, p[i][2]]
                q.append(q1)
                f = True
            if p[i][1] < H - 1 and S[p[i][1] + 1][p[i][2]] == 'G':
                f1 = True
                break

        if p[i][0] == 'V':
            if p[i][2] > 0 and S[p[i][1]][p[i][2] - 1] == '.':
                S[p[i][1]][p[i][2] - 1] = str(z)
                q1 = ['H', p[i][1], p[i][2] - 1]
                q.append(q1)
                f = True
            if p[i][2] > 0 and S[p[i][1]][p[i][2] - 1] == 'G':
                f1 = True
                break

            if p[i][2] < W - 1 and S[p[i][1]][p[i][2] + 1] == '.':
                S[p[i][1]][p[i][2] + 1] = str(z)
                q1 = ['H', p[i][1], p[i][2] + 1]
                q.append(q1)
                f = True
            if p[i][2] < W - 1 and S[p[i][1]][p[i][2] + 1] == 'G':
                f1 = True
                break
    if f1 == True:
        break
    p = copy.deepcopy(q)
    z += 1
    if f == False:
        break
if f1 == True:
    mH = z
else:
    mH = -1

if mH == -1 and mV == -1:
    print(-1)
elif mH == -1:
    print(mV)
elif mV == -1:
    print(mH)
else:
    print(min(mH, mV))
pass