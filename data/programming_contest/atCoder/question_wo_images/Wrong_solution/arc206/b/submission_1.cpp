#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define ull unsigned long long
#define PII pair<int,int>
#define yes cout << "Yes\n"
#define no cout << "No\n"
using namespace std;
const int N = 1e6 + 10;
const ll M = 998244353;
const int inf = -1e9;
int main()
{
    ios::sync_with_stdio(0),cin.tie(0);
    int _ = 1;
    while(_ --)
    {
        int n;cin >> n;
        vector<int>p(n + 1),c(n + 1);
        vector<vector<int>>f(n + 1);
        for(int i = 1;i <= n;i ++)
        {
            cin >> p[i];
        }
        for(int i = 1;i <= n;i ++)cin >> c[i];
        for(int i = 1;i <= n;i ++)f[c[i]].pb(p[i]);
        auto Lis = [&] (vector<int>a) -> int
        {
            int sz = a.size();
            if(!sz)return 0;
            vector<int>dp(sz + 2);int len = 1;dp[1] = a[0];dp[0] = 0;
            for(int i = 1;i < sz;i ++)
            {
                int l = 1,r = len;int t = 0;
                if(a[i] >= dp[len])dp[++ len] = a[i];
                else
                {
                    while(l <= r)
                    {
                        int mid = (l + r) >> 1;
                        if(dp[mid - 1] <= a[i] && dp[mid] > a[i])
                        {
                            l = mid + 1;t = max(t , mid);
                        }
                        else r = mid - 1;
                    }
                    dp[t] = min(dp[t] , a[i]);
                }
            }
            return len;
        };
        ll ans = 0;
        for(int i = 1;i <= n;i ++)
        {
            int len = Lis(f[i]);
            ans += 1ll * (f[i].size() - len) * i;
        }
        cout << ans << '\n';
    }
}