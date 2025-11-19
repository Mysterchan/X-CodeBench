#include <bits/stdc++.h>
using namespace std;
const int MAXV = 3000000;
const int B = 2000;
const int BLK = (MAXV + B - 1) / B;
static unsigned char alive[MAXV+1];
static unsigned char removed_flag[MAXV+1];
static int block_cnt[BLK];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int Q;
    if(!(cin>>Q))return 0;
    // initialize alive and block counts
    for(int i=1;i<=MAXV;i++){
        alive[i] = 1;
        int id = (i-1)/B;
        block_cnt[id]++;
    }
    int Ai, Bi;
    while(Q--){
        cin>>Ai>>Bi;
        if(Ai <= MAXV && !removed_flag[Ai]){
            removed_flag[Ai] = 1;
            for(int j = Ai; j <= MAXV; j += Ai){
                if(alive[j]){
                    alive[j] = 0;
                    int id = (j-1)/B;
                    block_cnt[id]--;
                }
            }
        }
        int k = Bi;
        int answer = -1;
        for(int id = 0; id < BLK; id++){
            if(block_cnt[id] < k){
                k -= block_cnt[id];
            } else {
                int start = id * B + 1;
                int end = start + B - 1;
                if(end > MAXV) end = MAXV;
                for(int j = start; j <= end; j++){
                    if(alive[j]){
                        k--;
                        if(k == 0){
                            answer = j;
                            break;
                        }
                    }
                }
                if(answer != -1) break;
            }
        }
        // it's guaranteed answer exists
        cout<<answer<<"\n";
    }
    return 0;
}