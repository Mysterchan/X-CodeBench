#include <bits/stdc++.h>
using namespace std;

const int N = 200005;

int n;
int a[N];
set<int> s;
int q000, q1;

int F(int l, int r)
{
    l += 2;
    r -= 1;
    if (l > r)
        return 0;
    if (l == 1 && r == n)
    {
        if (q1 == n)
            return 0;
        return 2 - (r - l + 1);
    }
    return 1 - (r - l + 1);
}

int calc_ans()
{
    int ans = n - q000;
    auto it = s.begin();
    while (it != s.end())
    {
        auto jt = next(it);
        if (jt != s.end())
            ans += F(*it, *jt);
        ++it;
    }
    return ans;
}

void update_set(int i)
{
    if (a[i] + a[i + 1] == 0)
        s.insert(i);
    else
        s.erase(i);
}

void update_q000(int i)
{
    if (i >= 1 && i + 2 <= n)
    {
        if (a[i] + a[i + 1] + a[i + 2] == 0)
            ++q000;
        else
            --q000;
    }
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(0);
    
    cin >> n;
    for (int i = 1; i <= n; ++i)
    {
        cin >> a[i];
        q1 += a[i];
    }
    
    a[n + 1] = a[n + 2] = 0;
    s.insert(-1);
    
    for (int i = 0; i <= n + 1; ++i)
    {
        if (a[i] + a[i + 1] == 0)
            s.insert(i);
    }
    
    q000 = 0;
    for (int i = 1; i + 2 <= n; ++i)
    {
        if (a[i] + a[i + 1] + a[i + 2] == 0)
            ++q000;
    }
    
    int qq;
    cin >> qq;
    while (qq--)
    {
        int i;
        cin >> i;
        
        // Remove old contributions
        for (int j = max(1, i - 2); j <= min(n - 2, i); ++j)
            update_q000(j);
        
        for (int j = i - 1; j <= i; ++j)
            if (j >= 0 && j <= n + 1)
                update_set(j);
        
        // Toggle
        a[i] ^= 1;
        q1 += (a[i] ? 1 : -1);
        
        // Add new contributions
        for (int j = i - 1; j <= i; ++j)
            if (j >= 0 && j <= n + 1)
                update_set(j);
        
        for (int j = max(1, i - 2); j <= min(n - 2, i); ++j)
            update_q000(j);
        
        cout << calc_ans() << "\n";
    }
    
    return 0;
}