#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define cd complex<double>

const double pi=acos(-1);
const int mxN=8e6;

int r[mxN];

void fft(vector<cd> &c, int n, int op) {
	for(int i=0; i<n; i++) {
		r[i]=r[i/2]/2+(i&1?n/2:0);
	}
	for(int i=0; i<n; i++) {
		if(i<r[i]) swap(c[i], c[r[i]]);
	}
	for(int len=2; len<=n; len*=2) {
		cd w1={cos(2*pi/len), sin(2*pi/len)*op};
		for(int i=0; i<n; i+=len) {
			cd wk={1, 0};
			for(int j=i; j<i+len/2; j++) {
				cd x=c[j], y=c[j+len/2];
				c[j]=x+y*wk;
				c[j+len/2]=x-y*wk;
				wk=wk*w1;
			}
		}
	}
		
	if(op==-1) {
		for(int i=0; i<n; i++) {
			c[i]/=n;	
		}
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int n; cin>>n;
	vector<int> x(n);
	vector<cd> a(mxN);
	int mx=0;
	for(int i=0; i<n; i++) {
		cin>>x[i];
		x[i]--;
		mx=max(mx, x[i]);
		a[x[i]]+=1;	
	}
	vector<cd> b=a;
	int len=1;
	while(len<2*mx) len*=2;
	vector<int> c(len);
	fft(a, len, 1);
	fft(b, len, 1);
	for(int i=0; i<len; i++) {
		a[i]=a[i]*b[i];
	}
	fft(a, len, -1);
	ll ans=0;
	for(int i=0; i<n; i++) {
		ans+=(ll)((a[2*x[i]].real()+0.5))/2;
	}
	cout<<ans<<"\n";
	return 0;
} 
