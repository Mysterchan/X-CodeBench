#include<bits/stdc++.h>
#define LL long long
using namespace std;

const int N = 200009;

const LL inf = 1e18;

struct mat
{
    LL a[9][9];
    mat()
    {
        for (int i = 0;i < 9;++ i)
            for (int j = 0;j < 9;++ j)
                a[i][j] = -inf;
    }
    friend mat operator * (const mat& a, const mat& b)
    {
        mat c;
        for (int i = 0;i < 5;++ i)
            for (int k = 0;k < 5;++ k)
                for (int j = 0;j < 5;++ j)
                        c.a[i][j] = max(c.a[i][j], a.a[i][k] + b.a[k][j]);
        return c;
    }
};

struct node
{
    int l, r;
    mat m;
}tr[N << 2];

#define ls (p << 1)
#define rs ((p << 1) | 1)

LL a[N];

int n, m;

mat get(LL v)
{
    mat res;
    res.a[0][2] = -v;
    res.a[0][3] = -v;
    res.a[0][4] = -v;
    res.a[1][0] = -v;
    res.a[1][1] = -v;
    res.a[2][1] = v;
    if (v & 1)
    {
        res.a[2][4] = -1;
        res.a[4][1] = res.a[4][3] = 1;
    }
    else
    {
        res.a[3][1] = res.a[3][3] = 0;
        res.a[4][4] = 0;
    }
    return res;
}

mat Vec()
{
    mat m;
    m.a[1][0] = 0;
    return m;
}

void bd(int l, int r, int p = 1)
{
    int mid = (l + r) >> 1;
    tr[p] = {l, r, get(a[l])};
    if (l ^ r)
    {
        bd(l, mid, ls), bd(mid + 1, r, rs);
        tr[p].m = tr[rs].m * tr[ls].m;
    }
}

LL s[N];

mat ask(int sl, int sr, int p = 1)
{
    int l = tr[p].l, r = tr[p].r, mid = (l + r) >> 1;
    if (l >= sl && r <= sr)
        return tr[p].m;
    if (sl <= mid && sr > mid)
        return ask(sl, sr, rs) * ask(sl, sr, ls);
    else if (sl <= mid)
        return ask(sl, sr, ls);
    else
        return ask(sl, sr, rs);
}

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1;i <= n;++ i)
        scanf("%lld", &a[i]), s[i] = s[i - 1] + a[i];
    bd(1, n);
    for (int l, r;m --;)
    {
        scanf("%d%d", &l, &r);
        mat v = ask(l, r) * Vec();
        LL ans = 0;
        for (int i = 0;i < 5;++ i)
            ans = max(ans, v.a[i][0]);
        ans = (s[r] - s[l - 1] - ans) / 2;
        printf("%lld\n", ans);
    }

    return 0;
}