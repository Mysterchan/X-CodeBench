import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			int n = sc.nextInt();
			int[] x = new int[n];
			int[] y = new int[n];
			for(int i = 0; i < n; i++) {
				x[i] = sc.nextInt();
				y[i] = sc.nextInt();
			}

			Map<Integer, Map<Integer, Integer>> para = new HashMap<Integer, Map<Integer,Integer>>();
			Map<Integer, Map<Integer, Integer>> mid = new HashMap<Integer,Map<Integer, Integer>>();

			for(int i = 0; i < n - 1; i++) {
				for(int j = i + 1; j < n; j++) {
					int xx = x[i] - x[j];
					int yy = y[i] - y[j];

					if(!mid.containsKey(x[i] + x[j])) mid.put(x[i] + x[j], new HashMap<Integer, Integer>());
					Map<Integer, Integer> midMap = mid.get(x[i] + x[j]);
					midMap.merge(y[i] + y[j], 1, Integer::sum);

					if(xx == 0) yy = 1;
					else if(yy == 0) xx = 1;

					if(xx < 0) {
						xx = -xx;
						yy = -yy;
					}

					int d = gcd(Math.abs(xx), Math.abs(yy));

					xx /= d;
					yy /= d;

					if(!para.containsKey(xx)) para.put(xx, new HashMap<Integer, Integer>());
					Map<Integer, Integer> paraMap = para.get(xx);
					paraMap.merge(yy, 1, Integer::sum);
				}
			}

			int cnt = 0;
			long ans = 0;
			for(Map<Integer, Integer>  values : para.values()) {
				for(Integer i : values.values()) {
					ans += i * (i - 1) / 2;
				}
			}

			for(Map<Integer, Integer> values : mid.values()) {
				for(Integer i : values.values()) {
					cnt += i * (i - 1) / 2;
				}
			}

			ans -= cnt;
			System.out.println(ans);
		}
	}

	static int gcd(int a, int b) {
		if (b == 0) {
			return a;
		} else {
			return gcd(b, a % b);
		}
	}
}