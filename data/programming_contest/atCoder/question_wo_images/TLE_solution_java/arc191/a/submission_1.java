import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String s = br.readLine();
        String t = br.readLine();
        int last = Integer.parseInt(t.substring(m-1));
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = s.charAt(i)-'0';
        }
        ArrayList<Integer> numt = new ArrayList<>();
        int[] freq = new int[10];
        for (int i = 0; i < m; i++) {
            int d = t.charAt(i)-'0';
            freq[d]++;
        }
        for (int i = 9; i >= 0; i--) {
            for (int j = 0; j < freq[i]; j++) {
                numt.add(i);
            }
        }
        int lastIndex = numt.indexOf(last);

        int index = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] < numt.get(index)) {
                nums[i] = numt.get(index);
                index++;
                if (index >= numt.size()) {
                    break;
                }
            }
        }

        boolean indicator = false;
        if (lastIndex <= index) {
            indicator = true;
        }
        if (!indicator) {
            for (int i = 0; i < n; i++) {
                if (nums[i] < last) {
                    nums[i] = last;
                    indicator = true;
                }
            }
        }
        if (!indicator) {
            for (int i = 0; i < n; i++) {
                if (nums[i] == last) {
                    indicator = true;
                }
            }
        }
        if (!indicator) {
            nums[n-1] = last;
        }
        String ans = "";
        for (int i = 0; i < n; i++) {
            ans += nums[i];
        }
        PrintWriter pw = new PrintWriter(new OutputStreamWriter(System.out));
        pw.println(ans);
        pw.close();
    }
}