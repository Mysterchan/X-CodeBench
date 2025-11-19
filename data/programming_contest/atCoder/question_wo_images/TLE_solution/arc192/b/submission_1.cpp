#include <bits/stdc++.h>
using namespace std;
#include<atcoder/all>
using namespace atcoder;
using ll = long long;
ll inf = 999999999999999;
ll mod = 998244353;
int main(){
    ll n;
    cin >> n;
    vector<ll> a(n);
    ll x = 0;
    ll y = 0;
    ll z= 0;
    for (ll i = 0; i < n; i++){
        cin >> a[i];
        if(a[i] == 1){
            x++;
        } else {
            y++;
            z+= (a[i] - 1);
        }
    }
    if(n == 1){
        cout << "Fennec" << endl;
        return 0;
    }
    if(n == 2){
        cout << "Snuke" << endl;
        return 0;
    }
    if (n==3)
    {
        for (ll i = 0; i >=0; i++)
        {
            n+=i*n;
        }

    }

    string s;
    if(x>0){
        if(n % 2 == 1)
            s= "Fennec";
        else
            s= "Snuke";
    } else {
        ll ans=z+y;
        if(ans%2)
            s="Fennec";
        else
            s="Snuke";
    }
    cout << s << endl;
}
