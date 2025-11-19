#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t)
    {
        --t;
        int h, w;
        string s;
        cin >> h >> w >> s;
        vector<pair<int, int>> a(h);
        int d = 0, r = 0;
        for(char c: s)
        {
            if(c == 'D')++d;
            else if(c == 'R')++r;
        }
        int i = 0, j = 0, k = 0;
        for(char c: s)
        {
            if(c == 'D')
            {
                ++i;
                a[i].first = j;
            }
            else if(c == 'R')
            {
                ++j;
            }
            else if(c == '?')
            {
                if(d + k < h - 1)
                {
                    ++k;
                    ++i;
                    a[i].first = j;
                }
                else
                {
                    ++j;
                }
            }
        }
        i = 0, j = 0, k = 0;
        for(char c: s)
        {
            if(c == 'D')
            {
                a[i].second = j + 1;
                ++i;
            }
            else if(c == 'R')
            {
                ++j;
            }
            else if(c == '?')
            {
                if(r + k < w - 1)
                {
                    ++k;
                    ++j;
                }
                else
                {
                    a[i].second = j + 1;
                    ++i;
                }
            }
        }
        a[i].second = j + 1;
        long long ans = 0;
        for(auto[l, r]: a)
        {
            ans += r - l;
        }
        cout << ans << "\n";
    }
    return 0;
}