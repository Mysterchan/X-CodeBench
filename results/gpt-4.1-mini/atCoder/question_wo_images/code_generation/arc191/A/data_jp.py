import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().rstrip())
T = list(input().rstrip())

S.sort()  # Sを昇順にソート
T.sort(reverse=True)  # Tを降順にソート

i = 0  # Sの置換対象のインデックス
j = 0  # Tのインデックス

while i < N and j < M:
    if S[i] < T[j]:
        S[i] = T[j]
        i += 1
        j += 1
    else:
        # S[i] >= T[j]なら置換しても意味がないので次のSへ
        i += 1

S.sort(reverse=True)  # 最終的に最大値にするため降順に並べ替え
print(''.join(S))