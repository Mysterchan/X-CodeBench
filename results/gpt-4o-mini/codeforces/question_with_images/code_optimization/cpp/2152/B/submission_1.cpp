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

        long long dx = abs(rK - rD);
        long long dy = abs(cK - cD);

        long long distance = max(dx, dy);

        // Check if Krug can infinitely hide, which happens when
        // Doran is diagonal or already adjacent to him in the same lane.
        if (distance <= 1) {
            cout << -1 << '\n';
        } else {
            cout << distance << '\n';
        }
    }
}