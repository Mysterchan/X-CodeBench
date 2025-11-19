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
        
        char[] result = s.toCharArray();
        int[] freq = new int[10];

        for (int i = 0; i < m; i++) {
            freq[t.charAt(i) - '0']++;
        }

        int index = 0;
        for (int i = 9; i >= 1; i--) {
            while (freq[i] > 0 && index < n) {
                if (result[index] < i + '0') {
                    result[index] = (char)(i + '0');
                    freq[i]--;
                }
                index++;
            }
        }

        System.out.println(new String(result));
    }
}