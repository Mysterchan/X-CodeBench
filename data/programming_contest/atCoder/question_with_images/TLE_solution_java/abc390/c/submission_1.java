import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int H = sc.nextInt();
		int W = sc.nextInt();
		int wMin = -1;
		int wMax = 0;
		int hMin = -1;
		int hMax = 0;
		String S[] = new String[H];
		for (int i = 0; i < H; i++) {
			S[i] = sc.next();
			int min = S[i].indexOf('#');
			if (min >= 0) {
				if (hMin == -1) hMin = i;
				hMax = i;
				int max = S[i].lastIndexOf('#');
				if (wMin == -1 || min < wMin) {
					wMin = min;
				}
				if (max > wMax) {
					wMax = max;
				}
			}
		}
		if (hMin == -1) {
			for (int i = 0; i < H; i++) {
				int min = S[i].indexOf('?');
				if (min >= 0) {
					System.out.println("Yes");
					return;
				}
			}
			System.out.println("No");
			return;
		}
		for (int i = 0; i < H; i++) {
			if (i >= hMin && i <= hMax) {
				int min = 0;
				while (min >= 0) {
					min = S[i].indexOf('.', min);
					if (min >= 0) {
						if (min >= wMin && min <= wMax) {
							System.out.println("No");
							return;
						}
					}
				}
			}
		}
		System.out.println("Yes");
	}
}