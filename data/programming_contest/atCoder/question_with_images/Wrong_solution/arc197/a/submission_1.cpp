#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	while(T--){
		int H,W;
		string s;
		int h=1,w=1;
		
		cin>>H>>W>>s;
		int Right[H+1]={0},Down[W+1]={0};
		Right[h]=w,Down[w]=h;
		for(int i=0;i<s.size();i++){
			if(s[i]=='D') h++;
			else if(s[i]=='R') w++;
			else {
				if(w<W) w++;
				else h++;
			}
			Right[h]=max(Right[h],w);
		}
		for(int i=2;i<=H;i++){
			if(Right[i]==0) Right[i]=Right[i-1];
		}
		
		h=1,w=1;
		
		for(int i=0;i<s.size();i++){
			if(s[i]=='D') h++;
			else if(s[i]=='R') w++;
			else {
				if(h<H) h++;
				else w++;
			}
			Down[w]=max(Down[w],h);
		}
		for(int i=2;i<=W;i++){
			if(Down[i]==0) Down[i]=Down[i-1];
		}
		int ans=0;
		for(int i=1;i<=H;i++){
			int left=1,right_w=W,w_min=W+1;
            while(left<=right_w){
                int mid=(left+right_w)/2;
                if(Down[mid]>=i){
                    w_min=mid;
                    right_w=mid-1;
                } else {
                    left=mid+1;
                }
            }
           
            if(w_min<=Right[i]){
                ans+=Right[i]-w_min+1;
            }
		}
		cout<<ans<<'\n';
	}
}