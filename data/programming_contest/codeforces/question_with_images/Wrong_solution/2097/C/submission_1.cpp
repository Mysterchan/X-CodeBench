#include <bits/stdc++.h>

using namespace std;

using i64 = long long;

int gcd(int n, int m) { return !m ? n : gcd(m, n % m); }

void exgcd(int a,int b,int &x,int &y){
	if(!b){
		x=1;
		y=0;
		return;
	}
	exgcd(b,a%b,x,y);
	int t=x;
	x=y;
	y=t-a/b*y;
}

int inv(int a,int b){
  int x, y;
	exgcd(a,b,x,y);
	x=(x%b+b)%b;
	return x;
}

int main() {
  ios::sync_with_stdio(0), cin.tie(0);

  int t;
  cin >> t;
  while (t--) {
    int n, x, y, ux, uy;

    cin >> n >> x >> y >> ux >> uy;
    ux %= n, uy %= n;
    if (x % gcd(n, ux) != 0 || y % gcd(n, uy) != 0) {
      cout << "-1\n";
      continue;
    }

    int d1 = gcd(n, ux), d2 = gcd(n, uy);
    int m1 = n / d1, m2 = n / d2;
    ux /= d1, uy /= d2;
    x /= d1, y /= d2;

    x = 1ll * (m1 - x) * inv(ux, m1) % m1;
    y = 1ll * (m2 - y) * inv(uy, m2) % m2;

    int d = gcd(m1, m2);
    int t1 = m1 / d, t2 = m2 / d;

    if ((y - x) % d != 0) {
      cout << "-1\n";
      continue;
    }

    int res = (y - x) / d;
    int lcm = t1 * t2 * d;
    int gu = 1ll * res * inv(t1, t2) % lcm;

    cout << ((x + 1ll * gu * m1) % lcm + lcm) % lcm << '\n';
  }
}