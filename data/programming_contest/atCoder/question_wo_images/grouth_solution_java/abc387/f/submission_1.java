import java.util.*;

public class Main {
	public static long MOD = 998244353;
	public static Pair[] p;
	public static int label = 1;
	public static ArrayList<Integer> roop = new ArrayList<>();
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();

		int[] bigger = new int[n + 1];
		ArrayList<ArrayList<Integer>> rev = new ArrayList<>();
		for(int i = 0;i <= n;i++) {
			rev.add(new ArrayList<>());
		}
		int[] in = new int[n + 1];
		p = new Pair[n + 1];
		for(int i = 1;i <= n;i++) {
			int a = sc.nextInt();
			bigger[i] = a;
			rev.get(a).add(i);
		}for(int i = 0;i <= n;i++) {
			p[i] = new Pair(0,i);
		}boolean[] vis = new boolean[n + 1];
		for(int i = 1;i <= n;i++) {
			if(p[i].x == 0 )dfs(i,bigger,vis);

		}
		Arrays.sort(p);
		UnionFind uf = new UnionFind(n);
		vis = new boolean[n + 1];
		for(int i = 0;i < n;i++) {

			if(!vis[p[i].y]) {
				roop = new ArrayList<>();
				dfs2(p[i].y,vis,rev);

				for(int s:roop) {
					uf.unite(p[i].y,s);
				}
			}
		}
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();
		for(int i = 0;i <= n;i++) {
			list.add(new ArrayList<>());
		}
		for(int i = 1;i <= n;i++){
			int a = uf.getRoot(bigger[i]);
			int b = uf.getRoot(i);
			if(i == b && a != b) {

				list.get(b).add(a);
				in[a]++;
			}
		}vis = new boolean[n + 1];
		boolean[] goal = new boolean[n + 1];
		long[][] pat = new long[n + 1][m];
		for(int i = 1;i <= n;i++) {
			for(int j = 0;j < m;j++) {
				pat[i][j] = 1;
			}
		}
		ArrayDeque<Integer> q = new ArrayDeque<>();
		for(int i = 1;i <= n;i++) {
			int a = uf.getRoot(i);

			if(list.get(a).size() == 0) {
				goal[i] = true;
			}
			if(i == a && in[a] == 0) {
				q.add(a);
			}
		}long ans = 1;

		while(!q.isEmpty()) {
			int p = q.poll();

			if(goal[p]) {
				long sum = 0;
				for(int i = m - 1;i >= 0;i--) {
					sum += pat[p][i];

				}sum %= MOD;
				ans = (ans * sum) % MOD;
			}
			for(int s:list.get(p)) {
				long sum = 0;
				for(int i = m - 1;i >= 0;i--) {
					sum += pat[p][i];
					sum %= MOD;
					pat[s][i] = (pat[s][i] * sum) % MOD;
				}in[s]--;
				if(in[s] == 0) {
					q.add(s);
				}
			}
		}System.out.print(ans % MOD);
	}public static void dfs(int ind,int[] bigger,boolean[] vis) {
		if(vis[ind])return;
		vis[ind] = true;
		dfs(bigger[ind],bigger,vis);
		p[ind].x = label;
		label++;
	}public static void dfs2(int ind,boolean[] vis,ArrayList<ArrayList<Integer>> rev) {
		if(vis[ind])return;
		vis[ind] = true;
		roop.add(ind);
		for(int s:rev.get(ind)) {
			dfs2(s,vis,rev);
		}
	}
	public static class UnionFind{
		  public int[] root;
		  public int[] size;
		  public UnionFind(int n) {
			  this.root = new int[n + 1];
			  this.size = new int[n + 1];
			  for(int i = 1;i < n + 1;i++) {
				  this.root[i] = i;
			  }
		  }
		  public void unite(int x,int y) {
			  x = getRoot(x);
			  y = getRoot(y);
			  this.root[y] = this.root[x];
		  }

		  public void rootPlus(int x,int y) {
			  this.root[x] = y;
			  this.size[y]++;
		  }

		  public int getRoot(int x) {
			  if(x == this.root[x]) {
				  return x;
			  }else
			  return this.root[x] = getRoot(this.root[x]);
		  }
		  public boolean same(int x,int y) {
			  x = getRoot(x);
			  y = getRoot(y);
			  return x == y;
		  }
	}public static class Pair implements Comparable<Pair> {
		int x;
		int y;
		public Pair(int a,int b) {
			x = a;
			y = b;
		}public int compareTo(Pair p) {
			if(this.x > p.x) {
				return -1;
			}if(this.x < p.x) {
				return 1;
			}if(this.y < p.y) {
				return -1;
			}if(this.y > p.y) {
				return 1;
			}return 0;
		}public boolean equals(Object o) {
			Pair p = (Pair)o;
			return p.x == this.x && p.y == this.y;
		}public int hashCode() {
			return x * 17 + y * 127;
		}
	}

}