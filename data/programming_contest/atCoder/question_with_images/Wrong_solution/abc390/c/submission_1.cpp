#include <bits/stdc++.h>
using namespace std;

int h, w;
int s[1005][1005];

int main()
{
    cin >> h >> w;
    int x1 = h, x2 = 0, y1 = w, y2 = 0;
    for(int i = 1; i <= h; i++)
    {
        for(int j = 1; j <= w; j++)
        {
            cin >> s[i][j];
            if(s[i][j] == '#')
            {
                x1 = min(x1, i);
                x2 = max(x2, i);
                y1 = min(y1, j);
                y2 = max(y2, j);
            }
        }
    }
    for(int i = x1; i <= x2; i++)
    {
        for(int j = y1; j <= y2; j++)
        {
            if(s[i][j] == '.')
            {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}
