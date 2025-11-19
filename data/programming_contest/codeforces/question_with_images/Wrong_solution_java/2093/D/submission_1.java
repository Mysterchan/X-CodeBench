import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		int ar[][]={{1,4},{3,2}};
		int a[][]={{1,1},{2,2},{2,1},{1,2}};
		while(t-->0){
		    int n=sc.nextInt();
		    int q=sc.nextInt();
		    while(q-->0){
		        String s=sc.next();
		        if(s.equals("->")){
        		    int x=sc.nextInt();
        		    int y=sc.nextInt();
        		    long  sol=1;
        		    long k=1<<n;
        		    while(k>2){
        		        int x1=(int)(((x-1)*2)/k);
        		        int y1=(int)(((y-1)*2)/k);
        		        sol+=(ar[x1][y1]-1)*k;
        		        x/=(x1+1);
        		        y/=(y1+1);
        		        k/=2;
        		    }
        		    sol+=(ar[x-1][y-1]-1);
        		  System.out.println(sol);
		        }else{
		            long d=sc.nextLong();
		            int x=1,y=1;
		            long k=1<<n;
		            while(d>4){
		                long dd=(k*k)/4;
		                int i=(int)((d-1)/dd);
		                x+=(k/2)*(a[i][0]-1);
		                y+=(k/2)*(a[i][1]-1);
		                d=d%dd;
		                if(d==0) d=dd;
		                k/=2;
		            }
		            x+=(a[(int)d-1][0]-1);
                    y+=(a[(int)d-1][1]-1);
		            System.out.println(x+" "+y);
		        }
		   }
		}
	}
}
