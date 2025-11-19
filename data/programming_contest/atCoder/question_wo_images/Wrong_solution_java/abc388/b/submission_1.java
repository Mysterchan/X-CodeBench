import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int d = sc.nextInt();

		Map<Integer,Integer> map = new HashMap<>();

		for(int i = 0; i < n; i++) {
			map.put(sc.nextInt(),sc.nextInt());
		}

		int max = Integer.MIN_VALUE;

		for(int i = 1; i <= d; i++) {
			for(int key: map.keySet()) {
				int weight = key * (map.get(key) + i);
				max = Integer.max(max,weight);
			}

			System.out.println(max);
		}
	}

}