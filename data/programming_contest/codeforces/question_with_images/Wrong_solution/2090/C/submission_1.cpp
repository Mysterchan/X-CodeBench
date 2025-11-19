#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define vll vector<ll>
#define vpll vector<pair<ll, ll>>
#define pb push_back
int main()
{
    ios::sync_with_stdio(false), cin.tie(nullptr);
    long long n1;
    cin >> n1;
    for (int z1 = 0; z1 < n1; z1++)
    {
        ll n;
        cin >> n;
        vll arr(n);
        for (ll i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        vector<pair<ll, ll>> x;
        vector<ll> y;
        ll ind = 0;
        for (ll ind2 = 0; ind2 < n; ind2++)
        {
            if (arr[ind2] == 0)
            {
                if (!x.empty())
                {
                    ll x1 = x.back().first;
                    ll y1 = y.back();
                    if (x1 < y1)
                    {
                        x.push_back({y1, 1});
                        y.push_back(x1);
                    }
                    else if (x1 > y1)
                    {
                        ll diff = x1 - y1;
                        if (diff == 1)
                        {
                            x.push_back({x1, 1});
                            y.push_back(x1);
                        }
                        else
                        {
                            x.push_back({y1 + 1, 1});
                            y.push_back(x1);
                        }
                    }
                    else
                    {
                        x.push_back({0, 1});
                        y.push_back(x1 + 1);
                    }
                }
                else
                {
                    x.push_back({0, 1});
                    y.push_back(0);
                }
            }
            else
            {
                if (!x.empty())
                {
                    ll move = 0;
                    ll intial = ind;
                    while (x[ind].second == 4 && ind < x.size())
                    {
                        ind++;
                    }
                    while (x[ind].second == 3 && ind < x.size())
                    {
                        if (move == 3)
                        {
                            break;
                        }
                        move++;
                        ind++;
                    }
                    if (move == 3)
                    {
                        ind = intial;
                    }
                    if (ind == x.size())
                    {
                        ll x1 = x.back().first;
                        ll y1 = y.back();
                        if (x1 < y1)
                        {
                            x.push_back({y1, 1});
                            y.push_back(x1);
                        }
                        else if (x1 > y1)
                        {
                            ll diff = x1 - y1;
                            if (diff == 1)
                            {
                                x.push_back({x1, 1});
                                y.push_back(x1);
                            }
                            else
                            {
                                x.push_back({y1 + 1, 1});
                                y.push_back(x1);
                            }
                        }
                        else
                        {
                            x.push_back({0, 1});
                            y.push_back(x1 + 1);
                        }
                    }
                    else
                    {
                        x[ind].second++;
                    }
                }
                else
                {
                    x.push_back({0, 1});
                    y.push_back(0);
                }
            }
            if (arr[ind2] == 0)
            {
                ll x1 = x.back().first;
                ll y1 = y.back();
                ll i = x.size() - 1;
                if (x[i].second == 1)
                {
                    cout << 3 * x1 + 1 << " " << 3 * y1 + 1 << endl;
                }
            }
            else
            {
                ll x1 = x[ind].first;
                ll y1 = y[ind];
                ll i = ind;
                if (x[i].second == 1)
                {
                    cout << 3 * x1 + 1 << " " << 3 * y1 + 1 << endl;
                }
                else if (x[i].second == 2)
                {
                    cout << 3 * x1 + 1 << " " << 3 * y1 + 2 << endl;
                }
                else if (x[i].second == 3)
                {
                    cout << 3 * x1 + 2 << " " << 3 * y1 + 1 << endl;
                }
                else
                {
                    cout << 3 * x1 + 2 << " " << 3 * y1 + 2 << endl;
                }
            }
        }
    }
    return 0;
}