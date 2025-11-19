inf = float("inf")

def get_sml2(A):
    lis = [inf] * 2
    for v in A:
        lis.append(v)
        lis.sort()
        lis = lis[:2]
    return sum(lis)

def get_sml3(A):
    lis = [inf] * 3
    for v in A:
        lis.append(v)
        lis.sort()
        lis = lis[:3]
    return sum(lis)

def calc(A,B):
    dp = [[inf] * 3 for _ in range(3)]
    dp[0][0] = 0
    for a,b in zip(A,B):
        ndp = [[inf] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if (i,j) not in ((0,2),(2,0)):
                    ndp[i][j] = min(ndp[i][j], dp[i][j])
                if i < 2:
                    ndp[i+1][j] = min(ndp[i+1][j], dp[i][j] + a)
                if j < 2:
                    ndp[i][j+1] = min(ndp[i][j+1], dp[i][j] + b)
                if i < 2 and j < 2:
                    ndp[i+1][j+1] = min(ndp[i+1][j+1], dp[i][j] + a + b)
        dp = ndp
    return dp[2][2]

def calc2(A,B):
    dp = [[inf] * 3 for _ in range(3)]
    dp[0][0] = 0
    for a,b in zip(A,B):
        ndp = [[inf] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if (i,j) != (0,2):
                    ndp[i][j] = min(ndp[i][j], dp[i][j])
                if i < 2:
                    ndp[i+1][j] = min(ndp[i+1][j], dp[i][j] + a)
                if j < 2:
                    ndp[i][j+1] = min(ndp[i][j+1], dp[i][j] + b)
                if i < 2 and j < 2:
                    ndp[i+1][j+1] = min(ndp[i+1][j+1], dp[i][j] + a + b)
        dp = ndp
    return dp[2][2]

TT = int(input())

for loop in range(TT):

    N = int(input())
    U = list(map(int,input().split()))
    D = list(map(int,input().split()))
    L = list(map(int,input().split()))
    R = list(map(int,input().split()))

    ans = min( calc(U,D) + get_sml2(L) + get_sml2(R) , calc(L,R) + get_sml2(U) + get_sml2(D) )
    ans = min(ans, get_sml2(L) + get_sml2(R) + get_sml3(U) + get_sml3(D) )
    ans = min(ans, get_sml3(L) + get_sml3(R) + get_sml2(U) + get_sml2(D) )

    ans = min(ans, calc2(U,D) + calc2(L,R) , calc2(D,U) + calc2(R,L) )

    print (ans)