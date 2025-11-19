import java.util.*;

public class Main{
    final static int M=998244353;
    static int[][] prev,cur;
    static int[] prefSum,prefSum2;

    public static int func(int n, int m, String[] str, int d){
        for(int i=0;i<m;i++){
            if(str[0].charAt(i)=='X'){
                prev[i][1]=1;
                prev[i][0]=1;
            }
        }

        for(int i=0;i<m;i++){
            int left=Math.max(i-d,0),right=Math.min(i+d,m-1);

            for(int j=left;j<=right;j++){
                if(str[0].charAt(i)=='X'&&i!=j) prev[i][0]=(prev[i][0]+prev[j][1])%M;
            }
        }

        for(int row=1;row<n;row++){
            prefSum[0]=prev[0][0];

            for(int col=1;col<m;col++) prefSum[col]=(prefSum[col-1]+prev[col][0])%M;

            for(int col=0;col<m;col++){
                if(str[row].charAt(col)=='#') continue;

                int left=Math.max(0,col-d+1),right=Math.min(col+d-1,m-1);

                for(int f=0;f<2;f++){
                    cur[col][f]=prefSum[right];
                    if(left>0) cur[col][f]-=prefSum[left-1];

                    cur[col][f]+=M;
                    cur[col][f]=cur[col][f]%M;
                }
            }


            prefSum2[0]=cur[0][1];

            for(int col=1;col<m;col++) prefSum2[col]=(prefSum2[col-1]+cur[col][1])%M;

            for(int col=0;col<m;col++){
                if(str[row].charAt(col)=='#') continue;

                int left=Math.max(0,col-d),right=Math.min(m-1,col+d);

                cur[col][0]+=prefSum2[right];
                if(left>0) cur[col][0]-=prefSum2[left-1];
                if(col>=left&&col<=right) cur[col][0]-=cur[col][1];

                cur[col][0]+=M;
                cur[col][0]=cur[col][0]%M;
            }

            int[][] temp=prev;
            prev=cur;
            cur=temp;
        }

        int ans=0;

        for(int col=0;col<m;col++) ans=(ans+prev[col][0])%M;

        return ans;
    }

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);

		int t=sc.nextInt();

		while(t-->0){
		    int n=sc.nextInt(),m=sc.nextInt(),d=sc.nextInt();
		    String[] str=new String[n];

		    for(int i=0;i<n;i++) str[i]=sc.next();

		    prev=new int[m+1][2];
		    cur=new int[m+1][2];

		    prefSum=new int[m+1];
		    prefSum2=new int[m+1];

		    System.out.println(func(n,m,str,d));
		}
	}
}
