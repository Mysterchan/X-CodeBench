import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    int[] A = new int[N];
    Map<Integer, Integer> freq = new HashMap<>();
    for (int i = 0; i < N; i++) {
      A[i] = scanner.nextInt();
      freq.put(A[i], freq.getOrDefault(A[i], 0) + 1);
    }
    long ans = 1;
    for (int i = 0; i < N; i++) {
      if (i > 0 && A[i] == A[i - 1]) continue;
      freq.put(A[i], freq.getOrDefault(A[i], 0) - 1);
      ans += (N - i - 1) - freq.getOrDefault(A[i], 0);
    }
    System.out.println(ans);
  }
}