import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int n = sc.nextInt();
            int k = sc.nextInt();

            // Count number of zero bits in n
            int zeroBits = 0;
            int temp = n;
            while(temp > 0){
                if((temp & 1) == 0) zeroBits++;
                temp >>= 1;
            }
            // If n=0 (not in constraints), handle separately, but here n>=1

            long maxCompatible = 1L << zeroBits; // total compatible numbers count

            if(k > maxCompatible){
                System.out.println(-1);
                continue;
            }

            // Construct the k-th compatible number
            // Compatible numbers X satisfy:
            // X = n + y, where y < n and (y & n) == 0
            // y is formed by placing bits of (k-1) into zero bit positions of n

            long y = 0;
            int bitPos = 0;
            int kMinus1 = k - 1;
            for(int i = 0; i < 31; i++){
                if((n & (1 << i)) == 0){
                    if((kMinus1 & (1 << bitPos)) != 0){
                        y |= (1 << i);
                    }
                    bitPos++;
                }
            }

            System.out.println((long)n + y);
        }
    }
}