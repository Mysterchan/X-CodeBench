#include <bits/stdc++.h>
#define mp make_pair
#define fi first
#define se second
using namespace std;

int64_t s, k;
int64_t ans;

inline void Solve();
int main()
{
	int t;
	cin >> t;
	++t;
	while (--t)
		Solve();
	return 0;
}
int v[1000010];
inline void Solve()
{
	cin >> s >> k;
	ans = 0;
	if (s % k == 0)
		cout << k << endl;
	else if (s >= k * k)
		cout << k - 2 << endl;
	else
	{
		queue<pair<int, bool>> p;
		vector<int> pos;
		memset(v, 0, sizeof(int) * (s + 1));
		p.push(mp(0, 0));
		for (int i = k; i >= 1; --i)
		{
			if (i == 1)
			{
				cout << "1" << endl;
				return;
			}
			if ((k - i) & 1)
			{
				while (p.size())
				{
					int x = p.front().fi, op = p.front().se;
					p.pop();
					if (x == s)
					{
						cout << i << endl;
						return;
					}
					if (op)
						pos.push_back(x);
					if (x - i >= 0 && v[x - i] != i)
					{
						v[x - 1] = i;
						p.push(mp(x - i, 1));
					}
				}
			}
			else
			{

				while (p.size())
				{
					int x = p.front().fi, op = p.front().se;
					p.pop();
					if (x == s)
					{
						cout << i << endl;
						return;
					}
					if (op)
						pos.push_back(x);
					if (x + i <= s && v[x + i] != i)
					{
						v[x + i] = i;
						p.push(mp(x + i, 1));
					}
				}
			}
			while (pos.size())
			{
				p.push(mp(pos.back(), 0)), pos.pop_back();
			}
		}
	}
}