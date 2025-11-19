#pragma GCC optimize("O3")
#include <bits/stdc++.h>
#pragma GCC target("avx,avx2,sse,sse4,popcnt")
#if __has_include(<tr2/dynamic_bitset>)
#include <tr2/dynamic_bitset>
#endif
using namespace std;
#if 0
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using ttree = tree<pair<ll, int>, null_type, less<pair<ll, int>>, rb_tree_tag, tree_order_statistics_node_update>;
#endif

using ll = long long;
using ull = unsigned long long;
using ldbl = long double;
template<typename T> using two = pair<T, T>;
#define all(X...) (X).begin(), (X).end()
#define all_r(X...) (X).rbegin(), (X).rend()
using _ntests_t = unsigned;
#define ntests _ntests_t _nt; cin >> _nt; [[maybe_unused]] NEXT_TEST: while (_nt --)
#define next_test goto NEXT_TEST
#define line "\n"

constexpr int mod  [[maybe_unused]] = 998244353;
constexpr int mod1 [[maybe_unused]] = 1000000007;
#define mod mod1
template<class T, class Cmp> using pq_cmp = priority_queue<T, vector<T>, Cmp>;
template<typename T> T sq(T x) { return x * x; }
template<typename T> void upd(T &x, T y) { x = max(x, y); }
template<typename T> void updm(T &x, T y) { x = min(x, y); }
template<typename T, typename U> T fst(pair<T, U> const &a) { return a.first; }
template<typename T, typename U> U scn(pair<T, U> const &a) { return a.second; }

#define fl(I,L,R) for(int I = (L); I < (R); I ++)
#define fL(I,L,R) for(int I = (L); (R); I ++)
#define mkp make_pair

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	ntests {
		int n;
		cin>>n;vector<int>a(n);for(auto&i:a)cin>>i;
		sort(all(a));
		int r=0;
		fl(i,0,n){
			ll cs=0;
			fl(j,i+1,n+1){
				cs+=a[j-1];
				int p=0;
				for(int Z=20;Z>=0;Z--){
					if((1<<Z)+p+i<j&&a[(1<<Z)+p+i]*(ll)(j-i)<=cs)p+=1<<Z;
				}
				upd(r,j-i-p);
			}
		}
		cout<<r-1<<line;
	}
}
