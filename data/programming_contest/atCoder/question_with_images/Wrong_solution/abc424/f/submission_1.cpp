#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
using LL = int64_t;
struct Seg{
    int mx;
    int acc;
};
Seg seg[12000005];
unordered_set<int> used;
void lazy_down(int now, int l, int r){
    if(l+1<r) {
        seg[2*now].acc=max(seg[now].acc, seg[2*now].acc);
        seg[2*now+1].acc=max(seg[now].acc, seg[2*now+1].acc);
    }
    seg[now].mx = max(seg[now].acc, seg[now].mx);
    seg[now].acc=0;
}
int query(int now, int l, int r, int x, int y) {
    if(x>=r || y<=l)
        return 0;
    else{
        if(seg[now].acc)
            lazy_down(now, l, r);
        if(l>=x&&r<=y){
            return seg[now].mx;
        }else{
            int mid = (l+r)/2;
            return max(query(2*now, l, mid, x,y),
                        query(2*now+1, mid, r, x, y));
        }
    }
}
void update(int now, int l, int r, int x, int y, int val) {
    if(l>=x&&r<=y){
        seg[now].acc = max(val, seg[now].acc);
        lazy_down(now, l, r);
    }else if(x>=r || y<=l){
        lazy_down(now, l, r);
        return;
    }else{
        if(seg[now].acc)
            lazy_down(now, l, r);
        int mid=(l+r)/2;
        update(2*now, l, mid, x, y, val);
        update(2*now+1, mid, r, x, y, val);
        seg[now].mx = max(seg[2*now].mx, seg[2*now+1].mx);
    }
}
int main(void) {
    int n,q;
    scanf("%d%d",&n,&q);
    for(int i=0;i<q;i++){
        int a,b;
        scanf("%d%d",&a,&b);
        a--;
        b--;
        if(used.find(a) != used.end() || used.find(b) != used.end()) continue;
        int c1 = query(1, 0, n, a, a+1);
        int c2 = query(1, 0, n, b, b+1);
        if(c1 != c2) {
            printf("No\n");
        }else{
            used.insert(a);
            used.insert(b);
            update(1, 0, n, a, b+1, q-i+1);
            printf("Yes\n");
        }
    }
    return 0;
}
