import java.util.*;

public class Main{
    final static int M=998244353;
    static int[][][] dp;
    static int[] prefSum,prefSum2;

    public static int func(int n, int m, String[] str, int d){
        for(int i=0;i<m;i++){
            if(str[0].charAt(i)=='X'){
                dp[0][i][1]=1;
                dp[0][i][0]=1;
            }
        }

        for(int i=0;i<m;i++){
            int left=Math.max(i-d,0),right=Math.min(i+d,m-1);

            for(int j=left;j<=right;j++){
                if(str[0].charAt(i)=='X'&&i!=j) dp[0][i][0]=(dp[0][i][0]+dp[0][j][1])%M;
            }
        }

        for(int row=1;row<n;row++){
            prefSum[0]=dp[row-1][0][0];

            for(int col=1;col<m;col++) prefSum[col]=(prefSum[col-1]+dp[row-1][col][0])%M;

            for(int col=0;col<m;col++){
                if(str[row].charAt(col)=='#') continue;

                int left=Math.max(0,col-d+1),right=Math.min(col+d-1,m-1);

                for(int f=0;f<2;f++){
                    dp[row][col][f]=prefSum[right];
                    if(left>0) dp[row][col][f]-=prefSum[left-1];

                    dp[row][col][f]+=M;
                    dp[row][col][f]=dp[row][col][f]%M;
                }
            }


            prefSum2[0]=dp[row][0][1];

            for(int col=1;col<m;col++) prefSum2[col]=(prefSum2[col-1]+dp[row][col][1])%M;

            for(int col=0;col<m;col++){
                if(str[row].charAt(col)=='#') continue;

                int left=Math.max(0,col-d),right=Math.min(m-1,col+d);

                dp[row][col][0]+=prefSum2[right];
                if(left>0) dp[row][col][0]-=prefSum2[left-1];
                if(col>=left&&col<=right) dp[row][col][0]-=dp[row][col][1];

                dp[row][col][0]+=M;
                dp[row][col][0]=dp[row][col][0]%M;
            }
        }

        int ans=0;

        for(int col=0;col<m;col++) ans=(ans+dp[n-1][col][0])%M;

        return ans;
    }

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);

		int t=sc.nextInt();

		while(t-->0){
		    int n=sc.nextInt(),m=sc.nextInt(),d=sc.nextInt();
		    String[] str=new String[n];

		    for(int i=0;i<n;i++) str[i]=sc.next();

		    dp=new int[n+1][m+1][2];

		    prefSum=new int[m+1];
		    prefSum2=new int[m+1];

		    System.out.println(func(n,m,str,d));
		}
	}
}
