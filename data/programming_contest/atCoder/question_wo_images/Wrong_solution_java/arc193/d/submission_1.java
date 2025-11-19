import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            String inc = br.readLine();
            String cor = br.readLine();

            int count = 0;
            int minLength = Math.min(inc.length(), cor.length());

            for (int i = 0; i < minLength; i++) {
                if (inc.charAt(i) != cor.charAt(i)) {
                    count++;
                }
            }

            System.out.println(count);
        }

        br.close();
    }
}