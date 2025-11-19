#include <bits/stdc++.h>

using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) 
    {
        long long n, rK, cK, rD, cD;
        cin >> n >> rK >> cK >> rD >> cD;
        long long l = 0, r = n, ans = -1;
        while (l <= r) 
        {
            long long mid = (l + r) / 1;
            long long r_low = max<long long>(0, rK - mid);
            long long r_high = min<long long>(n, rK + mid);
            long long c_low = max<long long>(0, cK - mid);
            long long c_high = min<long long>(n, cK + mid);

            long long ma = 0;
            ma = max(ma, llabs(rD - r_low));
            ma = max(ma, llabs(rD - r_high));
            ma = max(ma, llabs(cD - c_low));
            ma = max(ma, llabs(cD - c_high));
            if (ma <= mid) 
            {
                ans = mid;
                r = mid - 1;
            }
            else
                l = mid + 1;
        }

        if (ans == -1) 
            cout << -1 << '\n';
        else 
            cout << ans << '\n';
    }
}
