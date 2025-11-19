#include<bits/stdc++.h>
using namespace std;
#define For(i, l, r) for(int i = (l); i <= (r); ++i)
#define Rfor(i, r, l) for(int i = (r); i >= (l); --i)
#define O(x) cerr<<(#x)<<":"<<(x)<<endl
#define OO(x,y) cerr<<(#x)<<":"<<(x)<<" "<<(#y)<<":"<<y<<endl
#define OOO(x,y,z) cerr<<(#x)<<":"<<(x)<<" "<<(#y)<<":"<<y<<" "<<(#z)<<":"<<(z)<<endl
#define OOOO(x,y,z,w) cerr<<(#x)<<":"<<(x)<<" "<<(#y)<<":"<<y<<" "<<(#z)<<":"<<(z)<<" "<<(#w)<<":"<<(w)<<endl
#define OOOOO(x,y,z,w,q) cerr<<(#x)<<":"<<(x)<<" "<<(#y)<<":"<<y<<" "<<(#z)<<":"<<(z)<<" "<<(#w)<<":"<<(w)<<" "<<(#q)<<":"<<(q)<<endl
#define LO(a, l, r) {cerr<<(#a)<<":";For(supervarious, l, r)cerr<<" "<<(a[supervarious]);cerr<<endl;}
int read32(){int x=0,t=1;char ch;while(!isdigit(ch=getchar()))if(ch=='-')t=-t;while(x=(x<<1)+(x<<3)+(ch^48),isdigit(ch=getchar()));return x*t;}
long long read64(){long long x=0,t=1;char ch;while(!isdigit(ch=getchar()))if(ch=='-')t=-t;while(x=(x<<1)+(x<<3)+(ch^48),isdigit(ch=getchar()));return x*t;}
char getdig(){char ch = getchar(); while(ch == ' ' || ch == 10) ch = getchar(); return ch;}
int main()
{
	int T = read32();
	while(T--)
	{
		int X = read32(), Y = read32(), Z = read32();
		if(Z == 0)
		{
			if(X > 0 && (Y + 1) & 1) printf("Yes\n");
			else printf("No\n");
			continue;
		}
		if (X >= ((Y + 1) >> 1) && X >= Z) printf("Yes\n");
		else printf("No\n");
	}
}