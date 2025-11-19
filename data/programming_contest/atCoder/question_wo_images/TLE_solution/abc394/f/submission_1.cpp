#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#include <iomanip>
#include <stack>
#include <queue>
#include <numeric>
#include <map>
#include <unordered_map>
#include <set>
#include <fstream>
#include <chrono>
#include <random>
#include <bitset>
#define rep(i,n) for(int i=0;i<(n);i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define sz(x) ((int)(x).size())
#define pb push_back
using ll = long long;
using namespace std;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
ll gcd(ll a, ll b) {return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) {return a/gcd(a,b)*b;}

int N;
vector<vector<int>> G;
unordered_map<ll,int> memo;

ll f(int a,int b){
  return (ll)a*N*2+b;
}

int dfs(int n,int p){
  if(memo.find(f(n,p))!=memo.end()) return memo[f(n,p)];
  vector<int> V;
  for(auto x:G[n]){
    if(x==p) continue;
    V.pb(dfs(x,n));
    sort(rall(V));
    if(sz(V)>4) V.resize(4);
  }
  sort(rall(V));
  if(p==N){
    if(sz(V)<4) memo[f(n,p)] = -1;
    else memo[f(n,p)] = accumulate(V.begin(),V.begin()+4,1);
  }
  else{
    if(sz(V)<3) memo[f(n,p)] = 1;
    else memo[f(n,p)] = accumulate(V.begin(),V.begin()+3,1);
  }
  return memo[f(n,p)];
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> N;
  G.resize(N);
  rep(i,N-1){
    int a,b;
    cin >> a >> b; a--; b--;
    G[a].pb(b); G[b].pb(a);
  }
  rep(i,N) dfs(i,N);
  int ans = -1;
  for(auto [p,x]:memo){
    if(p%(N*2)==N) chmax(ans,x);
  }
  cout << ans << endl;
  return 0;
}

