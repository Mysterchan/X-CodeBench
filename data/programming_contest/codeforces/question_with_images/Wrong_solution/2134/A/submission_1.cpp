#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
    ios::sync_with_stdio(false); cin.tie(nullptr);
    ll t; cin>>t;
    while(t--)
    {
        ll n , r , b; cin>>n>>r>>b;
        if (r == b)
        {
            cout<<"YES"<<endl;
            continue;
        }
        if (n % 2 == 0)
        {
            if ((r+b) % 2 == 0)
            {
                cout<<"NO"<<endl;
            }
            else
            {
                cout<<"YES"<<endl;
            }
        }
        else
        {
            if ((r+b) % 2 == 1)
            {
                cout<<"NO"<<endl;
            }
            else
            {
                cout<<"YES"<<endl;
            }
        }
    }
}