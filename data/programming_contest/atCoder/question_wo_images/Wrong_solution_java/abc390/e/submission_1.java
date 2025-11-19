import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main
{
	static Vita[] vita = new Vita[3];
	static int budget;

	public static void main(String[] args)
	{
		FastReader sc = new FastReader();

		for(int i=0;i<3;i++)
			vita[i] = new Vita();

		int n = sc.nextInt();
		budget = sc.nextInt();

		for(int i=0;i<n;i++)
		{
			int v = sc.nextInt()-1;
			int a = sc.nextInt();
			int c = sc.nextInt();

			vita[v].vitaworth.add(a);
			vita[v].price.add(c);
		}

		int res = binser(1,1000000000);
		System.out.println(res);

	}

	static int binser(int min, int max)
	{

		int mid = (min+max)/2;

		if(investigate(mid) <= budget)
		{

			if(mid < max)
				return Math.max(mid, binser(mid+1, max));
			else
				return mid;
		}
		else
		{

			if(mid==min)
				return 0;
			else
				return binser(min, mid-1);
		}
	}

	static int investigate(int target)
	{
		int res = 0;
		for(int v=0;v<3;v++)
			res += getMinimum(vita[v].vitaworth, vita[v].price, target);

		return res;
	}

	static class Vita
	{
		ArrayList<Integer> vitaworth = new ArrayList<>();
		ArrayList<Integer> price = new ArrayList<>();
	}

	static int getMinimum(ArrayList<Integer> vitaworth, ArrayList<Integer> price, int target)
	{

		int[] dp = new int[5001];
		int[] dpAfter = new int[5001];

		for(int i=0;i<vitaworth.size();i++)
		{
			for(int k=0;k<=5000;k++)
			{
				dpAfter[k]=dp[k];
			}

			int wor = vitaworth.get(i);
			int pr = price.get(i);

			for(int k=0;k<=5000;k++)
			{

				int kAfter = k+pr;
				if(kAfter <= 5000)
				{
					dpAfter[kAfter] = Math.max(dpAfter[kAfter], dp[k]+wor);
				}
			}

			dp = dpAfter;
		}

		for(int k=0;k<=5000;k++)
		{
			if(dp[k] >= target)
				return k;
		}

		return 9999;
	}

	static class FastReader
	{
		BufferedReader br;
		StringTokenizer st;

		public FastReader()
		{
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next()
		{
			while (st == null || !st.hasMoreElements())
			{
				try
				{
					st = new StringTokenizer(br.readLine());
				} catch (IOException e)
				{
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt()
		{
			return Integer.parseInt(next());
		}

		long nextLong()
		{
			return Long.parseLong(next());
		}

		double nextDouble()
		{
			return Double.parseDouble(next());
		}

		String nextLine()
		{
			String str = "";
			try
			{
				if (st.hasMoreTokens())
				{
					str = st.nextToken("\n");
				} else
				{
					str = br.readLine();
				}
			} catch (IOException e)
			{
				e.printStackTrace();
			}
			return str;
		}
	}
}