#include<bits/stdc++.h>
using namespace std;
bool matching(char t[],int n)
{
	int i=0;
	bool mat=true;
	stack<char>s;
	while(i<n&&mat)
	{
		switch (t[i])
		{
			case'(':
			case'[':
			case'<':s.push(t[i]);i++;break;
			case')':
				if(!s.empty()&&s.top()=='(')
				{
					s.pop();
					i++;
				}else mat=false;
			break;
			case']':
				if(!s.empty()&&s.top()=='[')
				{
					s.pop();
					i++;
				}else mat=false;
			break;
			case'>':
				if(!s.empty()&&s.top()=='<')
				{
					s.pop();
					i++;
				}else mat=false;
			break;
		}
	}
	if(mat&&s.empty())return true;
	else return false;
}
int main()
{
	stack<int>s;
	int n,i;
	char t[1000];
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>t[i];
	if(matching(t,n))cout<<"Yes";
	else cout<<"No"; 
	return 0;
}