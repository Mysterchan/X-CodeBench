#include<bits/stdc++.h>
using namespace std;

#define ll long long

vector<int> va,vb;
int da[1000100],db[1000100],dact,dbct;
int tda[1000100],tdb[1000100];

int main(){ 
	int tc; scanf("%d",&tc);
	while(tc--){
		va.clear(); vb.clear();
		memset(da,0,sizeof da);
		memset(db,0,sizeof db);
		memset(tda,0,sizeof tda);
		memset(tdb,0,sizeof tdb);
		dact=0,dbct=0;
		int n; scanf("%d",&n);
		for (int i=1;i<=n;i++){
			char c; scanf(" %c",&c);
			if (c=='1'){
				va.push_back(i);
				if (va.size()>1) tda[++dact]=i-va[va.size()-2];
			}
		}
		for (int i=1;i<=n;i++){
			char c; scanf(" %c",&c);
			if (c=='1'){
				vb.push_back(i);
				if (vb.size()>1) tdb[++dbct]=i-vb[vb.size()-2];
			}
		}
		int ans=0x3f3f3f3f;
		bool fdans=false;
		for (int type=0;type<=1;type++){
			memcpy(da,tda,sizeof tda);
			memcpy(db,tdb,sizeof tdb);
			int tans=0;
			int ct=1;
			int nsum=0;
			int pc=0;
			bool aldn=true;
			if (type==1){
				da[1]--; tans++;
			}
			for (int i=1;i<=dbct;i++){
				int e=db[i];
				bool dne=false;
				if (ct>dact) aldn=false;
				while (true){
					if (ct>dact){
						aldn=false;
						break;
					}
					if (da[ct]>e){
						int nw=da[ct]-e;
						tans+=nsum/2;
						if (nsum%2==1){
							tans++;
							nw--;
						}
						nsum=0;
						tans+=nw/2;
						if (nw%2==1){
							tans++;
							da[ct+1]--;
						}
						ct++; dne=true; pc++;
						break;
					}else if (da[ct]==e&&nsum%2==0){
						tans+=nsum/2;
						nsum=0;
						ct++; dne=true; pc++;
						break;
					}
					nsum+=da[ct];
					ct++;
				}
				if (!aldn){
					break;
				}
				if (!dne){
					aldn=false;
					break;
				}
			}
			if (!aldn){
				continue;
			}
			fdans=true;
			int cttt=0;
			nsum=0;
			for (int i=ct;i<=dact;i++) nsum+=da[i];
			tans+=(nsum+1)/2;
			int sc=0;
			if ((nsum%2==1)||(da[dact+1]==-1)) sc++;
			if (type==1) sc--;
			tans+=abs((va[va.size()-1]+va[0]+sc)/2-(vb[vb.size()-1]+vb[0])/2);
			ans=min(ans,tans);
		}
		if (!fdans) printf("-1\n");
		else printf("%d\n",ans);
	}
}
