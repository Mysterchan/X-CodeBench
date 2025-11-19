#include <bits/stdc++.h>
using namespace std;

const int N = 201000;
const long long INF = 1e18;
int n, q, a[N];

int main() {
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
    
    while (q--) {
        int l, r;
        scanf("%d%d", &l, &r);
        
        long long dp[3][3];
        long long nd[3][3];
        
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                dp[i][j] = INF;
        
        dp[0][0] = 0;
        
        for (int pos = l; pos <= r; pos++) {
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    nd[i][j] = INF;
            
            for (int c1 = 0; c1 < 3; c1++) {
                for (int c2 = 0; c2 < 3; c2++) {
                    if (dp[c1][c2] >= INF) continue;
                    
                    for (int c3 = 0; c3 < 3; c3++) {
                        if (c1 + c3 >= 2 && c2 + c3 >= 2) {
                            nd[c2][c3] = min(nd[c2][c3], dp[c1][c2] + (long long)c3 * a[pos]);
                        }
                    }
                }
            }
            
            memcpy(dp, nd, sizeof(dp));
        }
        
        long long ans = INF;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                ans = min(ans, dp[i][j]);
        
        printf("%lld\n", ans / 2);
    }
    
    return 0;
}