#include <iostream>
#include <set>

using namespace std;

int n, m, q;
int tmp;
int u[300005];
int v[300005];
set<int> edges[300005];
int parent[300005];

int Find(int x) {
    if (parent[x] != x)
    {
        parent[x] = Find(parent[x]);
    }
    return parent[x];
}

void merge_node(int x, int y) {
    x = Find(x);
    y = Find(y);
    if (x == y)
    {
        return;
    }
    if (edges[x].find(y) == edges[x].end())
    {
        return;
    }
    edges[x].erase(y);
    edges[y].erase(x);
    m--;
    if (edges[x].size() < edges[y].size())
    {
        swap(x, y);
    }
    parent[y] = x;
    for (auto i : edges[y])
    {
        if (edges[x].find(i) == edges[x].end())
        {
            edges[x].insert(i);
            edges[i].insert(x);
        }
        else
        {
            m--;
        }
        edges[i].erase(y);
    }
    edges[y].clear();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> u[i] >> v[i];
        edges[u[i]].insert(v[i]);
        edges[v[i]].insert(u[i]);
    }
    for (int i = 1; i <= n; i++)
    {
        parent[i] = i;
    }
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> tmp;
        tmp--;
        merge_node(u[tmp], v[tmp]);
        cout << m << "\n";
    }
    return 0;
}
