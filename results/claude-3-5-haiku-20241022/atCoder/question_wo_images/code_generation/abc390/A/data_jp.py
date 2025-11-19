A = list(map(int, input().split()))

# 隣り合う2つの項を入れ替える操作を1回行った結果が[1,2,3,4,5]になるかチェック
found = False
for i in range(4):
    # i番目とi+1番目を入れ替える
    B = A[:]
    B[i], B[i+1] = B[i+1], B[i]
    
    if B == [1, 2, 3, 4, 5]:
        found = True
        break

if found:
    print("Yes")
else:
    print("No")