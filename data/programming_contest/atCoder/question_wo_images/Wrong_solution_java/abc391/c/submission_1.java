import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Map<Integer, Integer> resultMap = new HashMap<Integer, Integer>();

		int N = scanner.nextInt();
		int Q = scanner.nextInt();

		int[] cnt = new int[N + 1];
		int[] pos = new int[N + 1];
		int ans = 0;

		for(int i = 0;i <= N;i++) {
			cnt[i] = 1;
			pos[i] = i;
		}

		for (int i = 0; i < Q; i++) {
			int type = scanner.nextInt();
			if(type == 1) {
				int P = scanner.nextInt();
				int H = scanner.nextInt();

				if(cnt[pos[P]] == 2) {
					ans--;
				}

				pos[P] = H;
				cnt[H]++;

				if(cnt[H] == 2) {
					ans++;
				}
			}else {
				System.out.println(ans);
			}
		}
	}

}