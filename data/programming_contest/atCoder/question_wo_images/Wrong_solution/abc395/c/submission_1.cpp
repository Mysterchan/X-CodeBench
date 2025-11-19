

#include <bits/stdc++.h>

#define endl '\n'
#define all(a) a.begin(), a.end()

using namespace std;
using ull = unsigned long long;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {-1, 0, 1, 0, -1, -1, 1, 1};
const int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
const int MOD = 1e9 + 7;
const int N = 1e5 + 10;

template <typename T>
inline T read()
{
    T x = 0, f = 1;
    char ch = 0;
    for (; !isdigit(ch); ch = getchar())
        if (ch == '-')
            f = -1;
    for (; isdigit(ch); ch = getchar())
        x = (x << 3) + (x << 1) + (ch - '0');
    return x * f;
}

template <typename T>
inline void write(T x)
{
    if (x < 0)
        putchar('-'), x = -x;
    if (x > 9)
        write(x / 10);
    putchar(x % 10 + '0');
}

template <typename T>
inline void print(T x)
{
    write(x);
}



void miyan()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    map<int, vector<int>> m;
    for (int i = 0; i < n; ++i)
        m[a[i]].push_back(i);

    if (m.size() == n)
    {
        cout << -1 << endl;
        return;
    }

    int l = INT_MAX, r = INT_MIN;
    for (auto [x, v] : m)
        if (v.size() > 1)
            l = min(l, *v.begin()), r = max(r, *v.rbegin());

    cout << r - l + 1 << endl;
}

int main()
{
#ifdef LOCAL
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    clock_t c1 = clock();
#endif

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    miyan();

#ifdef LOCAL
    cerr << "Time used: " << clock() - c1 << " ms" << endl;
#endif

    return 0;
}