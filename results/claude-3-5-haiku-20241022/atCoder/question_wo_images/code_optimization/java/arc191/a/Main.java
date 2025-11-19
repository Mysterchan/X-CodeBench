import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[] s = br.readLine().toCharArray();
        char[] t = br.readLine().toCharArray();
        
        char lastChar = t[m - 1];
        
        // Count frequency of each digit in t
        int[] freq = new int[10];
        for (int i = 0; i < m; i++) {
            freq[t[i] - '0']++;
        }
        
        // Create sorted list of digits (descending)
        int totalDigits = m;
        int[] sortedT = new int[totalDigits];
        int idx = 0;
        for (int digit = 9; digit >= 0; digit--) {
            for (int count = 0; count < freq[digit]; count++) {
                sortedT[idx++] = digit;
            }
        }
        
        // Greedy replacement from left to right
        int tIndex = 0;
        for (int i = 0; i < n && tIndex < totalDigits; i++) {
            int currentDigit = s[i] - '0';
            if (currentDigit < sortedT[tIndex]) {
                s[i] = (char) ('0' + sortedT[tIndex]);
                tIndex++;
            }
        }
        
        // Check if we must use the last character
        int lastDigit = lastChar - '0';
        boolean lastUsed = false;
        
        // Find position of last digit in sorted array
        int lastPosInSorted = -1;
        for (int i = 0; i < totalDigits; i++) {
            if (sortedT[i] == lastDigit) {
                lastPosInSorted = i;
                break;
            }
        }
        
        // If last digit wasn't used in greedy phase, we must place it
        if (lastPosInSorted == -1 || lastPosInSorted >= tIndex) {
            // Find leftmost position where we can improve or place it
            for (int i = 0; i < n; i++) {
                if (s[i] - '0' < lastDigit) {
                    s[i] = lastChar;
                    lastUsed = true;
                    break;
                }
            }
            
            // If still not used, check if it already exists
            if (!lastUsed) {
                for (int i = 0; i < n; i++) {
                    if (s[i] == lastChar) {
                        lastUsed = true;
                        break;
                    }
                }
            }
            
            // If still not used, place at the end
            if (!lastUsed) {
                s[n - 1] = lastChar;
            }
        }
        
        System.out.println(new String(s));
    }
}