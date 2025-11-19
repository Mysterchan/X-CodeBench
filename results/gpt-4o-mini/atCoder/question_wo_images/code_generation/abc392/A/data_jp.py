A = list(map(int, input().split()))
A.sort()

# A_1, A_2, A_3をそれぞれB_1, B_2, B_3に割り当て
B1, B2, B3 = A[0], A[1], A[2]

# B1 * B2がB3に等しいかをチェック
if B1 * B2 == B3:
    print("Yes")
else:
    print("No")