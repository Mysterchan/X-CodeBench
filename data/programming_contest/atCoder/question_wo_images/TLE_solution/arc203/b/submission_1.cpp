#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
using namespace std;

const int NR = 2e5 + 10;
int a[NR], b[NR];
string s, t;

bool check(int n)
{
	for (int i = 1; i <= n; i ++)
	{
		if (s[i] != t[i]) return false;
	}
	return true;
}

int main()
{
	mt19937 gen(time(0));
	int T;
	scanf("%d", &T);
	while (T --)
	{
		clock_t st = clock();
		int n;
		scanf("%d", &n);
		s = " ";
		t = " ";
		for (int i = 1; i <= n; i ++)
		{
			scanf("%d", &a[i]);
			s += ('0' + a[i]);
		}
		for (int i = 1; i <= n; i ++)
		{
			scanf("%d", &b[i]);
			t += ('0' + b[i]);
		}
		uniform_int_distribution<int> A(1, n - 1);
		bool flag = true;
		while (!check(n))
		{
			int a = A(gen);
			uniform_int_distribution<int> B(a, n - 1);
			int b = B(gen);
			uniform_int_distribution<int> C(b + 1, n);
			int c = C(gen);
			uniform_int_distribution<int> D(c, n);
			int d = D(gen);
			int cnt1 = 0;
			int cnt2 = 0;
			for (int i = a; i <= b; i ++)
			{
				cnt1 += (s[i] == '1');
			}
			for (int i = c; i <= d; i ++)
			{
				cnt2 += (s[i] == '1');
			}
			if (cnt1 != cnt2) continue;
			string s1 = s.substr(1, a - 1);
			string s2 = s.substr(a, b - a + 1);
			string s3 = s.substr(b + 1, c - b - 1);
			string s4 = s.substr(c, d - c + 1);
			string s5 = s.substr(d + 1, n - d);
			s = " " + s1 + s4 + s3 + s2 + s5;
			if (clock() - st >= 1.9 * CLOCKS_PER_SEC / T)
			{
				flag = false;
				break;
			}
		}
		if (flag) puts("Yes");
		else puts("No");
	}
	return 0;
}