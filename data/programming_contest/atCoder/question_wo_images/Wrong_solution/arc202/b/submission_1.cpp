#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ldb;
const int INF = 0x3f3f3f3f;
const ll LLINF = 0x3f3f3f3f3f3f3f3f;
const ldb eps = 1e-14;
const ldb pi = acos(-1.0);
const int P = 998244353;
const int N = 400005;

int fac[N],inv[N];

int pwr(int x,int y){
	int ret = 1,tmp = x;
	while(y){
		if(y & 1) ret = 1ll * ret * tmp % P;
		tmp = 1ll * tmp * tmp % P; y >>= 1;
	}
	return ret;
}

int comb(int x,int y){
    if(x < y) return 0;
    return 1ll * fac[x] * inv[y] % P * inv[x - y] % P;
}

int solve(){
    int h,w;
    cin >> h >> w;
    auto chk = [&](int del) -> int {
        return del != 0 && __gcd(del,w) != 1;
    };
    if(!(h & 1)) return 0;
    if(!(w & 1)){
        int ans = 0;
        for(int a = 0;a <= h;a ++){
            for(int b = 0;b <= h;b ++){
                for(int c = 0;c <= h;c ++){
                    int d = h - a - b - c;
                    if(d >= 0){
                        if(chk(abs(a + c - b - d)) && chk(abs(b + c - a - d)))
                            ans = (ans + 1ll * comb(h,a) * comb(h - a,b) % P * comb(h - a - b,c) % P) % P;
                    }
                }
            }
        }
        return ans;
    }
    int ans = pwr(2,h);
    for(int a = 0;a <= h;a ++){
        int del = abs(a - (h - a));
        if(chk(del)){
            ans = (ans - comb(h,a) + P) % P;
        }
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    fac[0] = 1; for(int i = 1;i < N;i ++) fac[i] = 1ll * i * fac[i - 1] % P;
    for(int i = 0;i < N;i ++) inv[i] = pwr(fac[i],P - 2);
    cout << solve() << '\n';
    return 0;
}