#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<bitset>
#include<queue>
#include<ctime>
#include<cmath>
#include<set>
#include<map>
#define infile(filename) freopen(filename".in","r",stdin)
#define outfile(filename) freopen(filename".out","w",stdout)
#define usefile(filename) infile(filename),outfile(filename)
using namespace std; typedef long long ll; typedef unsigned long long ull; typedef __int128 I;
namespace IO {
	const int BUF=1<<20; static char ch[BUF]={},out[BUF]={},*l=ch,*r=ch,*o=out;
#define FASTIO
#ifdef FASTIO
	inline char gc() { return (l==r&&(r=(l=ch)+fread(ch,1,BUF,stdin),l==r))?EOF:*l++; }
#else
	inline char gc() { return getchar(); }
#endif
	inline void flush() { fwrite(out,1,o-out,stdout),o=out; }
	inline void putc(char ch) { if(o==out+BUF) flush(); *o++=ch; }
	struct flusher{~flusher(){flush();}}_;
}; using IO::gc; using IO::putc;
template <typename T> void read(T &a) { static char fushu,ch; a=fushu=0; do ch=gc(); while(ch!='-'&&(ch<48||ch>57)); if(ch=='-') ch=gc(),fushu=1; do a=(a<<1)+(a<<3)+(ch^48),ch=gc(); while(ch>47&&ch<58); if(fushu) a=-a; }
template <typename T,typename ...Args> void read(T &a,Args &...args) { read(a),read(args...); }
template <typename T> void write(T a) { static char que[114]={},*p=que; if(!a) putc(48); if(a<0) putc('-'),a=-a; while(a) *p++=(a%10)^48,a/=10; while(p!=que) putc(*--p); putc(32); }
template <typename T,typename ...Args> void write(T a,Args ...args) { write(a),write(args...); }
const int N=500099;
int n,X,Y; char s[N]={},t[N]={};
string a,b,c,d;
vector<int> p,q;
int main()
{
	int i,j,k,l;
	scanf("%d%d%d%s%s",&n,&X,&Y,s,t);
	for(i=0;i<n;i=k+1) {
		j=i; while(j+1<n&&s[j+1]==s[i]) ++j; k=j,j=k-i+1;
		if(s[i]=='0') { while(j>=X) j-=X,a.push_back('A'); }
		else { while(j>=Y) j-=Y,a.push_back('B'); }
		while(j) a.push_back(s[i]),--j;
	}
	for(i=0;i<n;i=k+1) {
		j=i; while(j+1<n&&t[j+1]==t[i]) ++j; k=j,j=k-i+1;
		if(t[i]=='0') { while(j>=X) j-=X,b.push_back('A'); }
		else { while(j>=Y) j-=Y,b.push_back('B'); }
		while(j) b.push_back(t[i]),--j;
	}


	for(auto v:a) if(v=='0'||v=='1') c.push_back(v);
	for(auto v:b) if(v=='0'||v=='1') d.push_back(v);
	if(c!=d) return printf("No\n"),0;
	j=0; for(auto v:a) if(v=='A') ++j;
	k=0; for(auto v:b) if(v=='A') ++k;
	if(j!=k) return printf("No\n"),0;
	j=0; for(auto v:a) if(v=='B') ++j;
	k=0; for(auto v:b) if(v=='B') ++k;
	if(j!=k) return printf("No\n"),0;

	int lena=a.length(),lenb=b.length();

	p.clear(),q.clear();
	for(i=0;i<lena;++i) if(a[i]=='0') p.push_back(i);
	for(i=0;i<lenb;++i) if(b[i]=='0') q.push_back(i);
	if(!p.empty()) {
		for(i=1;i<p.size();++i) {
			for(j=0,l=p[i-1];l<p[i];++l) if(a[l]=='B') ++j;
			for(k=0,l=q[i-1];l<q[i];++l) if(b[l]=='B') ++k;
			if(j!=k) return printf("No\n"),0;
		}
		for(j=0,l=0;l<p[0];++l) if(a[l]=='B') ++j;
		for(k=0,l=0;l<q[0];++l) if(b[l]=='B') ++k;
		if(j!=k) return printf("No\n"),0;
	}

	p.clear(),q.clear();
	for(i=0;i<lena;++i) if(a[i]=='1') p.push_back(i);
	for(i=0;i<lenb;++i) if(b[i]=='1') q.push_back(i);
	if(!p.empty()) {
		for(i=1;i<p.size();++i) {
			for(j=0,l=p[i-1];l<p[i];++l) if(a[l]=='A') ++j;
			for(k=0,l=q[i-1];l<q[i];++l) if(b[l]=='A') ++k;
			if(j!=k) return printf("No\n"),0;
		}
		for(j=0,l=0;l<p[0];++l) if(a[l]=='A') ++j;
		for(k=0,l=0;l<q[0];++l) if(b[l]=='A') ++k;
		if(j!=k) return printf("No\n"),0;
	}
	

	printf("Yes\n");
	return 0;
}