import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {

    static class Run { char ch; long len; Run(char ch, long len){ this.ch=ch; this.len=len; } }

    static long[] dir(char c){
        switch(c){
            case 'U': return new long[]{-1, 0};
            case 'D': return new long[]{ 1, 0};
            case 'L': return new long[]{ 0,-1};
            case 'R': return new long[]{ 0, 1};
        }
        throw new IllegalArgumentException("bad char "+c);
    }

    static long countMeet(long Rt, long Ct, long Ra, long Ca, List<Run> S, List<Run> T){
        long targetR = Ra - Rt;
        long targetC = Ca - Ct;

        int i = 0, j = 0;
        long remS = (S.size()>0 ? S.get(0).len : 0);
        long remT = (T.size()>0 ? T.get(0).len : 0);

        long prevR = 0, prevC = 0;
        long ans = 0;

        while(i < S.size() && j < T.size()){
            long len = Math.min(remS, remT);
            long[] dS = dir(S.get(i).ch);
            long[] dT = dir(T.get(j).ch);
            long rvR = dS[0] - dT[0];
            long rvC = dS[1] - dT[1];

            if(rvR == 0 && rvC == 0){
                if(prevR == targetR && prevC == targetC){
                    ans += len;
                }
            } else if(rvR == 0){
                if(prevR == targetR){
                    long need = targetC - prevC;
                    if(need % rvC == 0){
                        long t = need / rvC;
                        if(1 <= t && t <= len) ans += 1;
                    }
                }
            } else if(rvC == 0){
                if(prevC == targetC){
                    long need = targetR - prevR;
                    if(need % rvR == 0){
                        long t = need / rvR;
                        if(1 <= t && t <= len) ans += 1;
                    }
                }
            } else {
                long needR = targetR - prevR;
                long needC = targetC - prevC;
                if(needR % rvR == 0 && needC % rvC == 0){
                    long tR = needR / rvR;
                    long tC = needC / rvC;
                    if(tR == tC && 1 <= tR && tR <= len) ans += 1;
                }
            }

            prevR += rvR * len;
            prevC += rvC * len;

            remS -= len;
            remT -= len;
            if(remS == 0){
                i++;
                if(i < S.size()) remS = S.get(i).len;
            }
            if(remT == 0){
                j++;
                if(j < T.size()) remT = T.get(j).len;
            }
        }

        return ans;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        String[] in = br.readLine().split(" ");
        long Rt = Long.parseLong(in[0]);
        long Ct = Long.parseLong(in[1]);
        long Ra = Long.parseLong(in[2]);
        long Ca = Long.parseLong(in[3]);

        in = br.readLine().split(" ");
        long n = Long.parseLong(in[0]);
        int M = Integer.parseInt(in[1]);
        int L = Integer.parseInt(in[2]);
        List<Run> S = new ArrayList<>();
        for(int i=0;i<M;i++){
            in = br.readLine().split(" ");
            char ch = in[0].charAt(0);
            long len = Long.parseLong(in[1]);
            S.add(new Run(ch, len));
        }
        List<Run> T = new ArrayList<>();
        for(int i=0;i<L;i++){
            in = br.readLine().split(" ");
            char ch = in[0].charAt(0);
            long len = Long.parseLong(in[1]);
            T.add(new Run(ch, len));
        }

        long ans = countMeet(Rt, Ct, Ra, Ca, S, T);
        System.out.println(ans);
    }
}