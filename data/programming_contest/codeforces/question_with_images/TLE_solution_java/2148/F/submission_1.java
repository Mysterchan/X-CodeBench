import java.util.*;
import java.lang.*;
import java.io.*;
public class Main
    {
	static FastScanner fs = null;
	public static void main(String[] args) {
	    fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
	    int t = fs.nextInt();
	    while(t-->0){
	        int n = fs.nextInt();
	        int ml = 0;
	        int inf = (int)1e9;
	        Set<Integer> set = new HashSet<>();
	        int list[][]  = new int[n][];
	        for(int i = 0;i<n;i++){
	            int k = fs.nextInt();
	            list[i] = new int[k+1];
	            list[i][0] = k;
	            ml = Math.max(ml,k);
	            set.add(i);
	            for(int ii = 0;ii<k;ii++){
	                list[i][ii+1] = fs.nextInt();
	            }
	        }
	        Set<Integer> rem_row = new HashSet<>();
	        for(int i = 0;i<n;i++){
	            rem_row.add(i);
	        }
	        ArrayList<Integer> ll = new ArrayList<>();
	        int cur_idx = 1;
	        boolean vis[] = new boolean[n+1];
	        Arrays.fill(vis,false);
	        while(true){
	            int carry = 0;
	            int num_put = (int)inf;
	            Set<Integer> row_dele = new HashSet<>();
	            for(Integer p:rem_row){
	                if(list[p][0]==cur_idx){
	                    row_dele.add(p);
	                }
	                if(vis[p]){
	                    carry = 1;
	                }
	            }
	            if(carry==1){
	                for(Integer p:rem_row){
	                    if(vis[p]){
	                        num_put = Math.min(num_put,list[p][cur_idx]);
	                    }
	                }
	                for(Integer p:rem_row){
	                    if(vis[p]){
	                        if(num_put==list[p][cur_idx]){
	                            vis[p] = true;
	                        }
	                        else{
	                            vis[p] = false;
	                        }
	                    }
	                }
	            }
	            else{
	                for(Integer p:rem_row){
	                    num_put = Math.min(num_put,list[p][cur_idx]);
	                }
	                for(Integer p:rem_row){
	                    if(num_put==list[p][cur_idx]){
	                        vis[p] = true;
	                    }
	                }
	            }
	            ll.add(num_put);
	            for(Integer p:row_dele){
	                rem_row.remove(p);
	            }
	            if(cur_idx==ml){
	                break;
	            }
	            cur_idx+=1;
	        }
	        for(Integer p:ll){
	            out.print(p+" ");
	        }
	       out.println();
	    }
	    out.close();
	}
	static class Pair{
	    int x;
	    int y;
	    Pair(int x,int y){
	        this.x = x;
	        this.y = y;
	    }
	}
	static void sort(int[] a) {
		ArrayList<Integer> l=new ArrayList<>();
		for (int i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
	}
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}
		int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		long nextLong() {
			return Long.parseLong(next());
		}
		double nextD1ouble() {
			return Double.parseDouble(next());
		}
	}
}
