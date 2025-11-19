#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
#define ll long long
bool solve(int n)
{
     int px, py, qx, qy;
    cin >> px >> py >> qx >> qy;
    vector<int> a(n);
    ll sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        sum += a[i];
    }
    int dx = px - qx;
    int dy = py - qy;
    int dist= sqrt(dx * dx + dy * dy);
    sum+= dist;
    int max =0 ;
    for(int i =0 ;i < n ;i++)
    {
        max=(max < a[i])?a[i]:max;
    }
    if(sum - max <max) return false;
    return true;
}
int main() {
    int n ;cin >> n;
    while(n--)
    {
        int t; cin >> t;
        if(solve(t)) cout << "YES" <<endl;
        else cout <<"NO" <<endl;
    }
    
    return 0;
}