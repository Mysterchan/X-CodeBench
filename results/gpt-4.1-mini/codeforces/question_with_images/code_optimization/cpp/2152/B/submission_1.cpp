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

        // Calculate Chebyshev distance (Doran's moves)
        long long distD = max(abs(rD - rK), abs(cD - cK));
        // Calculate Manhattan distance (Krug's moves)
        long long distK = abs(rD - rK) + abs(cD - cK);

        // If Doran is fast enough to catch Krug eventually
        if (distD * 2 >= distK) 
            cout << distD << '\n';
        else 
            cout << -1 << '\n';
    }
}