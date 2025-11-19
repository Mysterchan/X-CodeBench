#include<bits/stdc++.h>
using namespace std;
#define int long long
int n;
const int N = 5e5+5;
int tree[N],p[N], ans[N];
void modify(int l, int r, int k){
    for(int i = l; i <= r; i += i&(-i)) tree[i] += k;
}
int query(int x){
    int res = 0;
    for(int i = x; i; i -= i&-i) res += tree[i];
    return res; 
}
void solve(){
    cin>>n;
    for(int i = 1; i <= n; i++) {
        cin>>p[i];
        modify(i,n,1);
    }
    for(int i = n; i >= 1; i--){
        int l = 1, r = n;
        while(l < r){
            int mid = l+r>>1;
            if(query(mid) >= p[i]) r = mid;
            else l = mid+1;
        }
        ans[l] = i;
        modify(l,n,-1);
    }
    for(int i = 1; i <= n; i++) cout<<ans[i]<<' ';

}
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    int T = 1;
    while(T--){
        solve();
    }
    return 0;
}