import java.util.*;

public class Main{

	public static int n;
	public static class xds{
		xds lson,rson;
		int val,lazy;
	}
	public static class trr{
		public void build(xds rt,int l,int r) {
			if(l==r) {
				rt.val=l;
				return;
			}
			rt.lson=new xds();rt.rson=new xds();
			int mid=(l+r)/2;
			build(rt.lson,l,mid);build(rt.rson,mid+1,r);
			return;
		}
		public void pushdown(xds rt,xds ls,xds rs) {
			if(rt.lazy>0) {
				ls.val+=rt.lazy;
				rs.val+=rt.lazy;
				ls.lazy+=rt.lazy;
				rs.lazy+=rt.lazy;
				rt.lazy=0;
				return;
			}
			return;
		}
		public void motify(xds rt,int l,int r,int ll,int rr,int v) {

			if(ll<=l&&r<=rr) {

				rt.val+=v;
				rt.lazy+=v;
				return;
			}
			int mid=(l+r)/2;
			xds lson=rt.lson,rson=rt.rson;
			pushdown(rt,lson,rson);
			if(ll<=mid) motify(lson,l,mid,ll,rr,v);
			if(rr>mid) motify(rson,mid+1,r,ll,rr,v);
		}
		public int query(xds rt,int l,int r,int pos) {
			if(l==r) return rt.val;
			pushdown(rt,rt.lson,rt.rson);
			int mid=(l+r)/2;
			if(pos<=mid) return query(rt.lson,l,mid,pos);
			else return query(rt.rson,mid+1,r,pos);
		}
	}
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		n=s.nextInt();
		xds root=new xds();
		trr tree=new trr();
		int N=(int)5e5+6;
		tree.build(root, 1, N);

		for(int i=1;i<=n;i++) {
			int l=s.nextInt(),r=s.nextInt();
			int ll=1,rr=N,as=1;
			while(ll<=rr) {
				int mid=(ll+rr)/2;
				int u=tree.query(root, 1, N, mid);
				if(u>=l) {
					as=mid;
					rr=mid-1;
				}
				else ll=mid+1;
			}
			int lk=as;
			ll=1;rr=N;as=N;
			while(ll<=rr) {
				int mid=(ll+rr)/2;
				int u=tree.query(root, 1, N, mid);
				if(u<=r) {
					as=mid;
					ll=mid+1;
				}
				else rr=mid-1;
			}
			int rk=as;

			tree.motify(root, 1, N, lk, rk, 1);

		}
		int q=s.nextInt();
		for(int i=1;i<=q;i++) {
			int x=s.nextInt();
			System.out.print(tree.query(root, 1, N, x)+"\n");
		}
	}

}