import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
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

			Map<Pair<Integer,Integer>, Integer> para = new HashMap<Pair<Integer,Integer>, Integer>();
			Map<Pair<Integer,Integer>, Integer> mid = new HashMap<Pair<Integer,Integer>, Integer>();

			for(int i = 0; i < n - 1; i++) {
				for(int j = i + 1; j < n; j++) {
					int px = x[j] - x[i];
					int py = y[j] - y[i];

					if(px == 0) py = 1;
					else if(py == 0) px = 1;
					else {
						if (px < 0) {
							px *= -1;
							py *= -1;
						}

						int g = gcd(Math.abs(px), Math.abs(py));
						px /= g;
						py /= g;
					}

					para.merge(new Pair<>(px, py), 1, Integer::sum);
					mid.merge(new Pair<>(x[j] + x[i], y[j] + y[i]), 1, Integer::sum);
				}
			}

			int cnt = 0;
			long ans = 0;
			for(Integer  i : para.values()) {
				ans += i * (i - 1) / 2;
			}

			for(Integer  i : mid.values()) {
				cnt += i * (i - 1) / 2;
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

class Pair<A, B> {
    public final A first;
    public final B second;

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Pair<?, ?>)) return false;
        Pair<?, ?> pair = (Pair<?, ?>) o;
        return Objects.equals(first, pair.first) &&
               Objects.equals(second, pair.second);
    }

    @Override
    public int hashCode() {
        return Objects.hash(first, second);
    }

    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}