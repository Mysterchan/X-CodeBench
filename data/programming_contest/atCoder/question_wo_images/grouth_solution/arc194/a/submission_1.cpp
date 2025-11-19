#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N = 2e5 + 10;
int n;
int a[N], f[N];
signed main()
{
	cin >> n;
	for(int i = 1; i <= n; i ++)
		scanf("%lld", &a[i]);
	f[0] = 0, f[1] = a[1];
	for(int i = 2; i <= n; i ++)
		f[i] = max(f[i - 1] + a[i], f[i - 2]);
	cout << f[n];
	return 0;
}
