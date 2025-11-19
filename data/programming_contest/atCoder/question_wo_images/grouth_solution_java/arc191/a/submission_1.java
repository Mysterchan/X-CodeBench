import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        char[] s = sc.next().toCharArray();
        char[] t = sc.next().toCharArray();

        int count[] = new int[128];
        for(int i = 0 ; i < m; i++) {
            count[t[i]]++;
        }

        boolean used[] = new boolean[128];
        for(int i = 0; i < n; i++) {
            for(char j = '9'; j > s[i]; j--) {
                if(count[j] > 0) {
                    s[i] = j;

                    count[j]--;
                    break;
                }
            }
            used[s[i]] = true;
        }

        if(!used[t[m - 1]]) {

            s[n - 1] = t[m - 1];
        }

        System.out.println(s);
    }
}

class Pair {
    char c;
    int index;

    Pair(char c, int index) {
        this.c = c;
        this.index = index;
    }
}