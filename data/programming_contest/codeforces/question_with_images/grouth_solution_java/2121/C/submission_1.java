import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-- > 0) {

			int n=sc.nextInt();
			int m=sc.nextInt();
			int[][] a=new int[n][m];
			int[] rowMax=new int[n];
			int[] colMax=new int[m];
			int globMax=0;
			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++) {
					a[i][j]=sc.nextInt();
					globMax=Math.max(globMax,a[i][j]);}
			int count=0;
			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++)
					if(a[i][j]==globMax) {
						rowMax[i]++;
						colMax[j]++;
						count++;
					}
			boolean yes=false;
			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++) {
					int c=rowMax[i]+colMax[j];
					if(a[i][j]==globMax)
						c--;
					if(c==count) {
						yes=true;
						break;
					}
				}
			if(yes)
				System.out.println(globMax-1);
			else
				System.out.println(globMax);

		}
		sc.close();

	}

}
