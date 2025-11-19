#include "bits/stdc++.h"
using namespace std;

#define integer int
#define int long long
#define endl '\n'

#define MOD (int)(1e9 + 7)
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(nullptr);

bool comp_by_y(const pair<int, int> &a, const pair<int, int> &b)
{
    return a.second < b.second;
}

void test()
{
    int n;
    cin >> n;
    vector<pair<int, int>> points(n);

    for (int i = 0; i < n; i++)
    {
        cin >> points[i].first >> points[i].second;
    }

    if (n == 1)
    {
        cout << 1 << '\n';
        return;
    }

    vector<pair<int, int>> by_x = points;
    vector<pair<int, int>> by_y = points;
    sort(by_x.begin(), by_x.end());
    sort(by_y.begin(), by_y.end(), comp_by_y);

    vector<int> candidates;
    for (int i = 0; i < n; i++)
    {
        if (points[i].first == by_x[0].first || points[i].first == by_x[n - 1].first ||
            points[i].second == by_y[0].second || points[i].second == by_y[n - 1].second)
        {
            candidates.push_back(i);
        }
    }

    int ans = LLONG_MAX;
    for (auto candidate : candidates)
    {
        vector<int> xs, ys;
        for (int i = 0; i < n; i++)
        {
            if (i == candidate)
            {
                continue;
            }
            xs.push_back(points[i].first);
            ys.push_back(points[i].second);
        }
        int len = *max_element(xs.begin(), xs.end()) - *min_element(xs.begin(), xs.end()) + 1;
        int wid = *max_element(ys.begin(), ys.end()) - *min_element(ys.begin(), ys.end()) + 1;
        int area = len * wid;
        if (area == n - 1)
        {
            area = min((len + 1) * wid, len * (wid + 1));
        }
        ans = min(ans, area);
    }
    cout << ans << '\n';
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
        test();
    return 0;
}