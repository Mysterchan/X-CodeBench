#include<bits/stdc++.h>
using namespace std;
const int M=1000+10;
const int Dir[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
int n,r,c;
string s,t;
vector<pair<int,int> > v;
bool f(){
	for(auto i:v){
		if(i.first==0&&i.second==0){
			return 0;	
		}
	}
	return 1;
}
int main(){
	ios::sync_with_stdio(false),cin.tie(0);
	cin>>n>>r>>c>>s;
	v.push_back({0,0});
	for(int i=1;i<=n;i++){
		int d=0;
		if(s[i-1]=='N') d=0;
		else if(s[i-1]=='W') d=1;
		else if(s[i-1]=='S') d=2;
		else d=3;
		for(auto &j:v){
			j.first+=Dir[d][0];
			j.second+=Dir[d][1];
		}
		if(f()) v.push_back({0,0});
		char ch='0';
		for(auto j:v){
			if(j.first==r&&j.second==c){
				ch='1';
				break;
			}
		}
		t+=ch;
	}
	cout<<t;
	return 0;
}