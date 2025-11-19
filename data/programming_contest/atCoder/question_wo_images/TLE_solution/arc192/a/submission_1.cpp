#include<bits/stdc++.h>
using namespace std;
int n,a[1000001],bz[1000001],l=1,sum,ture;char s[1000001];
int main()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&a[i]);if(a[i])sum++;
		if(a[i]&&!ture)
		{
			for(int j=1;i+j<=n;j+=2)if(a[i]&&a[i+j])ture=1;
		}
	}
	for(int i=1;i<=n;i++)
	{
		if(a[i])
		{
			for(int j=1;i+j<=n;j+=2)if(a[i]&&a[i+j])ture=1;
		}if(ture)break;
	}
	if(n%4==0||((n%4==1||n%4==3)&&sum>0)||(n%4==2&&ture))printf("Yes");
	else printf("No");
	return 0;
}