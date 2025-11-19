#include<bits/stdc++.h>
using namespace std;
#define int long long
const int maxval = 1e6 + 1;
signed main()
{
    int n,k;
    cin>>n>>k;
    vector <int> a(n+1);
    for(int i=1;i<=n;i++)cin>>a[i];
    vector <int> ff(maxval);
    vector <int> dd(maxval);
    vector <int> xx(maxval);
    for(int i=1;i<=n;i++)ff[a[i]]++;
    for(int x = 1;x < maxval;x++)
    {
        for(int y = x;y < maxval;y += x)
        {
            dd[x] += ff[y];
        }
    }
    for(int d = 1;d < maxval;d++)
    {
        if(dd[d] < k)continue;
        for(int e = d;e < maxval;e += d)
        {
            xx[e] = max(xx[e],d);
        }
    }
    for(int i=1;i<=n;i++)cout<<xx[a[i]]<<'\n';
}