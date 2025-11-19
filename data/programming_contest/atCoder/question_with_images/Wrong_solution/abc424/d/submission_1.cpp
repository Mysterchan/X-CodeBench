#include <iostream>

using namespace std;

const int N = 10, INF = 0x3f3f3f3f;

int t, h, w, ans;
char a[N][N];

void DFS(int cx, int cy, int step) {
    if (cx == h - 1 && cy == w) {
        ans = min(ans, step);
        return;
    }
    if (cy == w) {
        DFS(cx + 1, 1, step);
        return;
    }
    if (a[cx][cy] == '.' || a[cx][cy + 1] == '.' || a[cx + 1][cy] == '.' || a[cx + 1][cy + 1] == '.') {
        DFS(cx, cy + 1, step);
    } else {
        a[cx + 1][cy] = '.';
        DFS(cx, cy + 1, step + 1);
        a[cx + 1][cy] = '#';
        a[cx][cy + 1] = '.';
        DFS(cx, cy + 1, step + 1);
        a[cx][cy + 1] = '#';
    }
}

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &h, &w);
        for (int i = 1; i <= h; ++i) {
            for (int j = 1; j <= w; ++j) {
                scanf(" %c", &a[i][j]);
            }
        }

        ans = INF;
        DFS(1, 1, 0);
        printf("%d\n", ans);
    }

    return 0;
}
