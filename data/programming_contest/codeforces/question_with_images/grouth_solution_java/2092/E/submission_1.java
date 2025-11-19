import java.io.*;
import java.util.*;
public class Main {
	static Scanner cin=new Scanner(System.in);
	static PrintWriter cout=new PrintWriter(System.out);
	static final long P=1000000007L;
	static long ksm(long a,long p) {
		if(p<=0)return 1L;
		long ans=1L;
		while(p>1) {
			if(p%2==1) {
				p--;
				ans*=a;
				ans%=P;
			}
			else {
				p/=2;
				a*=a;
				a%=P;
			}
		}
		ans*=a;ans%=P;
		return ans;
	}
	public static void main(String[] args)throws IOException{
		long T,n,m,k,r,rr,B,W,i,x,y,cc,abc,ANS;
		T=cin.nextLong();
		while(T-->0) {
			n=cin.nextLong();m=cin.nextLong();k=cin.nextLong();
			r=(n-2L)*(m-2L)+4L;B=W=0L;
			rr=2L*n+2L*(m-2L)-4L;
			for(i=1;i<=k;i++) {
				x=cin.nextLong();y=cin.nextLong();cc=cin.nextLong();
				if(x>1&&x<n&&y>1&&y<m) {
					r--;
				}
				else if(x==1&&y==1||x==n&&y==1||x==1&&y==m||x==n&&y==m) {
					r--;
				}
				else {
					rr--;
					if(cc==0)B++;
					else W++;
				}
			}
			abc=ksm(2L,r);
			if(B%2==1&&W%2==1&&rr==0) {
				ANS=0L;
			}
			else ANS=ksm(2L,rr-1);
			ANS*=abc;ANS%=P;
			cout.println(ANS);
		}
		cout.flush();
	}
}
