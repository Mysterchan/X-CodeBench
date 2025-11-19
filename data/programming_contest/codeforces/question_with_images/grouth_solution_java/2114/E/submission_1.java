
import java.util.*;

public class Main {

	public static int n;
	public static long a[],mx[],mi[];
	public static ArrayList<Integer>sk[];
	public static void dfs(int fa,int cur) {
		mi[cur]=Math.min(mi[cur],mi[cur]-mx[fa]);
		mx[cur]=Math.max(mx[cur],mx[cur]-mi[fa]);
		for(int x:sk[cur]) {
			if(x==fa) continue;
			dfs(cur,x);
		}
	}
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int t=s.nextInt();
		while(t-->0) {
			n=s.nextInt();
			a=new long [n+10];mx=new long [n+10];mi=new long [n+10];
			for(int i=1;i<=n;i++) {
				a[i]=mx[i]=mi[i]=s.nextLong();
			}
			sk=new ArrayList [n+10];
			for(int i=1;i<=n;i++) sk[i]=new ArrayList<>();
			for(int i=1;i<n;i++) {
				int u=s.nextInt(),v=s.nextInt();
				sk[u].add(v);
				sk[v].add(u);
			}
			dfs(0,1);
			for(int i=1;i<=n;i++) System.out.print(mx[i]+" ");
			System.out.println("");
		}
	}

}
