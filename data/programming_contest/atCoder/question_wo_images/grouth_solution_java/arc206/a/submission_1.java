import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    int[] A = new int[N];
    for (int i = 0; i < N; i++) {
      A[i] = scanner.nextInt();
    }

    long ans = solve(N, A);
    System.out.println(ans);
  }

  private static long solve(int N, int[] A) {
    Map<Integer, Integer> freq = new HashMap<>();
    for (int i = 0; i < N; i++) {
      freq.put(A[i], freq.getOrDefault(A[i], 0) + 1);
    }

    long ans = 1;
    for (int i = 0; i < N; i++) {
      freq.put(A[i], freq.getOrDefault(A[i], 0) - 1);
      if (i > 0 && A[i] == A[i - 1]) continue;
      ans += (N - i - 1) - freq.getOrDefault(A[i], 0);
    }
    return ans;
  }
}