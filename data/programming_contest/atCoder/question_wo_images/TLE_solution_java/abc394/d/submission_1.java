import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){

			char S[] = sc.next().toCharArray();
			if(S.length % 2 == 1) {
				System.out.println("No"); return;
			}

			Queue<int[]> query = new ArrayDeque<>();

			int bridge[] = new int[S.length];
			Arrays.fill(bridge, -1);
			int count = 0;

			for(int i = 0; i < S.length-1; i++) {
				if(isPairBracket(S[i], S[i+1])) {
					bridge[i] = i+1;
					bridge[i+1] = i;
					query.add(new int[]{i-1, i+2});
					count += 2;
				}
			}

			int  outer[] = new int[2];
			int f, e;
			while(!query.isEmpty()) {
				outer = query.poll();
				f = outer[0]; e = outer[1];
				if(f < 0 || e >= S.length) continue;

				if(bridge[f] != -1) {
					query.add(new int[] {bridge[f]-1, e});
					continue;
				}
				if(bridge[e] != -1) {
					query.add(new int[] {f, bridge[e]+1});
					continue;
				}

				if(isPairBracket(S[f], S[e])) {
					bridge[f] = e;
					bridge[e] = f;
					query.add(new int[]{f-1, e+1});
					count += 2;
				}

			}

			if(count == S.length) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}

		}
	}

	private static boolean isPairBracket(char a, char b) {
		boolean b1 = (a == '(' && b == ')');
		boolean b2 = (a == '[' && b == ']');
		boolean b3 = (a == '<' && b == '>');
		return (b1 || b2 || b3);
	}
}