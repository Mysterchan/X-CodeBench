#include <bits/stdc++.h>
using namespace std;

const int N=2e5+10;

typedef long long ll;

int n;
int a[N];

int top;
int st[N];

ll solve()
{
    top=0;
    ll res=0;
    for(int i=1; i<=n; i++)
    {
        while(top && st[top]<=a[i])
            if(top==1) res+=a[i]-st[top--],a[i]++;
            else
                if(st[top-1]>a[i]) res+=a[i]-st[top--],a[i]++;
                else res+=st[top-1]-st[top--],st[top]++;

        while(top>1 && st[top]==st[top-1]) st[top-1]++,top--;
        st[++top]=a[i];
    }
    while(top>1) res+=st[top-1]-st[top--],st[top]++;
    return res;
}

int main()
{
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);

    int T;
    cin>>T;
    while(T--)
    {
        cin>>n;
        for(int i=1; i<=n; i++) cin>>a[i];
        cout<<solve()<<"\n";
    }

    return 0;
}
