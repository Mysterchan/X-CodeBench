#include <bits/stdc++.h>
using namespace std;
#define LZW0063 ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define VVI vector<vector<int>>
#define VVL vector<vector<long long>>
#define fr(i, n) for (int i = 0; i < (n); i++)
#define mx(v) *max_element(v.begin(), v.end())
#define all(v) (v).begin(), (v).end()
#define PII pair<int, int>
#define MII map<int, int>
#define VI vector<int>
#define VLL vector<long long>
#define VC vector<char>
#define SC set<char>
#define SI set<int>
#define SL set<long long>
#define ll long long
#define yes cout << "YES"
#define no cout << "NO"
#define PI 3.1415926535897932384626433832795
const int mod = 1e9+7;
const int N = 100005;
VLL fact(N);
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
int power(int x, int n){ int ans = 1%mod; while(n>0){ if(n&1){ans = 1LL*ans*x%mod;} x = 1LL*x*x%mod; n>>=1;} return ans;}
ll modInv(ll n){return power(n,mod-2);}
void facto(){fact[0]=1; for(int i =1; i<N;i++)fact[i]=fact[i-1]*i%mod;}
ll comb_small(ll n, ll k) {if (k < 0 || k > n) return 0;ll num = 1;for (int i = 0; i < k; i++)num = num * ((n - i + mod) % mod) % mod;return num * modInv(fact[k]) % mod;}
ll comb_lr(ll n, ll k) {ll res = 1;while (k) {res = res*comb_small(n%mod, k%mod)%mod;n /= mod;k /= mod;}return res;}
int check_kth_bits(int x,int k){return (x>>k)&1;}
bool iseven(int x){if(x&1){ return false;} else{return true;}}
void solve() {
    facto();
    ll a, b, k; cin >> a >> b >> k;
    ll n = ((a - 1) * k) % mod + 1;
    ll m = ((b - 1) * k % mod * comb_lr((a - 1) * k + 1, a) % mod + 1) % mod;
    cout << n << " " << m << "\n";
}
int main(){
    LZW0063;
    int TC = 1;
    cin>>TC;
    while(TC--) solve();
	return 0;
}