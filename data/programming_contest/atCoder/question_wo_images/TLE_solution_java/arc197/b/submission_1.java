import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
	static kattio sc = new kattio();
	static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

	static long[] jc, fm;
	static boolean p;

	public static void main(String[] args) {

		int t = sc.nextint();

		while (t-- > 0) {

			sovle2();
		}

		out.close();

	}

	static long[] jsum, osum;
	static int[] ls, arr;
	static TreeSet<Integer> treeSet;

	static long gcd(long a, long b) {
		return b == 0 ? a : gcd(b, a % b);
	}
	static int k,n;
	static void sovle2() {
		n=sc.nextint();
		int []arr=new int[n];
		for (int i = 0; i < arr.length; i++) {
			arr[i]=sc.nextint();
		}
		Arrays.sort(arr);
		int ans=0;
		for (int i = 1; i < arr.length; i++) {
			int l=i;int r=n-1;int mid=0;
			while (l<r) {
				mid=(l+r+1)/2;
				if (pan(mid, arr,i)) {
					l=mid;
				}else {
					r=mid-1;
				}

			}

			ans=Math.max(ans, r-i+1);
		}

		if (arr[0]==arr[n-1]) {
			out.println(0);
		}else {
			out.println(ans);
		}

	}
	static boolean pan(int x,int []arr,int id) {

		long sum=0;long ge=0;
		for (int i = id; i <=x; i++) {
			sum+=arr[i];ge++;
		}
		for (int i = 0; i < id; i++) {
			sum+=arr[i];ge++;
			if (ge*arr[id]>sum) {

				return true;
			}
		}
		return false;
	}
	static int[] f, h,si;

	static void init(int x) {
		f = new int[x + 1];
		h = new int[x + 1];
		si = new int[x + 1];
		for (int i = 0; i < x+1; i++) {
			f[i] = i;
			h[i] = 1;si[i]=1;
		}
	}

	static int find(int x) {
		return f[x] == x ? x : (f[x] = find(f[x]));
	}

	static void marge(int u, int v) {
		int x = find(u);
		int y = find(v);
		if (h[x] > h[y]) {
			f[y] = x;si[x]+=si[y];
		} else if (h[x] < h[y]) {
			f[x] = y;si[y]+=si[x];
		} else {
			if (x != y) {
				f[x] = y;si[y]+=si[x];
				h[y]++;
			}
		}
	}

	static long pow(long x, long a) {
		if (a == 0) {
			return 1;
		} else {
			long c = pow(x, a / 2);
			if (a % 2 == 0) {
				return c * c % mod;
			} else {
				return c * c % mod * x % mod;
			}
		}
	}

	static long mod = (long) (998244353);

	static void sovle1() {
		int n = sc.nextint();
		int x=sc.nextint();
		if (x==0) {
			if (n==1) {
				out.println(-1);return;
			}else {
				if (n%2==0) {
					out.println(n);return;
				}else {
					out.println(n+3);return;
				}
			}
		}else {
			int ge=0;long min=Long.MAX_VALUE;
			for (int i = 0; i < 31; i++) {
				long l = 1<<i;
				if ((l&x)!=0) {
					ge++;
				}else {
					min=Math.min(min, l);
				}
			}

			if (ge>=n) {

				out.println(x);
			}else {

				long ans=Long.MAX_VALUE;
				for (int i = 1; i <=ge; i++) {
					int u=n-i;
					if (u==1) {
						ans=Math.min(ans, x+min*2);
						ans=Math.min(ans, x+min*2+u-1);
					}else {
						if (u%2==0) {
							ans=Math.min(ans, x+u);

						}else {
							ans=Math.min(ans, x+u+3);
							ans=Math.min(ans, x+min*2+u-1);
						}

					}

				}
				out.println(ans);return;
			}

		}

	}

	static void cha(int[] ans, int n, int limit) {
		int[] ge = new int[ans.length];
		boolean p = false;
		for (int i = 0; i < ans.length; i++) {
			for (int j = 0; j < n; j++) {
				int x = (i ^ (1 << j));
				if (ans[x] == ans[i]) {
					ge[i]++;
				}
			}
			if (ge[i] > limit) {
				System.out.println(i);
			}
		}
	}

	static long[] c;

	static int lowbit(int x) {
		return x & -x;
	}

	static void add(int x, long v) {
		while (x < c.length) {

			c[x] += v;
			x += lowbit(x);
		}
	}

	static long sum(int x) {
		long ans = 0;

		while (x > 0) {

			ans += c[x];
			x -= lowbit(x);
		}
		return ans;
	}

	static Map<Integer, List<Integer>> map;

}

class kattio extends PrintWriter {

	BufferedReader r;
	StringTokenizer st;

	public kattio() {
		this(System.in, System.out);
	}

	public kattio(InputStream i, OutputStream o) {
		super(o);
		r = new BufferedReader(new InputStreamReader(i));
	}

	public kattio(String in, String out) throws IOException {
		super(out);
		r = new BufferedReader(new FileReader(in));
	}

	public String next() {
		try {
			while (st == null || !st.hasMoreTokens()) {
				st = new StringTokenizer(r.readLine());
			}
			return st.nextToken();
		} catch (Exception e) {

			return null;
		}
	}

	public int nextint() {
		return Integer.parseInt(next());
	}

	public long nextlong() {
		return Long.parseLong(next());
	}

	public double nextdouble() {
		return Double.parseDouble(next());
	}
}