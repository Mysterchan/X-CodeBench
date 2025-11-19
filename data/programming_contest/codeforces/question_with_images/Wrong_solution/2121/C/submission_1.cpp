
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define sqrt(a) sqrtl(a)
#define abs(a) llabs(a)
#define pow(a) powl(a)
typedef  pair<int,int> pi ;
#define if1(x) for(int i = 1;i<=x;i++)
#define if0(x) for(int i = 0;i< x;i++)
#define jf0(x) for(int j = 0;j< x;j++)
#define jf1(x) for(int j = 1;j<=x;j++)
#define pb push_back
const int mod = 1e9+7;
const int inf = 0xFFFFFFFFFFFFFFF;
const int N = 2e5+10;

void solve(){
    int m,n;
    cin>>n>>m;
    int mx = -1;
    vector<pi>ids;
    int mxc,mxr;
    if1(n)jf1(m){
        int te;
        cin>>te;
        if(te > mx){
            mx = te;
            ids.clear();
            ids.push_back({i,j});
        }else if(te == mx){
            ids.push_back({i,j});
        }
    }
    sort(ids.begin(),ids.end());
    pi pre = {0,0};
    pi te = {0,0};
    int ans = mx;
    if0(ids.size()-1){
        if(ids[i].first == ids[i+1].first ||ids[i].second == ids[i+1].second)continue;
        if(pre == te) pre = ids[i];//第一次
        else{
            if(ids[i+1].first == pre.first ||ids[i+1].second == pre.second)continue;
            else {
                cout<<mx<<endl;
                return;
            }
        }
    }
    cout<<mx-1<<endl;

}
signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr); 
    int t=1;
    cin>>t;
    while (t--)
    {
        solve();
    }
    return 0;
}
