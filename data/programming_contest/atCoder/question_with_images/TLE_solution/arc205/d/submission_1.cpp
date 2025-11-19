#include<bits/stdc++.h>
using namespace std;
typedef pair<int ,int > PII;
const int N = 5e5 + 10;
priority_queue<PII , vector<PII> >q;
int sizes[N];
int fa[N];
int depth[N];
int T;
void solve(){
	memset(sizes , 0 , sizeof sizes);
	int n , ans = 0;
	cin >> n;
	depth[1] = 1;
	for(int i = 2; i <= n ; i ++)
	{
		cin >> fa[i];
		sizes[fa[i]] ++;
		depth[i] = depth[fa[i]] + 1; 
	}
	for(int i = 1; i <= n ; i ++)
		if(!sizes[i])
		{
			q.push({depth[i] , i});
		}
			
	while(q.size() >= 2)
	{
		PII a = q.top() ;
		q.pop(); 
		PII b = q.top();
		q.pop();
		ans ++;
		int x = a.second , y = b.second;
		x = fa[x] , y = fa[y];
		sizes[x] --;
		if(!sizes[x])q.push({depth[x] , x});
		sizes[y] --;
		if(!sizes[y])q.push({depth[y] , y});
	}
	cout << ans << endl;
	while(!q.empty()) q.pop();
}
int main(){
	cin >> T;
	while(T --)
	{
		solve();
	} 
	
}