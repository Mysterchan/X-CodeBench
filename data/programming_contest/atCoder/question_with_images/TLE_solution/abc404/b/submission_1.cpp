#include <bits/stdc++.h>
using namespace std;
void opt2();
int bijiao(char w[][110],char v[][110]);

int n;
char s[110][110];
char t[110][110];
char r[110][110];
int mmin=1e6;

int bijiao(char w[][110],char v[][110]) {
	int cnt=0;
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=n; j++) {
			if(w[i][j]==v[i][j]) {
				cnt++;
			}
		}
	}
	return cnt;
}

void bfs(int k) {
	if(bijiao(s,t)==n*n) {
		if(k<mmin) {
			mmin=k;
		}
		return ;
	}
	opt2();
	if(bijiao(r,t)>=bijiao(s,t)+1) {
		for(int i=1; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				s[i][j]=r[i][j];
			}
		}
		bfs(k+1);
	} else {
		for(int i=1; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				if(s[i][j]!=t[i][j]) {
					char ch=s[i][j];
					s[i][j]=t[i][j];
					bfs(k+1);
					s[i][j]=ch;
				}
			}
		}
	}
	return ;
}

void opt2() {
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=n; j++) {
			r[j][1+n-i]=s[i][j];
		}
	}
}

int main() {
	cin>>n;
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=n; j++)
			cin>>s[i][j];
	}
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=n; j++)
			cin>>t[i][j];
	}
	bfs(0);
	cout<<mmin<<endl;
	return 0;
}