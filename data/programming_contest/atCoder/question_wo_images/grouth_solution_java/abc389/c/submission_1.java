import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int Q = scanner.nextInt();
		long now = 0;
		List<Long> x = new ArrayList<Long>();
		int id = 0;

		for(int i = 0;i < Q;i++) {
			int type = scanner.nextInt();

			if(type == 1) {
				long l = scanner.nextLong();
				x.add(now);
				now += l;
			}else  if(type == 2) {
				id++;
			}else {
				int k = scanner.nextInt() - 1;
				System.out.println(x.get(id + k) - x.get(id));
			}
		}

	}

}