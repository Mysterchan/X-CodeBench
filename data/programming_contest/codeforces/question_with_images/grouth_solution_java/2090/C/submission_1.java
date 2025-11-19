import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(in.readLine());
		while(t-->0) {
			int n = Integer.parseInt(in.readLine());
			StringTokenizer f = new StringTokenizer(in.readLine());

			int lx = 1;
			int ly = 1;

			PriorityQueue<P> pq = new PriorityQueue<>();
			for(int i = 0; i < n ;i++) {
				int type = Integer.parseInt(f.nextToken());

				if(type==0) {
					pq.add(new P(lx+ly+1,lx, ly+1));
					pq.add(new P(lx+ly+1,lx+1, ly));
					pq.add(new P(lx+ly+4,lx+1, ly+1));
					System.out.println(lx + " " + ly);
					if(ly == 1) {
						ly = lx+3;
						lx=1;
					}else {
						lx+=3;
						ly-=3;
					}
				}else if(pq.isEmpty() || lx+ly<pq.peek().dist){
					pq.add(new P(lx+ly,lx, ly));
					pq.add(new P(lx+ly+1,lx, ly+1));
					pq.add(new P(lx+ly+1,lx+1, ly));
					pq.add(new P(lx+ly+4,lx+1, ly+1));
					if(ly == 1) {
						ly = lx+3;
						lx=1;
					}else {
						lx+=3;
						ly-=3;
					}
					P rem = pq.poll();
					System.out.println(rem.x + " " + rem.y);
				}else {
					P rem = pq.poll();
					System.out.println(rem.x + " " + rem.y);
				}
			}

		}
	}
	static class P implements Comparable<P>{
		int dist,  x,  y;
		P(int dist, int x, int y){
			this.dist = dist;
			this.x=x;
			this.y=y;
		}
		@Override
		public int compareTo(Main.P o) {
			return this.dist==o.dist ? (this.x==o.x ? this.y-o.y : this.x-o.x) : this.dist-o.dist;
		}

	}

}
