n,r,c = map(int,input().split())

s = input()

delta = {'N':[1,0],'W':[0,1],'S':[-1,0],'E':[0,-1]}

smoke = set([(0,0)])

x,y = 0,0

answer = []

for i in range(n):

    p,q = delta[s[i]]

    x = x + p
    y = y + q

    dr = r + p
    dc = c + q

    smoke.add((x,y))

    if (dr,dc) in smoke:

        answer.append('1')

    else:

        answer.append('0')

print(''.join(answer))