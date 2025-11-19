#include<bits/stdc++.h>
using namespace std ; 

#define int long long

const int N = 405 , mod = 998244353 ;

int f[N][N] ; 

int c[N][N] , n , m , C ; 

int pw[N] ; 

int g[N][N] ; 

signed  main() {
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0) ; 
    cin >> n >> m >> C ; C %= mod ;
    pw[0] = 1; 
    for(int i = 1 ; i <= max(n,m) ; i ++ ) pw[i] = pw[i-1] * C % mod ;
    for(int i = 0 ; i <= max(n,m) ; i ++ ) {
        c[i][0] = 1 ;
        for(int j = 1 ; j <= i ; j ++ ) c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod ; 
    }
    for(int i = 0 ; i <= n ; i ++ ) f[i][0] = 1 ;
    for(int i = 0 ; i <= m ; i ++ ) f[0][i] = 1 ;
    for(int i = 0 ; i <= n ; i ++ ) {
        for(int j = 0 ; j <= m ; j ++ ) {
            for(int qd = 1 ; qd <= i ; qd ++ ) {
                if(!i || !j ) break ;  
                if(qd & 1) (f[i][j] += c[i][qd] * f[i-qd][j] % mod * pw[qd] % mod ) %= mod ;
                else (f[i][j] += mod - c[i][qd] * f[i-qd][j] % mod * pw[qd] % mod ) %= mod ; 
            }
            for(int qd = 1 ; qd <= j ; qd ++ ) {
                if(!i || !j ) break ; 
                if(qd & 1) (f[i][j] += c[j][qd] * f[i][j-qd] % mod * pw[qd] % mod ) %= mod ;
                else (f[i][j] += mod - c[j][qd] * f[i][j-qd] % mod * pw[qd] % mod ) %= mod ; 
            }
            for(int q1 = 1 ; q1 <= i ; q1 ++ ) {
                if(!i || !j ) break ; 
                if(q1 & 1) (f[i][j] += c[i][q1] * C % mod * g[i-q1][j] % mod ) %= mod ; 
                else (f[i][j] += mod - c[i][q1] * C % mod * g[i-q1][j] % mod ) %= mod ; 
            }
            for(int q2 = j + 1 ; q2 <= m ; q2 ++ ) {
                if( (q2 - j + 1)& 1) (g[i][q2] += c[q2][q2-j] * f[i][j] % mod ) %= mod ;
                else (g[i][q2] += mod - c[q2][q2-j] * f[i][j] % mod ) %= mod ;
            }
        }
    }
    int ans = 0 ; 
    for(int q1 = 1 ; q1 <= n ; q1 ++ ) {
        for(int q2 = 1 ; q2 <= m ; q2 ++ ) {
            if(q1+q2&1) (ans += mod - c[n][q1] * c[m][q2] % mod * C % mod * f[n-q1][m-q2] % mod ) %= mod ;
            else (ans += c[n][q1] * c[m][q2] % mod * C % mod * f[n-q1][m-q2] % mod ) %= mod ; 
        }
    } cout << ans ;
    return 0 ; 
}