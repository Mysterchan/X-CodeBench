import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();

		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        StringTokenizer st;

	        int N = Integer.parseInt(br.readLine());

	        long[] bigA = new long[N];
	        long[] A = new long[N];
	        st = new StringTokenizer(br.readLine());
	        for (int i = 0; i < N; i++) {
	            A[i] = Long.parseLong(st.nextToken());
	            bigA[i] = A[i]*2L;
	        }

        long jampA[] = new long[N];

        int Q = Integer.parseInt(br.readLine());
        int L[] = new int[Q];
        int R[] = new int[Q];
        for(int i = 0;i < Q;i++){
        	st = new StringTokenizer(br.readLine());
            L[i] = Integer.parseInt(st.nextToken());
            R[i] = Integer.parseInt(st.nextToken());

        }
        boolean flag = true;
        int n;
        int t;
        int tt;
        int sum;
        int l;
        int r;
        for(int i = 0;i < Q;i++){
            sum = 0;
            n = L[i]-1;
            l = L[i]-1;
            r = R[i]-1;
            if((L[i]+R[i])%2 == 1) {
            	t = (L[i]+R[i])/2;

            }else {
            	t = (L[i]+R[i])/2-1;
            }
            tt = t;
            while(t >= L[i]-1 && t < R[i]) {
            	if(bigA[n] < A[t]) {
            		if(tt == t)break;
            		if(t == l)break;
            		r = t;
            		t = (l+t)/2;
            	}else if(bigA[n] > A[t]) {
            		if(t+1 == r || t == r)break;
            		l = t;
            		t = (r+t)/2;
            	}else {
            		if(tt == t)break;
            		while(t >= 0 && A[t] == A[t-1])t--;
            		break;
            	}
            }

            int max = 0;
            for(t = t;t < R[i];t++) {
            	if(bigA[n] <= A[t]) {

            		max = n+(t-(L[i]-1));

            		n++;
            		sum++;
            		break;
            	}

            }

            for(t += 1;t < R[i];t++) {
            	if(bigA[n] <= A[t]) {

            		if(n == max)break;
            		n++;
            		sum++;
            	}
            }
            sb.append(sum+"\n");

        }
        bw.write(sb.toString());
        bw.flush();
	}
}