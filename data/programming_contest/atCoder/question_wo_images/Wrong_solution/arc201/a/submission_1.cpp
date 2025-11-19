#include<bits/stdc++.h>
using namespace std;
#define int long long
const int N=2e5+6;
struct node
{
    int a,b,c;
};
vector<node> p;
signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int i,j,k;
    int n,m;
    int T=1;
    cin>>T;
    while(T--)
    {   
        long long ans=0;
        long long t1=0,t2=0,t3=0;
        p.clear();
        cin>>n;
        for(i=1;i<=n;i++)
        {
            int x,y,z;
            cin>>x>>y>>z;
            p.push_back({x,y,z});
        }
        for(auto &it:p)
        {
            if(it.b>=it.a+it.c)
            {
                t1+=it.a;
                t2+=it.c;
            }
            else
            {
                if(it.b<=it.a)
                {
                    t1+=it.b;
                    t3+=it.b;
                }
                else
                {
                    t1+=it.a;
                    t3+=it.a;
                    t2=t2+it.b-it.a;
                    t3=t3+it.b-it.a;
                }
            }
        }
        if(t1<=t2)
        {
            ans=t1;
        }
        else
        {
            if(t1-t3<=t2+t3)
            {
                ans=(t1+t2)/2;
            }
            else
            {
                ans=t2+t3;
            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}