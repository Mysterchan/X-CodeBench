#include<bits/stdc++.h>
using namespace std;
#define rep(i, s, t) for(int i = (s); i <= (t); i ++)
#define per(i, s, t) for(int i = (s); i >= (t); i --)
template<typename T, typename T2>
inline void chmin(T &x, T2 &&y) { x = min(x, y); }
template<typename T, typename T2>
inline void chmax(T &x, T2 &&y) { x = max(x, y); }
typedef long long ll;

const int N = 3e5 + 5;
int n, a[N], q;

bool vis[N];
vector<int> sz[2];

bitset<N> ok;

int cnt[N];
void init(vector<int> v)
{
    for(int i : v) cnt[i] ++;
    rep(i, 1, n)
    {
        int d = (cnt[i] - 1) / 2;
        cnt[i] -= d * 2;
        cnt[i * 2] += d;
    }
    ok[0] = 1;
    rep(i, 1, n) if(cnt[i])
    {
        rep(j, 1, cnt[i])
            ok |= ok << i / 2;
    }
}

int ss[N];

signed main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    cin >> n;
    rep(i, 1, n) cin >> a[i];

    int s = 0, c = 0, cc = 0;
    rep(i, 1, n) if(!vis[i])
    {
        int cnt = 0;
        for(int j = i; !vis[j]; j = a[j])
            vis[j] = 1, cnt ++;
        if(cnt == 1)
        {
            cc ++;
            continue;
        }
        sz[cnt & 1].push_back(cnt);
        s += cnt / 2, c += cnt & 1;
    }
    rep(i, 0, 1) sort(sz[i].begin(), sz[i].end(), greater<int>());
    init(sz[0]); int ssz = accumulate(sz[0].begin(), sz[0].end(), 0);

    rep(i, 0, (int)sz[1].size() - 1)
    {
        if(i) ss[i] = ss[i - 1];
        ss[i] += sz[1][i] / 2;
    }

    cin >> q;
    while(q --)
    {
        int a, b, c; cin >> a >> b >> c;
        
        int ans = 0;
        
        int k1 = 0, k2 = 0;
        
        if(a >= ssz / 2 || ok[a])
        {
            int s = min(ssz, a * 2);
            a -= s / 2; k2 += s / 2; ans += s;
        }
        else
        {
            k2 += a - 1, k1 += 2, ans += 2 * a, a = 0;
        }


        int k = upper_bound(ss, ss + sz[1].size(), a) - ss - 1;
        a -= ss[k], k2 += ss[k] - k - 1, k1 += 2 * k + 2, ans += ss[k] * 2;
        if(a && k + 1 < sz[1].size())
            k2 += a - 1, k1 += 2, ans += a * 2, a = 0;
        
        int c1 = min(a, k1 / 2);
        a -= c1, k2 += c1, k1 -= 2 * c1, ans += c1;
        int ca = min(a, cc); ans += ca; a -= ca;
        
        int b2 = min(b, k2); ans += 2 * b2; b -= b2;
        int b1 = min(b, k1); ans += b1; b -= b1;

        cout << ans << "\n";
    }

    return 0;
}