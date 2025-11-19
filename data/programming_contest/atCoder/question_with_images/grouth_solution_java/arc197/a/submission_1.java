import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
	static PrintWriter output = new PrintWriter(System.out);
	public static void main(String[] args) {

        int T = sc.nextInt();

        for(int i=0;i<T;i++){
            int H = sc.nextInt();
            int W = sc.nextInt();
            char[] S = sc.next().toCharArray();

            int D = 0, R = 0;
            for(char s:S){
                if(s == 'D') D++;
                else if(s == 'R') R++;
            }
            D = H-1-D;
            R = W-1-R;

            int[][] tmp = new int[W+1][2];
            int count = 0, nowH = 0, nowW = 0;

            for(char s:S){
                if(s == 'D') nowH++;
                else if(s == 'R') {
                    nowW++;
                    tmp[nowW][0] = nowH;
                }
                else{
                    if(count < R){
                        nowW++;
                        count++;
                        tmp[nowW][0] = nowH;
                    }
                    else{
                        nowH++;
                    }
                }

            }

            nowH = 0;
            nowW = 0;
            count = 0;
            for(char s:S){
                if(s == 'D') nowH++;
                else if(s == 'R') nowW++;
                else{
                    if(count < D){
                        nowH++;
                        count++;
                    }
                    else{
                        nowW++;
                    }
                }
                tmp[nowW][1] = nowH;
            }

            long ans = 0;
            for(int j = 0;j<W;j++){
                ans += (long)(Math.abs(tmp[j][1] - tmp[j][0]) + 1);
            }
            output.println(ans);
        }

		output.flush();
		sc.close();
	}
}