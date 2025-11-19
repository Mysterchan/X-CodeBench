import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        long[] A = new long[N];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }
        
        int Q = Integer.parseInt(br.readLine());
        
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken()) - 1;
            int R = Integer.parseInt(st.nextToken()) - 1;
            
            int count = 0;
            int left = L;
            int right = L;
            
            while (left <= R && right <= R) {
                // Find the first mochi from 'right' that can be placed on top of A[left]
                while (right <= R && A[right] < 2 * A[left]) {
                    right++;
                }
                
                if (right <= R) {
                    count++;
                    left++;
                    right++;
                } else {
                    break;
                }
            }
            
            sb.append(count).append('\n');
        }
        
        bw.write(sb.toString());
        bw.flush();
    }
}