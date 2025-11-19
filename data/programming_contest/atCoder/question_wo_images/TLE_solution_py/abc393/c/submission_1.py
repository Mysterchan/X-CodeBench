N, M = map(int, input().split())
UV = []
ans = 0
for i in range(M):
    uv = list(map(int, input().split()))
    if uv[0] == uv[1]:
        ans += 1
    else:
        uv.sort()
        if uv in UV:
            ans += 1
        else:
            UV.append(uv)
print(ans)