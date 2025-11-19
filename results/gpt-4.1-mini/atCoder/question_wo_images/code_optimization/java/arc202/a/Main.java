import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    // The problem can be solved by simulating the merges using a stack.
    // Each element in the stack is a pair (value, count).
    // When the top two elements have the same value, they merge into one with value+1.
    // If count is odd, we need to insert one element to make it even before merging.
    // The total insertions needed is the sum of all such insertions.

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        // sum of N over all test cases <= 2*10^5, so total input size manageable

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] a = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }

            long insertions = 0;
            // stack stores pairs: value and count
            // use arrays for stack to avoid overhead
            int[] stackVal = new int[n];
            int[] stackCount = new int[n];
            int top = -1;

            for (int i = 0; i < n; i++) {
                int val = a[i];
                int count = 1;

                // If top of stack has same value, increment count
                if (top >= 0 && stackVal[top] == val) {
                    stackCount[top]++;
                } else {
                    // push new value
                    stackVal[++top] = val;
                    stackCount[top] = 1;
                }

                // Try to merge while top count >= 2
                while (top >= 0 && stackCount[top] >= 2) {
                    int c = stackCount[top];
                    int v = stackVal[top];
                    // If count is odd, insert one element to make it even
                    if ((c & 1) == 1) {
                        insertions++;
                        c++;
                    }
                    // merge pairs
                    int mergedCount = c / 2;
                    int mergedVal = v + 1;
                    top--; // pop current

                    // Now push merged element or merge with previous if same value
                    if (top >= 0 && stackVal[top] == mergedVal) {
                        stackCount[top] += mergedCount;
                    } else {
                        stackVal[++top] = mergedVal;
                        stackCount[top] = mergedCount;
                    }
                }
            }

            // After processing all elements, try to merge remaining stack elements
            // until only one element with count 1 remains
            while (top > 0 || (top == 0 && stackCount[top] > 1)) {
                int c = stackCount[top];
                int v = stackVal[top];
                if ((c & 1) == 1) {
                    insertions++;
                    c++;
                }
                int mergedCount = c / 2;
                int mergedVal = v + 1;
                top--;
                if (top >= 0 && stackVal[top] == mergedVal) {
                    stackCount[top] += mergedCount;
                } else {
                    stackVal[++top] = mergedVal;
                    stackCount[top] = mergedCount;
                }
            }

            sb.append(insertions).append('\n');
        }
        System.out.print(sb);
    }
}