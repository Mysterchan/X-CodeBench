import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashSet<Integer> set = new HashSet<>();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        boolean indicator = false;
        if (n % 4 == 0) indicator = true;
        else if (n % 4 != 2) {
            for (int i = 0; i < n; i++) {
                if (arr[i] == 1) {
                    indicator = true;
                    break;
                }
            }
        }
        else {
            for (int i = 0; i < n; i++) {
                if (arr[i] == 1) {
                    set.add(i % 2);
                }
            }
            if (set.size() == 2) {
                indicator = true;
            }
        }
        if (indicator) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}