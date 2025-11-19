#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
constexpr LL mod = 998244353ll;

template <typename Type> Type md(Type w1, const Type w2 = mod) { 
    w1 %= w2; 
    if(w1 < 0) w1 += w2; 
    return w1; 
}

const int N = 410;
LL C[N<<1][N<<1], z[N<<1];
LL dp[N][N];

void init(int len, LL d) {
    for(int i = 0; i <= len; i++) C[i][0] = 1ll;
    for(int i = 1; i <= len; i++) 
        for(int j = 1; j <= i; j++) 
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod;
    
    z[0] = 1ll; 
    for(int i = 1; i <= len; i++) 
        z[i] = z[i-1] * d % mod;
}

int main() {
    int n, m;
    LL d;
    scanf("%d%d%lld", &n, &m, &d);
    
    if(n == 1 || m == 1) {
        printf("%lld\n", d % mod);
        return 0;
    }
    
    init(n + m, d);
    
    for(int i = 0; i <= n; i++) {
        for(int j = 0; j <= m; j++) {
            if(min(i, j) <= 1) {
                dp[i][j] = ((i && j) ? z[(i ^ j ^ 1)] : 1ll);
                continue;
            }
            
            LL sum = 0;
            for(int i2 = 1; i2 <= i; i2++) {
                for(int j2 = 1; j2 <= j; j2++) {
                    LL w = dp[i-i2][j-j2] * d % mod;
                    w = w * C[i][i2] % mod * C[j][j2] % mod;
                    if((i2 ^ j2) & 1) sum = md(sum - w);
                    else sum = md(sum + w);
                }
            }
            
            for(int i2 = 1; i2 <= i; i2++) {
                LL w = dp[i-i2][j] * z[i2] % mod * C[i][i2] % mod;
                if(i2 & 1) sum = md(sum + w);
                else sum = md(sum - w);
            }
            
            for(int j2 = 1; j2 <= j; j2++) {
                LL w = dp[i][j-j2] * z[j2] % mod * C[j][j2] % mod;
                if(j2 & 1) sum = md(sum + w);
                else sum = md(sum - w);
            }
            
            dp[i][j] = sum;
        }
    }
    
    printf("%lld\n", dp[n][m]);
    return 0;
}