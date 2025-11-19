import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
		for(int i = 1;i <= n;i++) {
			map.put(i, new ArrayList<>());
		}
		for(int i = 0;i < n;i++) {
			int a = sc.nextInt();
			map.get(a).add(i);
		}for(int i = 1;i <= n;i++) {
			map.get(i).add(n);
		}long ans = 1;
		for(int i = 1;i <= n;i++) {
			int size = map.get(i).size();
			for(int j = 0;j < map.get(i).size() - 1;j++) {
				int a = map.get(i).get(j + 1);
				int b = map.get(i).get(j);
				if(a == b + 1)continue;
				ans += (n - map.get(i).get(j) - size + j + 1);
			}
		}System.out.print(ans);
	}

}