#include<bits/stdc++.h>
#define V 3000006
struct st{
    #define mid ((l+r)>>1)
    #define lch p*2
    #define rch p*2+1
    int val[V<<2];
    void build(int p,int l,int r){
        if(l==r){
            val[p]=1;
        }else{
            build(lch,l,mid);
            build(rch,mid+1,r);
            val[p]=r-l+1;
        }
    }
    void modify(int p,int l,int r,int x){
        if(l==r){
            val[p]=0;
        }else{
            if(x<=mid)modify(lch,l,mid,x);
            else modify(rch,mid+1,r,x);
            val[p]=val[lch]+val[rch];
        }
    }
    int query(int p,int l,int r,int x){
        if(l==r){
            return l;
        }else{
            if(val[lch]>=x)return query(lch,l,mid,x);
            else return query(rch,mid+1,r,x-val[lch]);
        }
    }
}T;
int q;
bool flag[V];
int main(){
    scanf("%d",&q);
    T.build(1,1,3000000);
    while(q--){
        int a,b;
        scanf("%d%d",&a,&b);
        if(a<V&&!flag[a]){
            for(int i=a;i<=3000000;i+=a){
                T.modify(1,1,3000000,i);
            }
            flag[a]=true;
        }
        printf("%d\n",T.query(1,1,3000000,b));
    }
}