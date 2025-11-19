import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
		    int n = sc.nextInt();
		    int m = sc.nextInt();
		    int fib[] = new int[12] ;
		    fib[1] = 1 ; fib[2] = 2 ;
		    for(int i=3;i<=11;i++){
		        fib[i] = fib[i-1] + fib[i-2] ;
		    }
		    for(int i=0;i<m;i++){
		        long dim[] = new long[3] ;
		        for(int j=0;j<3;j++){
		            dim[j] = sc.nextLong();
		        }
		        Arrays.sort(dim);
		        System.out.print((dim[0]>=fib[n] && dim[2]>=fib[n]+fib[n-1])? "1":"0");

		    }
		    System.out.println();
		}
	}
}
