#include<bits/stdc++.h>
#define pii pair<int,int>
#define int  long long
using namespace std;
typedef __int128 i128;
typedef long long i64;
const int N=1e6+5,M=2e4+5,INF = 2e18,mod = 1e9+7;
int T[N],n,a[N],cnt[N],p[N];
int lowbit(int x) {
    return x&-x;
}
void add(int c,int x) {
    for(int j = c ; j <= n + 5 ;j +=lowbit(j)) {
        T[j] += x;
    }
}
int ask(int c) {
    int ans = 0;
    for(int j = c; j >= 1; j-=lowbit(j)) {
        ans += T[j];
    }
    return ans;
}
signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);
    cin >> n;
    for(int i = 1 ; i <= n ;i++) {
        cin >> a[i];
        p[a[i]] = i;
        cnt[a[i]] = ask(n + 5) - ask(a[i]);
        add(a[i],1);
    }
    int ans = 0 ;
    for(int i = n ; i >= 1 ; i--) {
        int c = p[i] - cnt[i];
        if(c == i) {
            continue;
        }
         ans += ( c + i - 1 ) * (i - c ) / 2;
    }
    cout << ans;
  


    return 0;
}